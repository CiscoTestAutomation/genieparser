import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any
# import parser utils
from genie.libs.parser.utils.common import Common


# ==============================================
# Parser for 'show macsec summary'
# ==============================================

class ShowMacsecSummarySchema(MetaParser):
    """
    Schema for 'show macsec summary'

    """

    schema = {
        'interfaces': {
            Any(): {
                'transmit_sc': str,
                'receive_sc': str
            },
        }
    }


# ==========================================================
#  Parser for show macsec summary
# ==========================================================
class ShowMacsecSummary(ShowMacsecSummarySchema):
    """
    parser for
            * show macsec summary
    """

    cli_command = 'show macsec summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Te2/0/13                           1                   1
        p1 = re.compile(r'^(?P<interface>\S+\d+\/\d+\/\d+)\s+(?P<transmit_sc>\d+)\s+(?P<receive_sc>\d+)')

        ret_dict = {}
        if out != '':
            res_dict = ret_dict.setdefault('interfaces', {})
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name \
                    (intf=group['interface'].strip())
                intf_dict = res_dict.setdefault(interface,{})
                intf_dict['transmit_sc'] = group['transmit_sc']
                intf_dict['receive_sc'] = group['receive_sc']

        return ret_dict
