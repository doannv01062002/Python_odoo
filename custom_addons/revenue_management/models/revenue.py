# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime


class Revenue(models.Model):
    _name = 'revenue.management'
    _description = 'Revenue Management'

    date = fields.Date(string='Ngày', required=True, default=lambda self: date.today())
    amount = fields.Float(string='Số tiền', required=True)
    description = fields.Text(string='Mô tả')

    @api.model
    def create(self, vals):
        return super(Revenue, self).create(vals)

    def write(self, vals):
        return super(Revenue, self).write(vals)

    def total_revenue(self, start_date=None, end_date=None):
        domain = []
        if start_date:
            domain.append(('date', '>=', start_date))
        if end_date:
            domain.append(('date', '<=', end_date))
        
        revenues = self.search(domain)
        total = sum(revenues.mapped('amount'))
        return total

    def get_total_revenue_by_date(self, target_date=None):
        if not target_date:
            target_date = date.today()
        
        revenues = self.search([('date', '=', target_date)])
        total = sum(revenues.mapped('amount'))
        return total

