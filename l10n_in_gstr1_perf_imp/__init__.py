# Part of Odoo. See LICENSE file for full copyright and licensing details.

from . import report

def _create_temp_table_of_gstr1(cr):
    cr.execute("DROP TABLE IF EXISTS l10n_in_account_invoice_report_temp")
    cr.execute("CREATE TABLE l10n_in_account_invoice_report_temp AS select * from l10n_in_account_invoice_report")
