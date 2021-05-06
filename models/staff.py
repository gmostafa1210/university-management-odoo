from odoo import fields, models

class UniStaff(models.Model):
    _name = 'uni.staff'
    _description = 'Staff Information'

    name = fields.Char(string='Staff Name')
    salary = fields.Float(string='Salary')
    department = fields.Char(string='Department')
    photo = fields.Binary(string='Photo', attachment=True)