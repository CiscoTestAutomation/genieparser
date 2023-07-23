expected_output = {
     'policy_name': {
         'RED': {
             'class_map': {
                 'class-default': {
                     'average_rate_traffic_shaping': True,
                     'cir_percent': 10,
                     'class_val': {
                         '0': {
                             'mark_probability': '1/1',
                             'max_threshold': '100',
                             'min_threshold': '1',
                         },
                         '1': {
                             'mark_probability': '1/1',
                             'max_threshold': '-',
                             'min_threshold': '-',
                         },
                         '2': {
                             'mark_probability': '1/1',
                             'max_threshold': '-',
                             'min_threshold': '-',
                         },
                         '3': {
                             'mark_probability': '1/1',
                             'max_threshold': '-',
                             'min_threshold': '-',
                         },
                         '4': {
                             'mark_probability': '1/1',
                             'max_threshold': '-',
                             'min_threshold': '-',
                         },
                         '5': {
                             'mark_probability': '1/1',
                             'max_threshold': '-',
                             'min_threshold': '-',
                         },
                         '6': {
                             'mark_probability': '1/1',
                             'max_threshold': '-',
                             'min_threshold': '-',
                         },
                         '7': {
                             'mark_probability': '1/1',
                             'max_threshold': '-',
                             'min_threshold': '-',
                         },
                     },
                     'exponential_weight': 1,
                     'queue_limit_bytes': 100000000,
                     'wred_type': 'percent-based',
                 },
             },
         },
     },
 }
