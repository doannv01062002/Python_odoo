# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class EduClassroom(models.Model):
    _name = 'edu.classroom'
    _description = 'Phòng học'

    name = fields.Char(string='Tên phòng', required=True)
    capacity = fields.Integer(string='Sức chứa tối đa', default=30)

    @api.constrains('capacity')
    def _check_capacity(self):
        for r in self:
            if r.capacity <= 0:
                raise ValidationError("Sức chứa phòng học phải lớn hơn 0!")
