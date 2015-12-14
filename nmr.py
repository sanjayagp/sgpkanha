# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import _, SUPERUSER_ID
from openerp.osv import osv, fields
from openerp.tools import html2plaintext




class resuser(osv.osv):
    _name = "kanha.resuser"
    _description = "resuser"
    _columns = {
        'name': fields.char('Person Name',  required=True),
        'email': fields.char('Email'),
        'phone': fields.char('Mobile'),
    }

class project(osv.osv):
    _name = "kanha.project"
    _description = "List of Projects"
    _columns = {
        'name': fields.char('Project Name',  required=True),
        'code': fields.integer('Project Code', help="Project Code"),
        'description': fields.char('Project Description', required=True  ),
        'sequence': fields.integer('Sequence', help="Used to order the projects "),
      #  'manager': fields.many2one('kanha.supervisor', 'Project Manager', help="Project Manager or Supervisor", required=True ),
    }
    _order = 'sequence asc'
    _defaults = {
        'sequence' : 1,
    }


class location(osv.osv):
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




class equipment_type(osv.osv):
    _name = "kanha.equipment.type"
    _description = "Equipment Type"
    _columns = {
        'name': fields.char('Equipment Type',  required=True),
    }


class equipment(osv.osv):
    _name = "kanha.equipment"
    _description = "Equipment Details"
    _columns = {
        'equipmenttype': fields.many2one('kanha.equipment.type', 'Equipment Type', help="Equipment Type", required=True ),
        'name': fields.char('Equipment Number', required=True),
    }

class labour_type(osv.osv):
    _name = "kanha.labour.type"
    _description = "Labour Type"
    _columns = {
        'name': fields.char('Labour Type', help='default or mason or etc.',  required=True),
        'description': fields.char('Description', required=True),
    }


class labour(osv.osv):
    _name = "kanha.labour"
    _description = "Labour Details"

    _inherits = { 'kanha.resuser' : "resuser_id" }

    _columns = {

        'resuser_id': fields.many2one('kanha.resuser', 'ResUser', required=True, ondelete='cascade' ),
        'labourtype': fields.many2one('kanha.labour.type', 'Labour Type', help="Labour Type", required=True ),
        'name': fields.char('Labour Name',  required=True),
        'labourid': fields.char('Labour ID',  required=True),
        'phone': fields.char('Phone'),
        'rate': fields.integer('Labour Rate'),
    }




class contractor(osv.osv):
    _name = "kanha.contractor"
    _description = "contractor"

    _inherits = { 'kanha.resuser' : "resuser_id" }

    _columns = {
        'resuser_id': fields.many2one('kanha.resuser', 'ResUser', required=True, ondelete='cascade' ),
        'sequence': fields.integer('Contractor Sequence Number'),
    }

class supervisortype(osv.osv):
    _name = "kanha.supervisor.type"
    _description = "Supervisor type"
    _columns = {
        'name': fields.char('Supervisor Type', required=True),
        'supervisor_ids': fields.many2many('kanha.supervisor', 'supervisor_type_rel', 'supervisortype_id', 'supervisor_id', 'Supervisors'),
    }


class supervisor(osv.osv):
    _name = "kanha.supervisor"
    _description = "Supervisor"
    _inherits = { 'kanha.resuser' : "resuser_id" }
    _columns = {
        'resuser_id': fields.many2one('kanha.resuser', 'ResUser', required=True, ondelete='cascade' ),
        'sequence': fields.integer('Supervisor Sequence Number'),
        'supervisortype_ids': fields.many2many('kanha.supervisor.type', 'supervisor_type_rel', 'supervisor_id', 'supervisortype_id', 'Supervisor Types'),
    }



class billable_entity(osv.osv):
    _name = "kanha.billableentity"
    _description = "Billable entity"
    _columns = {
        'name': fields.char('Unique Id', required=True),
        'date': fields.datetime('Date', required=True, select=1),
        'billedperson': fields.many2one('kanha.resuser', 'Billed Person', help="Billed person", required=True ),
        'projectname': fields.many2one('kanha.project', 'Project', help="Project name", required=True ),
        'amount': fields.integer('Billed Amount', required=True),
    }
    _defaults = {
        'amount' : 0,
    }


class vehicle_equipment_slip(osv.osv):
    _name = "kanha.vehicleequipmentslip"
    _description = "Vehicle Equipment Slip"

    _inherits = { "kanha.billableentity"  : "bill_id"}

    _columns = {
        'bill_id': fields.many2one('kanha.billableentity', 'Billable Entity', required=True, ondelete='cascade' ),
        'name': fields.char('Gate Security Number', required=True),
        'billedperson': fields.many2one('kanha.contractor', 'Contractor', help="Contractor", required=True ),
        'equipmentnumber': fields.many2one('kanha.equipment', 'Equipment Number', help="Equipment Number", required=True ),
        'equipmentslipline_ids': fields.one2many('kanha.vehicleequipmentslip.lines', 'equipmentslip_id', 'Vehicle Equipment Slip Lines'),
    }


class vehicle_equipment_slip_lines(osv.osv):
    _name = "kanha.vehicleequipmentslip.lines"
    _description = "Vehicle equipment slip number"
    _columns = {
        'equipmentslip_id': fields.many2one('kanha.vehicleequipmentslip', 'Vehicle Equipment Slip', required=True ),
        'locationname': fields.many2one('kanha.location', 'Location Name', help="Location name", required=True ),
        'meteropening': fields.char('Opening Meter'),
        'meterclosing': fields.char('Closing Meter'),
        'houropen': fields.char('Opening Time'),
        'hourclose': fields.char('Closing Time'),
        'totalbillablehrs': fields.integer('Total Billable Hours'),
    }



class nmr(osv.osv):
    _name = "kanha.nmr"
    _description = "NMR Details"

    _inherits = { "kanha.billableentity"  : "bill_id"}

    _columns = {
        'bill_id': fields.many2one('kanha.billableentity', 'Billable Entity', required=True, ondelete='cascade' ),
        'name': fields.char('Gate Security Number', required=True),
        'billedperson': fields.many2one('kanha.labour', 'Labour Name', help="Labour Name", required=True ),

        'location': fields.many2one('kanha.location', 'Location Name', help="Location Name", required=True ),
        'workdone': fields.html('Brief Description of Work Done ' ),
    }



