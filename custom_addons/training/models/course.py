# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TrainingCourse(models.Model):
    _name = 'training.course'
    _description = 'Training Course'

    name = fields.Char(string='Tên khóa học', required=True)
    duration = fields.Integer(string='Thời lượng')
    active = fields.Boolean(string='Active', default=True)

