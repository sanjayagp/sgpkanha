# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import _, SUPERUSER_ID
from openerp.osv import osv, fields
from openerp.tools import html2plaintext

class projects(osv.osv):
    _name = "kanha.project"
    _description = "List of Projects"
    _columns = {
        'name': fields.char('Project Name',  required=True),
        'description': fields.char('Project Description', required=True  ),
        'sequence': fields.integer('Sequence', help="Used to order the projects "),
        'manager': fields.many2one('hr.employee', 'Project Manager', help="Project Manager or Supervisor", required=True ),
    }
    _order = 'sequence asc'
    _defaults = {
        'manager': lambda self, cr, uid, ctx: uid,
        'sequence' : 1,
    }


class locations(osv.osv):
    _name = "kanha.location"
    _description = "List of locations"
    _columns = {
        'name': fields.char('Location Name',  required=True),
        'description': fields.char('Location Description',  required=True),
        'sequence': fields.integer('Sequence', help="Used to order the Locations "),
    }
    _order = 'sequence asc'
    _defaults = {
        'sequence' : 1,
    }



class nmr_details(osv.osv):
    _name = "kanha.nmr"
    _description = "NMR Details"
    _columns = {
        'date': fields.datetime('Date', required=True, select=1),
        'labour': fields.many2one('hr.employee', 'Labour Name', help="Labour Name", required=True ),
        'project': fields.many2one('kanha.project', 'Project Name', help="Project Name", required=True ),
        'location': fields.many2one('kanha.location', 'Location Name', help="Location Name", required=True ),
        'workdone': fields.html('Brief Description of Work Done ', required=True ),
    }
