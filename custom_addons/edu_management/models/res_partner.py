# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_instructor = fields.Boolean(string='Là giảng viên', default=False)
    
    teaching_session_ids = fields.One2many('edu.session', 'instructor_id', string='Các lớp đang dạy')
    teaching_session_count = fields.Integer(string='Số lớp đang dạy', compute='_compute_teaching_session_count')
    
    def _compute_teaching_session_count(self):
        for r in self:
            r.teaching_session_count = len(r.teaching_session_ids)
