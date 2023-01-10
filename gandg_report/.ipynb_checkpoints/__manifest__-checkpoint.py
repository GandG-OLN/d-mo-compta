{
    'name': 'GandG external layout',
    'author': 'Gandg',
    'version': '1.4.0',
    'category': 'Tools',
    'description': """
    permet de faire une descripotion ...
""",
    'summary': 'Module de ...',
    'sequence': 9,
    'depends': ['base', 'account'],
    'data': [
        #'security/ir.model.access.csv',
        'data/custom_paper.xml',
        'views/custom_header_footer.xml',
        'views/custom_external_layout.xml',
    ],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
