from odoo import models, fields

class ModelOne(models.Model):
    _name = "model.one"
    _description = "Model One"

    name = fields.Char(string="Name", help='A normal name field', required=True, copy=False)
    age = fields.Integer(string="Age", default=18)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender", required=True, copy=False)
    active = fields.Boolean("Active", default=True)
    description = fields.Text("Description", default="Test Description")
    email = fields.Char(string="Email", required=True, copy=False)
    joining_date = fields.Date(string="Joining Date", required=True)
    partner_ids = fields.Many2many('res.partner',string="Partner")
    sale_ids = fields.Many2many('sale.order','model_one_sale_rel','model_one_id','sale_id', string="Sale")