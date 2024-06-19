# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class minivet(models.Model):
#     _name = 'minivet.minivet'
#     _description = 'minivet.minivet'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api
from dateutil.relativedelta import *
from datetime import date

class sucursal(models.Model):
    _name = 'minivet.sucursal'
    _description = 'Permite definir las características de una sucursal'

    nombre = fields.Char(string='Dirección', required=True)
    lugares = fields.Integer(string='Lugares', required=True)

    #RELACIONES ENTRE TABLAS
    animal_ids = fields.One2many('minivet.animal', 'sucursal_id', string='Animales')

class animal(models.Model):
    _name = 'minivet.animal'
    _description = 'Permite definir las características de un animal'
    _order = 'nombre'

    nombre = fields.Char(string='Nombre', required=True, size=10)
    tipo = fields.Char(string='Tipo', required=True)
    raza = fields.Char(string='Raza', required=True)
    nacimiento = fields.Date(string='Fecha de nacimiento')
    #store=True NO SE USA - EDAD AUTOCALCULADA CADA VEZ QUE SE EJECUTA.
    edad = fields.Integer('Edad', compute='_get_edad')
    observacion = fields.Text('Observación')

    #RELACIONES ENTRE TABLAS
    sucursal_id = fields.Many2one('minivet.sucursal', string='Sucursal')
    atencion_ids = fields.Many2many('minivet.atencion', string='Atención')

    @api.depends('nacimiento')
    def _get_edad(self):
        for animal in self:
            hoy = date.today()
            animal.edad = relativedelta(hoy, animal.nacimiento).years

    # POSIBLE MODIFICACION - GESTIONAR CLIENTES POR DOCUMENTO.
    # _sql_constraints=[('dni_uniq', 'unique(dni)', ' EL DNI YA EXISTE ')]
    
class atencion(models.Model):
    _name = 'minivet.atencion'
    _description = 'Permite definir una atencion animal'
    _order = 'fecha'

    #nombre=
    fecha = fields.Date('Fecha', required=True, default=fields.date.today())
    tipo = fields.Selection(string='Tipo', selection=[('b','Baño'),('c','Corte'),('k','Combinado')], default='b')
    precio = fields.Float('Precio', (8,2), help='Precio de atención')

    #RELACIONES ENTRE TABLAS
    animal_ids = fields.Many2many('minivet.animal', string='Animales')

    def name_get(self):
        resultados=[]
        for atencion in self:
            descripcion = f'{len(atencion.animal_ids)} animales - {atencion.precio} $'
            resultados.append((atencion.id, descripcion))
        return resultados