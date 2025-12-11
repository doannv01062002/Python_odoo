# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class Employee(models.Model):
    _name = 'employee.management'
    _description = 'Employee Management'

    name = fields.Char(string='Tên nhân viên', required=True)
    position = fields.Selection([
        ('manager', 'Manager'),
        ('developer', 'Developer'),
        ('hr', 'HR')
    ], string='Vị trí', required=True)
    salary = fields.Float(string='Lương', default=1000, required=True)
    start_date = fields.Date(string='Ngày bắt đầu', default=lambda self: date.today(), required=True)

