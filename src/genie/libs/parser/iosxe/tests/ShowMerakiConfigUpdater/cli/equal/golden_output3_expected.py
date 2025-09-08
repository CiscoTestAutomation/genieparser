expected_output = {
    'config_updater': {
        'current_state': "Ready"
    },
    'latest_operation': {
        'operation': "Cloud config ready",
        'download_running_config': {
            'status': "Pass",
            'start_time': "2025-04-04 23:13:38",
            'result_time': "2025-04-04 23:19:08",
            'config_location': "/flash/meraki/config_updater/monitor/dwnld_running.config"
        },
        'apply_running_config': {
            'status': "Pass",
            'start_time': "2025-04-04 23:19:08",
            'result_time': "2025-04-04 23:19:17",
        },
        'get_running_config': {
            'status': "Pass",
            'start_time': "2025-04-04 23:19:17",
            'result_time': "2025-04-04 23:19:23",
            'config_location': "/flash/meraki/config_updater/monitor/upload.config"
        },
        'get_presigned_url': {
            'status': "Fail, Retrying",
            'start_time': "2025-04-04 23:19:23",
            'result_time': "2025-04-04 23:24:31",
            'dashboard_status_code': "502",
            'retry_timeout': 300,
            'dashboard_provided': False,
            'retry_attempt': 2,
            'retry_count': 3,
            'retry_time': "2025-04-04 23:29:37"
        },
        'upload_config': {
            'status': "Not started"
        }
    }
}
