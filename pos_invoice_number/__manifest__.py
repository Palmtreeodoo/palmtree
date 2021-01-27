# -*- coding: utf-8 -*-
{
    'name': "POS Invoice Number",

    'summary': """
        A Common sequence to POS Order and its Invoice. Sequence are generated based on the prefix and number given in Point of Sale""",

    'description': """
        A Common sequence to POS Order and its Invoice. Sequence are generated based on the prefix and number given in Point of Sale
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/invoice_sequence_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # 'qweb': [
    #     'static/src/xml/*.xml'
    # ],
}
