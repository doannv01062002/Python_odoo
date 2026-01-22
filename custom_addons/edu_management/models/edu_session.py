# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import timedelta

class EduSession(models.Model):
    _name = 'edu.session'
    _description = 'Lớp học'

    code = fields.Char(string='Mã lớp', required=True, copy=False, readonly=True, default='New')
    name = fields.Char(string='Tên lớp', required=True)
    start_date = fields.Date(string='Ngày bắt đầu', default=fields.Date.today, required=True)
    duration = fields.Integer(string='Thời lượng (ngày)', default=1)
    end_date = fields.Date(string='Ngày kết thúc', compute='_compute_end_date', store=True)
    
    seats = fields.Integer(string='Số ghế', default=10)
    taken_seats = fields.Float(string='% Đã đăng ký', compute='_compute_taken_seats')

    active = fields.Boolean(string='Đang hoạt động', default=True)

    course_id = fields.Many2one('edu.course', string='Khóa học', required=True)
    instructor_id = fields.Many2one('res.partner', string='Giảng viên', domain=[('is_instructor', '=', True)])
    classroom_id = fields.Many2one('edu.classroom', string='Phòng học')
    
    attendee_ids = fields.Many2many('res.partner', string='Danh sách học viên')
    attendee_count = fields.Integer(string='Số học viên', compute='_compute_attendee_count', store=True)

    @api.model
    def create(self, vals):
        if vals.get('code', 'New') == 'New':
            vals['code'] = self.env['ir.sequence'].next_by_code('edu.session') or 'New'
        return super(EduSession, self).create(vals)

    @api.model
    def default_get(self, fields_list):
        defaults = super(EduSession, self).default_get(fields_list)
        if 'start_date' in fields_list:
             defaults['start_date'] = fields.Date.today() + timedelta(days=1)
        return defaults

    def name_get(self):
        result = []
        for r in self:
            name = f"[{r.code}] {r.name} - {r.start_date}"
            result.append((r.id, name))
        return result

    state = fields.Selection([
        ('draft', 'Dự thảo'),
        ('open', 'Mở đăng ký'),
        ('done', 'Kết thúc'),
        ('cancel', 'Đã hủy')
    ], string='Trạng thái', default='draft', required=True, tracking=True)

    product_id = fields.Many2one('product.product', string='Học phí', domain=[('is_edu_fee', '=', True)])
    revenue = fields.Monetary(string='Doanh thu', currency_field='currency_id', compute='_compute_revenue', store=True)
    currency_id = fields.Many2one('res.currency', string='Tiền tệ', default=lambda self: self.env.company.currency_id)

    def action_open(self):
        for r in self:
            if not r.instructor_id:
                raise ValidationError("Vui lòng chọn Giảng viên trước khi mở lớp!")
            if not r.classroom_id:
                raise ValidationError("Vui lòng chọn Phòng học trước khi mở lớp!")
            r.state = 'open'

    def action_done(self):
        for r in self:
            r.state = 'done'

    def action_cancel(self):
        for r in self:
            if r.state == 'done':
                raise ValidationError("Không thể hủy lớp học đã Đóng/Kết thúc!")
            r.state = 'cancel'
            
    def action_draft(self):
        for r in self:
            r.state = 'draft'

    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        default = dict(default or {})
        default.update({
            'state': 'draft',
            'attendee_ids': [],
            'code': 'New',
        })
        return super(EduSession, self).copy(default)

    def unlink(self):
        for r in self:
            if r.state not in ('draft', 'cancel'):
                raise ValidationError("Chỉ được xóa lớp học ở trạng thái Dự thảo hoặc Đã hủy!")
        return super(EduSession, self).unlink()

    @api.depends('attendee_ids', 'product_id')
    def _compute_revenue(self):
        for r in self:
            if r.product_id:
                r.revenue = len(r.attendee_ids) * r.product_id.list_price
            else:
                r.revenue = 0

    @api.model
    def _name_search(self, name, domain=None, operator='ilike', limit=None, order=None):
        domain = domain or []
        if name:
            # Search by Code OR Name OR Instructor Name
            domain = ['|', '|', 
                      ('code', operator, name), 
                      ('name', operator, name),
                      ('instructor_id.name', operator, name)] + domain
        return self._search(domain, limit=limit, order=order)

    @api.depends('start_date', 'duration')
    def _compute_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue
            r.end_date = r.start_date + timedelta(days=r.duration)

    @api.depends('attendee_ids')
    def _compute_attendee_count(self):
        for r in self:
            r.attendee_count = len(r.attendee_ids)

    @api.depends('seats', 'attendee_ids')
    def _compute_taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats

    @api.onchange('course_id')
    def _onchange_course_id(self):
        if self.course_id and self.course_id.responsible_id.partner_id:
            # Check if the responsible user's partner is an instructor
            partner = self.course_id.responsible_id.partner_id
            if partner.is_instructor:
                self.instructor_id = partner

    @api.onchange('seats')
    def _onchange_seats(self):
        if self.seats < 0:
            return {
                'warning': {
                    'title': "Giá trị không hợp lệ",
                    'message': "Số ghế không được nhỏ hơn 0",
                },
                'value': {
                    'seats': 0
                }
            }

    @api.constrains('instructor_id', 'attendee_ids')
    def _check_instructor_not_in_attendees(self):
        for r in self:
            if r.instructor_id and r.instructor_id in r.attendee_ids:
                raise ValidationError("Giảng viên phụ trách không được có tên trong danh sách học viên!")

    @api.constrains('duration', 'start_date')
    def _check_duration(self):
        for r in self:
            if r.duration <= 0:
                raise ValidationError("Thời lượng khóa học phải lớn hơn 0!")
            if not r.start_date:
                raise ValidationError("Ngày bắt đầu không được để trống!")

    @api.constrains('classroom_id', 'start_date', 'end_date')
    def _check_classroom_overlap(self):
        for r in self:
            if r.classroom_id and r.start_date and r.end_date:
                # Find other sessions in the same room that overlap
                domain = [
                    ('classroom_id', '=', r.classroom_id.id),
                    ('id', '!=', r.id),
                    ('start_date', '<=', r.end_date),
                    ('end_date', '>=', r.start_date)
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(f"Phòng {r.classroom_id.name} đã có lớp học khác trong khoảng thời gian này!")

    @api.constrains('seats')
    def _check_seats(self):
        for r in self:
            if r.seats < 0:
                raise ValidationError("Số lượng ghế không được nhỏ hơn 0!")
