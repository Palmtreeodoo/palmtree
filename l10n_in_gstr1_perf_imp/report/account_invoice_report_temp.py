# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, tools


class L10nInAccountInvoiceReportTemp(models.Model):
    _auto = False
    _name = "l10n_in.account.invoice.report.temp"
    _table = "l10n_in_account_invoice_report_temp"
    _description = "Account Invoice Statistics temp"
    _order = 'date desc'

    account_move_id = fields.Many2one('account.move', string="Account Move")
    company_id = fields.Many2one('res.company', string="Company")
    date = fields.Date(string="Accounting Date")
    name = fields.Char(string="Invoice Number")
    partner_id = fields.Many2one('res.partner', string="Customer")
    is_reverse_charge = fields.Char("Reverse Charge")
    l10n_in_export_type = fields.Selection([
        ('regular', 'Regular'), ('deemed', 'Deemed'),
        ('sale_from_bonded_wh', 'Sale from Bonded WH'),
        ('export_with_igst', 'Export with IGST'),
        ('sez_with_igst', 'SEZ with IGST payment'),
        ('sez_without_igst', 'SEZ without IGST payment')])
    journal_id = fields.Many2one('account.journal', string="Journal")
    state = fields.Selection([('draft', 'Unposted'), ('posted', 'Posted')], string='Status')
    igst_amount = fields.Float(string="IGST Amount")
    cgst_amount = fields.Float(string="CGST Amount")
    sgst_amount = fields.Float(string="SGST Amount")
    cess_amount = fields.Float(string="Cess Amount")
    price_total = fields.Float(string='Total Without Tax')
    total = fields.Float(string="Invoice Total")
    reversed_entry_id = fields.Many2one('account.move', string="Refund Invoice", help="From where this Refund is created")
    shipping_bill_number = fields.Char(string="Shipping Bill Number")
    shipping_bill_date = fields.Date(string="Shipping Bill Date")
    shipping_port_code_id = fields.Many2one('l10n_in.port.code', string='Shipping port code')
    ecommerce_partner_id = fields.Many2one('res.partner', string="E-commerce")
    move_type = fields.Selection(selection=[
        ('entry', 'Journal Entry'),
        ('out_invoice', 'Customer Invoice'),
        ('out_refund', 'Customer Credit Note'),
        ('in_invoice', 'Vendor Bill'),
        ('in_refund', 'Vendor Credit Note'),
        ('out_receipt', 'Sales Receipt'),
        ('in_receipt', 'Purchase Receipt')])
    partner_vat = fields.Char(string="Customer GSTIN")
    ecommerce_vat = fields.Char(string="E-commerce GSTIN")
    tax_rate = fields.Float(string="Rate")
    place_of_supply = fields.Char(string="Place of Supply")
    is_pre_gst = fields.Char(string="Is Pre GST")
    is_ecommerce = fields.Char(string="Is E-commerce")
    b2cl_is_ecommerce = fields.Char(string="B2CL Is E-commerce")
    b2cs_is_ecommerce = fields.Char(string="B2CS Is E-commerce")
    supply_type = fields.Char(string="Supply Type")
    export_type = fields.Char(string="Export Type")  # String from GSTR column.
    refund_export_type = fields.Char(string="UR Type")  # String from GSTR column.
    b2b_type = fields.Char(string="B2B Invoice Type")
    refund_invoice_type = fields.Char(string="Document Type")
    gst_format_date = fields.Char(string="Formated Date")
    gst_format_refund_date = fields.Char(string="Formated Refund Date")
    gst_format_shipping_bill_date = fields.Char(string="Formated Shipping Bill Date")
    tax_id = fields.Many2one('account.tax', string="Tax")

    @api.model
    def update_data_from_sql_view(self):
        self.env.cr.execute("DROP TABLE IF EXISTS l10n_in_account_invoice_report_temp")
        self.env.cr.execute("CREATE TABLE l10n_in_account_invoice_report_temp AS select * from l10n_in_account_invoice_report")
