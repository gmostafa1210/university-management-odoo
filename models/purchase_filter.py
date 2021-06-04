from odoo import models, fields, api,  _
from odoo.exceptions import UserError 

class PurchaseFilter(models.TransientModel):
    _name = 'purchase.filter'
    _description = 'Purchase Filter'

    filter_purchase = fields.Boolean(string='Filter Received GT Billed')

    def get_custom_purchase_filter(self):
        my_list = []
        if self.filter_purchase:
            purchase_filter_ids = self.env['purchase.order.line'].search([])
            for data in purchase_filter_ids:
                if data.qty_received > 0 and data.qty_received > data.qty_invoiced:
                    my_list.append(data.order_id.id)

            return{
                'name': 'Purchase Filter',
                'type': 'ir.actions.act_window',
                'res_model': 'purchase.order',
                'view_mode': 'tree,form',
                'domain': [('id','in',my_list)]
            }
        