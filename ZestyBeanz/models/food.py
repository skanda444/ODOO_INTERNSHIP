from odoo import models,fields

class Food(models.Model):
    _name = "food.food"
    _description = "Model For Food "

    name = fields.Char(string="Name")
    price = fields.Float(string="Standard Price")
    quantity = fields.Integer(string="Integer")
    review = fields.Text(string="Review of the Food")
    is_satisfied = fields.Boolean(string="Satisfied/Not")
    check_in = fields.Date(string="Check In")
    served_time = fields.Datetime(string="Served Time")
    types = fields.Selection([('dine_in','Dine In'),('delivery','Delivery')])
    images = fields.Binary(string="Images")
    blog = fields.Html(string="blog")
