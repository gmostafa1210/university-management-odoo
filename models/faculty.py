from odoo import api, models, fields, _
from odoo.exceptions import UserError

class UniFaculty(models.Model):
    _name = 'uni.faculty'
    _description = 'Faculty Information c'

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Full Name', compute='_get_full_name')
    department_id = fields.Many2one('uni.department', string='Department')
    faculty_code = fields.Integer(string='Faculty Code')
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


    # unique faculty code check (to be solve)

    @api.onchange('faculty_code')
    def onchange_faculty_code_unique_check(self):
        all_code = self.env['uni.faculty'].search([])
        if self.faculty_code:
            for val in all_code:
                if self.faculty_code == val.faculty_code:
                    raise UserError(_("Code already exists!"))

    def write(self, values):
        all_codes = self.env ['uni.faculty'].search([('faculty_code', '=', values['faculty_code'])])
        if 'faculty_code' in values.keys():
            if all_codes:
                raise UserError(_("Code already exists!"))
            else:
                return super(UniFaculty, self).write(values)

    @api.model 
    def create(self, values):
        all_codes = self.env ['uni.faculty'].search([('faculty_code', '=', values['faculty_code'])])
        if all_codes:
            raise UserError(_("Code already exists!"))
        else:
            return super(UniFaculty, self).create(values)


    # unique faculty code check (to be solve)

    # @api.onchange('faculty_code')
    # def faculty_code_unique_check(self):
    #     all_data = self.env['uni.faculty'].search([])
    #     if self.faculty_code:
    #         for data in all_data:
    #             if self.faculty_code == data.faculty_code:
    #                 raise UserError(_("Code already in use!"))
    
    # @api.model
    # def create(self, values):
    #     all_data = self.env['uni.faculty'].search([])
    #     for data in all_data:
    #         print('########c1')
    #         print(data.faculty_code)
    #         if data.faculty_code == values['faculty_code']:
    #             raise UserError(_("Code already in use!"))
    #     print("########c2")
    #     return super(UniFaculty, self).create(values)

    # def write(self, values):
    #     print("*******w1")
    #     all_data = self.env['uni.faculty'].search([])
    #     if 'faculty_code' in values.keys():
    #         for data in all_data:
    #             print('*******w2')
    #             print(data.faculty_code)
    #             if values['faculty_code'] == data.faculty_code:
    #                 raise UserError(_("Code already in use!"))
    #     return super(UniFaculty, self).write(values)
    