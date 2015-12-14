# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import fields, models, api
from openerp.tools import html2plaintext




class resuser(models.Model):
    _name = "kanha.resuser"
    _description = "resuser"
<<<<<<< HEAD
    name = fields.Char(string='Person Name',  required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Mobile')
=======
    _columns = {
        'name': fields.char('Person Name',  required=True),
        'email': fields.char('Email'),
        'phone': fields.char('Mobile', required=True),
    }
>>>>>>> f0eee6735ea9087b8d8100332b1eebdd8120c71e

class project(models.Model):
    _name = "kanha.project"
    _description = "List of Projects"
<<<<<<< HEAD
    
    name = fields.Char(string='Project Name',  required=True)
    code = fields.Integer(string='Project Code', help="Project Code")
    description = fields.Char(string='Project Description', required=True  )
    sequence = fields.Integer(string='Sequence', help="Used to order the projects ")
    #  'manager = fields.Many2one('kanha.supervisor', string='Project Manager', help="Project Manager or Supervisor", required=True )
=======
    _columns = {
        'name': fields.char('Project Name',  required=True),
        'code': fields.integer('Project Code', help="Project Code", required=True),
        'description': fields.char('Project Description', required=True  ),
        'sequence': fields.integer('Sequence', help="Used to order the projects "),
      #  'manager': fields.many2one('kanha.supervisor', 'Project Manager', help="Project Manager or Supervisor", required=True ),
    }
>>>>>>> f0eee6735ea9087b8d8100332b1eebdd8120c71e
    _order = 'sequence asc'
    _defaults = {
        'sequence' : 1,
    }


class location(models.Model):
    _name = "kanha.location"
    _description = "List of locations"
    
    name = fields.Char(string='Location Name',  required=True)
    description = fields.Char(string='Location Description',  required=True)
    sequence = fields.Integer(string='Sequence', help="Used to order the Locations ")
    
    _order = 'sequence asc'
    _defaults = {
        'sequence' : 1,
    }




class equipment_type(models.Model):
    _name = "kanha.equipment.type"
    _description = "Equipment Type"
    
    name = fields.Char(string='Equipment Type',  required=True)


class equipment(models.Model):
    _name = "kanha.equipment"
    _description = "Equipment Details"
    
    equipmenttype = fields.Many2one('kanha.equipment.type', string='Equipment Type', help="Equipment Type", required=True )
    name = fields.Char(string='Equipment Number', required=True)

class labour_type(models.Model):
    _name = "kanha.labour.type"
    _description = "Labour Type"
    
    name = fields.Char(string='Labour Type', help='default or mason or etc.',  required=True)
    description = fields.Char(string='Description', required=True)


class labour(models.Model):
    _name = "kanha.labour"
    _description = "Labour Details"

    _inherits = { 'kanha.resuser' : "resuser_id" }

    

    resuser_id = fields.Many2one('kanha.resuser', string='ResUser', required=True, ondelete='cascade' )
    labourtype = fields.Many2one('kanha.labour.type', string='Labour Type', help="Labour Type", required=True )
    name = fields.Char(string='Labour Name',  required=True)
    labourid = fields.Char(string='Labour ID',  required=True)
    phone = fields.Char(string='Phone')
    rate = fields.Integer(string='Labour Rate')




class contractor(models.Model):
    _name = "kanha.contractor"
    _description = "contractor"

    _inherits = { 'kanha.resuser' : "resuser_id" }

    
    resuser_id = fields.Many2one('kanha.resuser', string='ResUser', required=True, ondelete='cascade' )
    sequence = fields.Integer(string='Contractor Sequence Number')


class supervisortype(models.Model):
    _name = "kanha.supervisor.type"
    _description = "Supervisor type"
    
    name = fields.Char(string='Supervisor Type', required=True)
    


class supervisor(models.Model):
    _name = "kanha.supervisor"
    _description = "Supervisor"
    _inherits = { 'kanha.resuser' : "resuser_id" }
    
    resuser_id = fields.Many2one('kanha.resuser', string='ResUser', required=True, ondelete='cascade' )
    sequence = fields.Integer(string='Supervisor Sequence Number')
    supervisortype_ids = fields.Many2many('kanha.supervisor.type', string='Supervisor Types')



class billable_entity(models.Model):
    _name = "kanha.billableentity"
    _description = "Billable entity"
    
    name = fields.Char(string='Unique Id', required=True)
    date = fields.Date('Date', required=True, select=1)
    billedperson = fields.Many2one('kanha.resuser', string='Billed Person', help="Billed person", required=True )
    projectname = fields.Many2one('kanha.project', string='Project', help="Project name", required=True )
    amount = fields.Integer(string='Billed Amount', required=True)

    _defaults = {
        'amount' : 0,
    }


class vehicle_equipment_slip(models.Model):
    _name = "kanha.vehicleequipmentslip"
    _description = "Vehicle Equipment Slip"

    _inherits = { "kanha.billableentity"  : "bill_id"}

    
    bill_id = fields.Many2one('kanha.billableentity', string='Billable Entity', required=True, ondelete='cascade' )
    name = fields.Char(string='Gate Security Number', required=True)
    billedperson = fields.Many2one('kanha.contractor', string='Contractor', help="Contractor", required=True )
    equipmentnumber = fields.Many2one('kanha.equipment', string='Equipment Number', help="Equipment Number", required=True )
    


class vehicle_equipment_slip_lines(models.Model):
    _name = "kanha.vehicleequipmentslip.lines"
    _description = "Vehicle equipment slip number"
    
    equipmentslip_id = fields.Many2one('kanha.vehicleequipmentslip', string='Vehicle Equipment Slip', required=True )
    locationname = fields.Many2one('kanha.location', string='Location Name', help="Location name", required=True )
    meteropening = fields.Char(string='Opening Meter')
    meterclosing = fields.Char(string='Closing Meter')
    houropen = fields.Char(string='Opening Time')
    hourclose = fields.Char(string='Closing Time')
    totalbillablehrs = fields.Integer(string='Total Billable Hours')
    



class nmr(models.Model):
    _name = "kanha.nmr"
    _description = "NMR Details"

    _inherits = { "kanha.billableentity"  : "bill_id"}

    
    bill_id = fields.Many2one('kanha.billableentity', string='Billable Entity', required=True, ondelete='cascade' )
    name = fields.Char(string='Gate Security Number', required=True)
    billedperson = fields.Many2one('kanha.labour', string='Labour Name', help="Labour Name", required=True )

    location = fields.Many2one('kanha.location', string='Location Name', help="Location Name", required=True )
    workdone = fields.Html('Brief Description of Work Done ' )
    



