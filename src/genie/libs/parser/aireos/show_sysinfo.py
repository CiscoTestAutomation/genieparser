""" show_sysinfo.py

AireOS parser for the following command:
    * 'show sysinfo'

"""

# Python
import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

log = logging.getLogger(__name__)

# ======================
# Schema for:
#  * 'show sysinfo'
# ======================

class ShowSysInfoSchema(MetaParser):
    """ Schema for show sysinfo """

    schema = {
        'product_version': str,
        'system_name': str,
        'system_up_time': str,
        'ip_address':str,
        'active_clients': str,
    }

class ShowSysInfo(ShowSysInfoSchema):
    """ Parser for show sysinfo """

    cli_command = 'show sysinfo'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        parsed_dict = {}


        #Product Version.................................. 8.10.162.0
        #System Name...................................... PLAB-CW-WLC-01
        #IP Address....................................... 172.23.89.35
        #System Up Time................................... 51 days 16 hrs 12 mins 2 secs
        #Number of Active Clients......................... 1

        p_product_version = re.compile(r"^Product\s+Version\.+ +(?P<product_version>\S+)")
        p_system_name= re.compile(r"^System\s+Name\.+ +(?P<system_name>\S+)$")
        p_ip_address = re.compile(r"^IP\s+Address\.+ (?P<ip_address>\S+)$")
        p_system_up_time = re.compile(r"^System\s+Up\s+Time\.+ (?P<system_up_time>.+)$")
        p_number_of_active_clients = re.compile(r"^Number\s+of\s+Active\s+Clients\.+ (?P<active_clients>\d+)$")


        for line in out.splitlines():
            line = line.strip()

            if p_product_version.match(line):
                match = p_product_version.match(line)
                parsed_dict.update({ "product_version": match.group("product_version") })
                continue
            elif p_system_name.match(line):
                match = p_system_name.match(line)
                parsed_dict.update({ "system_name": match.group("system_name") })
                continue
            elif p_ip_address.match(line):
                match = p_ip_address.match(line)
                parsed_dict.update({ "ip_address": match.group("ip_address") })
                continue
            elif p_system_up_time.match(line):
                match = p_system_up_time.match(line)
                parsed_dict.update({ "system_up_time": match.group("system_up_time") })
                continue
            elif p_number_of_active_clients.match(line):
                match = p_number_of_active_clients.match(line)
                parsed_dict.update({ "active_clients": match.group("active_clients") })
        
        return parsed_dict


        
