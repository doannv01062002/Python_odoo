# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Employee(models.Model):
    _name = 'hr.employee'
    _description = 'Employee Management'

    employee_name = fields.Char(string='Tên nhân viên', required=True)
    employee_status = fields.Selection([
        ('active', 'Active'),
        ('inactive', 'Inactive')
    ], string='Trạng thái nhân viên', default='active', required=True)

