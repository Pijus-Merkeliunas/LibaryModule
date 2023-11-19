{
    'name': "Library by Pijus",

    'summary': """
        Library module""",

    'description': """
        In total there is 3 views in this module, 2 in file views/views.xml and one in wizard/print_data_view.xml.
        There are also 3 actions in this module, each assigned to a specific view. The menu bar is also defined in
        views/views.xml. This module uses 2 models. The folders controllers and demo were not used, but were generated
        automatically with "odoo scaffold" command.
    """,

    'author': "Pijus Merkeliūnas",
    'website': "https://www.linkedin.com/in/pijus-merkeliunas/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/print_data_view.xml',
        'wizard/templates.xml',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    #'demo': [
    #    'demo/demo.xml',
    #],
    'application': True,
}
