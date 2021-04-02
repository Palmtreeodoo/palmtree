from odoo import models, fields, api, _
from odoo.exceptions import UserError
class UpdateCompany(models.TransientModel):
    _name = 'update.product.company'
    _description = 'Update product company'


    def update_state(self):
        active_ids = self._context.get('active_ids', []) or []
        products = self.env['product.template'].search([('company_ids','in',(2))])
        company = self.env['res.company'].browse(2)
        company_kc = self.env['res.company'].browse(3)
        # s=0
        for record in products:
            if company in record.company_ids and company_kc not in record.company_ids:
                record.company_ids += company_kc
                # s+=1
                # print (s)
        return
