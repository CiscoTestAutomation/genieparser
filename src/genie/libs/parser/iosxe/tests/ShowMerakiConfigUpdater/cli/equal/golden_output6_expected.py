expected_output = {
    'config_updater': {
        'current_state': 'Ready',
        'pending_local_changes': True,
        'pending_local_changes_reason': 'next upload will trigger consilience',
        'last_save_time': '2026-07-02 18:50:45',
        'next_save_scheduled': False,
    },
    'latest_operation': {
        'operation': 'Upload running config after save',
        'save_config': {
            'status': 'Completed',
            'start_time': '2026-07-02 18:50:40',
            'result_time': '2026-07-02 18:50:45',
        },
        'get_running_config': {
            'status': 'Pass',
            'start_time': '2026-07-02 18:50:42',
            'result_time': '2026-07-02 18:50:45',
            'config_location': '/flash/meraki/config_updater/monitor/upload.config',
        },
        'get_presigned_url': {
            'status': 'Not needed',
            'start_time': '2026-07-02 18:50:45',
            'result_time': '2026-07-02 18:50:47',
            'dashboard_status_code': '204',
        },
        'upload_config': {
            'status': 'Not started',
        },
    },
}