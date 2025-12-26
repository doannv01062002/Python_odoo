# _*_ codeing: utf-8 _*_

{
    'name': "Quản lý tài chính",
    'summary': "Module quản lý yêu cầu hoàn tiền chi phí công tác",
    'description': """ Module cho phép nhân viên gửi yêu cầu hoàn tiền cho các chi phí công tác/mua sắm với kiểm sóa bảo mật theo vai trò""",
    'website': "https://www.yourcompany.com",
    'category': 'Accounting',
    'version': '0.1',
    'depends': ['base'],
    'data':[
        'security/finance_groups.xml',
        'security/ir.model.access.csv',
        'security/finance_rules.xml',
        'views/views.xml'
    ],
    'installable': True,
    'application': True,
    'author': 'Văn Đoan',
    'license': 'LGPL-3'
}