from odoo import models, fields, api,  _
from odoo.exceptions import UserError 

class PurchaseFilter(models.TransientModel):
    _name = 'purchase.filter'
    _description = 'Purchase Filter'

    filter_purchase = fields.Boolean(string='Filter Received GT Billed')
    
    date_from = fields.Date(string="From")
    date_to = fields.Date(string="To")

    def get_custom_purchase_filter(self):
        q_list = []
        d_list = []

        date_filter_data = self.env['purchase.order'].search([('date_approve','>=',self.date_from),('date_approve','>=',self.date_from)])
        for data in date_filter_data:
            d_list.append(data.id)

        if self.filter_purchase:
            purchase_filter_data = self.env['purchase.order.line'].search([])
            for data in purchase_filter_data:
                if data.qty_received > 0 and data.qty_received > data.qty_invoiced:
                    q_list.append(data.order_id.id)

        q_list = set(q_list)
        d_list = set(d_list)
        my_list = q_list.intersection(d_list)
        my_list = list(my_list)

        return{
            'name': 'Purchase Filter',
            'type': 'ir.actions.act_window',
            'res_model': 'purchase.order',
            'view_mode': 'tree,form',
            'domain': [('id','in',my_list)]
        }
        