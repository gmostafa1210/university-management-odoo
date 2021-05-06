from odoo import fields, models, api, _

class UniStudent(models.Model):
    _name = 'uni.student'
    _description = 'Student Information'

    name = fields.Char(string='Student Name')
    stu_id = fields.Char(string='student ID')
    department = fields.Char(string='Department')
    credit_earn = fields.Integer(string='Credit Earned')
    course_taken = fields.Char(string='Ongoing Courses')
    photo = fields.Binary(string="Photo", attachment=True)