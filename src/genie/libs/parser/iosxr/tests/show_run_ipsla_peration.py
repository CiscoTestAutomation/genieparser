import unittest
from unittest.mock import Mock

from pyats.topology import Device

from genie.libs.parser.iosxr.show_run_ipsla_operation import ShowRunIpslaOperation


class test_show_run_ipsla_peration(unittest.TestCase):
    ''' Unit test for "show run ipsla peration" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_brief = {
      "ipsla": {
        "operations": {
          "operation_ids": [
            {
              "oper_id": 100,
              "oper_types": {
                "type": {
                  "name": "udp jitter",
                  "vrf": "VRF-1",
                  "src_addr": "1.1.1.1",
                  "dest_addr": "2.2.2.2",
                  "packet": {
                    "count": 1000,
                    "interval": 20
                  },
                  "time_out": 3000,
                  "data_size_req": 500,
                  "dest_port": 15000,
                  "frequency": 60,
                  "verify-data": True
                }
              }
            }
          ]
        }
      }
    }

    golden_output_brief = {'execute.return_value': '''
    ipsla
     operation 100
      type udp jitter
       vrf VRF-1
       source address 1.1.1.1
       destination address 2.2.2.2
       packet count 1000
       packet interval 20
       timeout 3000
       datasize request 500
       destination port 15000
       frequency 60
       verify-data
      !
     !
    !
    '''}

    def test_show_run_ipsla_peration(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowRunIpslaOperation(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)


if __name__ == '__main__':
    unittest.main()