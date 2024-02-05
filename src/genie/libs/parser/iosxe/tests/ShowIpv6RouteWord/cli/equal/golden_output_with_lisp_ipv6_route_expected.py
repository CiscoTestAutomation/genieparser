expected_output = {
    "total_prefixes": 1,
    "entry": {
        "::/0": {
            "ip": "::",
            "tag_name": "2",
	    "tag_type": "LISP destinations-summary",
            "distance": "254",
            "metric": "1",
            "known_via": "lisp",
            "mask": "0",
            "paths": {
                1: {
                    "interface": "LISP0",
                    "age": "00:00:03",
                    "metric": "1",
                    "share_count": "1"
                }
            },
            "share_count": "0",
            "route_count": "1/1"
        }
    }
}
