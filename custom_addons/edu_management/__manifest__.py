# -*- coding: utf-8 -*-
{
    'name': 'Edu Management',
    'version': '1.0',
    'summary': 'Educational Management Module for Managing Courses and Classes',
    'description': """
        Hệ thống quản lý giáo dục:
        - Quản lý Khóa học, Môn học
        - Quản lý Lớp học, Giảng viên, Học viên
        - Tính toán học phí, doanh thu
    """,
    'category': 'Education',
    'author': 'Antigravity',
    'depends': ['base', 'product'],
    'data': [
        'security/edu_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/edu_course_views.xml',
        'views/edu_session_views.xml',
        'views/edu_classroom_views.xml',
        'views/edu_menus.xml',
        'views/res_partner_views.xml',
        'views/product_views.xml',
    ],
    'demo': [
        'data/edu_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
