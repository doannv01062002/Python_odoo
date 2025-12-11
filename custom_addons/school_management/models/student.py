# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'school.student'
    _description = 'Student Management'

    name = fields.Char(string='Tên học viên', required=True)
    age = fields.Integer(string='Tuổi học viên')
    school_id = fields.Many2one('school.management', string='Trường học', required=True)
    score = fields.Float(string='Điểm thi')

    exam_ids = fields.Many2many('school.exam', string='Kỳ thi tham gia')

    @api.model
    def create_student(self, vals):
        return self.create(vals)

    def update_student(self, vals):
        return self.write(vals)

    def calculate_average_score(self, exam_id=None):
        if exam_id:
            exam = self.env['school.exam'].browse(exam_id)
            students_in_exam = exam.student_ids.filtered(lambda s: s.id == self.id)
            if students_in_exam:
                return self.score if self.score else 0.0
        return self.score if self.score else 0.0

