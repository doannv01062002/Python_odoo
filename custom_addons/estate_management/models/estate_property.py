# -*- coding: utf-8 -*-

from odoo import models, fields, api


class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Tên bất động sản', required=True)
    customer_id = fields.Many2one('estate.customer', string='Khách hàng', required=True)
    address = fields.Char(string='Địa chỉ')
    price = fields.Float(string='Giá')

