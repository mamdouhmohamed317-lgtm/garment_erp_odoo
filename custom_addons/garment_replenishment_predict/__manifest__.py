{
    'name': 'Garment Raw Material Replenishment Prediction',
    'version': '17.0.1.0.0',
    'category': 'Manufacturing/Purchase',
    'summary': 'Predict raw material shortages based on branch sales rates',
    'author': 'Mohamed Mamdouh',
    'depends': ['mrp', 'point_of_sale', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'views/prediction_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}