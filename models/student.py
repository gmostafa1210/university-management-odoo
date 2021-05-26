from odoo import fields, models, api, _
from odoo.exceptions import UserError

class UniStudent(models.Model):
    _name = 'uni.student'
    _description = 'Student Information'

    name = fields.Char(string='Student Name')
    stu_id_num = fields.Char(string='Student ID')
    department_id = fields.Many2one('uni.department', string='Department')
    credit_earn = fields.Integer(string='Credit Earned')
    course_ids = fields.Many2many('uni.course', string='Courses')
    photo = fields.Binary(string="Photo", attachment=True)

    def check_orm(self):
        #ORM
        all_data = self.env['uni.course'].search([('credit_hour','=',3)])
        for data in all_data:
            print(data.course_name)

        raise UserError(_(all_data))