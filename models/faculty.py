from odoo import api, models, fields, _

class UniFaculty(models.Model):
    _name = 'uni.faculty'
    _description = 'Faculty Information c'

    name = fields.Char(string='Faculty Name')
    department_id = fields.Many2one('uni.department', string='Department')
    salary = fields.Float(String='Salary')
    course_id = fields.Char(string='Courses')
    designation = fields.Selection([('professor', 'Professor'), 
                                ('lecturer', 'Lecturer'),
                                ('adjunct_faculty', 'Adjunct Faculty')], 
                                default='lecturer')
    photo = fields.Binary(string="Photo", attachment=True)