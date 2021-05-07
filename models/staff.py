from odoo import fields, models

class UniStaff(models.Model):
    _name = 'uni.staff'
    _description = 'Staff Information'

    name = fields.Char(string='Staff Name')
    salary = fields.Float(string='Salary')
    department_ids = fields.Many2many('uni.department', string='Department')
    photo = fields.Binary(string='Photo', attachment=True)