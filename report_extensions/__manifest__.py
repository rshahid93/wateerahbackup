# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Report Extensions',
    'version' : '1.0',
    'author': 'Predrag Lazarevic',
    'category': 'Report',
    'maintainer': 'Predrag Lazarevic',
    'description': """
        Extensions for Reports
    """,
    'license': 'LGPL-3',
    'support':'websavetnik@gmail.com',
    'depends' : ['web','sale'],
    'data': [
        'data.xml',
        'views/report_templates.xml',
        'views/sale_report_templates.xml'
    ],
    
    'installable': True,
    'application': True,
    'auto_install': False
}


