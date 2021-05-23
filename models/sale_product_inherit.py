from odoo import fields, models

class SaleProductInherit(models.Model):
    _inherit = 'product.template'

    product_brand_ids = fields.Many2one('product.brand', string='Product Brand')
    dealer_name_ids = fields.Many2one('dealer.name', string='Dealer Name')
    