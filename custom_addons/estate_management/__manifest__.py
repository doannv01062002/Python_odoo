# -*- coding: utf-8 -*-
{
    'name': "Estate Management",
    'summary': "Module quản lý bất động sản",
    'description': """
        Module quản lý bất động sản với mối quan hệ Many2one/One2many
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
}

