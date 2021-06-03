from odoo import fields, models, api, _
from odoo.exceptions import UserError

class UniStudent(models.Model):
    _name = 'uni.student'
    _description = 'Student information.'

    name = fields.Char(string='Student Name')
    stu_id_num = fields.Char(string='Student ID')
    credit_earn = fields.Integer(string='Credit Earned', compute='_get_credit')
    photo = fields.Binary(string="Photo", attachment=True)

    course_ids = fields.Many2many('uni.course', string='Courses')
    department_id = fields.Many2one('uni.department', string='Department', domain=[('engr_dept','=',True)])
    faculty_assign_line = fields.One2many('uni.student.line', 'faculty_assign_id', string='Faculty Assign Line')

    f_id = fields.Many2one('uni.faculty', string='New faculty')

    def check_orm(self):
        #ORM
        all_data = self.env['uni.course'].search([('credit_hour','=',3)])
        for data in all_data:
            print(data.course_name)

        raise UserError(_(all_data))

    def check_sql(self): 
        # SQL
        self.env.cr.execute(""" select credit_hour from uni_course; """,)
        sql_data = self.env.cr.fetchall()

        raise UserError(_(sql_data))

    def calculate_credit(self):
        total_credit = 0
        all_data = self.env['uni.course'].search([('id','in',self.course_ids.ids)])
        for data in all_data:
            total_credit += data.credit_hour

        return total_credit

    def _get_credit(self):
        for item in self:
            item.credit_earn = item.calculate_credit()


class UniStudentLine(models.Model):
    _name = 'uni.student.line'
    _description = 'Student faculty information.'

    faculty_id = fields.Many2one('uni.faculty', string='Faculty Name')
    faculty_assign_id = fields.Many2one('uni.student', string='Assign ID')