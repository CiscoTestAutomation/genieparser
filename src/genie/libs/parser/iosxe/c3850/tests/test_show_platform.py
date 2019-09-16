#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.c3850.show_platform import ShowEnvironmentAll as ShowEnvironmentAllc3850


class test_show_environment_all_c3850(unittest.TestCase):
     dev1 = Device(name='empty')
     dev_c3850 = Device(name='c3850')
     empty_output = {'execute.return_value': '      '}

     golden_parsed_output_c3850 = {
        "switch": {
            "3": {
               "system_temperature_state": "ok",
               "hotspot_temperature": {
                    "yellow_threshold": "105",
                    "red_threshold": "125",
                    "state": "green",
                    "value": "43"
               },
               "power_supply": {
                    "2": {
                         "state": "not present",
                         "status": "not present"
                    },
                    "1": {
                         "pid": "PWR-C1-715WAC",
                         "serial_number": "DCB1844G1WW",
                         "watts": "715",
                         "system_power": "good",
                         "state": "ok",
                         "poe_power": "good",
                         "status": "ok"
                    }
               },
               "inlet_temperature": {
                    "yellow_threshold": "46",
                    "red_threshold": "56",
                    "state": "green",
                    "value": "33"
               },
               "fan": {
                    "3": {
                         "state": "ok"
                    },
                    "2": {
                         "state": "ok"
                    },
                    "1": {
                         "state": "ok"
                    }
               }
            },
            "2": {
               "system_temperature_state": "ok",
               "hotspot_temperature": {
                    "yellow_threshold": "105",
                    "red_threshold": "125",
                    "state": "green",
                    "value": "43"
               },
               "power_supply": {
                    "2": {
                         "state": "not present",
                         "status": "not present"
                    },
                    "1": {
                         "pid": "PWR-C1-715WAC",
                         "serial_number": "DCB1844G1X0",
                         "watts": "715",
                         "system_power": "good",
                         "state": "ok",
                         "poe_power": "good",
                         "status": "ok"
                    }
               },
               "inlet_temperature": {
                    "yellow_threshold": "46",
                    "red_threshold": "56",
                    "state": "green",
                    "value": "33"
               },
               "fan": {
                    "3": {
                         "state": "ok"
                    },
                    "2": {
                         "state": "ok"
                    },
                    "1": {
                         "state": "ok"
                    }
               }
            },
            "1": {
               "system_temperature_state": "ok",
               "hotspot_temperature": {
                    "yellow_threshold": "105",
                    "red_threshold": "125",
                    "state": "green",
                    "value": "45"
               },
               "power_supply": {
                    "2": {
                         "state": "not present",
                         "status": "not present"
                    },
                    "1": {
                         "pid": "PWR-C1-715WAC",
                         "serial_number": "DCB1844G1ZY",
                         "watts": "715",
                         "system_power": "good",
                         "state": "ok",
                         "poe_power": "good",
                         "status": "ok"
                    }
               },
               "inlet_temperature": {
                    "yellow_threshold": "46",
                    "red_threshold": "56",
                    "state": "green",
                    "value": "34"
               },
               "fan": {
                    "3": {
                         "state": "ok"
                    },
                    "2": {
                         "state": "ok"
                    },
                    "1": {
                         "state": "ok"
                    }
               }
            }
        }
     }

     golden_output_c3850 = {'execute.return_value': '''\
        Switch 1 FAN 1 is OK
        Switch 1 FAN 2 is OK
        Switch 1 FAN 3 is OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch 2 FAN 1 is OK
        Switch 2 FAN 2 is OK
        Switch 2 FAN 3 is OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch 3 FAN 1 is OK
        Switch 3 FAN 2 is OK
        Switch 3 FAN 3 is OK
        FAN PS-1 is OK
        FAN PS-2 is NOT PRESENT
        Switch 1: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 34 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Hotspot Temperature Value: 45 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        Switch 2: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 33 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Hotspot Temperature Value: 43 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        Switch 3: SYSTEM TEMPERATURE is OK
        Inlet Temperature Value: 33 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 46 Degree Celsius
        Red Threshold    : 56 Degree Celsius

        Hotspot Temperature Value: 43 Degree Celsius
        Temperature State: GREEN
        Yellow Threshold : 105 Degree Celsius
        Red Threshold    : 125 Degree Celsius
        SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
        --  ------------------  ----------  ---------------  -------  -------  -----
        1A  PWR-C1-715WAC       DCB1844G1ZY  OK              Good     Good     715
        1B  Not Present
        2A  PWR-C1-715WAC       DCB1844G1X0  OK              Good     Good     715
        2B  Not Present
        3A  PWR-C1-715WAC       DCB1844G1WW  OK              Good     Good     715
        3B  Not Present
     '''}

     golden_parsed_output1 = {
          "switch": {
               "1": {
                    "fan": {
                         "1": {
                              "state": "ok",
                              "direction": "front to back"
                         },
                         "2": {
                              "state": "ok",
                              "direction": "front to back"
                         },
                         "3": {
                              "state": "ok",
                              "direction": "front to back"
                         },
                         "4": {
                              "state": "ok",
                              "direction": "front to back"
                         },
                         "5": {
                              "state": "ok",
                              "direction": "front to back"
                         }
                    },
                    "power_supply": {
                         "1": {
                              "state": "ok",
                              "pid": "PWR-C3-750WAC-R",
                              "serial_number": "QCS22123Y8E",
                              "watts": "750",
                              "status": "ok",
                              "system_power": "good",
                              "poe_power": "good"
                         },
                         "2": {
                              "state": "not present",
                              "status": "not present"
                         }
                    },
                    "system_temperature_state": "ok",
                    "inlet_temperature": {
                         "value": "31",
                         "state": "green",
                         "yellow_threshold": "46",
                         "red_threshold": "56"
                    },
                    "asic_temperature": {
                         "value": "36",
                         "state": "green",
                         "yellow_threshold": "105",
                         "red_threshold": "125"
                    }
               }
          }
     }
     golden_output1 = {'execute.return_value': '''\
          show environment all
          Switch 1 FAN 1 is OK
          Switch 1 FAN 2 is OK
          Switch 1 FAN 3 is OK
          Switch 1 FAN 4 is OK
          Switch 1 FAN 5 is OK
          FAN PS-1 is OK
          FAN PS-2 is NOT PRESENT
          Switch 1: SYSTEM TEMPERATURE is OK
          Inlet Temperature Value: 31 Degree Celsius
          Temperature State: GREEN
          Yellow Threshold : 46 Degree Celsius
          Red Threshold    : 56 Degree Celsius

          ASIC Temperature Value: 36 Degree Celsius
          Temperature State: GREEN
          Yellow Threshold : 105 Degree Celsius
          Red Threshold    : 125 Degree Celsius
          Switch 1 FAN 1 direction is Front to Back
          Switch 1 FAN 2 direction is Front to Back
          Switch 1 FAN 3 direction is Front to Back
          Switch 1 FAN 4 direction is Front to Back
          Switch 1 FAN 5 direction is Front to Back
          SW  PID                 Serial#     Status           Sys Pwr  PoE Pwr  Watts
          --  ------------------  ----------  ---------------  -------  -------  -----
          1A  PWR-C3-750WAC-R     QCS22123Y8E  OK              Good     Good     750
          1B  Not Present
     '''}

     def test_empty(self):
          self.dev1 = Mock(**self.empty_output)
          platform_obj = ShowEnvironmentAllc3850(device=self.dev1)
          with self.assertRaises(SchemaEmptyParserError):
               parsed_output = platform_obj.parse()

     def test_golden(self):
          self.maxDiff = None
          self.dev_c3850 = Mock(**self.golden_output_c3850)
          platform_obj = ShowEnvironmentAllc3850(device=self.dev_c3850)
          parsed_output = platform_obj.parse()
          self.assertEqual(parsed_output, self.golden_parsed_output_c3850)

     def test_golden1(self):
          self.maxDiff = None
          self.dev_c3850 = Mock(**self.golden_output1)
          platform_obj = ShowEnvironmentAllc3850(device=self.dev_c3850)
          parsed_output = platform_obj.parse()
          self.assertEqual(parsed_output,self.golden_parsed_output1)

if __name__ == '__main__':
     unittest.main()
