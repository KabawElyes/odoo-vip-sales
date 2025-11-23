{
    'name':"VIP Sales Approval",
    'version':'17.0.1.0',
    'category':'Sales',
    'Summary':'Requires manager approval for high-value VIP orders',
    'depends':['base','sale','sale_management'],
    'data':[
        'security/security.xml',
        'views/res_partner_views.xml',
        'views/sale_order_views.xml',
    ],
    'installable':True,
    'application':False,
}