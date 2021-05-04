from odoo import api, models, fields, _

class UniFaculty(models.Model):
    _name = 'uni.faculty'
    _description = 'Faculty Information'

    name = fields.Char(string='Faculty Name')
    dept_name = fields.Char(string='Department')
    salary = fields.Float(String='Salary')
    course_id = fields.Char(string='Courses')