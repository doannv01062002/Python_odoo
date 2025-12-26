# -*- coding: utf-8 -*-
{
    'name': "University Data",
    'summary': "Module quản lý đại học",
    'description': """
        Module quản lý đại học với models university.course và university.student
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

