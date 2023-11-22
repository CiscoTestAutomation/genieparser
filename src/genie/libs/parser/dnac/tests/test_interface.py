# Python
import unittest
from unittest.mock import Mock
from requests.models import Response
# ATS
from pyats.topology import Device
# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
    SchemaMissingKeyError

# Parser
from genie.libs.parser.dnac.interface import Interface


class TestInterfaceRest(unittest.TestCase):
    device = Device(name='aDevice')

    golden_parsed_output = {
        'hostname': {
            'csrl': {
                'interfaces': {
                    'GigabitEthernet0/0/0': {
                        'adminStatus': 'UP',
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
                        'macAddress': 'f4:4e:05:ff:fe:b0',
                        'mediaType': 'RJ45',
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
                    },
                    'GigabitEthernet0/0/1': {
                        'adminStatus': 'UP',
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
                        'macAddress': 'f4:4e:05:ff:fe:b1',
                        'mediaType': 'Auto',
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
                        'mtu': '1500',
                        'owningEntityId': '315320_315320',
                        'poweroverethernet': 0,
                    },
                }
            }
        }
    }


    golden_response_output1 = {'response': [
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
         'macAddress': 'f4:4e:05:ff:fe:b0',
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
         'macAddress': 'f4:4e:05:ff:fe:b1',
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
         'mtu': '1500',
         'owningEntityId': '315320_315320',
         'poweroverethernet': 0,
         'voiceVlan': None}]
    }

    golden_response_output2 = {
        'response': {
            'memorySize': 'NA',
            'family': 'Routers',
            'lastUpdateTime': 1575478820235,
            'collectionInterval': 'Global Default',
            'inventoryStatusDetail': '<status><general code="SUCCESS"/></status>',
            'upTime': '1 days, 6:34:24.15',
            'macAddress': '00:1e:7c:ff:72:60',
            'serialNumber': '9JBC0PK2YEK',
            'hostname': 'csrl',
            'deviceSupportLevel': 'Supported',
            'softwareType': 'IOS-XE',
            'softwareVersion': '16',
            'tagCount': '0',
            'tunnelUdpPort': None,
            'waasDeviceMode': None,
            'errorDescription': None,
            'interfaceCount': '0',
            'lastUpdated': '2014-06-12 14:00:25',
            'lineCardCount': '0',
            'lineCardId': '',
            'locationName': None,
            'managementIpAddress': '192.168.0.1',
            'roleSource': 'AUTO',
            'type': 'Cisco 4400 Series Integrated Services Routers',
            'errorCode': None,
            'location': None,
            'role': 'BORDER ROUTER',
            'apManagerInterfaceIp': '',
            'associatedWlcIp': '',
            'bootDateTime': '2014-06-12 14:00:25',
            'collectionStatus': 'Managed',
            'platformId': 'C4400ISR',
            'reachabilityFailureReason': '',
            'reachabilityStatus': 'Reachable',
            'series': 'Cisco 4400 Series Integrated Services Routers',
            'snmpContact': '',
            'snmpLocation': '',
            'instanceUuid': 'f34890c0-ff08-4562-af83-dfe516b2dcab',
            'instanceTenantId': '5bde9f95041e6f004dcc24e6',
            'id': 'f34890c0-ff08-4562-af83-dfe516b2dcab'
        },
        'version': '1.0'
    }

    def test_empty(self):
        empty_response = Mock(spec=Response)
        empty_response.json.return_value = {'response': []}
        empty_response.status_code = 200

        empty_output = {'get.return_value': empty_response}
        self.device1 = Mock(**empty_output)

        obj = Interface(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        golden_response = Mock(spec=Response)
        golden_response.json.side_effect = [self.golden_response_output1, self.golden_response_output2]
        golden_response.status_code = 200

        golden_output = {'get.return_value': golden_response}
        self.device = Mock(**golden_output)

        obj = Interface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
