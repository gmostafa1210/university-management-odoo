from odoo import fields, models

class ProductBrand(models.Model):
    _name = 'product.brand'
    _description = 'Product Brand Description.'
    _rec_name = 'product_brand'

    product_brand = fields.Char(string='Product Brand Name')

class DealerName(models.Model):
    _name = 'dealer.name'
    _description = 'Dealer Name Description.'
    _rec_name = 'dealer_name'

    dealer_name = fields.Char(string='All Dealer Name')
    