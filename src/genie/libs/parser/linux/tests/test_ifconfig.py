import re
import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.metaparser.util.exceptions import (SchemaMissingKeyError, 
                                              SchemaEmptyParserError)

from genie.libs.parser.linux.ifconfig import Ifconfig


#############################################################################
# unitest For ifconfig [<interface>]
#############################################################################

class test_ifconfig(unittest.TestCase):
    device = Device(name='aDevice')
    
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "br-225e1b78e114": {
            "interface": "br-225e1b78e114",
            "flags": "4163<UP,BROADCAST,RUNNING,MULTICAST>",
            "mtu": 1500,
            "ipv4": {
                "192.168.66.1": {
                    "ip": "192.168.66.1",
                    "netmask": "255.255.255.0",
                    "broadcast": "192.168.66.255"
                }
            },
            "ipv6": {
                "fe80::42:4ff:feff:689b": {
                    "ip": "fe80::42:4ff:feff:689b",
                    "prefixlen": 64,
                    "scopeid": "0x20<link>"
                }
            },
            "type": "ether",
            "description": "Ethernet",
            "mac": "02:42:04:ff:68:9b",
            "txqueuelen": 0,
            'counters': {
                "rx_pkts": 2567079,
                "rx_bytes": 636136982,
                "rx_value": "606.6 MiB",
                "rx_errors": 0,
                "rx_dropped": 0,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 3057807,
                "tx_bytes": 628781252,
                "tx_value": "599.6 MiB",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            },
        },
        "docker0": {
            "interface": "docker0",
            "flags": "4099<UP,BROADCAST,MULTICAST>",
            "mtu": 1500,
            "ipv4": {
                "172.17.0.1": {
                    "ip": "172.17.0.1",
                    "netmask": "255.255.0.0",
                    "broadcast": "172.17.255.255"
                }
            },
            "ipv6": {
                "fe80::42:b0ff:feff:602f": {
                    "ip": "fe80::42:b0ff:feff:602f",
                    "prefixlen": 64,
                    "scopeid": "0x20<link>"
                }
            },
            "type": "ether",
            "description": "Ethernet",
            "mac": "02:42:b0:ff:60:2f",
            "txqueuelen": 0,
            'counters': {
                "rx_pkts": 201975,
                "rx_bytes": 13092415,
                "rx_value": "12.4 MiB",
                "rx_errors": 0,
                "rx_dropped": 0,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 464814,
                "tx_bytes": 610816249,
                "tx_value": "582.5 MiB",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            },
        },
        "enp0s20f0u1": {
            "interface": "enp0s20f0u1",
            "flags": "4163<UP,BROADCAST,RUNNING,MULTICAST>",
            "mtu": 1500,
            "ipv4": {
                "10.71.131.250": {
                    "ip": "10.71.131.250",
                    "netmask": "255.255.248.0",
                    "broadcast": "10.71.135.255"
                }
            },
            "ipv6": {
                "fe80::8cd5:9a1e:621f:6328": {
                    "ip": "fe80::8cd5:9a1e:621f:6328",
                    "prefixlen": 64,
                    "scopeid": "0x20<link>"
                }
            },
            "type": "ether",
            "description": "Ethernet",
            "mac": "10:6f:3f:ff:f0:ba",
            "txqueuelen": 1000,
            'counters': {
                "rx_pkts": 33613574,
                "rx_bytes": 5840995377,
                "rx_value": "5.4 GiB",
                "rx_errors": 0,
                "rx_dropped": 146055,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 1774425,
                "tx_bytes": 310494465,
                "tx_value": "296.1 MiB",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            }
        },
        "enp0s31f6": {
            "interface": "enp0s31f6",
            "flags": "4163<UP,BROADCAST,RUNNING,MULTICAST>",
            "mtu": 1500,
            "ipv4": {
                "192.168.100.51": {
                    "ip": "192.168.100.51",
                    "netmask": "255.255.255.0",
                    "broadcast": "192.168.100.255"
                }
            },
            "ipv6": {
                "fe80::39:1a5c:726d:b23e": {
                    "ip": "fe80::39:1a5c:726d:b23e",
                    "prefixlen": 64,
                    "scopeid": "0x20<link>"
                }
            },
            "type": "ether",
            "description": "Ethernet",
            "mac": "48:2a:e3:ff:58:55",
            "txqueuelen": 1000,
            'counters': {
                "rx_pkts": 66766,
                "rx_bytes": 4274334,
                "rx_value": "4.0 MiB",
                "rx_errors": 0,
                "rx_dropped": 0,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 365916,
                "tx_bytes": 67689136,
                "tx_value": "64.5 MiB",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            },
            "device_interrupt": 16,
            "device_memory": "0xe9200000-e9220000"
        },
        "lo": {
            "interface": "lo",
            "flags": "73<UP,LOOPBACK,RUNNING>",
            "mtu": 65536,
            "ipv6": {
                "::1": {
                    "ip": "::1",
                    "prefixlen": 128,
                    "scopeid": "0x10<host>"
                }
            },
            "type": "loop",
            "description": "Local Loopback",
            "txqueuelen": 1000,
            'counters': {
                "rx_pkts": 100389,
                "rx_bytes": 16793726,
                "rx_value": "16.0 MiB",
                "rx_errors": 0,
                "rx_dropped": 0,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 100389,
                "tx_bytes": 16793726,
                "tx_value": "16.0 MiB",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            }
        },
        "veth9882519": {
            "interface": "veth9882519",
            "flags": "4163<UP,BROADCAST,RUNNING,MULTICAST>",
            "mtu": 1500,
            "ipv6": {
                "fe80::48e2:88ff:feff:2812": {
                    "ip": "fe80::48e2:88ff:feff:2812",
                    "prefixlen": 64,
                    "scopeid": "0x20<link>"
                }
            },
            "type": "ether",
            "description": "Ethernet",
            "mac": "4a:e2:88:ff:28:12",
            "txqueuelen": 0,
            'counters': {
                "rx_pkts": 18100,
                "rx_bytes": 1952201,
                "rx_value": "1.8 MiB",
                "rx_errors": 0,
                "rx_dropped": 0,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 41811,
                "tx_bytes": 6932145,
                "tx_value": "6.6 MiB",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            },
        },
        "veth00b6d52": {
            "interface": "veth00b6d52",
            "flags": "4163<UP,BROADCAST,RUNNING,MULTICAST>",
            "mtu": 1500,
            "ipv6": {
                "fe80::60e7:71ff:feff:cdc2": {
                    "ip": "fe80::60e7:71ff:feff:cdc2",
                    "prefixlen": 64,
                    "scopeid": "0x20<link>"
                }
            },
            "type": "ether",
            "description": "Ethernet",
            "mac": "62:e7:71:ff:cd:c2",
            "txqueuelen": 0,
            'counters': {
                "rx_pkts": 16974,
                "rx_bytes": 2234130,
                "rx_value": "2.1 MiB",
                "rx_errors": 0,
                "rx_dropped": 0,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 39152,
                "tx_bytes": 3745874,
                "tx_value": "3.5 MiB",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            },
        }
    }

    golden_output = {'execute.return_value': '''
        br-225e1b78e114: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.66.1  netmask 255.255.255.0  broadcast 192.168.66.255
            inet6 fe80::42:4ff:feff:689b  prefixlen 64  scopeid 0x20<link>
            ether 02:42:04:ff:68:9b  txqueuelen 0  (Ethernet)
            RX packets 2567079  bytes 636136982 (606.6 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 3057807  bytes 628781252 (599.6 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        docker0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
            inet 172.17.0.1  netmask 255.255.0.0  broadcast 172.17.255.255
            inet6 fe80::42:b0ff:feff:602f  prefixlen 64  scopeid 0x20<link>
            ether 02:42:b0:ff:60:2f  txqueuelen 0  (Ethernet)
            RX packets 201975  bytes 13092415 (12.4 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 464814  bytes 610816249 (582.5 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        enp0s20f0u1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 10.71.131.250  netmask 255.255.248.0  broadcast 10.71.135.255
            inet6 fe80::8cd5:9a1e:621f:6328  prefixlen 64  scopeid 0x20<link>
            ether 10:6f:3f:ff:f0:ba  txqueuelen 1000  (Ethernet)
            RX packets 33613574  bytes 5840995377 (5.4 GiB)
            RX errors 0  dropped 146055  overruns 0  frame 0
            TX packets 1774425  bytes 310494465 (296.1 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        enp0s31f6: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 192.168.100.51  netmask 255.255.255.0  broadcast 192.168.100.255
            inet6 fe80::39:1a5c:726d:b23e  prefixlen 64  scopeid 0x20<link>
            ether 48:2a:e3:ff:58:55  txqueuelen 1000  (Ethernet)
            RX packets 66766  bytes 4274334 (4.0 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 365916  bytes 67689136 (64.5 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
            device interrupt 16  memory 0xe9200000-e9220000

        lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
            inet 127.0.0.1  netmask 255.0.0.0
            inet6 ::1  prefixlen 128  scopeid 0x10<host>
            loop  txqueuelen 1000  (Local Loopback)
            RX packets 100389  bytes 16793726 (16.0 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 100389  bytes 16793726 (16.0 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        veth9882519: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet6 fe80::48e2:88ff:feff:2812  prefixlen 64  scopeid 0x20<link>
            ether 4a:e2:88:ff:28:12  txqueuelen 0  (Ethernet)
            RX packets 18100  bytes 1952201 (1.8 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 41811  bytes 6932145 (6.6 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

        veth00b6d52: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet6 fe80::60e7:71ff:feff:cdc2  prefixlen 64  scopeid 0x20<link>
            ether 62:e7:71:ff:cd:c2  txqueuelen 0  (Ethernet)
            RX packets 16974  bytes 2234130 (2.1 MiB)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 39152  bytes 3745874 (3.5 MiB)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    '''}

    golden_parsed_output_interface = {
        "eth1": {
            "interface": "eth1",
            "flags": "4163<UP,BROADCAST,RUNNING,MULTICAST>",
            "mtu": 1500,
            "ipv4": {
                "172.16.189.208": {
                    "ip": "172.16.189.208",
                    "netmask": "255.255.255.128",
                    "broadcast": "172.16.189.255"
                }
            },
            "ipv6": {
                "2001:db8:b4e5:7de:81f3:ca32:f3fd:6c30": {
                    "ip": "2001:db8:b4e5:7de:81f3:ca32:f3fd:6c30",
                    "prefixlen": 64,
                    "scopeid": "0x0<global>"
                },
                "2001:db8:b4e5:7de:49a5:3e88:bf17:82f2": {
                    "ip": "2001:db8:b4e5:7de:49a5:3e88:bf17:82f2",
                    "prefixlen": 128,
                    "scopeid": "0x0<global>"
                },
                "2001:db8:b4e5:7de:514c:446:354e:933e": {
                    "ip": "2001:db8:b4e5:7de:514c:446:354e:933e",
                    "prefixlen": 128,
                    "scopeid": "0x0<global>"
                },
                "fe80::81f3:ca32:f3fd:6c30": {
                    "ip": "fe80::81f3:ca32:f3fd:6c30",
                    "prefixlen": 64,
                    "scopeid": "0x0<global>"
                }
            },
            "type": "ether",
            "description": "Ethernet",
            "mac": "00:50:b6:ff:4b:83",
            'counters': {
                "rx_pkts": 0,
                "rx_bytes": 0,
                "rx_value": "0.0 B",
                "rx_errors": 0,
                "rx_dropped": 0,
                "rx_overruns": 0,
                "rx_frame": 0,
                "tx_pkts": 0,
                "tx_bytes": 0,
                "tx_value": "0.0 B",
                "tx_errors": 0,
                "tx_dropped": 0,
                "tx_overruns": 0,
                "tx_carrier": 0,
                "tx_collisions": 0,
            },
        }
    }

    golden_output_interface = {'execute.return_value': '''
        eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
            inet 172.16.189.208  netmask 255.255.255.128  broadcast 172.16.189.255
            inet6 2001:db8:b4e5:7de:81f3:ca32:f3fd:6c30  prefixlen 64  scopeid 0x0<global>
            inet6 2001:db8:b4e5:7de:49a5:3e88:bf17:82f2  prefixlen 128  scopeid 0x0<global>
            inet6 2001:db8:b4e5:7de:514c:446:354e:933e  prefixlen 128  scopeid 0x0<global>
            inet6 fe80::81f3:ca32:f3fd:6c30  prefixlen 64  scopeid 0x0<global>
            ether 00:50:b6:ff:4b:83  (Ethernet)
            RX packets 0  bytes 0 (0.0 B)
            RX errors 0  dropped 0  overruns 0  frame 0
            TX packets 0  bytes 0 (0.0 B)
            TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
    '''
    }


    golden_output_two = {'execute.return_value': '''
        eth0      Link encap:Ethernet  HWaddr 00:50:56:FF:01:14
          inet addr:172.27.114.205  Bcast:172.27.114.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:feff:114/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:2004256429 errors:0 dropped:0 overruns:0 frame:0
          TX packets:4779769715 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:2084687440241 (1.8 TiB)  TX bytes:6145946777794 (5.5 TiB)

        eth1      Link encap:Ethernet  HWaddr 00:50:56:ff:a7:82
          inet addr:10.1.6.104  Bcast:10.1.6.255  Mask:255.255.255.0
          inet6 addr: fe80::250:56ff:feff:a782/64 Scope:Link
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:15305561 errors:0 dropped:0 overruns:0 frame:0
          TX packets:10687824 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:1000
          RX bytes:7049907887 (6.5 GiB)  TX bytes:732246659 (698.3 MiB)

        lo        Link encap:Local Loopback
          inet addr:127.0.0.1  Mask:255.0.0.0
          inet6 addr: ::1/128 Scope:Host
          UP LOOPBACK RUNNING  MTU:65536  Metric:1
          RX packets:1894651 errors:0 dropped:0 overruns:0 frame:0
          TX packets:1894651 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:168964687 (161.1 MiB)  TX bytes:168964687 (161.1 MiB)

        virbr0    Link encap:Ethernet  HWaddr 52:54:00:FF:65:9F
          inet addr:192.168.122.1  Bcast:192.168.122.255  Mask:255.255.255.0
          UP BROADCAST RUNNING MULTICAST  MTU:1500  Metric:1
          RX packets:0 errors:0 dropped:0 overruns:0 frame:0
          TX packets:0 errors:0 dropped:0 overruns:0 carrier:0
          collisions:0 txqueuelen:0
          RX bytes:0 (0.0 b)  TX bytes:0 (0.0 b)
    '''}

    golden_parsed_output_two = {
        "eth0":{
            "interface":"eth0",
            "description":"Ethernet",
            "type":"Ethernet",
            "ipv4":{
                "172.27.114.205":{
                    "ip":"172.27.114.205",
                    "broadcast":"172.27.114.255",
                    "netmask":"255.255.255.0"
                }
            },
            "flags":"UP BROADCAST RUNNING MULTICAST",
            "mtu":1500,
            "counters":{
                "rx_pkts":2004256429,
                "rx_errors":0,
                "rx_dropped":0,
                "rx_overruns":0,
                "rx_frame":0,
                "tx_pkts":4779769715,
                "tx_errors":0,
                "tx_dropped":0,
                "tx_overruns":0,
                "tx_carrier":0,
                "tx_collisions":0,
                "rx_bytes":2084687440241,
                "rx_value":"1.8 TiB",
                "tx_bytes":6145946777794,
                "tx_value":"5.5 TiB"
            },
            "txqueuelen":1000
        },
        "eth1":{
            "interface":"eth1",
            "description":"Ethernet",
            "type":"Ethernet",
            "ipv4":{
                "10.1.6.104":{
                    "ip":"10.1.6.104",
                    "broadcast":"10.1.6.255",
                    "netmask":"255.255.255.0"
                }
            },
            "flags":"UP BROADCAST RUNNING MULTICAST",
            "mtu":1500,
            "counters":{
                "rx_pkts":15305561,
                "rx_errors":0,
                "rx_dropped":0,
                "rx_overruns":0,
                "rx_frame":0,
                "tx_pkts":10687824,
                "tx_errors":0,
                "tx_dropped":0,
                "tx_overruns":0,
                "tx_carrier":0,
                "tx_collisions":0,
                "rx_bytes":7049907887,
                "rx_value":"6.5 GiB",
                "tx_bytes":732246659,
                "tx_value":"698.3 MiB"
            },
            "txqueuelen":1000
        },
        "lo":{
            "interface":"lo",
            "description":"Local Loopback",
            "type":"Local Loopback",
            "ipv4":{
                "127.0.0.1":{
                    "ip":"127.0.0.1",
                    "broadcast":"",
                    "netmask":"255.0.0.0"
                }
            },
            "flags":"UP LOOPBACK RUNNING",
            "mtu":65536,
            "counters":{
                "rx_pkts":1894651,
                "rx_errors":0,
                "rx_dropped":0,
                "rx_overruns":0,
                "rx_frame":0,
                "tx_pkts":1894651,
                "tx_errors":0,
                "tx_dropped":0,
                "tx_overruns":0,
                "tx_carrier":0,
                "tx_collisions":0,
                "rx_bytes":168964687,
                "rx_value":"161.1 MiB",
                "tx_bytes":168964687,
                "tx_value":"161.1 MiB"
            },
            "txqueuelen":0
        },
        "virbr0":{
            "interface":"virbr0",
            "description":"Ethernet",
            "type":"Ethernet",
            "ipv4":{
                "192.168.122.1":{
                    "ip":"192.168.122.1",
                    "broadcast":"192.168.122.255",
                    "netmask":"255.255.255.0"
                }
            },
            "flags":"UP BROADCAST RUNNING MULTICAST",
            "mtu":1500,
            "counters":{
                "rx_pkts":0,
                "rx_errors":0,
                "rx_dropped":0,
                "rx_overruns":0,
                "rx_frame":0,
                "tx_pkts":0,
                "tx_errors":0,
                "tx_dropped":0,
                "tx_overruns":0,
                "tx_carrier":0,
                "tx_collisions":0,
                "rx_bytes":0,
                "rx_value":"0.0 b",
                "tx_bytes":0,
                "tx_value":"0.0 b"
            },
            "txqueuelen":0
        }
    }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = Ifconfig(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Ifconfig(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_interface(self):
        self.device = Mock(**self.golden_output_interface)
        obj = Ifconfig(device=self.device)
        parsed_output = obj.parse(interface='eth1')
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_interface)

    def test_golden_two(self):
        self.device = Mock(**self.golden_output_two)
        obj = Ifconfig(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_two)

if __name__ == '__main__':
    unittest.main()
