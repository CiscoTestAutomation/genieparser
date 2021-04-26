# Import the Python mock functionality
import unittest
from unittest.mock import Mock

# pyATS
# from pyats.topology import Device
# from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxe show_lisp
from genie.libs.parser.iosxr.show_shmwin import ShowShmwinSummary


# ===================================
# Unit test for 'show shmwin summary'
# ===================================
class test_show_shmwin_summary(unittest.TestCase):

    '''Unit test for "show lisp session"'''

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'summary': {
            'total_shmwin_usage': 984,
            '1': {'virtual_mem_range_end': '0xb0000000',
                  'virtual_mem_range_start': '0x50000000',
                  'virtual_mem_size': 1536
                  },
            '2': {
                'virtual_mem_range_end': '0xd0000000',
                'virtual_mem_range_start': '0xb8000000',
                'virtual_mem_size': 384,
            },
        },
        'windows': {
            0: {'window_name': 'subdb_sco_tbl',
                'group': '1',
                'id': 70,
                'num_users': 1,
                'num_writers': 1,
                'owner': '159',
                'peak': 0,
                'peak_date': '',
                'peak_time': '',
                'usage': 3},
            1: {'window_name': 'subsession_db',
                'group': '1',
                'id': 81,
                'num_users': 2,
                'num_writers': 2,
                'owner': '0',
                'peak': 9859,
                'peak_date': '03/21/2021',
                'peak_time': '21:13:51',
                'usage': 9859},
            2: {'window_name': 'subdb_co_tbl',
                'group': '2',
                'id': 71,
                'num_users': 11,
                'num_writers': 1,
                'owner': '0',
                'peak': 4115,
                'peak_date': '03/18/2021',
                'peak_time': '02:07:40',
                'usage': 4115},
            3: {'window_name': 'ifo_ea_shm',
                'group': 'P',
                'id': 130,
                'num_users': 1,
                'num_writers': 1,
                'owner': '0',
                'peak': 2795,
                'peak_date': '03/18/2021',
                'peak_time': '02:09:01',
                'usage': 1234},
        }
    }

    golden_output1 = {'execute.return_value': '''
RP/0/RSP0/CPU0:adr-ar90#show shmwin summary location 0/2/cpu0



Mon Mar 22 12:33:52.414 EET

----------------------------------------

Shared memory window summary information

----------------------------------------

Data for Window "subdb_sco_tbl":

-----------------------------

Virtual Memory size  : 1536 MBytes

Virtual Memory Range : 0x50000000 - 0xb0000000

Virtual Memory Group 2 size  : 384 MBytes

Virtual Memory Group 2 Range : 0xb8000000 - 0xd0000000



Window Name      ID  GRP #Usrs #Wrtrs Ownr Usage(KB) Peak(KB) Peak Timestamp

---------------- --- --- ----- ------ ---- --------- -------- -------------------

subdb_sco_tbl    70  1   1     1      159  3         0        --/--/---- --:--:--

Data for Window "subsession_db":

-----------------------------

subsession_db    81  1   2     2      0    9859      9859     03/21/2021 21:13:51

Data for Window "subdb_co_tbl":

-----------------------------

subdb_co_tbl     71  2   11    1      0    4115      4115     03/18/2021 02:07:40

Data for Window "ifo_ea_shm":

-----------------------------

ifo_ea_shm       130 P   1     1      0    1234      2795     03/18/2021 02:09:01

---------------------------------------------

Total SHMWIN memory usage : 984 MBytes

        '''}

    golden_parsed_output2 = {
        'summary': {
            'total_shmwin_usage': 984,
            '1': {'virtual_mem_range_end': '0xb0000000',
                  'virtual_mem_range_start': '0x50000000',
                  'virtual_mem_size': 1536
                  },
        },
        'windows': {
            0: {'window_name': 'subdb_sco_tbl',
                'group': '1',
                'id': 70,
                'num_users': 1,
                'num_writers': 1,
                'owner': '159',
                'peak': 0,
                'peak_date': '',
                'peak_time': '',
                'usage': 3},
            1: {'window_name': 'subsession_db',
                'group': '1',
                'id': 81,
                'num_users': 2,
                'num_writers': 2,
                'owner': '0',
                'peak': 9859,
                'peak_date': '03/21/2021',
                'peak_time': '21:13:51',
                'usage': 9859},
            2: {'window_name': 'ifo_ea_shm',
                'group': 'P',
                'id': 130,
                'num_users': 1,
                'num_writers': 1,
                'owner': '0',
                'peak': 2795,
                'peak_date': '03/18/2021',
                'peak_time': '02:09:01',
                'usage': 1234},
        }
    }

    golden_output2 = {'execute.return_value': '''
RP/0/RSP0/CPU0:adr-ar90#show shmwin summary



Mon Mar 22 12:33:52.414 EET

----------------------------------------

Shared memory window summary information

----------------------------------------

Data for Window "subdb_sco_tbl":

-----------------------------

Virtual Memory size  : 1536 MBytes

Virtual Memory Range : 0x50000000 - 0xb0000000


Window Name      ID  GRP #Usrs #Wrtrs Ownr Usage(KB) Peak(KB) Peak Timestamp

---------------- --- --- ----- ------ ---- --------- -------- -------------------

subdb_sco_tbl    70  1   1     1      159  3         0        --/--/---- --:--:--

Data for Window "subsession_db":

-----------------------------

subsession_db    81  1   2     2      0    9859      9859     03/21/2021 21:13:51

Data for Window "ifo_ea_shm":

-----------------------------

ifo_ea_shm       130 P   1     1      0    1234      2795     03/18/2021 02:09:01

---------------------------------------------

Total SHMWIN memory usage : 984 MBytes

        '''}

    def test_show_shmwin_summary_full_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowShmwinSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_shmwin_summary_full_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowShmwinSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_shmwin_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowShmwinSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()


if __name__ == '__main__':
    unittest.main()
