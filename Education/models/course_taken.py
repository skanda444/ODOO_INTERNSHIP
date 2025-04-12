from odoo import models, fields

class CourseTaken(models.Model):
    _name = 'course_taken'
    _description = 'Course Taken'

    student_id = fields.Many2one('student', string='Student')
    course_name = fields.Char(string='Course Name')
    enrollment_date = fields.Date(string='Enrollment Date')
