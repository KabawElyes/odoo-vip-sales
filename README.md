# VIP Sales Approval Module (Odoo 17)

## 📌 Project Overview
This custom Odoo module implements a strict approval workflow for High-Value Sales Orders placed by VIP Customers. It prevents unauthorized confirmation of risky orders by enforcing Manager Approval.

##  Key Features
* **VIP Customer Flag:** Mark specific contacts as "VIP" with a defined "Credit Limit".
* **Automated Risk Detection:** Orders over 5,000 QAR are automatically flagged as "High Value" and highlighted in **RED** in the sales list.
* **Approval Blocking:** The "Confirm" button is blocked for VIP orders exceeding their limit.
* **Manager Workflow:** Specific "VIP Approver" security group required to see and click the "Approve" button.
* **Rejection Wizard:** Managers can reject orders with a specific reason via a pop-up wizard, which logs the reason in the chatter.

## 🛠 Technical Implementation
* **Models:** Inheritance of `sale.order` and `res.partner`.
* **Views:** XPath modifications to Form and Tree views.
* **Logic:** Method overriding (`super()`) on `action_confirm`.
* **Automation:** Computed fields with `@api.depends` and `store=True`.
* **Security:** ACLs (Access Control Lists) and Group definitions.
* **Wizard:** TransientModel for handling rejection logic.

##  How to Test
1.  Create a customer "Qatar Trading" and mark as VIP (Limit: 1000).
2.  Create a Sales Order for 6,000.
3.  Observe the "High Value" flag and Red text in the list.
4.  Try to Confirm (System will block you).
5.  Log in as a Manager and click "Approve".
6.  Confirm the order successfully.
