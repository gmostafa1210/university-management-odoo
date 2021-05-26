from odoo import fields, models

class UniStaffInherit(models.Model):
    _inherit = 'uni.staff'

    address = fields.Text(string='Address')
    