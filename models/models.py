# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError


class hellowolrd(models.Model):
    _name = 'hellowolrd.hellowolrd'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    description = fields.Text()
#
    extra_ids = fields.One2many('hellow.extras', 'hellow_id')
    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100

    @api.multi
    def create_another(self):
        self.create({'name': '1234', 'value': 100, 'description':'Esto es una prueba', 'value2': 500})


    @api.multi
    def create_partner(self):
        partner = self.env['res.partner']

        partner.create({'name': self.name, 'phone': self.value, 'customer': True,})

    @api.multi
    def create_hijos(self):
        partner = self.env['res.partner']
        if len(self.extra_ids) <= 3:
            raise UserError("No cumples La condicion para crear los como contactos.")

        for i in self.extra_ids:
            partner.create({'name': i.name, 'phone': i.telf})


class extras(models.Model):
    _name = 'hellow.extras'

    name = fields.Char(string="Nombre", required=1)
    telf = fields.Char(string="Telf")
    hellow_id = fields.Many2one('hellowolrd.hellowolrd')
    

