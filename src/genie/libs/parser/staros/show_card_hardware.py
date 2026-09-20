"""starOS implementation of show_card_hardware.py

"""
from operator import contains
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowCardHardwareSchema(MetaParser):
    """Schema for show card hardware"""

    schema = {
        'hardware_table': {
            Any(): {
                'Card Type': str,
                'Serial Number': str,
                'Card Programmables': str,
            },
        }    
    }



class ShowCardSchema(ShowCardHardwareSchema):
    """Parser for show card hardware"""

    cli_command = 'show card hardware'

    """
Card 1:
  Card Type               : Data Processing Card 2 (R04)
  Description             : DPC2
  Cisco Part Number       : 73-18817-05 A0
  UDI Serial Number       : FLM21500296
  UDI Product ID          : ASR55-DPC2-K9
  UDI Version ID          : V04
  UDI Top Assem Num       : 68-6433-05 A0
  Card Programmables      : up to date
  BCF2                    : on-card 0.18.0
  CAF2                    : on-card 0.0.15
  CPU 0 Type/Memory       : Socket 0: Xeon E5-2648L v3 B1, 1800 MHz
                          : Socket 1: Xeon E5-2648L v3 B1, 1800 MHz
                          : Chipset: DH8920CC A0, 64 GB
  CPU 0 DIMM-N0C0D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 0 DIMM-N0C1D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 0 DIMM-N1C0D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 0 DIMM-N1C1D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 0 BIOS              : on-card-a 0.4.8, on-card-b 0.4.8
  CPU 0 i82599            : eeprom-a 0.0.3
  CPU 0 i210              : eeprom-a 0.0.2
  CPU 0 CFE Loaded        : on-card 3.3.3
  CPU 0 CFE ROM           : on-card-a 3.3.3, on-card-b 3.3.3
  CPU 0 DH89XXCC          : on-card 0.3.4
  CPU 1 Type/Memory       : Socket 0: Xeon E5-2648L v3 B1, 1800 MHz
                          : Socket 1: Xeon E5-2648L v3 B1, 1800 MHz
                          : Chipset: DH8920CC A0, 64 GB
  CPU 1 DIMM-N0C0D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 1 DIMM-N0C1D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 1 DIMM-N1C0D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 1 DIMM-N1C1D0 P/N   : 18ADF2G72PDZ-2G3B
  CPU 1 BIOS              : on-card-a 0.4.8, on-card-b 0.4.8
  CPU 1 i82599            : eeprom-a 0.0.3
  CPU 1 i210              : eeprom-a 0.0.2
  CPU 1 CFE Loaded        : on-card 3.3.3
  CPU 1 CFE ROM           : on-card-a 3.3.3, on-card-b 3.3.3
  CPU 1 DH89XXCC          : on-card 0.3.4
  CPU 2 Type/Memory       : Socket 0: Xeon E5-2648L v3 B1, 1800 MHz
                          : Socket 1: Xeon E5-2648L v3 B1, 1800 MHz
                          : Chipset: DH8920CC A0, 64 GB
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        card_hardware_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(?P<card_id>^Card.\d+)')
        p1 = re.compile(r'(UDI.Serial.Number\s+:.(?P<serial_number>\w+))')
        p2 = re.compile(r'(Card.Programmables\s+:(?P<card_prog>.*$))')
        p3 = re.compile(r'(Description\s+:(?P<type>.*$))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'hardware_table' not in card_hardware_dict:
                    result_dict = card_hardware_dict.setdefault('hardware_table',{})
                card_id = m.groupdict()['card_id']
                result_dict[card_id] = {}
                
            m = p1.match(line)
            if m:
                if 'hardware_table' not in card_hardware_dict:
                    result_dict = card_hardware_dict.setdefault('hardware_table',{})
                serial_number = m.groupdict()['serial_number']
                result_dict[card_id]["Serial Number"] = serial_number

            m = p2.match(line)
            if m:
                if 'hardware_table' not in card_hardware_dict:
                    result_dict = card_hardware_dict.setdefault('hardware_table',{})
                card_prog = m.groupdict()['card_prog']
                result_dict[card_id]["Card Programmables"] = card_prog

            m = p3.match(line)
            if m:
                if 'hardware_table' not in card_hardware_dict:
                    result_dict = card_hardware_dict.setdefault('hardware_table',{})
                type = m.groupdict()['type']
                if  "CHASSIS" in type:
                    type ="MIO"
                result_dict[card_id]["Card Type"] = type
                continue

        return card_hardware_dict