# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Cash Register Automation',
    'version' : '1.0',
    'author': 'Predrag Lazarevic',
    'category': 'Sales',
    'maintainer': 'Predrag Lazarevic',
    'description': """
        You can directly cash register from Sale Order by single click

    """,
    'license': 'LGPL-3',
    'support':'websavetnik@gmail.com',
    'depends' : ['sale_order_automation'],
    'data': [
        'data.xml',
        'views/account_payment_view.xml',
        'views/res_users_view.xml',
        'views/warehouse_view.xml',
        'views/journal_view.xml',
        'wizard/account_payment_register_view.xml'
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False
}


