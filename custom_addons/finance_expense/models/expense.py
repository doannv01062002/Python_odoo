# _*_ coding: utf-8 _*_

from odoo import models, fields

class FinanceExpense(models.Model):
    _name = "finance.expense"
    _description = "Yêu cầu hoàn chi phí"
    _order = "create_date desc"

    name = fields.Char(
        string = 'tên khoản chi',
        required = True,
        help = "Mô tả ngắn gọn khoản chi phí"
    )

    expense_type = fields.Selection(
        string = 'Loại  chi phí',
        selection = [
            ('food', 'Ăn uống'),
            ('transport', 'Di chuyển'),
            ('other', 'Khác')
        ],
        required = True,
        help = "Phân loại chi phí"
    )

    amount = fields.Float(
        string = 'Số tiền',
        required = True,
        help = "Số tiền cần hoàn trả",
        default = 0.0
    )

    state = fields.Selection(
        string = 'Trạng thái',
        selection = [
            ('draft', 'Bản nháp'),
            ('submitted', 'Đã gửi'),
            ('approved', 'Đã duyệt'),
            ('paid', 'Đã thanh toán'),
            ('rejected', 'Từ chối')
        ],
        default = 'draft',
        help = "Trạng thái xử lý của yêu cầu hoàn chi phí"
    )

    approval_note = fields.Text(
        string = 'Ghi chú duyệt',
        groups = 'finance_expense.group_finance_manager',
        help = "Ghi chú từ người duyệt về yêu cầu hoàn chi phí"
    )

    create_date = fields.Datetime(
        string = 'Ngày tạo',
        readonly = True,
    )

    write_date = fields.Datetime(
        string = 'Ngày cập nhật',
        readonly = True,
    )