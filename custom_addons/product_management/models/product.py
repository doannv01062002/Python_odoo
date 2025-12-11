# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Product(models.Model):
    _name = 'product.management'
    _description = 'Product Management'

    product_name = fields.Char(string='Tên sản phẩm', required=True)
    product_price = fields.Float(string='Giá sản phẩm', default=0, required=True)
    product_quantity = fields.Integer(string='Số lượng sản phẩm', default=0, required=True)

