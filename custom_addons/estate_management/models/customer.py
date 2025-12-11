# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Customer(models.Model):
    _name = 'estate.customer'
    _description = 'Customer'

    name = fields.Char(string='Tên khách hàng', required=True)
    property_ids = fields.One2many('estate.property', 'customer_id', string='Bất động sản')

