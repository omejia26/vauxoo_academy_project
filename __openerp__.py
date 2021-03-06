# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Primer modulo de entrenamiento vauxoo""",

    'description': """
        Open Academy module for managing trainings:
    """,

    'author': "omejia",
    'website': "http://www.typrefrigeracion.com.mx",
    'category': 'TyP_training',
    'version': '0.1',
    'depends': ['base','board'],
    'data': [
        'view/openacademy_course_view.xml',
        'view/openacademy_session_view.xml',
        'view/partner_view.xml',
        'report/openacademy_session_report.xml',
        'view/openacademy_session_board.xml',
    ],
    'demo': [
         'demo/openacademy_course_demo.xml',
    ],
}
