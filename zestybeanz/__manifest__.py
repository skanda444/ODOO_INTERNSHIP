# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2025 ZestyBeanz Technologies(<http://www.zbeanztech.com>)R
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
'name': 'Sample Module',
'version': '18.0.0.0',
'summary': 'This Module is for training purposes.',
'description': """This Module is for training purposes.
""",
'category':'',
'author': ' Skanda.C',
'website': 'www.zbeanztech.com',
"license": "LGPL-3",
'depends': ['report_xlsx','sale','sale_management','account','contacts','product','sale'],
'data': ['security/ir.model.access.csv','security/security.xml','Data/sequence.xml','Data/cron.xml','Data/my_mail_template.xml','report/model_one_qweb_report.xml',
'report/sale_order_report.xml','report/report.xml','wizard/sample_wizard_view.xml','views/car_rental_views.xml','views/food_view.xml','views/model_one_view.xml',
'views/model_one_lines.xml','views/sale_order_view.xml','views/my_employee_view.xml','views/menu.xml'],
'test': [],
'demo': [],
'installable': True,
'auto_install': False,
'application': False,
}