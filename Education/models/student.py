from odoo import models, fields

class Student(models.Model):
    _name = 'student'
    _description = 'Student'

    name = fields.Char(string='Student Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    email = fields.Char(string='Email')
    course_ids = fields.One2many('course_taken', 'student_id', string='Courses')
