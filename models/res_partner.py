from odoo import models,fields
class ResPartner(models.Model):
    _inherit='res.partner'

    #Boolean field: Is this cutstom a VIP?
    x_is_vip=fields.Boolean(string="Is VIP Customer")
    #FLoat field:How much credit do they have?
    x_credit_limit=fields.Float(string="VIP credit Lemit")
