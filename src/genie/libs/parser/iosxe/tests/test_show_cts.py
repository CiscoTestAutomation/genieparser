import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_cts import ShowCtsRbacl.Py


# =================================
# Unit test for 'show cts rbacl.py'
# =================================
class TestShowCtsRbacl.Py(unittest.TestCase):
    """Unit test for 'show cts rbacl.py'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
    "cts_rbacl": {
        "ip_ver_support": "IPv4 & IPv6",
        "TCP_51005-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 51005
            }
        },
        "TCP_51060-02": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 51060
            }
        },
        "TCP_51144-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 10,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 51144
            }
        },
        "TCP_51009-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 51009
            }
        },
        "TCP_GT_1023-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1023
            }
        },
        "TCP_GT_1024-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 14,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1024
            }
        },
        "TCP_27017-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 27017
            }
        },
        "TCP_51237-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 51237
            }
        },
        "Deny IP-00": {
            "ip_protocol_version": "IPV4, IPV6",
            "refcnt": 1373,
            "flag": "0xC1000000",
            "stale": "FALSE",
            1: {
                "action": "deny",
                "protocol": "ip"
            }
        },
        "PERMIT_ALL-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "ip"
            }
        },
        "UDP_GT_1024-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 1024
            }
        },
        "TCP_3000-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3000
            }
        },
        "TCP_4000-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4000
            }
        },
        "MS_REMOTE-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3389
            }
        },
        "UDP_ISAKMP-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 500
            }
        },
        "TCP_6010-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6010
            }
        },
        "GENERIC_ACCESS-04": {
            "ip_protocol_version": "IPV4",
            "refcnt": 222,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp"
            },
            2: {
                "action": "permit",
                "protocol": "icmp"
            },
            3: {
                "action": "permit",
                "protocol": "icmp"
            },
            4: {
                "action": "permit",
                "protocol": "icmp"
            },
            5: {
                "action": "permit",
                "protocol": "icmp"
            },
            6: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 139
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 445
            },
            8: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 53
            },
            9: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 53
            },
            10: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 123
            },
            11: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 16384
            }
        },
        "TCP_29418-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 29418
            }
        },
        "UDP_4011-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 4011
            }
        },
        "Hyperion-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 10080
            },
            2: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 28080
            },
            3: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 19000
            },
            4: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1423
            },
            5: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7000
            },
            6: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6423
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 32768
            },
            8: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 33768
            },
            9: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7001
            },
            10: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 13080
            },
            11: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3389
            }
        },
        "TCP_6002-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6002
            }
        },
        "TCP_8001-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8001
            }
        },
        "TCP_1521-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1521
            }
        },
        "TCP_1530-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1530
            }
        },
        "TCP_6003-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6003
            }
        },
        "TCP_1270-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1270
            }
        },
        "TCP_9001-05": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 9001
            }
        },
        "TCP_1522-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1522
            }
        },
        "TCP_1531-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1531
            }
        },
        "TCP_6040-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6040
            }
        },
        "TCP_6014-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6014
            }
        },
        "TCP_5222-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5222
            }
        },
        "UDP_4500-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 4500
            }
        },
        "TCP_5015-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5015
            }
        },
        "TCP_5600-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5600
            }
        },
        "TCP_5150-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5150
            }
        },
        "TCP_6050-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6050
            }
        },
        "TCP_9200-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 9200
            }
        },
        "TCP_6060-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6060
            }
        },
        "TCP_5601-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5601
            }
        },
        "TCP_3036-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3036
            }
        },
        "TCP_3306-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3306
            }
        },
        "TCP_1029-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1029
            }
        },
        "TCP_5412-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5412
            }
        },
        "TCP_8400-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8400
            }
        },
        "TCP_8140-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8140
            }
        },
        "TCP_8500-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8500
            }
        },
        "TCP_4046-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4046
            }
        },
        "TCP_1535-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1535
            }
        },
        "TCP_5900-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5900
            }
        },
        "UDP_1029-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 1029
            }
        },
        "TCP_8600-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8600
            }
        },
        "TCP_2049-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 2049
            }
        },
        "TCP_1536-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1536
            }
        },
        "TCP_6090-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6090
            }
        },
        "TCP_8080-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 34,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8080
            }
        },
        "AD_ACCESS-02": {
            "ip_protocol_version": "IPV4",
            "refcnt": 5,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7
            },
            2: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 7
            },
            3: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 9
            },
            4: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 9
            },
            5: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 53
            },
            6: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 53
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 88
            },
            8: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 88
            },
            9: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 123
            },
            10: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 135
            },
            11: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 138
            },
            12: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 137
            },
            13: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 139
            },
            14: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 389
            },
            15: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 389
            },
            16: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 445
            },
            17: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 464
            },
            18: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 464
            },
            19: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 636
            },
            20: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3268
            },
            21: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3269
            },
            22: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 55150
            },
            23: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 55150
            }
        },
        "TCP_8530-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8530
            }
        },
        "TCP_1546-02": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1546
            }
        },
        "UDP_4046-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 4046
            }
        },
        "TCP_5155-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5155
            }
        },
        "TCP_6055-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6055
            }
        },
        "TCP_4282-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4282
            }
        },
        "TCP_18888-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 18888
            }
        },
        "TCP_8081-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 10,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8081
            }
        },
        "TCP_8531-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8531
            }
        },
        "UDP_2049-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 2049
            }
        },
        "TCP_6605-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6605
            }
        },
        "TCP_3149-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3149
            }
        },
        "TCP_8090-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8090
            }
        },
        "TCP_9090-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 6,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 9090
            }
        },
        "TCP_1666-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1666
            }
        },
        "TCP_8443-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 10,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8443
            }
        },
        "TCP_4285-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4285
            }
        },
        "TCP_8830-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8830
            }
        },
        "TCP_9443-04": {
            "ip_protocol_version": "IPV4",
            "refcnt": 6,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 9443
            }
        },
        "TCP_7625-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7625
            }
        },
        "TCP_5591-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5591
            }
        },
        "TCP_6059-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6059
            }
        },
        "TCP_5592-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5592
            }
        },
        "TCP_9418-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 10,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 9418
            }
        },
        "TCP_5647-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5647
            }
        },
        "Crashplan-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 3,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 80
            },
            2: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 443
            },
            3: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 445
            },
            4: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8530
            },
            5: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8531
            },
            6: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 10123
            },
            7: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 67
            },
            8: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 68
            },
            9: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 69
            },
            10: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 4011
            }
        },
        "TCP_7547-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 8,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7547
            }
        },
        "TCP_3389-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 6,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3389
            }
        },
        "TCP_1688-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1688
            }
        },
        "Deny_TCP_80-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "deny",
                "protocol": "tcp",
                "direction": "dst",
                "port": 80
            }
        },
        "UDP_123-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 123
            }
        },
        "TCP_ALL-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 25,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp"
            }
        },
        "TCP_7549-02": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7549
            }
        },
        "TCP_8089-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8089
            }
        },
        "RANGE_8080_9999-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8080
            }
        },
        "TCP_8189-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8189
            }
        },
        "TCP_443-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 232,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 443
            }
        },
        "TCP_371-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 371
            }
        },
        "UDP_162-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 162
            }
        },
        "TCP_515-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 515
            }
        },
        "RANGE_3000_30010-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 3000
            }
        },
        "TCP_445-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 14,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 445
            }
        },
        "TCP_139-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 6,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 139
            }
        },
        "UDP_443-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 443
            }
        },
        "MAIL-02": {
            "ip_protocol_version": "IPV4",
            "refcnt": 7,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 25
            },
            2: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 110
            },
            3: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 465
            },
            4: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 587
            },
            5: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 995
            },
            6: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 80
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 443
            }
        },
        "UDP_137-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 137
            }
        },
        "TCP_229-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 229
            }
        },
        "TCP_8778-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8778
            }
        },
        "UDP_138-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 138
            }
        },
        "TCP_635-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 635
            }
        },
        "NFS-07": {
            "ip_protocol_version": "IPV4",
            "refcnt": 204,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 111
            },
            2: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 111
            },
            3: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 635
            },
            4: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 635
            },
            5: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 2049
            },
            6: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 2049
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4045
            },
            8: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 4045
            },
            9: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4046
            },
            10: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 4046
            },
            11: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4047
            },
            12: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 4047
            }
        },
        "TCP_20-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 20
            }
        },
        "DENY_ALL-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 8,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "deny",
                "protocol": "ip"
            }
        },
        "TCP_7999-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7999
            }
        },
        "ICMP-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 172,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "icmp"
            },
            2: {
                "action": "permit",
                "protocol": "icmp"
            },
            3: {
                "action": "permit",
                "protocol": "icmp"
            },
            4: {
                "action": "permit",
                "protocol": "icmp"
            },
            5: {
                "action": "permit",
                "protocol": "icmp"
            }
        },
        "TCP_21-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 16,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 21
            }
        },
        "TCP_22-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 66,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 22
            }
        },
        "Permit IP-00": {
            "ip_protocol_version": "IPV4, IPV6",
            "refcnt": 14,
            "flag": "0xC1000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "ip"
            }
        },
        "TCP_389-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 3,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 389
            }
        },
        "PRINTING-11": {
            "ip_protocol_version": "IPV4",
            "refcnt": 5,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp"
            },
            2: {
                "action": "permit",
                "protocol": "udp"
            },
            3: {
                "action": "permit",
                "protocol": "udp"
            },
            4: {
                "action": "permit",
                "protocol": "tcp"
            },
            5: {
                "action": "permit",
                "protocol": "tcp"
            },
            6: {
                "action": "permit",
                "protocol": "udp"
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 443
            },
            8: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 9100
            }
        },
        "TCP_23-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 23
            }
        },
        "TCP_25-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 25
            }
        },
        "TCP_80-03": {
            "ip_protocol_version": "IPV4",
            "refcnt": 230,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 80
            }
        },
        "TCP_53-04": {
            "ip_protocol_version": "IPV4",
            "refcnt": 9,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 53
            }
        },
        "TCP_ESTABLISHED-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp"
            }
        },
        "UDP_ANY-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 18,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp"
            }
        },
        "UDP_53-09": {
            "ip_protocol_version": "IPV4",
            "refcnt": 12,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 53
            }
        },
        "TCP_FTP-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 21
            }
        },
        "SRM-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 80
            },
            2: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 443
            },
            3: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8080
            },
            4: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4432
            },
            5: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5431
            },
            6: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5432
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4431
            },
            8: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5433
            },
            9: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 4433
            },
            10: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8081
            },
            11: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8082
            },
            12: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8083
            }
        },
        "UDP_67-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 67
            }
        },
        "UDP_68-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 68
            }
        },
        "UCM_ACCESS-05": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 69
            },
            2: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 80
            },
            3: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 443
            },
            4: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 2748
            },
            5: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5060
            },
            6: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 5060
            },
            7: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5061
            },
            8: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5222
            },
            9: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6970
            },
            10: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6972
            },
            11: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 7080
            },
            12: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8080
            },
            13: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8443
            },
            14: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 2000
            },
            15: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 5061
            },
            16: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 1720
            }
        },
        "TCP_88-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 88
            }
        },
        "TCP_10000-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 10000
            }
        },
        "UDP_69-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 69
            }
        },
        "TCP_99-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 99
            }
        },
        "RANGE_6000_6010-02": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 6000
            }
        },
        "UDP_1024_to_65535-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 1024
            }
        },
        "UDP_10000-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 10000
            }
        },
        "UDP_NTP-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "udp",
                "direction": "dst",
                "port": 123
            }
        },
        "TCP_5900_to_6000-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 4,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 5900
            }
        },
        "TCP_13101-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 13101
            }
        },
        "TCP_10123-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 10123
            }
        },
        "RANGE_8000_8020-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 8000
            }
        },
        "TCP_13131-01": {
            "ip_protocol_version": "IPV4",
            "refcnt": 2,
            "flag": "0x41000000",
            "stale": "FALSE",
            1: {
                "action": "permit",
                "protocol": "tcp",
                "direction": "dst",
                "port": 13131
            }
        }
    }
}

    golden_output1 = {'execute.return_value': '''
CTS RBACL Policy
================
RBACL IP Version Supported: IPv4 & IPv6
  name   = TCP_51005-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 51005

  name   = TCP_51060-02
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 51060

  name   = TCP_51144-01
  IP protocol version = IPV4
  refcnt = 10
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 51144

  name   = TCP_51009-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 51009

  name   = TCP_GT_1023-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst gt 1023

  name   = TCP_GT_1024-01
  IP protocol version = IPV4
  refcnt = 14
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst gt 1024

  name   = TCP_27017-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 27017
         
  name   = TCP_51237-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 51237

  name   = Deny IP-00
  IP protocol version = IPV4, IPV6
  refcnt = 1373
  flag   = 0xC1000000
  stale  = FALSE
  RBACL ACEs:
    deny ip

  name   = PERMIT_ALL-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit ip

  name   = UDP_GT_1024-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst gt 1024

  name   = TCP_3000-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 3000

  name   = TCP_4000-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 4000

  name   = MS_REMOTE-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 3389

  name   = UDP_ISAKMP-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 500

  name   = TCP_6010-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6010
  name   = GENERIC_ACCESS-04
  IP protocol version = IPV4
  refcnt = 222
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    remark TCP_ESTABLISHED
    remark ------------------
    permit tcp established
    remark ICMP
    remark ------------------
    permit icmp echo
    permit icmp echo-reply
    permit icmp time-exceeded
    permit icmp unreachable
    remark NETBIOS
    remark ------------------
    permit tcp dst eq 139
    remark TCP_445
    permit tcp dst eq 445
    remark DNS
    remark ------------------
    permit tcp dst eq 53
    permit udp dst eq 53
    remark NTP
    remark ------------------
    permit udp dst eq 123
    remark ------------------
    remark Jabber_Bearer
    permit udp dst range 16384 32767
    remark ------------------

  name   = TCP_29418-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 29418
          
  name   = UDP_4011-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 4011
          
  name   = Hyperion-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 10080
    permit tcp dst eq 28080
    permit tcp dst eq 19000
    permit tcp dst eq 1423
    permit tcp dst eq 7000
    permit tcp dst eq 6423
    permit tcp dst eq 32768
    permit tcp dst eq 33768
    permit tcp dst eq 7001
    permit tcp dst eq 13080
    permit tcp dst eq 3389
          
  name   = TCP_6002-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6002

  name   = TCP_8001-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8001

  name   = TCP_1521-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1521
          
  name   = TCP_1530-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1530

  name   = TCP_6003-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6003

  name   = TCP_1270-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1270

  name   = TCP_9001-05
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 9001

  name   = TCP_1522-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1522

  name   = TCP_1531-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1531

  name   = TCP_6040-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6040

  name   = TCP_6014-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6014

  name   = TCP_5222-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5222

  name   = UDP_4500-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 4500

  name   = TCP_5015-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5015

  name   = TCP_5600-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5600

  name   = TCP_5150-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5150

  name   = TCP_6050-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6050

  name   = TCP_9200-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 9200

  name   = TCP_6060-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6060

  name   = TCP_5601-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5601

  name   = TCP_3036-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 3036

  name   = TCP_3306-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 3306

  name   = TCP_1029-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1029

  name   = TCP_5412-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5412

  name   = TCP_8400-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp  dst eq 8400

  name   = TCP_8140-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8140

  name   = TCP_8500-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8500

  name   = TCP_4046-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 4046

  name   = TCP_1535-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1535

  name   = TCP_5900-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5900

  name   = UDP_1029-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 1029

  name   = TCP_8600-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8600

  name   = TCP_2049-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 2049

  name   = TCP_1536-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1536

  name   = TCP_6090-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6090

  name   = TCP_8080-01
  IP protocol version = IPV4
  refcnt = 34
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8080

  name   = AD_ACCESS-02
  IP protocol version = IPV4
  refcnt = 5
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 7
    permit udp dst eq 7
    permit tcp dst eq 9
    permit udp dst eq 9
    permit tcp dst eq 53
    permit udp dst eq 53
    permit tcp dst eq 88
    permit udp dst eq 88
    permit udp dst eq 123
    permit tcp dst eq 135
    permit udp dst eq 138
    permit udp dst eq 137
    permit tcp dst eq 139
    permit tcp dst eq 389
    permit udp dst eq 389
    permit tcp dst eq 445
    permit tcp dst eq 464
    permit udp dst eq 464
    permit tcp dst eq 636
    permit tcp dst eq 3268
    permit tcp dst eq 3269
    permit tcp dst range 55150 55750
    permit udp dst range 55150 55750

  name   = TCP_8530-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8530

  name   = TCP_1546-02
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1546

  name   = UDP_4046-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 4046

  name   = TCP_5155-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5155

  name   = TCP_6055-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6055

  name   = TCP_4282-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 4282

  name   = TCP_18888-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 18888

  name   = TCP_8081-01
  IP protocol version = IPV4
  refcnt = 10
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8081

  name   = TCP_8531-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8531

  name   = UDP_2049-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 2049

  name   = TCP_6605-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6605

  name   = TCP_3149-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 3149

  name   = TCP_8090-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8090

  name   = TCP_9090-01
  IP protocol version = IPV4
  refcnt = 6
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 9090

  name   = TCP_1666-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1666

  name   = TCP_8443-01
  IP protocol version = IPV4
  refcnt = 10
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8443

  name   = TCP_4285-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 4285

  name   = TCP_8830-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8830

  name   = TCP_9443-04
  IP protocol version = IPV4
  refcnt = 6
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 9443

  name   = TCP_7625-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 7625

  name   = TCP_5591-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5591

  name   = TCP_6059-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 6059

  name   = TCP_5592-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5592

  name   = TCP_9418-01
  IP protocol version = IPV4
  refcnt = 10
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 9418

  name   = TCP_5647-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 5647

  name   = Crashplan-01
  IP protocol version = IPV4
  refcnt = 3
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 80
    permit tcp dst eq 443
    permit tcp dst eq 445
    permit tcp dst eq 8530
    permit tcp dst eq 8531
    permit tcp dst eq 10123
    permit udp dst eq 67
    permit udp dst eq 68
    permit udp dst eq 69
    permit udp dst eq 4011

  name   = TCP_7547-01
  IP protocol version = IPV4
  refcnt = 8
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 7547

  name   = TCP_3389-01
  IP protocol version = IPV4
  refcnt = 6
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 3389

  name   = TCP_1688-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 1688

  name   = Deny_TCP_80-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    deny tcp dst eq 80

  name   = UDP_123-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 123

  name   = TCP_ALL-01
  IP protocol version = IPV4
  refcnt = 25
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp

  name   = TCP_7549-02
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 7549

  name   = TCP_8089-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8089

  name   = RANGE_8080_9999-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst range 8080 9999

  name   = TCP_8189-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8189

  name   = TCP_443-01
  IP protocol version = IPV4
  refcnt = 232
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 443

  name   = TCP_371-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 371

  name   = UDP_162-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 162

  name   = TCP_515-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 515

  name   = RANGE_3000_30010-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst range 3000 30010

  name   = TCP_445-01
  IP protocol version = IPV4
  refcnt = 14
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 445

  name   = TCP_139-01
  IP protocol version = IPV4
  refcnt = 6
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 139

  name   = UDP_443-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 443

  name   = MAIL-02
  IP protocol version = IPV4
  refcnt = 7
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 25
    permit tcp dst eq 110
    permit tcp dst eq 465
    permit tcp dst eq 587
    permit tcp dst eq 995
    permit tcp dst eq 80
    permit tcp dst eq 443

  name   = UDP_137-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 137

  name   = TCP_229-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 229

  name   = TCP_8778-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 8778

  name   = UDP_138-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 138

  name   = TCP_635-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 635

  name   = NFS-07
  IP protocol version = IPV4
  refcnt = 204
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 111
    permit udp dst eq 111
    permit tcp dst eq 635
    permit udp dst eq 635
    permit tcp dst eq 2049
    permit udp dst eq 2049
    permit tcp dst eq 4045
    permit udp dst eq 4045
    permit tcp dst eq 4046
    permit udp dst eq 4046
    permit tcp dst eq 4047
    permit udp dst eq 4047

  name   = TCP_20-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 20

  name   = DENY_ALL-01
  IP protocol version = IPV4
  refcnt = 8
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    deny ip

  name   = TCP_7999-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 7999

  name   = ICMP-01
  IP protocol version = IPV4
  refcnt = 172
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit icmp ech
    permit icmp echo
    permit icmp echo-reply
    permit icmp time-exceeded
    permit icmp unreachable

  name   = TCP_21-01
  IP protocol version = IPV4
  refcnt = 16
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 21

  name   = TCP_22-01
  IP protocol version = IPV4
  refcnt = 66
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 22

  name   = Permit IP-00
  IP protocol version = IPV4, IPV6
  refcnt = 14
  flag   = 0xC1000000
  stale  = FALSE
  RBACL ACEs:
    permit ip

  name   = TCP_389-01
  IP protocol version = IPV4
  refcnt = 3
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 389

  name   = PRINTING-11
  IP protocol version = IPV4
  refcnt = 5
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq bootps
    permit udp dst eq snmp
    permit udp dst eq snmptrap
    permit tcp dst eq lpd
    permit tcp dst eq www
    permit udp src eq snmp
    permit tcp dst eq 443
    permit tcp dst eq 9100

  name   = TCP_23-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 23

  name   = TCP_25-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 25

  name   = TCP_80-03
  IP protocol version = IPV4
  refcnt = 230
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 80

  name   = TCP_53-04
  IP protocol version = IPV4
  refcnt = 9
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 53

  name   = TCP_ESTABLISHED-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp established

  name   = UDP_ANY-01
  IP protocol version = IPV4
  refcnt = 18
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp

  name   = UDP_53-09
  IP protocol version = IPV4
  refcnt = 12
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 53

  name   = TCP_FTP-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 21

  name   = SRM-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 80
    permit tcp dst eq 443
    permit tcp dst eq 8080
    permit tcp dst eq 4432
    permit tcp dst eq 5431
    permit tcp dst eq 5432
    permit tcp dst eq 4431
    permit tcp dst eq 5433
    permit tcp dst eq 4433
    permit tcp dst eq 8081
    permit tcp dst eq 8082
    permit tcp dst eq 8083

  name   = UDP_67-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 67

  name   = UDP_68-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 68

  name   = UCM_ACCESS-05
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 69
    permit tcp dst eq 80
    permit tcp dst eq 443
    permit tcp dst eq 2748
    permit tcp dst eq 5060
    permit udp dst eq 5060
    permit tcp dst eq 5061
    permit tcp dst eq 5222
    permit tcp dst eq 6970
    permit tcp dst eq 6972
    permit tcp dst eq 7080
    permit tcp dst eq 8080
    permit tcp dst eq 8443
    permit tcp dst eq 2000
    permit udp dst eq 5061
    permit tcp dst eq 1720

  name   = TCP_88-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 88

  name   = TCP_10000-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 10000

  name   = UDP_69-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 69

  name   = TCP_99-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 99

  name   = RANGE_6000_6010-02
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst range 6000 6010

  name   = UDP_1024_to_65535-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst range 1024 65535

  name   = UDP_10000-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 10000

  name   = UDP_NTP-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit udp dst eq 123

  name   = TCP_5900_to_6000-01
  IP protocol version = IPV4
  refcnt = 4
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst range 5900 6000

  name   = TCP_13101-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 13101

  name   = TCP_10123-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 10123

  name   = RANGE_8000_8020-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst range 8000 8020

  name   = TCP_13131-01
  IP protocol version = IPV4
  refcnt = 2
  flag   = 0x41000000
  stale  = FALSE
  RBACL ACEs:
    permit tcp dst eq 13131

 
    '''}

    def test_show_cts_rbacl.py_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowCtsRbacl.Py(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_cts_rbacl.py_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCtsRbacl.Py(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
