from odoo import fields, models

class UniDepartment(models.Model):
    _name = 'uni.department'
    _description = 'Department Information'

    name = fields.Char(string='Department Name')
    budget = fields.Float(string='Department Budget')
    faculty_list = fields.Char(string='Faculty List')