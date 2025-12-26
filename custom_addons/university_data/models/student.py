# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityStudent(models.Model):
    _name = 'university.student'
    _description = 'University Student'

    name = fields.Char(string='Tên sinh viên')
    year = fields.Integer(string='Năm học')

