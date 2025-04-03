from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Food(models.Model):
    _name = "food.food"
    _description = "Model For Food"

    name = fields.Char(string="Name")
    partner_id = fields.Many2one('res.partner', string="Name")
    price = fields.Float(string="Standard Price")
    quantity = fields.Integer(string="Integer")
    review = fields.Text(string="Review of the Food")
    is_satisfied = fields.Boolean(string="Satisfied/Not")
    check_in = fields.Date(string="Check In")
    served_time = fields.Datetime(string="Served Time")
    types = fields.Selection([('dine_in', 'Dine In'), ('delivery', 'Delivery')])
    images = fields.Binary(string="Images")
    blog = fields.Html(string="blog")
    sale_order_id = fields.Many2one('sale.order', string="Sale Order")
    invoice_id = fields.Many2one('account.move', string="Related Invoice")

    def test_function(self):
        print("This function is triggered ==")
        print("This function is triggered ==")

    @api.model
    def create(self, vals):
        res = super(Food, self).create(vals)
        print("Record created ==")
        if not res.is_satisfied:
            res.is_satisfied = True
        return res

    def write(self, vals):
        raise ValidationError("You are not permitted to edit the record")
        return super(Food, self).write(vals)
