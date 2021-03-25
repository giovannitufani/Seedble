# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class ProjectProject(models.Model):
    _name = 'project.project'
    _inherit = ['project.project', 'mail.thread', 'mail.activity.mixin']