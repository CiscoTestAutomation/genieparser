"""show_arp.py

NXOS parsers for the following show commands:
    * 'show ip arp'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use
from genie import parsergen

# =====================================
# Schema for 'show ip arp'
# =====================================
class ShowIpArpSchema(MetaParser):
    """Schema for show ip arp"""

    schema = {
        Any():
          {'Age': str,
           'MAC Address': str,
           'Interface': str,
           'Address': str,
           Optional('Flags'): str}}

# =====================================
# Parser for 'show ip arp'
# =====================================
class ShowIpArp(ShowIpArpSchema):
    """Parser for:
        show bgp process vrf all
        parser class - implements detail parsing mechanisms for cli,xml and yang output.
    """

    def cli(self):
        output = self.device.execute('show ip arp')
         
        if not 'Flags' not in output:
            header = ['Address', 'Age', 'MAC Address', 'Interface']
        else:
            header = ['Address', 'Age', 'MAC Address', 'Interface', 'Flags']
        result = parsergen.oper_fill_tabular(
                      device_output=output,
                      device_os= 'nxos',
                      header_fields= header,
                      index= [0])
        return result.entries
