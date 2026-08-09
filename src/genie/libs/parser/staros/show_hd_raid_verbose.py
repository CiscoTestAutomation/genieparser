"""starOS implementation of show_hd_raid_verbose.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowHDRaidSchema(MetaParser):
    """Schema for show hd raid verbose"""

    schema = {
        'raid_table': {
            'STATE': str,
            'DEGRADED': str,
            Any(): {
                'CARD_STATE': str,
            }
        },
    }


class Showhdraid(ShowHDRaidSchema):
    """Parser for show hd raid verbose"""

    cli_command = 'show hd raid verbose'

    """
HD RAID:
  State                     : Available (clean)
  Degraded                  : No
  UUID                      : 63f3b330:e16ca170:49b8ac9b:4c75d758
  Size                      : 1.2TB (1200000073728 bytes)
  Action                    : Idle
  Card 14
    State                   : In-sync card
    Created                 : Thu Jan 17 14:15:53 2019
    Updated                 : Thu Jul 21 11:52:52 2022
    Events                  : 198076
    Description             : FSC14 FLM2223022H
    Size                    : 400GB (400088457216 bytes)
    Disk hd14a
      State                 : In-sync component
      Model                 : MICRON S650DC-400 M018
      Serial Number         : ZB015QCZ0000822150Z3
      Size                  : 400GB (400088457216 bytes)
  Card 15
    State                   : In-sync card
    Created                 : Thu Jan 17 14:15:53 2019
    Updated                 : Thu Jul 21 11:52:52 2022
    Events                  : 198076
    Description             : FSC15 FLM22230226
    Size                    : 400GB (400088457216 bytes)
    Disk hd15a
      State                 : In-sync component
      Model                 : MICRON S650DC-400 M018
      Serial Number         : ZB015QG90000822150Z3
      Size                  : 400GB (400088457216 bytes)
  Card 16
    State                   : In-sync card
    Created                 : Thu Jan 17 14:15:53 2019
    Updated                 : Thu Jul 21 11:52:52 2022
    Events                  : 198076
    Description             : FSC16 FLM2217064P
    Size                    : 400GB (400088457216 bytes)
    Disk hd16a
      State                 : In-sync component
      Model                 : MICRON S650DC-400 M018
      Serial Number         : ZB0160MB0000822150Z3
      Size                  : 400GB (400088457216 bytes)
  Card 17
    State                   : In-sync card
    Created                 : Thu Jan 17 14:15:53 2019
    Updated                 : Thu Jul 21 11:52:52 2022
    Events                  : 198076
    Description             : FSC17 FLM2223022D
    Size                    : 400GB (400088457216 bytes)
    Disk hd17a
      State                 : In-sync component
      Model                 : MICRON S650DC-400 M018
      Serial Number         : ZB015Q5D0000822150Z3
      Size                  : 400GB (400088457216 bytes)
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        raid_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'^State\s+.\s(?P<state>Available.+$)')
        p1 = re.compile(r'Degraded\s+.\s(?P<degrad>.+$)')
        p2 = re.compile(r'\w+\s(?P<card>\d+$)')
        p3 = re.compile(r'State\s+:\s(?P<card_state>.+card$)')
        for line in out.splitlines():
            line = line.strip()
            m = p0.match(line)
            if m:
                if 'raid_table' not in raid_dict:
                    result_dict = raid_dict.setdefault('raid_table',{})
                state = m.groupdict()['state']
                result_dict['STATE'] = state
                continue
                
            m = p1.match(line)
            if m:
                if 'raid_table' not in raid_dict:
                    result_dict = raid_dict.setdefault('raid_table',{})
                degrad = m.groupdict()['degrad']
                result_dict['DEGRADED'] = degrad
                continue

            m = p2.match(line)
            if m:
                if 'raid_table' not in raid_dict:
                    result_dict = raid_dict.setdefault('raid_table',{})
                card = m.groupdict()['card']
                result_dict[card] = {}
                continue

            m = p3.match(line)
            if m:
                if 'raid_table' not in raid_dict:
                    result_dict = raid_dict.setdefault('raid_table',{})
                card_state = m.groupdict()['card_state']
                result_dict[card]['CARD_STATE'] = card_state

        return raid_dict