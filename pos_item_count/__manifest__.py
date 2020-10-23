# -*- coding: utf-8 -*-
{
    'name': "POS Items Count",

    'summary': """
        POS Items Count module is used to show total number of items in POS cart per order.""",

    'description': """
        POS Items Count module is used to show total number of items in POS cart per order.
        This module helps the POS user to keep a count on the number of items in POS cart per order as well as 
        makes it convenient for POS user or customer to verify item(s) count.
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        'static/src/xml/count_item_widget.xml',
    ],
}
