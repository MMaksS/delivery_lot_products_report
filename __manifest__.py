# -*- coding: utf-8 -*-

{
    'name': 'Delivery Lot Products',
    'version': '12.0.1.0.0',
    'summary': 'Delivery Lot Products',
    'author': 'The256',
    'maintainer': 'The256',
    'company': 'The256',
    'website': 'https://the256.pro/',
    'depends': ['stock'],
    'demo': [],
    'data': [
        'views/report.xml',
		'views/stock.picking_report_lot_label.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'AGPL-3',
}