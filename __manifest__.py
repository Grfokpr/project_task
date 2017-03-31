# -*- coding: utf-8 -*-
{
    'name': "project_task_followers",

    'summary': """
        Buttons for Project Task""",

    'description': """
        This module add 2 buttons with functionality
        to project.task module adding 2 buttons.
        
    """,

    'author': "Anton Prusakov",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'project'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
