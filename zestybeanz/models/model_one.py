from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError

class ModelOne(models.Model):
    _name = "model.one"
    _description = "Model One"
    _inherits = {'my.employee': 'employee_id'}

    seq = fields.Char(string="Sequence")
    name = fields.Char(string="Name", required=True, copy=False)
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(string="Age", compute='_compute_age', store=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], required=True, copy=False)
    active = fields.Boolean(default=True)
    description = fields.Text(default="Test Description")
    email = fields.Char(required=True, copy=False)
    joining_date = fields.Date(required=True)

    partner_ids = fields.Many2many('res.partner', string="Partner")
    sale_ids = fields.Many2many('sale.order', 'model_one_sale_rel', 'model_one_id', 'sale_id', string="Sales")
    product_ids = fields.Many2many('product.template', 'model_one_product_rel', 'model_one_id', 'product_id', string="Products")
    model_one_line_ids = fields.One2many('model.one.lines', 'model_one_id', string="Lines")
    sale_id = fields.Many2one('sale.order', string="Main Sale")
    partner_count = fields.Integer(string="Partner Count", compute="get_partner_count")
    is_special = fields.Boolean('Is Special')
    email = fields.Char(string="Email")
    employee_id = fields.Many2one('my.employee', string="Employee")
    sale_count = fields.Integer(string="Sale Count", compute="get_sale_count")

    # Fields to calculate total (price * quantity)
    price = fields.Float(string="Price")
    quantity = fields.Integer(string="Quantity")
    total = fields.Float(string="Total", compute='_compute_total', store=True)

    @api.depends('dob')
    def _compute_age(self):
        today = date.today()
        for rec in self:
            if rec.dob:
                rec.age = today.year - rec.dob.year - ((today.month, today.day) < (rec.dob.month, rec.dob.day))
            else:
                rec.age = 0

    @api.depends('price', 'quantity')
    def _compute_total(self):
        for record in self:
            record.total = record.price * record.quantity if record.price and record.quantity else 0.0

    def write_values(self):
        products = self.env['product.template'].search([('list_price', '>', 200)], limit=1).id
        order = self.env['sale.order'].search([('id', '=', 26)], limit=1).id
        ex_line = self.env['model.one.lines'].search([('model_one_id', '=', False)], limit=1).ids
        self.write({'model_one_line_ids': [(6, 0, ex_line)]})

    def helloworld(self):
        print("Hello World")

    def show_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'My Sample Wizard',
            'res_model': 'sample.wizard',
            'view_mode': 'form',
            'view_id': self.env.ref('zestybeanz.view_form_sample_wizard').id,
            'target': 'new',
            'context': {
                'default_name': self.name,
                'default_dob': self.dob
            }
        }

    @api.model
    def create(self, vals):
        vals['seq'] = self.env['ir.sequence'].next_by_code('sequence.model.one')
        return super().create(vals)

    @api.depends('partner_ids')
    def get_partner_count(self):
        for record in self:
            record.partner_count = len(record.partner_ids)
    
    @api.depends('sale_ids')
    def get_sale_count(self):
        for record in self:
            if record.sale_ids:
                record.sale_count = len(record.sale_ids)
            else:
                record.sale_count = 0
        
    @api.onchange('gender')
    def onchange_gender(self):
        for record in self:
            record.is_special = record.gender == 'other'

    @api.constrains('email')
    def check_email(self):
        for record in self:
            if not record.email.endswith('@gmail.com'):
                raise ValidationError("Email must end with @gmail.com")

    _sql_constraints = [
        ('unique_email_user', 'unique(email)', 'Email must be unique. This one already exists.')
    ]

    def increase_age(self):
        records = self.search([])
        for record in self.search([]):
            print("age before :", record.age)
            record.age += 1
            print("age after :", record.age) 

    def change_description(self):
        for record in self:
            record.description = "Description added through server action"

    def send_my_email(self):
        template = self.env.ref('zestybeanz.my_sample_email_template')
        for record in self:
            values = {'subject' : 'My Custom Subject via Method'}
            template.send_mail(record.id, force_send=True, email_values=values)

    
    def create_purchase_order_from_sale(self):
        for sale in self.sale_ids:
            # Create a new purchase order (PO)
            po_vals = {
                'partner_id': sale.partner_id.id,  # Vendor/Supplier (same as Sale Order partner)
                'date_order': fields.Datetime.now(),  # Set today's date as the order date
                'origin': sale.name,  # Reference to the Sale Order
            }

            # Create the Purchase Order
            purchase_order = self.env['purchase.order'].create(po_vals)

            # Now, create the purchase order lines based on Sale Order lines
            for sale_line in sale.order_line:
                # Create Purchase Order line for each Sale Order line
                po_line_vals = {
                    'order_id': purchase_order.id,  # Link to Purchase Order
                    'product_id': sale_line.product_id.id,  # Product from Sale Order line
                    'product_qty': sale_line.product_uom_qty,  # Quantity from Sale Order line
                    'price_unit': sale_line.price_unit,  # Unit price from Sale Order line
                    'name': sale_line.name,  # Description from Sale Order line
                }
                self.env['purchase.order.line'].create(po_line_vals)

            return purchase_order
    def show_sale(self):
        return{
            'type': 'ir.actions.act_window',
            'name': 'Sale Order',
            'res_model': 'sale.order',
            'view_mode': 'list,form',
            'target': 'current',
            'domain' : [('id', 'in', self.sale_ids.ids)]
        }


class ModelOneLines(models.Model):
    _name = "model.one.lines"
    _description = "Model One lines"

    name = fields.Char(string="Name")
    price = fields.Float(string="Standard Price")
    quantity = fields.Integer(string="Quantity")
    product_id = fields.Many2one('product.template', string="Product")
    model_one_id = fields.Many2one('model.one', string="Model One", domain="['|', ('gender', '=', 'female'), ('age', '>', 18)]")
    total = fields.Float(string="Total", compute='_compute_line_total', store=True)

    @api.depends('price', 'quantity')
    def _compute_line_total(self):
        for record in self:
            record.total = record.price * record.quantity if record.price and record.quantity else 0.0
