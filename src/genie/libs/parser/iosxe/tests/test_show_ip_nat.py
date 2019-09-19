import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.show_ip_nat import ShowIpNatTranslations


####################################################
# Unit test for:
#   * 'show ip nat translations'
#   * 'show ip nat translations verbose'
####################################################

class TestShowIpNatTranslations(unittest.TestCase):

    dev_c3850 = Device(name='c3850')
    empty_output = {'execute.return_value': ''}

    golden_output = {'execute.return_value': '''\
        Device# show ip nat translations

		Pro  Inside global         Inside local          Outside local         Outside global
		udp  10.5.5.1:1025          192.0.2.1:4000        ---                   ---
		udp  10.5.5.1:1024          192.0.2.3:4000        ---                   ---
        udp  10.5.5.1:1026          192.0.2.2:4000        ---                   ---
    '''
    }

    golden_output_1 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global      Inside local       Outside local      Outside global
        --- 171.69.233.209     192.168.1.95       ---                ---
        --- 171.69.233.210     192.168.1.89       ---                --
    '''
    }

    golden_output_2 = {'execute.return_value': '''\
        Router#show ip nat translations
        Pro Inside global        Inside local       Outside local      Outside global
        udp 171.69.233.209:1220  192.168.1.95:1220  171.69.2.132:53    171.69.2.132:53
        tcp 171.69.233.209:11012 192.168.1.89:11012 171.69.1.220:23    171.69.1.220:23
        tcp 171.69.233.209:1067  192.168.1.95:1067  171.69.1.161:23    171.69.1.161:23
    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowIpNatTranslations(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()
    
    def test_golden_translations(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpPimDf(device=self.device)
        parsed_output = obj.parse()
        import pprint
        pprint.pprint(parsed_output)
        #self.assertEqual(parsed_output, self.golden_parsed_output)
