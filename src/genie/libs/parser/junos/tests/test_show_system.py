# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.junos.show_system import ShowSystemBuffer, ShowSystemCoreDumps

#=========================================================
# Unit test for show system buffer
#=========================================================
class test_show_system_buffer(unittest.TestCase):

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        'memory-statistics': {
            'cached-bytes': '1971',
            'cached-jumbo-clusters-16k': '0',
            'cached-jumbo-clusters-4k': '2',
            'cached-jumbo-clusters-9k': '0',
            'cached-mbuf-clusters': '714',
            'cached-mbufs': '2142',
            'cluster-failures': '0',
            'current-bytes-in-use': '1179',
            'current-jumbo-clusters-16k': '0',
            'current-jumbo-clusters-4k': '0',
            'current-jumbo-clusters-9k': '0',
            'current-mbuf-clusters': '516',
            'current-mbufs': '588',
            'io-initiated': '0',
            'jumbo-cluster-failures-16k': '0',
            'jumbo-cluster-failures-4k': '0',
            'jumbo-cluster-failures-9k': '0',
            'max-jumbo-clusters-16k': '10396',
            'max-jumbo-clusters-4k': '62377',
            'max-jumbo-clusters-9k': '18482',
            'max-mbuf-clusters': '124756',
            'mbuf-failures': '0',
            'packet-count': '513',
            'packet-failures': '0',
            'packet-free': '499',
            'sfbuf-requests-delayed': '0',
            'sfbuf-requests-denied': '0',
            'total-bytes': '3150',
            'total-jumbo-clusters-16k': '0',
            'total-jumbo-clusters-4k': '2',
            'total-jumbo-clusters-9k': '0',
            'total-mbuf-clusters': '1230',
            'total-mbufs': '2730'
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show system buffers
                588/2142/2730 mbufs in use (current/cache/total)
                516/714/1230/124756 mbuf clusters in use (current/cache/total/max)
                513/499 mbuf+clusters out of packet secondary zone in use (current/cache)
                0/2/2/62377 4k (page size) jumbo clusters in use (current/cache/total/max)
                0/0/0/18482 9k (page size) jumbo clusters in use (current/cache/total/max)
                0/0/0/10396 16k (page size) jumbo clusters in use (current/cache/total/max)
                1179K/1971K/3150K bytes allocated to network (current/cache/total)
                0/0/0 requests for mbufs denied (mbufs/clusters/mbuf+clusters)
                0/0/0 requests for jumbo clusters denied (4k/9k/16k)
                0 requests for sfbufs denied
                0 requests for sfbufs delayed
                0 requests for I/O initiated by sendfile

    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemBuffer(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemBuffer(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

#=========================================================
# Unit test for show system core-dumps
#=========================================================
class test_show_system_core_dumps(unittest.TestCase):

    device = Device(name='aDevice')

    maxDiff = None

    empty_output = {'execute.return_value': ''}

    golden_parsed_output_1 = {
        "directory-list": {
            "directory": {
                "file-information": [
                    {
                        "file-date": {
                            "@junos:format": "Aug 8   2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.riot.mpc0.1565307741.1716.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1252383"
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 8   2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565307747.1791.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "4576464"
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565841060.1528.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139316"
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565841991.4312.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139249"
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565842608.6212.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139299"
                    },
                    {
                        "file-date": {
                            "@junos:format": "Aug 15  2019"
                        },
                        "file-group": "wheel",
                        "file-links": "1",
                        "file-name": "/var/crash/core.vmxt.mpc0.1565892564.3392.gz",
                        "file-owner": "root",
                        "file-permissions": {
                            "@junos:format": "-rw-r--r--"
                        },
                        "file-size": "1139321"
                    }
                ],
                "output": [
                    "/var/tmp/*core*: No such file or directory",
                    "/var/tmp/pics/*core*: No such file or directory",
                    "/var/crash/kernel.*: No such file or directory",
                    "/var/jails/rest-api/tmp/*core*: No such file or directory",
                    "/tftpboot/corefiles/*core*: No such file or directory"
                ],
                "total-files": "6"
            }
        }
    }


    golden_output_1 = {'execute.return_value': '''
                show system core-dumps
                -rw-r--r--  1 root  wheel    1252383 Aug 8   2019 /var/crash/core.riot.mpc0.1565307741.1716.gz
                -rw-r--r--  1 root  wheel    4576464 Aug 8   2019 /var/crash/core.vmxt.mpc0.1565307747.1791.gz
                -rw-r--r--  1 root  wheel    1139316 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565841060.1528.gz
                -rw-r--r--  1 root  wheel    1139249 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565841991.4312.gz
                -rw-r--r--  1 root  wheel    1139299 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565842608.6212.gz
                -rw-r--r--  1 root  wheel    1139321 Aug 15  2019 /var/crash/core.vmxt.mpc0.1565892564.3392.gz
                /var/tmp/*core*: No such file or directory
                /var/tmp/pics/*core*: No such file or directory
                /var/crash/kernel.*: No such file or directory
                /var/jails/rest-api/tmp/*core*: No such file or directory
                /tftpboot/corefiles/*core*: No such file or directory
                total files: 6

    '''
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemCoreDumps(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSystemCoreDumps(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()