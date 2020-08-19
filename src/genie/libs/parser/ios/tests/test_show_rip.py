# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

from genie.libs.parser.ios.show_rip import ShowIpRipDatabase, \
										   ShowIpv6Rip, \
										   ShowIpv6RipDatabase

# ============================================
# unit test for 'show ipv6 rip'
# unit test for 'show ipv6 rip vrf {vrf}'
# ============================================
class test_show_ipv6_rip(unittest.TestCase):

	device = Device(name='aDevice')
	golden_parsed_output_ios_none = {
	  "vrf": {
		"one": {
		  "address_family": {
		    "ipv6": {
		      "distance": 25,
		      "interfaces": {
		        "Ethernet2": {}
		      },
		      "maximum_paths": 4,
		      "multicast_group": "FF02::9",
		      "originate_default_route": {
		        "enabled": False
		      },
		      "pid": 55,
		      "poison_reverse": False,
		      "port": 521,
		      "split_horizon": True,
		      "statistics": {
		        "periodic_updates": 8883,
		        "trigger_updates": 2
		      },
		      "timers": {
		        "expire_time": 180,
		        "flush_interval": 120,
		        "holddown_interval": 0,
		        "update_interval": 30
		      }
		    }
		  }
		},
		"two": {
		      "address_family": {
		        "ipv6": {
		          "distance": 120,
		          "maximum_paths": 4,
		          "multicast_group": "FF02::9",
		          "originate_default_route": {
		            "enabled": False
		          },
		          "pid": 61,
		          "poison_reverse": False,
		          "port": 521,
		          "split_horizon": True,
		          "statistics": {
		            "periodic_updates": 8883,
		            "trigger_updates": 0
		          },
		          "timers": {
		            "expire_time": 180,
		            "flush_interval": 120,
		            "holddown_interval": 0,
		            "update_interval": 30
		          }
		        }
		      }
		    }
		}
	}
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
			          65001: {
			          	"route_policy": "bgp-to-rip"
			          }
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


	golden_output_ios_none = {'execute.return_value': '''\
	RIP process "one", port 521, multicast-group FF02::9, pid 55
		Administrative distance is 25. Maximum paths is 4
		Updates every 30 seconds, expire after 180
		Holddown lasts 0 seconds, garbage collect after 120
		Split horizon is on; poison reverse is off
		Default routes are not generated
		Periodic updates 8883, trigger updates 2
	 Interfaces:
		Ethernet2
	 Redistribution:
	RIP process "two", port 521, multicast-group FF02::9, pid 61
		Administrative distance is 120. Maximum paths is 4
		Updates every 30 seconds, expire after 180
		Holddown lasts 0 seconds, garbage collect after 120
		Split horizon is on; poison reverse is off
		Default routes are not generated
		Periodic updates 8883, trigger updates 0
	 Interfaces:
		None
	 Redistribution:
    '''}

	def test_golden_ios(self):
	    self.maxDiff = None
	    self.device = Mock(**self.golden_output_ios)
	    obj = ShowIpv6Rip(device=self.device)
	    parsed_output = obj.parse()
	    self.assertEqual(parsed_output, self.golden_parsed_output_ios)

	def test_golden_ios_none(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_ios_none)
		obj = ShowIpv6Rip(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_ios_none)

if __name__ == '__main__':
    unittest.main()