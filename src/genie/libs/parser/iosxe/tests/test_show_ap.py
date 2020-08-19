import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_ap import ShowApSummary


# ===============================
# Unit test for 'show ap summary'
# ===============================
class TestShowApSummary(unittest.TestCase):
    """Unit test for 'show ap summary'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "ap_summary": {
            "ap_neighbor_count": 149,
            "a121-cap22": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.9b28",
                "radio_mac": "2c57.4119.a060",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.106",
                "state": "Registered"
            },
            "a132-cap15": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2244",
                "radio_mac": "2c57.4120.d2a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.146",
                "state": "Registered"
            },
            "a112-cap11": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.22d0",
                "radio_mac": "2c57.4120.d700",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.160",
                "state": "Registered"
            },
            "a112-cap10": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2420",
                "radio_mac": "2c57.4120.b180",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.102",
                "state": "Registered"
            },
            "a112-cap17": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2434",
                "radio_mac": "2c57.4120.b220",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.203",
                "state": "Registered"
            },
            "a112-cap14": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2438",
                "radio_mac": "2c57.4120.b240",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.202",
                "state": "Registered"
            },
            "a122-cap09": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2450",
                "radio_mac": "2c57.4120.b300",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.133",
                "state": "Registered"
            },
            "a131-cap43": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2454",
                "radio_mac": "2c57.4120.b320",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.93",
                "state": "Registered"
            },
            "a122-cap08": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2458",
                "radio_mac": "2c57.4120.b340",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.166",
                "state": "Registered"
            },
            "a122-cap05": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2464",
                "radio_mac": "2c57.4120.b3a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.117",
                "state": "Registered"
            },
            "a112-cap02": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2478",
                "radio_mac": "2c57.4120.b440",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.152",
                "state": "Registered"
            },
            "a112-cap08": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.247c",
                "radio_mac": "2c57.4120.b460",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.200",
                "state": "Registered"
            },
            "a112-cap21": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2488",
                "radio_mac": "2c57.4120.b4c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.199",
                "state": "Registered"
            },
            "a121-cap40": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2490",
                "radio_mac": "2c57.4120.b500",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.123",
                "state": "Registered"
            },
            "a121-cap28": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24a0",
                "radio_mac": "2c57.4120.b580",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.152",
                "state": "Registered"
            },
            "a112-cap22": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24b4",
                "radio_mac": "2c57.4120.b620",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.191",
                "state": "Registered"
            },
            "a122-cap13": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24b8",
                "radio_mac": "2c57.4120.b640",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.169",
                "state": "Registered"
            },
            "a121-cap30": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24bc",
                "radio_mac": "2c57.4120.b660",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.107",
                "state": "Registered"
            },
            "a111-cap29": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24c4",
                "radio_mac": "2c57.4120.b6a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.139",
                "state": "Registered"
            },
            "a122-cap10": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24d0",
                "radio_mac": "2c57.4120.b700",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.161",
                "state": "Registered"
            },
            "a121-cap27": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24d8",
                "radio_mac": "2c57.4120.b740",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.149",
                "state": "Registered"
            },
            "a111-cap52": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24dc",
                "radio_mac": "2c57.4120.b760",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.170",
                "state": "Registered"
            },
            "a111-cap30": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24f0",
                "radio_mac": "2c57.4120.b800",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.177",
                "state": "Registered"
            },
            "a111-cap50": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.24f4",
                "radio_mac": "2c57.4120.b820",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.183",
                "state": "Registered"
            },
            "a111-cap55": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2500",
                "radio_mac": "2c57.4120.b880",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.165",
                "state": "Registered"
            },
            "a111-cap45": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2508",
                "radio_mac": "2c57.4120.b8c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.144",
                "state": "Registered"
            },
            "a132-cap25": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2514",
                "radio_mac": "2c57.4120.b920",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.88",
                "state": "Registered"
            },
            "a111-cap28": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2518",
                "radio_mac": "2c57.4120.b940",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.175",
                "state": "Registered"
            },
            "a111-cap31": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.251c",
                "radio_mac": "2c57.4120.b960",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.145",
                "state": "Registered"
            },
            "a112-cap12": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2534",
                "radio_mac": "2c57.4120.ba20",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.197",
                "state": "Registered"
            },
            "a111-cap32": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2540",
                "radio_mac": "2c57.4120.ba80",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.184",
                "state": "Registered"
            },
            "a131-cap46": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2548",
                "radio_mac": "2c57.4120.bac0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.99",
                "state": "Registered"
            },
            "a112-cap07": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2554",
                "radio_mac": "2c57.4120.bb20",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.158",
                "state": "Registered"
            },
            "a111-cap54": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.255c",
                "radio_mac": "2c57.4120.bb60",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.179",
                "state": "Registered"
            },
            "a112-cap06": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2560",
                "radio_mac": "2c57.4120.bb80",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.201",
                "state": "Registered"
            },
            "a112-cap18": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2564",
                "radio_mac": "2c57.4120.bba0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.198",
                "state": "Registered"
            },
            "a122-cap12": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2570",
                "radio_mac": "2c57.4120.bc00",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.127",
                "state": "Registered"
            },
            "a132-cap12": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2578",
                "radio_mac": "2c57.4120.bc40",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.108",
                "state": "Registered"
            },
            "a122-cap11": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2584",
                "radio_mac": "2c57.4120.bca0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.162",
                "state": "Registered"
            },
            "a132-cap19": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2588",
                "radio_mac": "2c57.4120.bcc0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.110",
                "state": "Registered"
            },
            "a121-cap33": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.258c",
                "radio_mac": "2c57.4120.bce0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.118",
                "state": "Registered"
            },
            "a131-cap35": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2590",
                "radio_mac": "2c57.4120.bd00",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.128",
                "state": "Registered"
            },
            "a121-cap39": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2594",
                "radio_mac": "2c57.4120.bd20",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.157",
                "state": "Registered"
            },
            "a132-cap09": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25a4",
                "radio_mac": "2c57.4120.bda0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.42",
                "state": "Registered"
            },
            "a131-cap40": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25a8",
                "radio_mac": "2c57.4120.bdc0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.96",
                "state": "Registered"
            },
            "a132-cap14": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25ac",
                "radio_mac": "2c57.4120.bde0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.120",
                "state": "Registered"
            },
            "a112-cap20": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25b4",
                "radio_mac": "2c57.4120.be20",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.151",
                "state": "Registered"
            },
            "a122-cap15": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25b8",
                "radio_mac": "2c57.4120.be40",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.163",
                "state": "Registered"
            },
            "a122-cap21": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25bc",
                "radio_mac": "2c57.4120.be60",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.121",
                "state": "Registered"
            },
            "a112-cap09": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25cc",
                "radio_mac": "2c57.4120.bee0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.194",
                "state": "Registered"
            },
            "a132-cap08": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25f0",
                "radio_mac": "2c57.4120.d000",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.122",
                "state": "Registered"
            },
            "a122-cap06": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25f8",
                "radio_mac": "2c57.4120.d040",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.119",
                "state": "Registered"
            },
            "a132-cap04": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.25fc",
                "radio_mac": "2c57.4120.d060",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.137",
                "state": "Registered"
            },
            "a112-cap01": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2600",
                "radio_mac": "2c57.4120.d080",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.178",
                "state": "Registered"
            },
            "a112-cap15": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2618",
                "radio_mac": "2c57.4120.d140",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.161",
                "state": "Registered"
            },
            "a121-cap38": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.262c",
                "radio_mac": "2c57.4120.d1e0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.148",
                "state": "Registered"
            },
            "a112-cap13": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2648",
                "radio_mac": "2c57.4120.d2c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.153",
                "state": "Registered"
            },
            "a132-cap30": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2660",
                "radio_mac": "2c57.4120.d380",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.104",
                "state": "Registered"
            },
            "a111-cap42": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2698",
                "radio_mac": "2c57.4120.d540",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.185",
                "state": "Registered"
            },
            "a111-cap53": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.26a8",
                "radio_mac": "2c57.4120.d5c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.186",
                "state": "Registered"
            },
            "a112-cap04": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2a90",
                "radio_mac": "2c57.4120.db60",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.155",
                "state": "Registered"
            },
            "a111-cap43": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2ae0",
                "radio_mac": "2c57.4120.dde0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.187",
                "state": "Registered"
            },
            "a112-cap05": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2ae8",
                "radio_mac": "2c57.4120.de20",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.159",
                "state": "Registered"
            },
            "a122-cap20": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2afc",
                "radio_mac": "2c57.4120.dec0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.168",
                "state": "Registered"
            },
            "a131-cap31": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2ca0",
                "radio_mac": "2c57.4118.7be0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.135",
                "state": "Registered"
            },
            "a132-cap16": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2e44",
                "radio_mac": "2c57.4118.8900",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.118",
                "state": "Registered"
            },
            "a111-cap41": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2e64",
                "radio_mac": "2c57.4118.8a00",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.181",
                "state": "Registered"
            },
            "a122-cap02": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50b4",
                "radio_mac": "2c57.4121.bc80",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.128",
                "state": "Registered"
            },
            "a132-cap26": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2f48",
                "radio_mac": "2c57.4118.9120",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.41",
                "state": "Registered"
            },
            "a111-cap33": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2f5c",
                "radio_mac": "2c57.4118.91c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.164",
                "state": "Registered"
            },
            "a132-cap21": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.2f6c",
                "radio_mac": "2c57.4118.9240",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.60",
                "state": "Registered"
            },
            "a131-cap27": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.44d0",
                "radio_mac": "2c57.4118.bd60",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.130",
                "state": "Registered"
            },
            "a122-cap19": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.4674",
                "radio_mac": "2c57.4118.ca80",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.158",
                "state": "Registered"
            },
            "a111-cap44": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7ea0",
                "radio_mac": "2c57.4122.cbe0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.142",
                "state": "Registered"
            },
            "a121-cap44": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7f18",
                "radio_mac": "2c57.4122.cfa0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.147",
                "state": "Registered"
            },
            "a131-cap51": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7f1c",
                "radio_mac": "2c57.4122.cfc0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.92",
                "state": "Registered"
            },
            "a112-cap19": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7f2c",
                "radio_mac": "2c57.4121.b040",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.195",
                "state": "Registered"
            },
            "a122-cap18": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7f30",
                "radio_mac": "2c57.4121.b060",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.120",
                "state": "Registered"
            },
            "a131-cap36": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7fcc",
                "radio_mac": "2c57.4121.b540",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.95",
                "state": "Registered"
            },
            "a121-cap25": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7fe4",
                "radio_mac": "2c57.4121.b600",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.159",
                "state": "Registered"
            },
            "a121-cap45": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.7ffc",
                "radio_mac": "2c57.4121.b6c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.141",
                "state": "Registered"
            },
            "a121-cap42": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5024",
                "radio_mac": "2c57.4121.b800",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.122",
                "state": "Registered"
            },
            "a121-cap43": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5028",
                "radio_mac": "2c57.4121.b820",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.139",
                "state": "Registered"
            },
            "a132-cap06": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5038",
                "radio_mac": "2c57.4121.b8a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.109",
                "state": "Registered"
            },
            "a132-cap10": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5048",
                "radio_mac": "2c57.4121.b920",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.138",
                "state": "Registered"
            },
            "a131-cap50": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5054",
                "radio_mac": "2c57.4121.b980",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.125",
                "state": "Registered"
            },
            "a131-cap38": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5074",
                "radio_mac": "2c57.4121.ba80",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.134",
                "state": "Registered"
            },
            "a122-cap07": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50a0",
                "radio_mac": "2c57.4121.bbe0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.132",
                "state": "Registered"
            },
            "a132-cap11": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50a4",
                "radio_mac": "2c57.4121.bc00",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.105",
                "state": "Registered"
            },
            "a121-cap37": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50b8",
                "radio_mac": "2c57.4121.bca0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.112",
                "state": "Registered"
            },
            "a112-cap26": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50c4",
                "radio_mac": "2c57.4121.bd00",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.162",
                "state": "Registered"
            },
            "a131-cap48": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50d0",
                "radio_mac": "2c57.4121.bd60",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.132",
                "state": "Registered"
            },
            "a132-cap07": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50dc",
                "radio_mac": "2c57.4121.bdc0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.84",
                "state": "Registered"
            },
            "a131-cap42": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.50ec",
                "radio_mac": "2c57.4121.be40",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.101",
                "state": "Registered"
            },
            "a122-cap16": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5100",
                "radio_mac": "2c57.4121.bee0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.130",
                "state": "Registered"
            },
            "a132-cap28": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5110",
                "radio_mac": "2c57.4121.bf60",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.124",
                "state": "Registered"
            },
            "a121-cap31": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5120",
                "radio_mac": "2c57.4121.bfe0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.129",
                "state": "Registered"
            },
            "a131-cap39": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5128",
                "radio_mac": "2c57.4121.b020",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.97",
                "state": "Registered"
            },
            "a131-cap34": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.513c",
                "radio_mac": "2c57.4121.b0c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.126",
                "state": "Registered"
            },
            "a132-cap20": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5140",
                "radio_mac": "2c57.4121.b0e0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.123",
                "state": "Registered"
            },
            "a112-cap03": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5168",
                "radio_mac": "2c57.4121.b220",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.154",
                "state": "Registered"
            },
            "a111-cap38": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.518c",
                "radio_mac": "2c57.4121.b340",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.143",
                "state": "Registered"
            },
            "a111-cap49": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5190",
                "radio_mac": "2c57.4121.b360",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.138",
                "state": "Registered"
            },
            "a111-cap34": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.51cc",
                "radio_mac": "2c57.4121.b540",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.146",
                "state": "Registered"
            },
            "a121-cap32": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.51e4",
                "radio_mac": "2c57.4121.b600",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.113",
                "state": "Registered"
            },
            "a111-cap40": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.51e8",
                "radio_mac": "2c57.4121.b620",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.176",
                "state": "Registered"
            },
            "a132-cap22": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.51ec",
                "radio_mac": "2c57.4121.b640",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.121",
                "state": "Registered"
            },
            "a131-cap44": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.51f8",
                "radio_mac": "2c57.4121.b6a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.94",
                "state": "Registered"
            },
            "a111-cap36": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5208",
                "radio_mac": "2c57.4121.b720",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.140",
                "state": "Registered"
            },
            "a111-cap39": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5218",
                "radio_mac": "2c57.4121.b7a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.141",
                "state": "Registered"
            },
            "a131-cap33": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5220",
                "radio_mac": "2c57.4121.b7e0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.136",
                "state": "Registered"
            },
            "a112-cap24": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5224",
                "radio_mac": "2c57.4121.b800",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.190",
                "state": "Registered"
            },
            "a121-cap34": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5254",
                "radio_mac": "2c57.4121.b980",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.155",
                "state": "Registered"
            },
            "a132-cap02": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5280",
                "radio_mac": "2c57.4121.bae0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.90",
                "state": "Registered"
            },
            "a131-cap41": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5288",
                "radio_mac": "2c57.4121.bb20",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.127",
                "state": "Registered"
            },
            "a132-cap05": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.528c",
                "radio_mac": "2c57.4121.bb40",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.105",
                "state": "Registered"
            },
            "a121-cap26": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5290",
                "radio_mac": "2c57.4121.bb60",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.154",
                "state": "Registered"
            },
            "a132-cap24": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.52a0",
                "radio_mac": "2c57.4121.bbe0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.86",
                "state": "Registered"
            },
            "a132-cap17": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.52b4",
                "radio_mac": "2c57.4121.bc80",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.81",
                "state": "Registered"
            },
            "a122-cap14": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.52b8",
                "radio_mac": "2c57.4121.bca0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.167",
                "state": "Registered"
            },
            "a121-cap35": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.52c4",
                "radio_mac": "2c57.4121.bd00",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.124",
                "state": "Registered"
            },
            "a121-cap41": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.52cc",
                "radio_mac": "2c57.4121.bd40",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.156",
                "state": "Registered"
            },
            "a111-cap35": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.52fc",
                "radio_mac": "2c57.4121.bec0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.137",
                "state": "Registered"
            },
            "a111-cap51": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5304",
                "radio_mac": "2c57.4121.bf00",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.136",
                "state": "Registered"
            },
            "a131-cap45": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5308",
                "radio_mac": "2c57.4121.bf20",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.100",
                "state": "Registered"
            },
            "a132-cap03": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5314",
                "radio_mac": "2c57.4121.bf80",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.106",
                "state": "Registered"
            },
            "a122-cap24": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5324",
                "radio_mac": "2c57.4120.a000",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.131",
                "state": "Registered"
            },
            "a131-cap29": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5328",
                "radio_mac": "2c57.4120.a020",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.129",
                "state": "Registered"
            },
            "a132-cap01": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5334",
                "radio_mac": "2c57.4120.a080",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.107",
                "state": "Registered"
            },
            "a111-cap47": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.533c",
                "radio_mac": "2c57.4120.a0c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.180",
                "state": "Registered"
            },
            "a122-cap01": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5344",
                "radio_mac": "2c57.4120.a100",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.153",
                "state": "Registered"
            },
            "a121-cap29": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5358",
                "radio_mac": "2c57.4120.a1a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.125",
                "state": "Registered"
            },
            "a112-cap23": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5360",
                "radio_mac": "2c57.4120.a1e0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.156",
                "state": "Registered"
            },
            "a111-cap48": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5374",
                "radio_mac": "2c57.4120.a280",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.182",
                "state": "Registered"
            },
            "a131-cap37": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5378",
                "radio_mac": "2c57.4120.a2a0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.133",
                "state": "Registered"
            },
            "a111-cap46": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.537c",
                "radio_mac": "2c57.4120.a2c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.171",
                "state": "Registered"
            },
            "a131-cap32": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5390",
                "radio_mac": "2c57.4120.a360",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.103",
                "state": "Registered"
            },
            "a131-cap47": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5394",
                "radio_mac": "2c57.4120.a380",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.131",
                "state": "Registered"
            },
            "a122-cap04": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.53a4",
                "radio_mac": "2c57.4120.a400",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.126",
                "state": "Registered"
            },
            "a132-cap23": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.53ac",
                "radio_mac": "2c57.4120.a440",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.119",
                "state": "Registered"
            },
            "a122-cap03": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.53bc",
                "radio_mac": "2c57.4120.a4c0",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.160",
                "state": "Registered"
            },
            "a131-cap49": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5ae4",
                "radio_mac": "2c57.4122.d880",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.33.91",
                "state": "Registered"
            },
            "a112-cap16": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5ee0",
                "radio_mac": "2c57.4119.e860",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.193",
                "state": "Registered"
            },
            "a121-cap23": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "a4b2.3291.5f9c",
                "radio_mac": "2c57.4119.ee40",
                "location": "Fab A  UK",
                "ap_ip_address": "10.6.32.140",
                "state": "Registered"
            },
            "b11-4800": {
                "slots_count": 3,
                "ap_model": "4800",
                "ethernet_mac": "7c21.0e1f.2360",
                "radio_mac": "7c21.0eec.1120",
                "location": "UK HUB/Fab A - S  UK",
                "ap_ip_address": "10.6.33.16",
                "state": "Registered"
            },
            "b12-9130": {
                "slots_count": 2,
                "ap_model": "9130AXI",
                "ethernet_mac": "6c71.0de6.1e00",
                "radio_mac": "a4b2.3904.8860",
                "location": "UK HUB/Fab B - S  UK",
                "ap_ip_address": "10.6.33.17",
                "state": "Registered"
            }
        }
    }


    golden_output1 = {'execute.return_value': '''
Number of APs: 149

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a121-cap22                       2      9130AXI   a4b2.3291.9b28  2c57.4119.a060  Fab A  UK          10.6.33.106                               Registered    
a132-cap15                       2      9130AXI   a4b2.3291.2244  2c57.4120.d2a0  Fab A  UK          10.6.32.146                               Registered    
a111-cap27                       2      9130AXI   a4b2.3291.225c  2c57.4120.d360  Fab A  UK          10.6.32.118.                              Registered    
a112-cap11                       2      9130AXI   a4b2.3291.22d0  2c57.4120.d700  Fab A  UK          10.6.33.160                               Registered    
a112-cap10                       2      9130AXI   a4b2.3291.2420  2c57.4120.b180  Fab A  UK          10.6.33.102                               Registered    
a112-cap17                       2      9130AXI   a4b2.3291.2434  2c57.4120.b220  Fab A  UK          10.6.32.203                               Registered    
a112-cap14                       2      9130AXI   a4b2.3291.2438  2c57.4120.b240  Fab A  UK          10.6.32.202                               Registered    
a122-cap09                       2      9130AXI   a4b2.3291.2450  2c57.4120.b300  Fab A  UK          10.6.33.133                               Registered    
a131-cap43                       2      9130AXI   a4b2.3291.2454  2c57.4120.b320  Fab A  UK          10.6.33.93                                Registered    
a122-cap08                       2      9130AXI   a4b2.3291.2458  2c57.4120.b340  Fab A  UK          10.6.32.166                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a122-cap05                       2      9130AXI   a4b2.3291.2464  2c57.4120.b3a0  Fab A  UK          10.6.33.117                               Registered    
a112-cap02                       2      9130AXI   a4b2.3291.2478  2c57.4120.b440  Fab A  UK          10.6.33.152                               Registered    
a112-cap08                       2      9130AXI   a4b2.3291.247c  2c57.4120.b460  Fab A  UK          10.6.32.200                               Registered    
a112-cap21                       2      9130AXI   a4b2.3291.2488  2c57.4120.b4c0  Fab A  UK          10.6.32.199                               Registered    
a121-cap40                       2      9130AXI   a4b2.3291.2490  2c57.4120.b500  Fab A  UK          10.6.33.123                               Registered    
a121-cap28                       2      9130AXI   a4b2.3291.24a0  2c57.4120.b580  Fab A  UK          10.6.32.152                               Registered    
a112-cap22                       2      9130AXI   a4b2.3291.24b4  2c57.4120.b620  Fab A  UK          10.6.32.191                               Registered    
a122-cap13                       2      9130AXI   a4b2.3291.24b8  2c57.4120.b640  Fab A  UK          10.6.32.169                               Registered    
a121-cap30                       2      9130AXI   a4b2.3291.24bc  2c57.4120.b660  Fab A  UK          10.6.33.107                               Registered    
a111-cap29                       2      9130AXI   a4b2.3291.24c4  2c57.4120.b6a0  Fab A  UK          10.6.33.139                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a122-cap10                       2      9130AXI   a4b2.3291.24d0  2c57.4120.b700  Fab A  UK          10.6.32.161                               Registered    
a121-cap27                       2      9130AXI   a4b2.3291.24d8  2c57.4120.b740  Fab A  UK          10.6.32.149                               Registered    
a111-cap52                       2      9130AXI   a4b2.3291.24dc  2c57.4120.b760  Fab A  UK          10.6.32.170                               Registered    
a111-cap30                       2      9130AXI   a4b2.3291.24f0  2c57.4120.b800  Fab A  UK          10.6.32.177                               Registered    
a111-cap50                       2      9130AXI   a4b2.3291.24f4  2c57.4120.b820  Fab A  UK          10.6.32.183                               Registered    
a111-cap55                       2      9130AXI   a4b2.3291.2500  2c57.4120.b880  Fab A  UK          10.6.32.165                               Registered    
a111-cap45                       2      9130AXI   a4b2.3291.2508  2c57.4120.b8c0  Fab A  UK          10.6.33.144                               Registered    
a132-cap25                       2      9130AXI   a4b2.3291.2514  2c57.4120.b920  Fab A  UK          10.6.32.88                                Registered    
a111-cap28                       2      9130AXI   a4b2.3291.2518  2c57.4120.b940  Fab A  UK          10.6.32.175                               Registered    
a111-cap31                       2      9130AXI   a4b2.3291.251c  2c57.4120.b960  Fab A  UK          10.6.33.145                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a112-cap12                       2      9130AXI   a4b2.3291.2534  2c57.4120.ba20  Fab A  UK          10.6.32.197                               Registered    
a111-cap32                       2      9130AXI   a4b2.3291.2540  2c57.4120.ba80  Fab A  UK          10.6.32.184                               Registered    
a131-cap46                       2      9130AXI   a4b2.3291.2548  2c57.4120.bac0  Fab A  UK          10.6.33.99                                Registered    
a112-cap07                       2      9130AXI   a4b2.3291.2554  2c57.4120.bb20  Fab A  UK          10.6.33.158                               Registered    
a111-cap54                       2      9130AXI   a4b2.3291.255c  2c57.4120.bb60  Fab A  UK          10.6.32.179                               Registered    
a112-cap06                       2      9130AXI   a4b2.3291.2560  2c57.4120.bb80  Fab A  UK          10.6.32.201                               Registered    
a112-cap18                       2      9130AXI   a4b2.3291.2564  2c57.4120.bba0  Fab A  UK          10.6.32.198                               Registered    
a122-cap12                       2      9130AXI   a4b2.3291.2570  2c57.4120.bc00  Fab A  UK          10.6.33.127                               Registered    
a132-cap12                       2      9130AXI   a4b2.3291.2578  2c57.4120.bc40  Fab A  UK          10.6.32.108                               Registered    
a122-cap11                       2      9130AXI   a4b2.3291.2584  2c57.4120.bca0  Fab A  UK          10.6.32.162                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a132-cap19                       2      9130AXI   a4b2.3291.2588  2c57.4120.bcc0  Fab A  UK          10.6.33.110                               Registered    
a121-cap33                       2      9130AXI   a4b2.3291.258c  2c57.4120.bce0  Fab A  UK          10.6.33.118                               Registered    
a131-cap35                       2      9130AXI   a4b2.3291.2590  2c57.4120.bd00  Fab A  UK          10.6.32.128                               Registered    
a121-cap39                       2      9130AXI   a4b2.3291.2594  2c57.4120.bd20  Fab A  UK          10.6.32.157                               Registered    
a132-cap09                       2      9130AXI   a4b2.3291.25a4  2c57.4120.bda0  Fab A  UK          10.6.32.42                                Registered    
a131-cap40                       2      9130AXI   a4b2.3291.25a8  2c57.4120.bdc0  Fab A  UK          10.6.33.96                                Registered    
a132-cap14                       2      9130AXI   a4b2.3291.25ac  2c57.4120.bde0  Fab A  UK          10.6.32.120                               Registered    
a112-cap20                       2      9130AXI   a4b2.3291.25b4  2c57.4120.be20  Fab A  UK          10.6.33.151                               Registered    
a122-cap15                       2      9130AXI   a4b2.3291.25b8  2c57.4120.be40  Fab A  UK          10.6.32.163                               Registered    
a122-cap21                       2      9130AXI   a4b2.3291.25bc  2c57.4120.be60  Fab A  UK          10.6.33.121                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a112-cap09                       2      9130AXI   a4b2.3291.25cc  2c57.4120.bee0  Fab A  UK          10.6.32.194                               Registered    
a132-cap08                       2      9130AXI   a4b2.3291.25f0  2c57.4120.d000  Fab A  UK          10.6.32.122                               Registered    
a122-cap06                       2      9130AXI   a4b2.3291.25f8  2c57.4120.d040  Fab A  UK          10.6.33.119                               Registered    
a132-cap04                       2      9130AXI   a4b2.3291.25fc  2c57.4120.d060  Fab A  UK          10.6.32.137                               Registered    
a112-cap01                       2      9130AXI   a4b2.3291.2600  2c57.4120.d080  Fab A  UK          10.6.32.178                               Registered    
a112-cap15                       2      9130AXI   a4b2.3291.2618  2c57.4120.d140  Fab A  UK          10.6.33.161                               Registered    
a121-cap38                       2      9130AXI   a4b2.3291.262c  2c57.4120.d1e0  Fab A  UK          10.6.32.148                               Registered    
a112-cap13                       2      9130AXI   a4b2.3291.2648  2c57.4120.d2c0  Fab A  UK          10.6.33.153                               Registered    
a132-cap30                       2      9130AXI   a4b2.3291.2660  2c57.4120.d380  Fab A  UK          10.6.33.104                               Registered    
a111-cap42                       2      9130AXI   a4b2.3291.2698  2c57.4120.d540  Fab A  UK          10.6.32.185                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a111-cap53                       2      9130AXI   a4b2.3291.26a8  2c57.4120.d5c0  Fab A  UK          10.6.32.186                               Registered    
a112-cap04                       2      9130AXI   a4b2.3291.2a90  2c57.4120.db60  Fab A  UK          10.6.33.155                               Registered    
a111-cap43                       2      9130AXI   a4b2.3291.2ae0  2c57.4120.dde0  Fab A  UK          10.6.32.187                               Registered    
a112-cap05                       2      9130AXI   a4b2.3291.2ae8  2c57.4120.de20  Fab A  UK          10.6.33.159                               Registered    
a122-cap20                       2      9130AXI   a4b2.3291.2afc  2c57.4120.dec0  Fab A  UK          10.6.32.168                               Registered    
a131-cap31                       2      9130AXI   a4b2.3291.2ca0  2c57.4118.7be0  Fab A  UK          10.6.32.135                               Registered    
a132-cap16                       2      9130AXI   a4b2.3291.2e44  2c57.4118.8900  Fab A  UK          10.6.32.118                               Registered    
a111-cap41                       2      9130AXI   a4b2.3291.2e64  2c57.4118.8a00  Fab A  UK          10.6.32.181                               Registered    
a122-cap02                       2      9130AXI   a4b2.3291.2f2c  2c57.4118.9040  default location                  UK          10.6.32.204                               Registered    
a132-cap26                       2      9130AXI   a4b2.3291.2f48  2c57.4118.9120  Fab A  UK          10.6.32.41                                Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a111-cap33                       2      9130AXI   a4b2.3291.2f5c  2c57.4118.91c0  Fab A  UK          10.6.32.164                               Registered    
a132-cap21                       2      9130AXI   a4b2.3291.2f6c  2c57.4118.9240  Fab A  UK          10.6.32.60                                Registered    
a131-cap27                       2      9130AXI   a4b2.3291.44d0  2c57.4118.bd60  Fab A  UK          10.6.32.130                               Registered    
a122-cap19                       2      9130AXI   a4b2.3291.4674  2c57.4118.ca80  Fab A  UK          10.6.32.158                               Registered    
a112-cap25                       2      9130AXI   a4b2.3291.49d4  2c57.4118.e580  Fab A  UK          10.6.32.119.                              Registered    
a111-cap44                       2      9130AXI   a4b2.3291.7ea0  2c57.4122.cbe0  Fab A  UK          10.6.33.142                               Registered    
a121-cap44                       2      9130AXI   a4b2.3291.7f18  2c57.4122.cfa0  Fab A  UK          10.6.32.147                               Registered    
a131-cap51                       2      9130AXI   a4b2.3291.7f1c  2c57.4122.cfc0  Fab A  UK          10.6.33.92                                Registered    
a112-cap19                       2      9130AXI   a4b2.3291.7f2c  2c57.4121.b040  Fab A  UK          10.6.32.195                               Registered    
a122-cap18                       2      9130AXI   a4b2.3291.7f30  2c57.4121.b060  Fab A  UK          10.6.33.120                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a131-cap36                       2      9130AXI   a4b2.3291.7fcc  2c57.4121.b540  Fab A  UK          10.6.33.95                                Registered    
a121-cap25                       2      9130AXI   a4b2.3291.7fe4  2c57.4121.b600  Fab A  UK          10.6.32.159                               Registered    
a121-cap45                       2      9130AXI   a4b2.3291.7ffc  2c57.4121.b6c0  Fab A  UK          10.6.32.141                               Registered    
a121-cap42                       2      9130AXI   a4b2.3291.5024  2c57.4121.b800  Fab A  UK          10.6.33.122                               Registered    
a121-cap43                       2      9130AXI   a4b2.3291.5028  2c57.4121.b820  Fab A  UK          10.6.32.139                               Registered    
a132-cap06                       2      9130AXI   a4b2.3291.5038  2c57.4121.b8a0  Fab A  UK          10.6.32.109                               Registered    
a132-cap10                       2      9130AXI   a4b2.3291.5048  2c57.4121.b920  Fab A  UK          10.6.32.138                               Registered    
a131-cap50                       2      9130AXI   a4b2.3291.5054  2c57.4121.b980  Fab A  UK          10.6.32.125                               Registered    
a131-cap38                       2      9130AXI   a4b2.3291.5074  2c57.4121.ba80  Fab A  UK          10.6.32.134                               Registered    
a122-cap07                       2      9130AXI   a4b2.3291.50a0  2c57.4121.bbe0  Fab A  UK          10.6.33.132                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a132-cap11                       2      9130AXI   a4b2.3291.50a4  2c57.4121.bc00  Fab A  UK          10.6.32.105                               Registered    
a122-cap02                       2      9130AXI   a4b2.3291.50b4  2c57.4121.bc80  Fab A  UK          10.6.33.128                               Registered    
a121-cap37                       2      9130AXI   a4b2.3291.50b8  2c57.4121.bca0  Fab A  UK          10.6.33.112                               Registered    
a112-cap26                       2      9130AXI   a4b2.3291.50c4  2c57.4121.bd00  Fab A  UK          10.6.33.162                               Registered    
a131-cap48                       2      9130AXI   a4b2.3291.50d0  2c57.4121.bd60  Fab A  UK          10.6.32.132                               Registered    
a132-cap07                       2      9130AXI   a4b2.3291.50dc  2c57.4121.bdc0  Fab A  UK          10.6.33.84                                Registered    
a131-cap42                       2      9130AXI   a4b2.3291.50ec  2c57.4121.be40  Fab A  UK          10.6.33.101                               Registered    
a122-cap16                       2      9130AXI   a4b2.3291.5100  2c57.4121.bee0  Fab A  UK          10.6.33.130                               Registered    
a132-cap28                       2      9130AXI   a4b2.3291.5110  2c57.4121.bf60  Fab A  UK          10.6.32.124                               Registered    
a121-cap31                       2      9130AXI   a4b2.3291.5120  2c57.4121.bfe0  Fab A  UK          10.6.33.129                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a131-cap39                       2      9130AXI   a4b2.3291.5128  2c57.4121.b020  Fab A  UK          10.6.33.97                                Registered    
a131-cap34                       2      9130AXI   a4b2.3291.513c  2c57.4121.b0c0  Fab A  UK          10.6.32.126                               Registered    
a132-cap20                       2      9130AXI   a4b2.3291.5140  2c57.4121.b0e0  Fab A  UK          10.6.32.123                               Registered    
a112-cap03                       2      9130AXI   a4b2.3291.5168  2c57.4121.b220  Fab A  UK          10.6.33.154                               Registered    
a111-cap38                       2      9130AXI   a4b2.3291.518c  2c57.4121.b340  Fab A  UK          10.6.33.143                               Registered    
a111-cap49                       2      9130AXI   a4b2.3291.5190  2c57.4121.b360  Fab A  UK          10.6.33.138                               Registered    
a111-cap34                       2      9130AXI   a4b2.3291.51cc  2c57.4121.b540  Fab A  UK          10.6.33.146                               Registered    
a121-cap32                       2      9130AXI   a4b2.3291.51e4  2c57.4121.b600  Fab A  UK          10.6.33.113                               Registered    
a111-cap40                       2      9130AXI   a4b2.3291.51e8  2c57.4121.b620  Fab A  UK          10.6.32.176                               Registered    
a132-cap22                       2      9130AXI   a4b2.3291.51ec  2c57.4121.b640  Fab A  UK          10.6.32.121                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a131-cap44                       2      9130AXI   a4b2.3291.51f8  2c57.4121.b6a0  Fab A  UK          10.6.33.94                                Registered    
a111-cap36                       2      9130AXI   a4b2.3291.5208  2c57.4121.b720  Fab A  UK          10.6.33.140                               Registered    
a111-cap39                       2      9130AXI   a4b2.3291.5218  2c57.4121.b7a0  Fab A  UK          10.6.33.141                               Registered    
a131-cap33                       2      9130AXI   a4b2.3291.5220  2c57.4121.b7e0  Fab A  UK          10.6.32.136                               Registered    
a112-cap24                       2      9130AXI   a4b2.3291.5224  2c57.4121.b800  Fab A  UK          10.6.32.190                               Registered    
a121-cap34                       2      9130AXI   a4b2.3291.5254  2c57.4121.b980  Fab A  UK          10.6.32.155                               Registered    
a132-cap02                       2      9130AXI   a4b2.3291.5280  2c57.4121.bae0  Fab A  UK          10.6.32.90                                Registered    
a131-cap41                       2      9130AXI   a4b2.3291.5288  2c57.4121.bb20  Fab A  UK          10.6.32.127                               Registered    
a132-cap05                       2      9130AXI   a4b2.3291.528c  2c57.4121.bb40  Fab A  UK          10.6.33.105                               Registered    
a121-cap26                       2      9130AXI   a4b2.3291.5290  2c57.4121.bb60  Fab A  UK          10.6.32.154                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a132-cap24                       2      9130AXI   a4b2.3291.52a0  2c57.4121.bbe0  Fab A  UK          10.6.32.86                                Registered    
a132-cap17                       2      9130AXI   a4b2.3291.52b4  2c57.4121.bc80  Fab A  UK          10.6.33.81                                Registered    
a122-cap14                       2      9130AXI   a4b2.3291.52b8  2c57.4121.bca0  Fab A  UK          10.6.32.167                               Registered    
a121-cap35                       2      9130AXI   a4b2.3291.52c4  2c57.4121.bd00  Fab A  UK          10.6.33.124                               Registered    
a121-cap41                       2      9130AXI   a4b2.3291.52cc  2c57.4121.bd40  Fab A  UK          10.6.32.156                               Registered    
a111-cap35                       2      9130AXI   a4b2.3291.52fc  2c57.4121.bec0  Fab A  UK          10.6.33.137                               Registered    
a111-cap51                       2      9130AXI   a4b2.3291.5304  2c57.4121.bf00  Fab A  UK          10.6.33.136                               Registered    
a131-cap45                       2      9130AXI   a4b2.3291.5308  2c57.4121.bf20  Fab A  UK          10.6.33.100                               Registered    
a132-cap03                       2      9130AXI   a4b2.3291.5314  2c57.4121.bf80  Fab A  UK          10.6.32.106                               Registered    
a122-cap24                       2      9130AXI   a4b2.3291.5324  2c57.4120.a000  Fab A  UK          10.6.33.131                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a131-cap29                       2      9130AXI   a4b2.3291.5328  2c57.4120.a020  Fab A  UK          10.6.32.129                               Registered    
a132-cap01                       2      9130AXI   a4b2.3291.5334  2c57.4120.a080  Fab A  UK          10.6.32.107                               Registered    
a111-cap47                       2      9130AXI   a4b2.3291.533c  2c57.4120.a0c0  Fab A  UK          10.6.32.180                               Registered    
a122-cap01                       2      9130AXI   a4b2.3291.5344  2c57.4120.a100  Fab A  UK          10.6.32.153                               Registered    
a121-cap29                       2      9130AXI   a4b2.3291.5358  2c57.4120.a1a0  Fab A  UK          10.6.33.125                               Registered    
a112-cap23                       2      9130AXI   a4b2.3291.5360  2c57.4120.a1e0  Fab A  UK          10.6.33.156                               Registered    
a111-cap48                       2      9130AXI   a4b2.3291.5374  2c57.4120.a280  Fab A  UK          10.6.32.182                               Registered    
a131-cap37                       2      9130AXI   a4b2.3291.5378  2c57.4120.a2a0  Fab A  UK          10.6.32.133                               Registered    
a111-cap46                       2      9130AXI   a4b2.3291.537c  2c57.4120.a2c0  Fab A  UK          10.6.32.171                               Registered    
a131-cap32                       2      9130AXI   a4b2.3291.5390  2c57.4120.a360  Fab A  UK          10.6.33.103                               Registered    

AP Name                            Slots    AP Model  Ethernet MAC    Radio MAC       Location                          Country     IP Address                                 State         
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a131-cap47                       2      9130AXI   a4b2.3291.5394  2c57.4120.a380  Fab A  UK          10.6.32.131                               Registered    
a122-cap04                       2      9130AXI   a4b2.3291.53a4  2c57.4120.a400  Fab A  UK          10.6.33.126                               Registered    
a132-cap23                       2      9130AXI   a4b2.3291.53ac  2c57.4120.a440  Fab A  UK          10.6.32.119                               Registered    
a122-cap03                       2      9130AXI   a4b2.3291.53bc  2c57.4120.a4c0  Fab A  UK          10.6.32.160                               Registered    
a131-cap49                       2      9130AXI   a4b2.3291.5ae4  2c57.4122.d880  Fab A  UK          10.6.33.91                                Registered    
a112-cap16                       2      9130AXI   a4b2.3291.5ee0  2c57.4119.e860  Fab A  UK          10.6.32.193                               Registered    
a121-cap23                       2      9130AXI   a4b2.3291.5f9c  2c57.4119.ee40  Fab A  UK          10.6.32.140                               Registered    
b11-4800                    3      4800      7c21.0e1f.2360  7c21.0eec.1120  UK HUB/Fab A - S  UK          10.6.33.16                                Registered    
b12-9130                    2      9130AXI   6c71.0de6.1e00  a4b2.3904.8860  UK HUB/Fab B - S  UK          10.6.33.17                                Registered    

    '''}

    def test_show_ap_summary_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
