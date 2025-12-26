# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CompanyEmployee(models.Model):
    _name = 'company.employee'
    _description = 'Company Employee'

    name = fields.Char(string='Tên nhân viên', required=True)
    position = fields.Selection([
        ('staff', 'Staff'),
        ('leader', 'Leader'),
        ('manager', 'Manager')
    ], string='Vị trí', default='staff')
    is_active = fields.Boolean(string='Active', default=True)

