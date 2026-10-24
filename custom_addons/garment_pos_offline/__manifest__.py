{
    'name': 'Garment POS Offline Resilience',
    'version': '17.0.1.0.0',
    'category': 'Sales/Point of Sale',
    'summary': 'Enhanced POS Offline Sync and Network Status Handlers for Garment Stores',
    'author': 'Mohamed Mamdouh',
    'depends': ['point_of_sale'],
    'assets': {
        'point_of_sale._assets_pos': [
            'garment_pos_offline/static/src/js/pos_offline_service.js',
        ],
    },
    'installable': True,
    'application': False,
    'license': 'LGPL-3',
}