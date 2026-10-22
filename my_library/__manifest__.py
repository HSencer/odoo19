{
    'name': 'My Library',
    'version': '19.0.1.0.0',
    'summary': 'Manage a library of books',
    'author': 'Odoo',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/book_views.xml',
    ],
    'application': True,
    'installable': True,
}
