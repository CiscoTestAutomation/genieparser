expected_output = {
    'load_avg': {
        'load_avg_1min': 0.34,
        'load_avg_5min': 0.4,
        'load_avg_15min': 0.4},
    'processes': {
        'processes_total': 901,
        'processes_running': 2
    },
    'cpu_state':
        {
            'cpu_state_user': 2.11,
            'cpu_state_kernel': 11.64,
            'cpu_state_idle': 86.24,
            'cpus': {
                0: {
                    'cpu_state_user': 3.33,
                    'cpu_state_kernel': 12.22,
                    'cpu_state_idle': 84.44},
                1: {
                    'cpu_state_user': 1.04,
                    'cpu_state_kernel': 9.37,
                    'cpu_state_idle': 89.58
                }
            }
        },
    'memory_usage': {
        'memory_usage_total_kb': 5873172,
        'memory_usage_used_kb': 4189652,
        'memory_usage_free_kb': 1683520},
    'kernel': {
        'kernel_vmalloc_total_kb': 0,
        'kernel_vmalloc_free_kb': 0,
        'kernel_buffers_kb': 144876,
        'kernel_cached_kb': 2296916
    },
    'current_memory_status': 'OK'
}
