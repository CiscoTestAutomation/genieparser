expected_output = {
    'config_updater': {
        'current_state': "Ready"
    },
    'latest_operation': {
        'operation': "Upload running config after save",
        'save_config': {
            'status': "Completed",
            'start_time': "2025-04-09 23:44:24",
            'result_time': "2025-04-09 23:44:30",
        },
        'get_running_config': {
            'status': "Pass",
            'start_time': "2025-04-09 23:44:24",
            'result_time': "2025-04-09 23:44:30",
            'config_location': "/flash/meraki/config_updater/monitor/upload.config"
        },
        'get_presigned_url': {
            'status': "Not needed",
            'start_time': "2025-04-09 23:44:30",
            'result_time': "2025-04-09 23:44:32",
            'dashboard_status_code': "204",
        },
        'upload_config': {
            'status': "Not started"
        }
    }
}
