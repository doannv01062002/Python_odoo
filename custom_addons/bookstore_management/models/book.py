# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Book(models.Model):
    _name = 'bookstore.book'
    _description = 'Book Management'

    title = fields.Char(string='Tên sách', required=True)
    author = fields.Char(string='Tác giả', required=True)
    price = fields.Float(string='Giá sách', required=True)
    publish_date = fields.Date(string='Ngày xuất bản')

