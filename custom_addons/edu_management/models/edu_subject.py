# -*- coding: utf-8 -*-
from odoo import models, fields

class EduSubject(models.Model):
    _name = 'edu.subject'
    _description = 'Môn học / Chuyên ngành'

    name = fields.Char(string='Tên chuyên ngành', required=True)
    description = fields.Text(string='Mô tả')
    
    course_ids = fields.One2many('edu.course', 'subject_id', string='Danh sách khóa học')
