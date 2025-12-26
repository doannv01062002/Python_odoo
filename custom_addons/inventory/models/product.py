# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InventoryProduct(models.Model):
    _name = 'inventory.product'
    _description = 'Inventory Product'

    name = fields.Char(string='Tên sản phẩm')
    price = fields.Float(string='Giá')
    stock = fields.Integer(string='Tồn kho')

