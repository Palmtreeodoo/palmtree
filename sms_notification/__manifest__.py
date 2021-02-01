# -*- coding: utf-8 -*-
{
    'name': "SMS Notification",

    'summary': """
        Customized SMS form and its template for sending messages""",

    'description': """
        Customized SMS form and its template for sending messages to individual person or group of people
    """,

    'author': "Loyal IT Solutions Pvt Ltd",
    'website': "http://www.loyalitsolutions.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '13.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'stock', 'sms', 'sale', 'point_of_sale'],

    # always loaded
    'data': [
        'security/ir_rule.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'edi/general_messages.xml',
        'edi/sms_template_for_order_creation.xml',
        'edi/sms_template_for_order_confirm.xml',
        'edi/sms_template_for_session_close.xml',
        'edi/sms_template_for_invoice_validate.xml',
        'edi/sms_template_for_delivery_done.xml',
        'edi/sms_template_for_invoice_payment_register.xml',
        'wizard/sms_template_preview_view.xml',
        'views/configure_gateway_view.xml',
        'views/sms_sms_view.xml',
        'views/sms_group_view.xml',
        'views/res_config_view.xml',
        'views/sms_report_view.xml',
        'views/sms_cron_view.xml',
        'views/sms_template_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
