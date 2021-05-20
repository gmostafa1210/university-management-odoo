from odoo import fields, models

class SaleInherit(models.Model):
    _inherit = 'sale.order'

    customer_notes = fields.Text(string='Customer Notes')
    