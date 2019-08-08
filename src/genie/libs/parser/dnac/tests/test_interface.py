# Python
import unittest
from unittest.mock import Mock
from requests.models import Response
# ATS
from ats.topology import Device
# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# Parser
from genie.libs.parser.dnac.interface import Interface


class test_interface_rest(unittest.TestCase):
    device = Device(name='aDevice')

    golden_parsed_output = {
        'GigabitEthernet0/0/0': {'adminStatus': 'UP',
                                 'className': 'EthrntPrtclEndpntExtndd',
                                 'description': '',
                                 'deviceId': 'f34890c0-ff08-4562-af83-dfe516b2dcab',
                                 'duplex': 'FullDuplex',
                                 'id': '2c8c9a04-6cb2-4116-abc8-3ca2c45593af',
                                 'ifIndex': '1',
                                 'instanceTenantId': '5bde9f95041e6f004dcc24e6',
                                 'instanceUuid': '2c8c9a04-6cb2-4116-abc8-3ca2c45593af',
                                 'interfaceType': 'Physical',
                                 'ipv4Address': '10.1.4.2',
                                 'ipv4Mask': '255.255.255.248',
                                 'isisSupport': 'false',
                                 'lastUpdated': '2019-05-31 16:17:51.735',
                                 'macAddress': 'f4:4e:05:cf:2f:e0',
                                 'mediaType': 'RJ45',
                                 'ospfSupport': 'false',
                                 'pid': 'ISR4451-X/K9',
                                 'portMode': 'routed',
                                 'portName': 'GigabitEthernet0/0/0',
                                 'portType': 'Ethernet Port',
                                 'serialNo': 'FTX1842AHM1',
                                 'series': 'Cisco 4400 Series Integrated Services '
                                           'Routers',
                                 'speed': '1000000',
                                 'status': 'up',
                                 'vlanId': '0', },
        'GigabitEthernet0/0/1': {'adminStatus': 'UP',
                                 'className': 'EthrntPrtclEndpntExtndd',
                                 'description': '',
                                 'deviceId': 'f34890c0-ff08-4562-af83-dfe516b2dcab',
                                 'duplex': 'FullDuplex',
                                 'id': '25995afc-9e4a-4e95-90dd-2c114af5633e',
                                 'ifIndex': '2',
                                 'instanceTenantId': '5bde9f95041e6f004dcc24e6',
                                 'instanceUuid': '25995afc-9e4a-4e95-90dd-2c114af5633e',
                                 'interfaceType': 'Physical',
                                 'ipv4Address': '10.1.3.2',
                                 'ipv4Mask': '255.255.255.248',
                                 'isisSupport': 'false',
                                 'lastUpdated': '2019-05-31 16:17:51.735',
                                 'macAddress': 'f4:4e:05:cf:2f:e1',
                                 'mediaType': 'Auto',
                                 'ospfSupport': 'false',
                                 'pid': 'ISR4451-X/K9',
                                 'portMode': 'routed',
                                 'portName': 'GigabitEthernet0/0/1',
                                 'portType': 'Ethernet Port',
                                 'serialNo': 'FTX1842AHM1',
                                 'series': 'Cisco 4400 Series Integrated Services '
                                           'Routers',
                                 'speed': '1000000',
                                 'status': 'down',
                                 'vlanId': '0',
                                 },
    }

    golden_response_output = {'response': [
        {'adminStatus': 'UP',
         'className': 'EthrntPrtclEndpntExtndd',
         'description': '',
         'deviceId': 'f34890c0-ff08-4562-af83-dfe516b2dcab',
         'duplex': 'FullDuplex',
         'id': '2c8c9a04-6cb2-4116-abc8-3ca2c45593af',
         'ifIndex': '1',
         'instanceTenantId': '5bde9f95041e6f004dcc24e6',
         'instanceUuid': '2c8c9a04-6cb2-4116-abc8-3ca2c45593af',
         'interfaceType': 'Physical',
         'ipv4Address': '10.1.4.2',
         'ipv4Mask': '255.255.255.248',
         'isisSupport': 'false',
         'lastUpdated': '2019-05-31 16:17:51.735',
         'macAddress': 'f4:4e:05:cf:2f:e0',
         'mappedPhysicalInterfaceId': None,
         'mappedPhysicalInterfaceName': None,
         'mediaType': 'RJ45',
         'nativeVlanId': None,
         'ospfSupport': 'false',
         'pid': 'ISR4451-X/K9',
         'portMode': 'routed',
         'portName': 'GigabitEthernet0/0/0',
         'portType': 'Ethernet Port',
         'serialNo': 'FTX1842AHM1',
         'series': 'Cisco 4400 Series Integrated Services Routers',
         'speed': '1000000',
         'status': 'up',
         'vlanId': '0',
         'voiceVlan': None},
        {'adminStatus': 'UP',
         'className': 'EthrntPrtclEndpntExtndd',
         'description': '',
         'deviceId': 'f34890c0-ff08-4562-af83-dfe516b2dcab',
         'duplex': 'FullDuplex',
         'id': '25995afc-9e4a-4e95-90dd-2c114af5633e',
         'ifIndex': '2',
         'instanceTenantId': '5bde9f95041e6f004dcc24e6',
         'instanceUuid': '25995afc-9e4a-4e95-90dd-2c114af5633e',
         'interfaceType': 'Physical',
         'ipv4Address': '10.1.3.2',
         'ipv4Mask': '255.255.255.248',
         'isisSupport': 'false',
         'lastUpdated': '2019-05-31 16:17:51.735',
         'macAddress': 'f4:4e:05:cf:2f:e1',
         'mappedPhysicalInterfaceId': None,
         'mappedPhysicalInterfaceName': None,
         'mediaType': 'Auto',
         'nativeVlanId': None,
         'ospfSupport': 'false',
         'pid': 'ISR4451-X/K9',
         'portMode': 'routed',
         'portName': 'GigabitEthernet0/0/1',
         'portType': 'Ethernet Port',
         'serialNo': 'FTX1842AHM1',
         'series': 'Cisco 4400 Series Integrated Services Routers',
         'speed': '1000000',
         'status': 'down',
         'vlanId': '0',
         'voiceVlan': None}]
    }
    empty_response = Mock(spec=Response)
    empty_response.json.return_value = {'response': []}
    empty_response.status_code = 200
    empty_output = {'get.return_value': empty_response}
    golden_response = Mock(spec=Response)
    golden_response.json.return_value = golden_response_output
    golden_response.status_code = 200
    golden_output = {'get.return_value':golden_response}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = Interface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = Interface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
