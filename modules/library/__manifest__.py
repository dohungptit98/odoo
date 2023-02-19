# -*- coding: utf-8 -*-

{
    'name': 'Library Management',
    'version': '1.0.0',
    'category': 'Library',
    'author': 'HungDo',
    'sequence': -100,
    'summary': 'Library management system',
    'description': """
        Library management system
    """,
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/library_security.xml',
        'views/menu.xml',
        'views/student_view.xml',
        'views/book_view.xml',
        'views/voucher_view.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
