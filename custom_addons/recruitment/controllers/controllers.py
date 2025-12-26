# -*- coding: utf-8 -*-
# from odoo import http


# class HrRecruitment(http.Controller):
#     @http.route('/hr_recruitment/hr_recruitment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_recruitment/hr_recruitment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_recruitment.listing', {
#             'root': '/hr_recruitment/hr_recruitment',
#             'objects': http.request.env['hr_recruitment.hr_recruitment'].search([]),
#         })

#     @http.route('/hr_recruitment/hr_recruitment/objects/<model("hr_recruitment.hr_recruitment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_recruitment.object', {
#             'object': obj
#         })

