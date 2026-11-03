expected_output = {
    'control_plane_cpu_alloc': '0',
    'control_plane_cpu_alloc_core_ids': [0],
    'data_plane_cpu_alloc': '0,6-11',
    'data_plane_cpu_alloc_core_ids': [0, 6, 7, 8, 9, 10, 11],
    'service_plane_cpu_alloc': '1-5',
    'service_plane_cpu_alloc_core_ids': [1, 2, 3, 4, 5],
    'slow_control_plane_cpu_alloc': '',
    'slow_control_plane_cpu_alloc_core_ids': [],
    'template_used': 'default-service_plane_heavy',
}
