# -*- coding: utf-8 -*-
{
    'name': "Estate Management",
    'summary': "Module quản lý bất động sản",
    'description': """
        Module quản lý bất động sản với mối quan hệ Many2one/One2many
    """,

    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'security/estate_record_rules.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'author': 'Văn Đoan',
    'license': 'LGPL-3'
}

