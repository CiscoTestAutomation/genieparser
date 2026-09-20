"""starOS implementation of show_crash_list.py

"""
import re
from tokenize import Number
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowCrashListSchema(MetaParser):
    """Schema for show crash list"""

    schema = {
        'crash_table': {
            Any(): {
            'Date': str,
            'Instance': str,
            'CARD/CPU/PID': str,
            'SW Version': str,
            'MIO': str,
            },
        }    
    }
class ShowCrashList(ShowCrashListSchema):
    """Parser for show crash list"""

    cli_command = 'show crash list'

    """
=== ==================== ======== ========== =============== =======================
#           Time         Process  Card/CPU/        SW          HW_SER_NUM
                                     PID         VERSION       MIO / Crash Card
=== ==================== ======== ========== =============== =======================

1   2020-Oct-15+13:57:40 sessmgr  01/0/48672 21.13.1         FLM2236045H/FLM21500296
2   2020-Oct-15+14:06:56 sessmgr  01/0/48672 21.13.1         FLM2236045H/FLM21500296
3   2020-Oct-15+14:11:29 sessmgr  01/0/48672 21.13.1         FLM2236045H/FLM21500296

[local]COR-VPC-1# show crash list
Monday February 05 02:44:49 ART 2024
=== ==================== ======== ========== =============== =======================
#           Time         Process  Card/CPU/        SW          HW_SER_NUM
                                     PID         VERSION       CF / Crash Card
=== ==================== ======== ========== =============== =======================

1   2020-Aug-03+04:07:26 sessmgr  08/0/11914 21.15.28        NA                     
2   2020-Aug-03+18:07:10 sessmgr  08/0/12007 21.15.28        NA                     
3   2020-Aug-03+18:07:23 sessmgr  07/0/12017 21.15.28        NA                     
4   2020-Aug-12+13:21:04 sessmgr  10/0/17154 21.15.28        NA                     
5   2020-Aug-12+13:21:37 sessmgr  10/0/20541 21.15.28        NA                     
6   2020-Sep-21+17:27:26 sessmgr  06/0/13426 21.15.28        NA                     
7   2020-Sep-21+17:55:18 egtpinmg 04/0/12642 21.15.28        NA                     
8   2020-Sep-22+00:47:29 sessmgr  10/0/13441 21.15.28        NA                     
9   2020-Sep-22+00:48:31 sessmgr  08/0/11726 21.15.28        NA                     
10  2020-Sep-22+11:08:54 egtpinmg 04/0/12642 21.15.28        NA                     
11  2020-Sep-22+11:10:55 sessmgr  09/0/11999 21.15.28        NA                     
12  2020-Nov-14+21:07:39 sessmgr  05/0/11848 21.15.28        NA                     
13  2020-Nov-20+01:02:35 sessmgr  05/0/24099 21.15.28        NA                     
14  2020-Dec-06+23:32:09 sessmgr  03/0/11985 21.15.28        NA                     
15  2022-Oct-17+00:02:11 sessmgr  03/0/07509 21.19.11        NA                     
16  2022-Oct-17+17:37:00 sessmgr  07/0/11509 21.19.11        NA                     
17  2022-Oct-23+23:41:41 sessmgr  10/0/00684 21.19.11        NA                     
18  2022-Dec-05+23:53:33 sessmgr  09/0/06495 21.25.10        NA                     
19  2022-Dec-07+06:10:38 sessmgr  06/0/01122 21.25.10        NA                     
20  2022-Dec-15+00:34:16 cli      01/0/18359 21.25.10        NA                     
21  2024-Feb-01+12:44:40 vpnmgr   02/0/08392 21.25.10        NA                     

Total Crashes : 240
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        crash_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(?P<Number>\d+)\s+(?P<Date>\d{4}-[A-Za-z]{3}-\d{2}\+\d{2}:\d{2}:\d{2})\s+(?P<Instance>[a-z]+)\s+(?P<Card_CPU_PID>\d{2}\/\d{1}\/\d{5})\s+(?P<SW_Version>[\d\.]+)\s+(?P<card>[A-Z\d\/]+)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'crash_table' not in crash_dict:
                    result_dict = crash_dict.setdefault('crash_table',{})
                Number = m.groupdict()['Number']
                Date = m.groupdict()['Date']
                Instance = m.groupdict()['Instance']
                Card_CPU_PID = m.groupdict()['Card_CPU_PID']
                SW_Version = m.groupdict()['SW_Version']
                card = m.groupdict()['card']

                result_dict[Number] = {}
                result_dict[Number]['Date'] = Date
                result_dict[Number]['Instance'] = Instance
                result_dict[Number]['CARD/CPU/PID'] = Card_CPU_PID
                result_dict[Number]['SW Version'] = SW_Version
                result_dict[Number]['MIO'] = card      
                continue

        return crash_dict
