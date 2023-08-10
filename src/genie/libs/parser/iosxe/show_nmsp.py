""" show_nmsp.py

IOSXE parsers for the following show commands:

    * show nmsp status

"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


# ==============================================
#  Schema for show nmsp status
# ==============================================
class ShowNmspStatusSchema(MetaParser):
    """Schema for show nmsp status"""

    schema = {
        Any(): {
            'active': str,
            'tx_echo_resp': int,
            'rx_echo_req': int,
            'tx_data': int,
            'rx_data': int,
            'transport': str
        }
    }


# ==============================================
#  Parser for show nmsp status
# ==============================================
class ShowNmspStatus(ShowNmspStatusSchema):
    """Parser for show nmsp status"""

    cli_command = 'show nmsp status'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = dict()

        p_line = re.compile(
            # Parsing line:
            # 9.9.71.110|2001:bebe::1                          Active    439           439           22965       22          TLS
            r'(?P<ip_addr>(^(\d{1,3}\.){3}\d{1,3})|([a-fA-F\d]{1,4}:*:?){1,7}[a-fA-F\d]{1,4})\s+(?P<active>([A-Za-z]+))\s+(?P<tx_echo_resp>(\d+))\s+(?P<rx_echo_req>(\d+))\s+(?P<tx_data>(\d+))\s+(?P<rx_data>(\d+))\s+(?P<transport>(\w+)$)'
        )
        for line in output.splitlines():
            # 9.9.71.110|2001:bebe::1                          Active    439           439           22965       22          TLS
            m = re.match(p_line, line)
            if m:
                m_dict = m.groupdict()
                ip_addr = m_dict.get('ip_addr')
                dev_ip_dict = ret_dict.setdefault(ip_addr, dict())
                dev_ip_dict.update({
                    'active': m_dict.get('active'),
                    'tx_echo_resp': int(m_dict.get('tx_echo_resp')),
                    'rx_echo_req': int(m_dict.get('rx_echo_req')),
                    'tx_data': int(m_dict.get('tx_data')),
                    'rx_data': int(m_dict.get('rx_data')),
                    'transport': m_dict.get('transport')
                })
        return ret_dict
