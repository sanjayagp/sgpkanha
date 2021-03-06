# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from openerp import fields, models, api
from openerp.tools import html2plaintext





class project(models.Model):
    _name = "kanha.project"
    _description = "List of Projects"
    
    name = fields.Char(string='Project Name',  required=True)
    code = fields.Integer(string='Project Code', help="Project Code")
    description = fields.Char(string='Project Description', required=True  )
    sequence = fields.Integer(string='Sequence', help="Used to order the projects ")
    manager = fields.Many2many('kanha.supervisor',  string='Project Manager', help="Project Manager or Supervisor", required=True )

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
    description = fields.Char(string='Description' )


class labour(models.Model):
    _name = "kanha.labour"
    _description = "Labour Details"

    name = fields.Char(string='Labour Name',  required=True)
    phone = fields.Char(string='Mobile')
    labourtype = fields.Many2one('kanha.labour.type', required=True )
    labourid = fields.Char(string='Labour ID',  required=True)
    rate = fields.Integer(string='Labour Rate')




class contractor(models.Model):
    _name = "kanha.contractor"
    _description = "contractor"


    name = fields.Char(string='Contractor Name',  required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Mobile')
    sequence = fields.Integer(string='Contractor Sequence Number')


class supervisortype(models.Model):
    _name = "kanha.supervisor.type"
    _description = "Supervisor type"
    
    name = fields.Char(string='Supervisor Type', required=True)
    


class supervisor(models.Model):
    _name = "kanha.supervisor"
    _description = "Supervisor"
    
    name = fields.Char(string='Supervisor Name',  required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Mobile')
    sequence = fields.Integer(string='Supervisor Sequence Number')
    supervisortype_ids = fields.Many2many('kanha.supervisor.type', string='Supervisor Types')





class vehicle_equipment_slip(models.Model):
    _name = "kanha.vehicleequipmentslip"
    _description = "Vehicle Equipment Slip"


    
    name = fields.Char(string='Gate Security Number', required=True)
    billedperson = fields.Many2one('kanha.contractor', string='Contractor', help="Contractor", required=True )
    date = fields.Date('Date', required=True, select=1)
    projectname = fields.Many2one('kanha.project', string='Project', help="Project name", required=True )
    amount = fields.Integer(string='Billed Amount', required=True)

    equipmentnumber = fields.Many2one('kanha.equipment', string='Equipment Number', help="Equipment Number", required=True )
    equipmentslip_lines_ids = fields.One2many('kanha.vehicleequipmentslip.lines', 'equipmentslip_id', string='Vehicle Equipment Slip Lines', required=True )
    


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


    
    name = fields.Char(string='Gate Security Number', required=True)
    billedperson = fields.Many2one('kanha.labour', string='Labour Name', help="Labour Name", required=True )
    date = fields.Date('Date', required=True, select=1)
    projectname = fields.Many2one('kanha.project', string='Project', help="Project name", required=True )
    amount = fields.Integer(string='Billed Amount', required=True)

    location = fields.Many2one('kanha.location', string='Location Name', help="Location Name", required=True )
    workdone = fields.Html('Brief Description of Work Done ' )
    



