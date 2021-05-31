from odoo import fields, models, _

class UniStaff(models.Model):
    _name = 'uni.staff'
    _description = 'Staff Information'
    _sql_constraints = [
        ('staff_code_unique', 'unique(staff_code)', 'Code already exists!')
    ]


    name = fields.Char(string='Staff Name')
    staff_code = fields.Integer(string='Staff Code')
    salary = fields.Float(string='Salary')
    department_ids = fields.Many2many('uni.department', string='Department')
    photo = fields.Binary(string='Photo', attachment=True)

    def create_orm(self):
        self.env['uni.staff'].create({
            'name' : 'test',
            'salary' : 1234,
        })

    def write_orm(self):
        all_data = self.env['uni.staff'].search([])
        for data in all_data:
            if data.name == 'test':
                data.write({
                    'name' : 'testupdated'
                })

    def unlink_orm(self):
        all_data = self.env['uni.staff'].search([])
        for data in all_data:
            if data.name == 'test' or data.name == 'testupdated':
                data.unlink()