# -*- coding: utf-8 -*-
from odoo import http

# class ProjectTaskFollowers(http.Controller):
#     @http.route('/project_task_followers/project_task_followers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/project_task_followers/project_task_followers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('project_task_followers.listing', {
#             'root': '/project_task_followers/project_task_followers',
#             'objects': http.request.env['project_task_followers.project_task_followers'].search([]),
#         })

#     @http.route('/project_task_followers/project_task_followers/objects/<model("project_task_followers.project_task_followers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('project_task_followers.object', {
#             'object': obj
#         })