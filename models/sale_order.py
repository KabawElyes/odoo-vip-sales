from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    #A flag to track if the manager approved it
    x_manager_approved=fields.Boolean(string="Manager Approved",default=False)

    # --- NEW FIELD (For High Value Logic) ---
    x_is_high_value=fields.Boolean(
        string="High Value Order",
        compute="_compute_high_value",
        store=True
    )

    # --- NEW FUNCTION (To calculate High Value) ---
    @api.depends('amount_total')
    def _compute_high_value(self):
        for order in self:
            if order.amount_total>5000:
                order.x_is_high_value = True
            else:
                order.x_is_high_value= False


    def action_approve_vip(self):
        """ Function called by the button to approve the order """
        for order in self:
            order.x_manager_approved=True
            # Log a note in the chatter (history)
            order.message_post(body="VIP Order approved By Manager.")
    # We override the standard "Confirm" button function
    def action_confirm(self):
        for order in self:
             # CHECK 1: Is the customer a VIP?
             if order.partner_id.x_is_vip:
        # CHECK 2: Is the total amount higher than their limit?
                if order.amount_total > order.partner_id.x_credit_limit:
    # CHECK 3: Has the manager approved it yet?
                      if not order.x_manager_approved:
                            raise UserError("VIP Limit Exceeded! A Manager must approve this order first.")

            # If all checks pass, run the standard Odoo confirm method
        return super(SaleOrder, self).action_confirm()

    def action_open_reject_wizard(self):
        return{
            'type':'ir.actions.act_window',
            'name':'Reject VIP Order',
            'res_model':'vip.reject.wizard',
            'view_mode':'form',
            'target':'new',
            'context':{'default_sale_order_id':self.id}

        }