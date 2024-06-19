# -*- coding: utf-8 -*-
{
    'name': "MiniVet",

    'summary': """
        Gestión de guardería""",

    'description': """
        Gestión de guardería para dos sucursales, en las cuales se pueden registrar y dar de baja ingresos.
    """,

    'author': "juan",
    'website': "http://www.minivet.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/minivet_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/minivet_sucursal_report.xml',
        'data/minivet_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # indicamos que es una aplicacion.
    'application': True,
}
