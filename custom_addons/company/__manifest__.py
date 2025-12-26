# -*- coding: utf-8 -*-
{
    'name': "Company",
    'summary': "Module quản lý nhân viên công ty",
    'description': """
        Module quản lý nhân viên công ty với model company.employee
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

