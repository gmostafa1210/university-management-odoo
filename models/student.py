from odoo import fields, models, api, _

class UniStudent(models.Model):
    _name = 'uni.student'
    _description = 'Student Information'

    name = fields.Char(string='Student Name')
    stu_id_num = fields.Char(string='Student ID')
    department_id = fields.Many2one('uni.department', string='Department')
    credit_earn = fields.Integer(string='Credit Earned')
    course_ids = fields.Many2many('uni.course', string='Courses')
    photo = fields.Binary(string="Photo", attachment=True)