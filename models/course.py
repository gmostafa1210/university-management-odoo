from odoo import models, fields, api,  _
from odoo.exceptions import UserError 

class UniCourse(models.Model):
    _name = 'uni.course'
    _description = 'Course Information'
    _rec_name = 'course_name'

    course_name = fields.Char(string='Course Name')
    course_code = fields.Char(string='Course Code')
    course_description = fields.Text(string='Course Description')
    credit_hour = fields.Integer(string='Credit')
    have_lab = fields.Char(string='Lab')

    @api.model
    def create(self, values):
        if values['credit_hour'] != 3 and values['credit_hour'] != 4:
            raise UserError(_('Invalid input. Please input 3 or 4.'))
        return super(UniCourse, self).create(values)

    def write(self, values):
        if 'credit_hour' in values.keys():
            if values['credit_hour'] != 3 and values['credit_hour'] != 4:
                raise UserError(_('Invalid input. Please input 3 or 4.'))
        return super(UniCourse, self).write(values)

    @api.onchange('credit_hour')
    def lab_assign(self):
        if self.credit_hour:
            if self.credit_hour == 3:
                self.have_lab = 'No'
            elif self.credit_hour == 4:
                self.have_lab = 'Yes'