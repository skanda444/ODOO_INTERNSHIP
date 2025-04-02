from odoo import models, fields

class CarRental(models.Model):
    _name = "car.rental"
    _description = "Car Rental"

    car_name = fields.Char(string="Car Name", required=True, copy=False)
    car_model = fields.Char(string="Car Model", required=True, copy=False)
    wheel_type = fields.Selection([
        ('alloy', 'Alloy'),
        ('steel', 'Steel'),
        ('carbon_fiber', 'Carbon Fiber')
    ], string="Wheel Type", required=True, copy=False)
    body_color = fields.Char(string="Body Color", required=True, copy=False)
    available = fields.Boolean(string="Available", default=True)
    seat_count = fields.Integer(string="Seat Count", required=True, default=4)
    amount = fields.Float(string="Amount", required=True)
