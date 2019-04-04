# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.ios.show_rip import ShowIpRipDatabase, \
										   ShowIpv6Rip

from genie.libs.parser.iosxe.tests.test_show_rip import test_show_ip_rip_database as \
                                                        test_show_ip_rip_database_iosxe, \
                                                        test_show_ipv6_rip as \
                                                        test_show_ipv6_rip_iosxe

# ============================================
# Parser for 'show ip rip database'
# Parser for 'show ip rip database vrf {vrf}'
# ============================================
class test_show_ip_rip_database(test_show_ip_rip_database_iosxe):
	def test_empty(self):
		self.device1 = Mock(**self.empty_output)
		obj = ShowIpRipDatabase(device=self.device1)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden_vrf_default(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowIpRipDatabase(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_vrf_vrf1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_2)
		obj = ShowIpRipDatabase(device=self.device)
		parsed_output = obj.parse(vrf="VRF1")
		self.assertEqual(parsed_output, self.golden_parsed_output_2)


# ============================================
# unit test for 'show ipv6 rip'
# unit test for 'show ipv6 rip vrf {vrf}'
# ============================================
class test_show_ipv6_rip(test_show_ipv6_rip_iosxe):

	device = Device(name='aDevice')

	golden_parsed_output_ios = {
		"vrf": {
			"process1": {
			  "address_family": {
			    "ipv6": {
			      "distance": 120,
			      "interfaces": {
			        "Gigabitethernet0/0/0": {}
			      },
			      "maximum_paths": 1,
			      "multicast_group": "FF02::9",
			      "originate_default_route": {
			        "enabled": True
			      },
			      "pid": 62,
			      "poison_reverse": False,
			      "port": 521,
			      "redistribute": {
			        "bgp": {
			          "protocol_number": 65001,
			          "route_policy": "bgp-to-rip"
			        }
			      },
			      "split_horizon": True,
			      "statistics": {
			        "periodic_updates": 223,
			        "trigger_updates": 1
			      },
			      "timers": {
			        "expire_time": 15,
			        "flush_interval": 30,
			        "holddown_interval": 10,
			        "update_interval": 5
			      }
			    }
			  }
			}
		}
	}

	golden_output_ios = {'execute.return_value': '''\
		Router> show ipv6 rip
		RIP process "process1", port 521, multicast-group FF02::9, pid 62
		     Administrative distance is 120. Maximum paths is 1
		     Updates every 5 seconds, expire after 15
		     Holddown lasts 10 seconds, garbage collect after 30
		     Split horizon is on; poison reverse is off
		     Default routes are generated
		     Periodic updates 223, trigger updates 1
		  Interfaces:
		    Gigabitethernet0/0/0
		  Redistribution:
		    Redistributing protocol bgp 65001 route-map bgp-to-rip
    '''}
	def test_empty(self):
	    self.device1 = Mock(**self.empty_output)
	    obj = ShowIpv6Rip(device=self.device1)
	    with self.assertRaises(SchemaEmptyParserError):
	        parsed_output = obj.parse()

	def test_golden_vrf_default(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse()
	    self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_vrf_vrf1(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output_2)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse(vrf="VRF1")
	    self.assertEqual(parsed_output, self.golden_parsed_output_2)

	def test_golden_vrf_vrf1_non_distribution(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output_3)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse(vrf="VRF1")
	    self.assertEqual(parsed_output, self.golden_parsed_output_3)

	def test_golden_ios(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output_ios)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse()
	    self.assertEqual(parsed_output, self.golden_parsed_output_ios)


if __name__ == '__main__':
    unittest.main()