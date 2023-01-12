# -*- coding: utf-8 -*-
{
    'name': "gg_cash_report16",

    'summary': """
        Rapport de caisse""",

    'description': """
        Long description of module's purpose
    """,

    'author': "G&G",
    'website': "http://www.gandgcorp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Advanced Reporting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'gandg_report'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv', 
        'data/custom_paper.xml',
        'views/cash_report_header.xml',
        'views/account_bank_statement_form.xml',
        'qweb/cash_report.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
