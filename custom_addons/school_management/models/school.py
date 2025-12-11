# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'school.management'
    _description = 'School Management'

    name = fields.Char(string='Tên trường học', required=True)
    location = fields.Char(string='Địa chỉ trường học')
    start_date = fields.Date(string='Ngày thành lập')

    student_ids = fields.One2many('school.student', 'school_id', string='Học viên')
    exam_ids = fields.One2many('school.exam', 'school_id', string='Kỳ thi')

    @api.model
    def create_school(self, vals):
        return self.create(vals)

    def update_school(self, vals):
        return self.write(vals)

