# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    title = fields.Char(string='Tiêu đề', required=True)
    pages = fields.Integer(string='Số trang', default=100)
    summary = fields.Text(string='Tóm tắt', copy=False)

