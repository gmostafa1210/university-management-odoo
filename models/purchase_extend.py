from odoo import fields, models

class PurchaseExtendDealer(models.Model):
    _inherit = 'purchase.order'

    dealer_name_ids = fields.Many2one('dealer.name', string='Dealer Name')

class PurchaseExtendProduct(models.Model):
    _inherit = 'purchase.order.line'

    product_brand_ids = fields.Many2one('product.brand', string='Product Brand', readonly=True, related='product_id.product_brand_ids')