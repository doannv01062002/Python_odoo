# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Exam(models.Model):
    _name = 'school.exam'
    _description = 'Exam Management'

    exam_date = fields.Date(string='Ngày thi', required=True)
    subject = fields.Char(string='Tên môn học', required=True)
    school_id = fields.Many2one('school.management', string='Trường học', required=True)
    students = fields.Many2many('school.student', string='Học viên tham gia')

    def calculate_average_score_for_exam(self):
        if not self.students:
            return 0.0
        
        total_score = sum(self.students.mapped('score')) if self.students.mapped('score') else 0.0
        count = len(self.students)
        
        if count > 0:
            return total_score / count
        return 0.0

