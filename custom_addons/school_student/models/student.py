# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'School Student'

    name = fields.Char(string='Tên học sinh', required=True)
    age = fields.Integer(string='Tuổi')
    bio = fields.Text(string='Tiểu sử')
    is_active = fields.Boolean(string='Active', default=True)

