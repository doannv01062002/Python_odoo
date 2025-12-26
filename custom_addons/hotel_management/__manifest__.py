# -*- coding: utf-8 -*-
{
    'name': 'hotel_management',
    'summary': 'Quản lý khách sạn: phòng, khách hàng, booking.',
    'description': 'Module quản lý phòng khách sạn, khách hàng và phiếu đặt phòng kèm dịch vụ.',
    'author': 'My Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Services/Hotel',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/hotel_groups.xml',
        'security/ir.model.access.csv',
        'security/hotel_record_rules.xml',
        'views/hotel_views.xml',
        'views/hotel_menus.xml',
    ],
    'demo': [],
    'application': True,
    'license': 'LGPL-3',
    'installable': True,
}
