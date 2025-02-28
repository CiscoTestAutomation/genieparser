expected_output ={
    'tty': {
            49: [ 
                    {
                        'interface': 'Lo7', 
                        'destip': '40.1.1.1', 
                        'destport': 5000, 
                        'localip': '50.1.1.1', 
                        'localport': 4000, 
                        'state': 'DOWN'
                    },
                    {
                        'interface': 'Lo7',
                        'destip': '40.1.1.1', 
                        'destport': 5001, 
                        'localip': '50.1.1.1', 
                        'localport': 4010, 
                        'state': 'UP'
                    }
                ], 
            50: [
                    {
                        'interface': 'Lo6', 
                        'destip': '40.1.1.1', 
                        'destport': 5001, 
                        'localip': '50.1.1.1', 
                        'localport': 4011, 
                        'state': 'UP'
                    }, 
                    {
                        'interface': '0/3/0', 
                        'destip': '40.1.1.1', 
                        'destport': 5000, 
                        'localip': '50.1.1.1', 
                        'localport': 4544, 
                        'state': 'DOWN'
                    }
                ]
            }
}