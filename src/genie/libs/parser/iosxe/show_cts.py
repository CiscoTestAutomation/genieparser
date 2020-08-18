import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================
# Schema for:
#  * 'show cts rbacl'
# ======================
class ShowCtsRbaclSchema(MetaParser):
    """Schema for show cts rbacl."""

    schema = {
        "cts_rbacl": {
            "ip_ver_support": str,
            str: {
                "ip_protocol_version": str,
                "refcnt": int,
                "flag": str,
                "stale": bool,
                Optional(int): {
                    Optional("action"): str,
                    Optional("protocol"): str,
                    Optional("direction"): str,
                    Optional("port"): int
                }
            }
        }
    }


# ======================
# Parser for:
#  * 'show cts rbacl'
# ======================
class ShowCtsRbacl(ShowCtsRbaclSchema):
    """Parser for show cts rbacl"""

    cli_command = ['show cts rbacl']

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        cts_rbacl_dict = {}

        # CTS RBACL Policy
        # ================
        # RBACL IP Version Supported: IPv4 & IPv6
        #   name   = TCP_51005-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51005
        #
        #   name   = TCP_51060-02
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51060
        #
        #   name   = TCP_51144-01
        #   IP protocol version = IPV4
        #   refcnt = 10
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51144
        #
        #   name   = TCP_51009-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51009
        #
        #   name   = TCP_GT_1023-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst gt 1023
        #
        #   name   = TCP_GT_1024-01
        #   IP protocol version = IPV4
        #   refcnt = 14
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst gt 1024
        #
        #   name   = TCP_27017-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 27017
        #
        #   name   = TCP_51237-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51237
        #
        #   name   = Deny IP-00
        #   IP protocol version = IPV4, IPV6
        #   refcnt = 1373
        #   flag   = 0xC1000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     deny ip
        #
        #   name   = PERMIT_ALL-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit ip
        #
        #   name   = UDP_GT_1024-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst gt 1024
        #
        #   name   = TCP_3000-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 3000
        #
        #   name   = TCP_4000-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 4000
        #
        #   name   = MS_REMOTE-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 3389
        #
        #   name   = UDP_ISAKMP-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 500
        #
        #   name   = TCP_6010-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6010
        #   name   = GENERIC_ACCESS-04
        #   IP protocol version = IPV4
        #   refcnt = 222
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     remark TCP_ESTABLISHED
        #     remark ------------------
        #     permit tcp established
        #     remark ICMP
        #     remark ------------------
        #     permit icmp echo
        #     permit icmp echo-reply
        #     permit icmp time-exceeded
        #     permit icmp unreachable
        #     remark NETBIOS
        #     remark ------------------
        #     permit tcp dst eq 139
        #     remark TCP_445
        #     permit tcp dst eq 445
        #     remark DNS
        #     remark ------------------
        #     permit tcp dst eq 53
        #     permit udp dst eq 53
        #     remark NTP
        #     remark ------------------
        #     permit udp dst eq 123
        #     remark ------------------
        #     remark Jabber_Bearer
        #     permit udp dst range 16384 32767
        #     remark ------------------
        #
        #   name   = TCP_29418-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 29418
        #
        #   name   = UDP_4011-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 4011
        #
        #   name   = Hyperion-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 10080
        #     permit tcp dst eq 28080
        #     permit tcp dst eq 19000
        #     permit tcp dst eq 1423
        #     permit tcp dst eq 7000
        #     permit tcp dst eq 6423
        #     permit tcp dst eq 32768
        #     permit tcp dst eq 33768
        #     permit tcp dst eq 7001
        #     permit tcp dst eq 13080
        #     permit tcp dst eq 3389
        #
        #   name   = TCP_6002-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6002
        #
        #   name   = TCP_8001-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8001
        #
        #   name   = TCP_1521-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1521
        #
        #   name   = TCP_1530-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1530
        #
        #   name   = TCP_6003-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6003
        #
        #   name   = TCP_1270-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1270
        #
        #   name   = TCP_9001-05
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 9001
        #
        #   name   = TCP_1522-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1522
        #
        #   name   = TCP_1531-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1531
        #
        #   name   = TCP_6040-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6040
        #
        #   name   = TCP_6014-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6014
        #
        #   name   = TCP_5222-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5222
        #
        #   name   = UDP_4500-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 4500
        #
        #   name   = TCP_5015-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5015
        #
        #   name   = TCP_5600-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5600
        #
        #   name   = TCP_5150-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5150
        #
        #   name   = TCP_6050-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6050
        #
        #   name   = TCP_9200-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 9200
        #
        #   name   = TCP_6060-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6060
        #
        #   name   = TCP_5601-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5601
        #
        #   name   = TCP_3036-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 3036
        #
        #   name   = TCP_3306-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 3306
        #
        #   name   = TCP_1029-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1029
        #
        #   name   = TCP_5412-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5412
        #
        #   name   = TCP_8400-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp  dst eq 8400
        #
        #   name   = TCP_8140-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8140
        #
        #   name   = TCP_8500-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8500
        #
        #   name   = TCP_4046-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 4046
        #
        #   name   = TCP_1535-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1535
        #
        #   name   = TCP_5900-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5900
        #
        #   name   = UDP_1029-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 1029
        #
        #   name   = TCP_8600-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8600
        #
        #   name   = TCP_2049-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 2049
        #
        #   name   = TCP_1536-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1536
        #
        #   name   = TCP_6090-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6090
        #
        #   name   = TCP_8080-01
        #   IP protocol version = IPV4
        #   refcnt = 34
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8080
        #
        #   name   = AD_ACCESS-02
        #   IP protocol version = IPV4
        #   refcnt = 5
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 7
        #     permit udp dst eq 7
        #     permit tcp dst eq 9
        #     permit udp dst eq 9
        #     permit tcp dst eq 53
        #     permit udp dst eq 53
        #     permit tcp dst eq 88
        #     permit udp dst eq 88
        #     permit udp dst eq 123
        #     permit tcp dst eq 135
        #     permit udp dst eq 138
        #     permit udp dst eq 137
        #     permit tcp dst eq 139
        #     permit tcp dst eq 389
        #     permit udp dst eq 389
        #     permit tcp dst eq 445
        #     permit tcp dst eq 464
        #     permit udp dst eq 464
        #     permit tcp dst eq 636
        #     permit tcp dst eq 3268
        #     permit tcp dst eq 3269
        #     permit tcp dst range 55150 55750
        #     permit udp dst range 55150 55750
        #
        #   name   = TCP_8530-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8530
        #
        #   name   = TCP_1546-02
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1546
        #
        #   name   = UDP_4046-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 4046
        #
        #   name   = TCP_5155-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5155
        #
        #   name   = TCP_6055-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6055
        #
        #   name   = TCP_4282-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 4282
        #
        #   name   = TCP_18888-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 18888
        #
        #   name   = TCP_8081-01
        #   IP protocol version = IPV4
        #   refcnt = 10
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8081
        #
        #   name   = TCP_8531-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8531
        #
        #   name   = UDP_2049-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 2049
        #
        #   name   = TCP_6605-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6605
        #
        #   name   = TCP_3149-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 3149
        #
        #   name   = TCP_8090-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8090
        #
        #   name   = TCP_9090-01
        #   IP protocol version = IPV4
        #   refcnt = 6
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 9090
        #
        #   name   = TCP_1666-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1666
        #
        #   name   = TCP_8443-01
        #   IP protocol version = IPV4
        #   refcnt = 10
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8443
        #
        #   name   = TCP_4285-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 4285
        #
        #   name   = TCP_8830-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8830
        #
        #   name   = TCP_9443-04
        #   IP protocol version = IPV4
        #   refcnt = 6
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 9443
        #
        #   name   = TCP_7625-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 7625
        #
        #   name   = TCP_5591-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5591
        #
        #   name   = TCP_6059-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 6059
        #
        #   name   = TCP_5592-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5592
        #
        #   name   = TCP_9418-01
        #   IP protocol version = IPV4
        #   refcnt = 10
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 9418
        #
        #   name   = TCP_5647-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 5647
        #
        #   name   = Crashplan-01
        #   IP protocol version = IPV4
        #   refcnt = 3
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 80
        #     permit tcp dst eq 443
        #     permit tcp dst eq 445
        #     permit tcp dst eq 8530
        #     permit tcp dst eq 8531
        #     permit tcp dst eq 10123
        #     permit udp dst eq 67
        #     permit udp dst eq 68
        #     permit udp dst eq 69
        #     permit udp dst eq 4011
        #
        #   name   = TCP_7547-01
        #   IP protocol version = IPV4
        #   refcnt = 8
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 7547
        #
        #   name   = TCP_3389-01
        #   IP protocol version = IPV4
        #   refcnt = 6
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 3389
        #
        #   name   = TCP_1688-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 1688
        #
        #   name   = Deny_TCP_80-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     deny tcp dst eq 80
        #
        #   name   = UDP_123-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 123
        #
        #   name   = TCP_ALL-01
        #   IP protocol version = IPV4
        #   refcnt = 25
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp
        #
        #   name   = TCP_7549-02
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 7549
        #
        #   name   = TCP_8089-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8089
        #
        #   name   = RANGE_8080_9999-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst range 8080 9999
        #
        #   name   = TCP_8189-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8189
        #
        #   name   = TCP_443-01
        #   IP protocol version = IPV4
        #   refcnt = 232
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 443
        #
        #   name   = TCP_371-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 371
        #
        #   name   = UDP_162-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 162
        #
        #   name   = TCP_515-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 515
        #
        #   name   = RANGE_3000_30010-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst range 3000 30010
        #
        #   name   = TCP_445-01
        #   IP protocol version = IPV4
        #   refcnt = 14
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 445
        #
        #   name   = TCP_139-01
        #   IP protocol version = IPV4
        #   refcnt = 6
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 139
        #
        #   name   = UDP_443-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 443
        #
        #   name   = MAIL-02
        #   IP protocol version = IPV4
        #   refcnt = 7
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 25
        #     permit tcp dst eq 110
        #     permit tcp dst eq 465
        #     permit tcp dst eq 587
        #     permit tcp dst eq 995
        #     permit tcp dst eq 80
        #     permit tcp dst eq 443
        #
        #   name   = UDP_137-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 137
        #
        #   name   = TCP_229-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 229
        #
        #   name   = TCP_8778-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 8778
        #
        #   name   = UDP_138-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 138
        #
        #   name   = TCP_635-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 635
        #
        #   name   = NFS-07
        #   IP protocol version = IPV4
        #   refcnt = 204
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 111
        #     permit udp dst eq 111
        #     permit tcp dst eq 635
        #     permit udp dst eq 635
        #     permit tcp dst eq 2049
        #     permit udp dst eq 2049
        #     permit tcp dst eq 4045
        #     permit udp dst eq 4045
        #     permit tcp dst eq 4046
        #     permit udp dst eq 4046
        #     permit tcp dst eq 4047
        #     permit udp dst eq 4047
        #
        #   name   = TCP_20-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 20
        #
        #   name   = DENY_ALL-01
        #   IP protocol version = IPV4
        #   refcnt = 8
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     deny ip
        #
        #   name   = TCP_7999-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 7999
        #
        #   name   = ICMP-01
        #   IP protocol version = IPV4
        #   refcnt = 172
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit icmp ech
        #     permit icmp echo
        #     permit icmp echo-reply
        #     permit icmp time-exceeded
        #     permit icmp unreachable
        #
        #   name   = TCP_21-01
        #   IP protocol version = IPV4
        #   refcnt = 16
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 21
        #
        #   name   = TCP_22-01
        #   IP protocol version = IPV4
        #   refcnt = 66
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 22
        #
        #   name   = Permit IP-00
        #   IP protocol version = IPV4, IPV6
        #   refcnt = 14
        #   flag   = 0xC1000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit ip
        #
        #   name   = TCP_389-01
        #   IP protocol version = IPV4
        #   refcnt = 3
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 389
        #
        #   name   = PRINTING-11
        #   IP protocol version = IPV4
        #   refcnt = 5
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq bootps
        #     permit udp dst eq snmp
        #     permit udp dst eq snmptrap
        #     permit tcp dst eq lpd
        #     permit tcp dst eq www
        #     permit udp src eq snmp
        #     permit tcp dst eq 443
        #     permit tcp dst eq 9100
        #
        #   name   = TCP_23-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 23
        #
        #   name   = TCP_25-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 25
        #
        #   name   = TCP_80-03
        #   IP protocol version = IPV4
        #   refcnt = 230
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 80
        #
        #   name   = TCP_53-04
        #   IP protocol version = IPV4
        #   refcnt = 9
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 53
        #
        #   name   = TCP_ESTABLISHED-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp established
        #
        #   name   = UDP_ANY-01
        #   IP protocol version = IPV4
        #   refcnt = 18
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp
        #
        #   name   = UDP_53-09
        #   IP protocol version = IPV4
        #   refcnt = 12
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 53
        #
        #   name   = TCP_FTP-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 21
        #
        #   name   = SRM-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 80
        #     permit tcp dst eq 443
        #     permit tcp dst eq 8080
        #     permit tcp dst eq 4432
        #     permit tcp dst eq 5431
        #     permit tcp dst eq 5432
        #     permit tcp dst eq 4431
        #     permit tcp dst eq 5433
        #     permit tcp dst eq 4433
        #     permit tcp dst eq 8081
        #     permit tcp dst eq 8082
        #     permit tcp dst eq 8083
        #
        #   name   = UDP_67-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 67
        #
        #   name   = UDP_68-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 68
        #
        #   name   = UCM_ACCESS-05
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 69
        #     permit tcp dst eq 80
        #     permit tcp dst eq 443
        #     permit tcp dst eq 2748
        #     permit tcp dst eq 5060
        #     permit udp dst eq 5060
        #     permit tcp dst eq 5061
        #     permit tcp dst eq 5222
        #     permit tcp dst eq 6970
        #     permit tcp dst eq 6972
        #     permit tcp dst eq 7080
        #     permit tcp dst eq 8080
        #     permit tcp dst eq 8443
        #     permit tcp dst eq 2000
        #     permit udp dst eq 5061
        #     permit tcp dst eq 1720
        #
        #   name   = TCP_88-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 88
        #
        #   name   = TCP_10000-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 10000
        #
        #   name   = UDP_69-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 69
        #
        #   name   = TCP_99-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 99
        #
        #   name   = RANGE_6000_6010-02
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst range 6000 6010
        #
        #   name   = UDP_1024_to_65535-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst range 1024 65535
        #
        #   name   = UDP_10000-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 10000
        #
        #   name   = UDP_NTP-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit udp dst eq 123
        #
        #   name   = TCP_5900_to_6000-01
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst range 5900 6000
        #
        #   name   = TCP_13101-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 13101
        #
        #   name   = TCP_10123-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 10123
        #
        #   name   = RANGE_8000_8020-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst range 8000 8020
        #
        #   name   = TCP_13131-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 13131

        # RBACL IP Version Supported: IPv4 & IPv6
        ip_ver_capture = re.compile(r"^RBACL\s+IP\s+Version\s+Supported:\s(?P<ip_ver_support>.*$)")
        #   name   = TCP_13131-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        rbacl_capture = re.compile(r"^(?P<rbacl_key>.*)(?==)=\s+(?P<rbacl_value>.*$)")
        #     permit tcp dst eq 13131
        rbacl_ace_capture = re.compile(
            r"^(?P<action>(permit|deny))\s+(?P<protocol>\S+)(\s+(?P<direction>dst|src)\s+((?P<port_condition>)\S+)\s+(?P<port>\d+)|)")

        remove_lines = ('CTS RBACL Policy', '================', 'RBACL ACEs:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)
        rbacl_name = ''
        rbacl_ace_index = 1
        for line in out:
            # RBACL IP Version Supported: IPv4 & IPv6
            ip_ver_match = ip_ver_capture.match(line)
            if ip_ver_match:
                groups = ip_ver_match.groupdict()
                ip_ver_support = groups['ip_ver_support']
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                cts_rbacl_dict['cts_rbacl']['ip_ver_support'] = ip_ver_support
                continue
            #   name   = TCP_13131-01
            #   IP protocol version = IPV4
            #   refcnt = 2
            #   flag   = 0x41000000
            #   stale  = FALSE
            if rbacl_capture.match(line):
                groups = rbacl_capture.match(line).groupdict()
                rbacl_key = groups['rbacl_key'].strip().lower().replace(' ', '_')
                rbacl_value = groups['rbacl_value']
                if rbacl_value.isdigit():
                    rbacl_value = int(rbacl_value)
                if rbacl_value == "TRUE" or rbacl_value == "FALSE":
                    if rbacl_value == "TRUE":
                        rbacl_value = True
                    else:
                        rbacl_value = False
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                if rbacl_key == 'name':
                    rbacl_name = rbacl_value
                    cts_rbacl_dict['cts_rbacl'][rbacl_name] = {}
                    rbacl_ace_index = 1
                else:
                    cts_rbacl_dict['cts_rbacl'][rbacl_name].update({rbacl_key: rbacl_value})
                continue
            #     permit tcp dst eq 13131
            if rbacl_ace_capture.match(line):
                groups = rbacl_ace_capture.match(line).groupdict()
                ace_group_dict = {}
                if groups['action']:
                    ace_group_dict.update({'action': groups['action']})
                if groups['protocol']:
                    ace_group_dict.update({'protocol': groups['protocol']})
                if groups['direction']:
                    ace_group_dict.update({'direction': groups['direction']})
                if groups['port_condition']:
                    ace_group_dict.update({'port_condition': groups['port_condition']})
                if groups['port']:
                    ace_group_dict.update({'port': int(groups['port'])})
                if not cts_rbacl_dict['cts_rbacl'][rbacl_name].get(rbacl_ace_index, {}):
                    cts_rbacl_dict['cts_rbacl'][rbacl_name][rbacl_ace_index] = ace_group_dict
                rbacl_ace_index = rbacl_ace_index + 1
                continue
        return cts_rbacl_dict