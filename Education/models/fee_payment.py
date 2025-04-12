from odoo import models, fields

class FeePayment(models.Model):
    _name = 'fee_payment'
    _description = 'Fee Payment'

    student_id = fields.Many2one('student', string='Student', required=True)
    amount = fields.Float(string='Amount Paid', required=True)
    date = fields.Date(string='Payment Date', default=fields.Date.today)
    note = fields.Text(string='Note')
