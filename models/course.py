from odoo import models, fields

class UniCourse(models.Model):
    _name = 'uni.course'
    _description = 'Course Information'

    name = fields.Char(string='Course Name')
    course_code = fields.Char(string='Course Code')
    course_description = fields.Text(string='Course Description')
    credit = fields.Integer(string='Credit')