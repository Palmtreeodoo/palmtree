# -*- coding: utf-8 -*-
{
    'name': "Palm Tree Weight Scale",

    'summary': """
        Compute weight based on barcodes with prices""",

    'description': """
        This module extends Odoo Point Of Sale features, to allow to scan barcode with price and to compute according quantity.
        This module add a new option:

* 'Priced Product (Computed Weight)' (type='price_to_weight'). A price is 
  extracted from the barcode, and a new line with the given price, and a
  computed quantity (Price / Unit Price) is added to the current order.
* Also generates barcode while creating product
    """,

    'author': "Loyal IT Solutions",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'barcodes', 'product', 'point_of_sale'],

    # always loaded
    'data': [
        'data/barcode_patterns.xml',
        'data/ir_sequence_data.xml',
        'security/ir.model.access.csv',
        'views/barcode_settings.xml',
        'views/product.xml',
        'views/templates.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
}
