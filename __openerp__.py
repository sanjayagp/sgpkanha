# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Kanha',
    'version': '1.0',
    'category': 'Tools',
    'description': """
This module allows users to create their own notes inside OpenERP
=================================================================

Use notes to write meeting minutes, organize ideas, organize personal todo
lists, etc. Each user manages his own personal Notes. Notes are available to
their authors only, but they can share notes to others users so that several
people can work on the same note in real time. It's very efficient to share
meeting minutes.

Notes can be found in the 'Home' menu.
""",
    'website': 'https://www.odoo.com/page/notes',
    'summary': 'Kanha Project Management',
    'sequence': 45,
    'depends': [
        'base',
    ],
    'data': [
	'kanha_security.xml',
	'ir.model.access.csv',
	'nmr_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
