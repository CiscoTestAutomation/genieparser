expected_output = {
    'id': {
        101: {
            'state': 'Valid',
            'state_description': 'Subscription validated',
            'type': 'Configured'},
        102: {
            'state': 'Invalid',
            'state_description': "Value 'unknown' not supported for "
            "parameter 'filter-type' (supported values "
            "include 'xpath,sensor-group').",
            'type': 'Configured'}
    }
}
