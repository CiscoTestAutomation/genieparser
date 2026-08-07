expected_output = {
    'cloud_mgmt_cloud_monitoring': 'Compatible',
    'cloud_mgmt_cloud_management': {
        'boot_mode': {
            'mode': 'INSTALL',
            'status': 'Compatible',
        },
        'switch_details': [
            {
                'switch_number': 1,
                'sku': {'model': 'IE-3500-8U3X', 'status': 'Compatible'},
                'bootloader_version': {'version': '17_18_2r', 'status': 'Compatible'},
                'expansion_modules': [{'model': 'IEM-3500-4MU', 'status': 'Compatible'}],
            }
        ],
        'compatible_expansion_modules': ['IEM-3500-8T', 'IEM-3500-4MU'],
    },
}
