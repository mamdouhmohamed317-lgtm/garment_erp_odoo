{
    'name': 'Garment Manufacturing & Costing',
    'version': '17.0.1.0.0',
    'category': 'Manufacturing',
    'summary': 'Garment Manufacturing, BOM Fabric Consumption & Operation Costs',
    'author': 'Mohamed Mamdouh',
    'depends': ['mrp', 'product', 'stock'],
    'data': [
        'security/ir.model.access.csv',
        'views/garment_bom_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}