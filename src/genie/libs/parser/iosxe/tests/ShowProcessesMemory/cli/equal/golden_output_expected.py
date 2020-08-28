expected_output = {
    "lsmi_io_pool": {"free": 832, "total": 6295128, "used": 6294296},
    "pid": {
        0: {
            "index": {
                1: {
                    "allocated": 678985440,
                    "freed": 347855496,
                    "getbufs": 428,
                    "holding": 304892096,
                    "pid": 0,
                    "process": "*Init*",
                    "retbufs": 2134314,
                    "tty": 0,
                },
                2: {
                    "allocated": 800,
                    "freed": 4965889216,
                    "getbufs": 17,
                    "holding": 800,
                    "pid": 0,
                    "process": "*Sched*",
                    "retbufs": 17,
                    "tty": 0,
                },
                3: {
                    "allocated": 2675774192,
                    "freed": 2559881512,
                    "getbufs": 2111,
                    "holding": 43465512,
                    "pid": 0,
                    "process": "*Dead*",
                    "retbufs": 351,
                    "tty": 0,
                },
                4: {
                    "allocated": 0,
                    "freed": 0,
                    "getbufs": 0,
                    "holding": 4070880,
                    "pid": 0,
                    "process": "*MallocLite*",
                    "retbufs": 0,
                    "tty": 0,
                },
            }
        },
        1: {
            "index": {
                1: {
                    "allocated": 3415536,
                    "freed": 879912,
                    "getbufs": 0,
                    "holding": 2565568,
                    "pid": 1,
                    "process": "Chunk Manager",
                    "retbufs": 0,
                    "tty": 0,
                }
            }
        },
    },
    "processor_pool": {"free": 9662451880, "total": 10147887840, "used": 485435960},
    "reserve_p_pool": {"free": 102316, "total": 102404, "used": 88},
}
