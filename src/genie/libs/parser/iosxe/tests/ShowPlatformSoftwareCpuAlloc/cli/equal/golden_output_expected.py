expected_output = {
    'control_plane_cpu_alloc': '0-1',
    'control_plane_cpu_alloc_core_ids': [0, 1],
    'data_plane_cpu_alloc': '0,11-23',
    'data_plane_cpu_alloc_core_ids': [
        0, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23
    ],
    'service_plane_cpu_alloc': '2-10',
    'service_plane_cpu_alloc_core_ids': [2, 3, 4, 5, 6, 7, 8, 9, 10],
    'slow_control_plane_cpu_alloc': '',
    'slow_control_plane_cpu_alloc_core_ids': [],
    'template_used': 'CLI-service_plane_heavy',
}
