from odoo import models,fields,api
class RejectReasonWizard(models.TransientModel):
    _name = 'vip.reject.wizard'
    _description = 'Get reason for rejecting VIP order'
    # The field to type the reason
    reason=fields.Text(string="Rejection Reason",required=True)
    # WHICH order we are rejecting
    sale_order_id=fields.Many2one('sale.order',string="Order")

    def action_reject(self):
        # Find the order
        order=self.sale_order_id
        # Log the reason in chatter
        order.message_post(body=f"VIP Order Rejected by Manager. Reason :{self.reason}")
        # Set the order to 'cancelled' (Odoo standard state)
        order.action_cancel()