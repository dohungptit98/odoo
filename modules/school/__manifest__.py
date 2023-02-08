{
    'name': 'School Management',
    'version': '1.1',
    'summary': 'Management',
    'sequence': '1',
    'author': 'The Odoo Show',
    'description': """
        App Quan Ly Truong Hoc
    """,
    'depends': [],
    'data': [
        'views/school_information.xml',
        'views/class_information.xml',
        'views/student_information.xml',
        'views/subject_information.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}