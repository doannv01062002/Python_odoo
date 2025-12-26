# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityCourse(models.Model):
    _name = 'university.course'
    _description = 'University Course'

    name = fields.Char(string='Tên khóa học')
    credit = fields.Integer(string='Tín chỉ')

