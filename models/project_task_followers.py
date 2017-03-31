# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ProjectTask(models.Model):
    _inherit = "project.task"

    @api.multi
    def add_project_followers(self):
        for i in self:
            project_followers = i.project_id.message_follower_ids
            for follower in project_followers:
                i.message_subscribe(partner_ids=follower.partner_id.ids, subtype_ids=follower.subtype_ids.ids)

    @api.multi
    def clear_assigned_to(self):
        for i in self:
            i.user_id = False
