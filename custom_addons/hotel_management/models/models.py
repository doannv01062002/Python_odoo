# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HotelRoomType(models.Model):
    _name = 'hotel.room.type'
    _description = 'Loại phòng'

    name = fields.Char(string='Tên loại', required=True)
    code = fields.Char(string='Mã loại')


class HotelService(models.Model):
    _name = 'hotel.service'
    _description = 'Dịch vụ đi kèm'

    name = fields.Char(string='Tên dịch vụ', required=True)
    price = fields.Integer(string='Giá dịch vụ', default=1)

    _sql_constraints = [
        ('service_price_positive', 'CHECK(price > 0)', 'Giá dịch vụ phải lớn hơn 0.')
    ]


class HotelCustomer(models.Model):
    _name = 'hotel.customer'
    _description = 'Khách hàng khách sạn'
    _order = 'name asc'

    name = fields.Char(string='Tên khách', required=True)
    identity_card = fields.Char(string='Số CMND/CCCD')
    phone = fields.Char(string='Số điện thoại')

    _sql_constraints = [
        ('identity_card_unique', 'UNIQUE(identity_card)', 'Số CMND/CCCD đã tồn tại.')
    ]


class HotelRoom(models.Model):
    _name = 'hotel.room'
    _description = 'Phòng khách sạn'

    name = fields.Char(string='Số phòng', required=True)
    floor = fields.Integer(string='Tầng')
    price_per_night = fields.Integer(string='Giá/đêm', default=500000)
    status = fields.Selection(
        [('available', 'Trống'), ('occupied', 'Đang ở'), ('maintenance', 'Bảo trì')],
        string='Trạng thái',
        default='available',
    )
    type_id = fields.Many2one('hotel.room.type', string='Loại phòng', required=True)

    _sql_constraints = [
        ('room_name_unique', 'UNIQUE(name)', 'Tên phòng phải là duy nhất.'),
        ('room_price_positive', 'CHECK(price_per_night > 0)', 'Giá phòng phải lớn hơn 0.')
    ]


class HotelBooking(models.Model):
    _name = 'hotel.booking'
    _description = 'Phiếu đặt phòng'

    code = fields.Char(string='Mã booking')
    check_in = fields.Date(string='Ngày nhận phòng', default=fields.Date.context_today)
    check_out = fields.Date(string='Ngày trả phòng')
    duration = fields.Integer(string='Số đêm lưu trú', compute='_compute_duration', store=True)
    total_amount = fields.Integer(string='Tổng thành tiền', compute='_compute_total_amount', store=True)
    state = fields.Selection(
        [('draft', 'Nháp'), ('confirmed', 'Đã xác nhận'), ('done', 'Hoàn thành')],
        string='Trạng thái',
        default='draft',
    )

    customer_id = fields.Many2one('hotel.customer', string='Khách hàng', required=True)
    room_id = fields.Many2one('hotel.room', string='Phòng', required=True)
    service_ids = fields.Many2many('hotel.service', string='Dịch vụ thêm')

    @api.depends('check_in', 'check_out')
    def _compute_duration(self):
        for record in self:
            if record.check_in and record.check_out:
                record.duration = max((record.check_out - record.check_in).days, 0)
            else:
                record.duration = 0

    @api.depends('duration', 'room_id.price_per_night', 'service_ids.price')
    def _compute_total_amount(self):
        for record in self:
            room_total = (record.room_id.price_per_night or 0) * (record.duration or 0)
            service_total = sum(record.service_ids.mapped('price'))
            record.total_amount = room_total + service_total

    @api.onchange('room_id')
    def _onchange_room_id_warning(self):
        for record in self:
            if record.room_id and record.room_id.status == 'maintenance':
                return {
                    'warning': {
                        'title': 'Cảnh báo phòng bảo trì',
                        'message': 'Phòng này đang bảo trì, vui lòng chọn phòng khác!'
                    }
                }

    @api.onchange('check_in')
    def _onchange_check_in(self):
        for record in self:
            if record.check_in:
                record.check_out = record.check_in + timedelta(days=1)

    @api.constrains('check_in', 'check_out')
    def _check_dates(self):
        for record in self:
            if record.check_in and record.check_out and record.check_out <= record.check_in:
                raise ValidationError('Ngày trả phòng không hợp lệ!')

    @api.constrains('room_id')
    def _check_room_status(self):
        for record in self:
            if record.room_id and record.room_id.status == 'occupied':
                raise ValidationError('Phòng này đang có khách ở!')
