from odoo import api, models, fields, _

class UniFaculty(models.Model):
    _name = 'uni.faculty'
    _description = 'Faculty Information c'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Full Name', compute='_get_full_name')
    department_id = fields.Many2one('uni.department', string='Department')
    salary = fields.Float(String='Salary')
    course_id = fields.Char(string='Courses')
    designation = fields.Selection([('professor', 'Professor'), 
                                ('lecturer', 'Lecturer'),
                                ('adjunct_faculty', 'Adjunct Faculty')], 
                                default='lecturer')
    photo = fields.Binary(string="Photo", attachment=True)

    def _get_full_name(self):
        first_name = ''
        last_name = ''
        for item in self:
            if item.first_name:
                first_name = item.first_name
            if item.last_name:
                last_name = item.last_name

            item.name = first_name + ' ' + last_name

    