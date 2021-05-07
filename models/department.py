from odoo import fields, models

class UniDepartment(models.Model):
    _name = 'uni.department'
    _description = 'Department Information'

    name = fields.Char(string='Department Name')
    budget = fields.Float(string='Department Budget')
    faculty_ids = fields.One2many('uni.faculty', 'department_id', string='Faculty List')
    student_ids = fields.One2many('uni.student', 'department_id', string='Student List')