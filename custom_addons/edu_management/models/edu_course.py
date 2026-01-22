# -*- coding: utf-8 -*-
from odoo import models, fields, api

class EduCourse(models.Model):
    _name = 'edu.course'
    _description = 'Khóa học'

    name = fields.Char(string='Tên khóa học', required=True)
    description = fields.Html(string='Mô tả chi tiết')
    active = fields.Boolean(string='Đang hoạt động', default=True)
    
    subject_id = fields.Many2one('edu.subject', string='Chuyên ngành')
    responsible_id = fields.Many2one('res.users', string='Người phụ trách', default=lambda self: self.env.user)
    session_ids = fields.One2many('edu.session', 'course_id', string='Các lớp học')
    session_count = fields.Integer(string='Số lượng lớp', compute='_compute_session_count')
    
    def _compute_session_count(self):
        for r in self:
            r.session_count = len(r.session_ids)

    _sql_constraints = [
        ('name_unique', 'UNIQUE(name)', 'Tên khóa học phải là duy nhất!'),
    ]

    @api.onchange('responsible_id')
    def _onchange_responsible_id(self):
        if self.responsible_id and self.responsible_id.email:
            contact_info = f"<p>Liên hệ giảng viên: {self.responsible_id.email}</p>"
            if self.description:
                self.description += contact_info
            else:
                self.description = contact_info
