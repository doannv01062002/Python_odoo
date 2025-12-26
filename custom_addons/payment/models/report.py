# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PaymentReport(models.Model):
    _name = 'payment.report'
    _description = 'Payment Report'

    title = fields.Char(string='Tiêu đề')
    total = fields.Float(string='Tổng tiền')

