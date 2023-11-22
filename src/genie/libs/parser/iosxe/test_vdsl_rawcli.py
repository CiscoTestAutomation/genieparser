''' test_vdsl_rawcli.py

IOSXE parsers for the following test commands:

    * 'test vdsl rawcli "basic show summary <number>"'
'''

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use
from genie.libs.parser.utils.common import Common

# ==================================================================
# Parser Schema for 'test vdsl rawcli "basic show summary <number>"'
# ==================================================================


class TestVdslRawcliSchema(MetaParser):
    """Schema for test vdsl rawcli 'basic show summary <number>' """

    schema = {
        "link_time": int,
        "rate_us": int,
        "rate_ds": int,
        "mode": str,
        "status": str,
        Optional('annex'): str,
        Optional('profile'): str,
        "txpkts": int,
        "rxpkts": int,            
    }

# ===========================================================
# Parser for 'test vdsl rawcli "basic show summary <number>"'
# ===========================================================

class TestVdslRawCli(TestVdslRawcliSchema):
    """ parser for test vdsl rawcli 'basic show summary <number>' """

    cli_command = 'test vdsl rawcli "basic show summary {number}"'
            
    def cli(self, number, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(number=number))
        else:
            out = output
          
        parsed_dict = {}

        #Link time Rate US/DS     Mode      Status    Annex  Profile TxPkts/RxPkts
        #1032746   60014/149783 VDSL2     Showtime  AnnexB 17a     1688269/1654598        
        p1 = re.compile(r'^(?P<link_time>(\d+))\s+(?P<rate_us>(\d+))\/(?P<rate_ds>(\d+))\s+(?P<mode>([A-Z0-9+-]+))\s+(?P<status>(\w+))\s+(?P<annex>([0-9a-zA-Z]+))\s+(?P<profile>([A-Za-z0-9]+))\s+(?P<txpkts>(\d+))\/(?P<rxpkts>(\d+))$')
              
        for line in out.splitlines():
            line = line.strip()
            
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict['link_time'] = int(group['link_time'])
                parsed_dict['rate_us'] = int(group['rate_us'])
                parsed_dict['rate_ds'] = int(group['rate_ds'])
                parsed_dict['mode'] = group['mode']
                parsed_dict['status'] = group['status']
                if group['annex']:
                    parsed_dict['annex'] = group['annex']
                if group['profile']:
                    parsed_dict['profile'] = group['profile']
                parsed_dict['txpkts'] = int(group['txpkts'])
                parsed_dict['rxpkts'] = int(group['rxpkts'])                
                continue
               
        return parsed_dict          