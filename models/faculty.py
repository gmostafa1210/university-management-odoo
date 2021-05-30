from odoo import api, models, fields, _
from odoo.exceptions import UserError

class UniFaculty(models.Model):
    _name = 'uni.faculty'
    _description = 'Faculty Information c'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Full Name', compute='_get_full_name')
    department_id = fields.Many2one('uni.department', string='Department')
    salary = fields.Float(String='Salary')
    designation = fields.Selection([('professor', 'Professor'), 
                                ('lecturer', 'Lecturer'),
                                ('adjunct_faculty', 'Adjunct Faculty')], 
                                default='lecturer')
    photo = fields.Binary(string="Photo", attachment=True)

    course_ids = fields.Many2many('uni.course', string='Courses')

    have_address = fields.Boolean(string='Have Address')
    address = fields.Text(string='Address')

    def test_user_error(self):
        raise UserError(_('Error Raised!'))

    def full_name(self):
        first_name = ''
        last_name = ''
        if self.first_name:
            first_name = self.first_name
        if self.last_name:
            last_name = self.last_name

        return first_name + ' ' + last_name
        
    def _get_full_name(self):
        for item in self:
            item.name = item.full_name()

    