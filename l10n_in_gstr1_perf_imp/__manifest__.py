# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Indian - GSTR-1 report performance improvement',
    'version': '1.0',
    'description': """GSTR-1 take to much time to load where journal entry have big datas.

Note: After installing this module data in gstr-1 is updated in next day by cron job.
    """,
    'category': 'Localization',
    'depends': [
        'l10n_in_reports'
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/service_cron.xml"
    ],
    'auto_install': True,
    'pre_init_hook': "_create_temp_table_of_gstr1"
}
