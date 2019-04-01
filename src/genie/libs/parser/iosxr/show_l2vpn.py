"""show_l2vpn.py

show l2vpn parser class

"""

import re
from netaddr import EUI
from ipaddress import ip_address

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

from genie.libs.parser.base import *


class ShowL2vpnMacLearning(MetaParser):
    """Parser for show l2vpn mac-learning <mac_type> all location <location>"""

    # TODO schema

    def __init__(self, mac_type='mac', location='local', **kwargs):
        self.location = location
        self.mac_type = mac_type
        super().__init__(**kwargs)

    cli_command = 'show l2vpn mac-learning {mac_type} all location {location}'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(
                mac_type=self.mac_type,
                location=self.location))
        else:
            out = output

        result = {
            'entries': [],
        }


        for line in out.splitlines():
            line = line.rstrip()
            # Topo ID   Producer       Next Hop(s)       Mac Address       IP Address
            # -------   --------       -----------       --------------    ----------

            # 1         0/0/CPU0       BE1.7             7777.7777.0002
            # 0         0/0/CPU0       BV1               fc00.0001.0006    192.168.30.3
            m = re.match(r'^(?P<topo_id>\d+)'
                         r' +(?P<producer>\S+)'
                         r' +(?:none|(?P<next_hop>\S+))'
                         r' +(?P<mac>[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+)'
                         r'(?: +(?P<ip_address>\d+\.\d+\.\d+\.\d+|[A-Za-z0-9:]+))?$', line)
            if m:
                entry = {
                    'topo_id': eval(m.group('topo_id')),
                    'producer': m.group('producer'),
                    'next_hop': m.group('next_hop'),
                    'mac': EUI(m.group('mac')),
                    'ip_address': m.group('ip_address') \
                    and ip_address(m.group('ip_address')),
                }
                result['entries'].append(entry)
                continue

        return result


class ShowL2vpnForwardingBridgeDomainMacAddress(MetaParser):
    """Parser for:
        show l2vpn forwarding bridge-domain mac-address location <location>
        show l2vpn forwarding bridge-domain <bridge_domain> mac-address location <location>
    """
    # TODO schema

    def __init__(self,location=None,bridge_domain=None,**kwargs) :
        assert location is not None
        self.location = location
        self.bridge_domain = bridge_domain
        super().__init__(**kwargs)

    cli_command = ['show l2vpn forwarding bridge-domain mac-address location {location}', \
                   'show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}']

    def cli(self,output=None):
        if output is None:
            if self.bridge_domain is None:
                cmd = self.cli_command[0].format(location=self.location)
            else:
                cmd = self.cli_command[1].format(bridge_domain=self.bridge_domain,location=self.location)

            out = self.device.execute(cmd)
        else:
            out = output

        result = {
            'entries' : []
        }

        ## Sample Output

        #  To Resynchronize MAC table from the Network Processors, use the command...
        #     l2vpn resynchronize forwarding mac-address-table location <r/s/i>
        #
        # Mac Address    Type    Learned from/Filtered on    LC learned Resync Age/Last Change Mapped to
        # -------------- ------- --------------------------- ---------- ---------------------- --------------
        # 0021.0001.0001 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 0021.0001.0003 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 0021.0001.0004 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 0021.0001.0005 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 1234.0001.0001 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 1234.0001.0002 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 1234.0001.0003 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 1234.0001.0004 EVPN    BD id: 0                    N/A        N/A                    N/A
        # 0021.0001.0002 dynamic (10.25.40.40, 10007)        N/A        14 Mar 12:46:04        N/A
        # 1234.0001.0005 static  (10.25.40.40, 10007)        N/A        N/A                    N/A
        # 0021.0002.0005 dynamic BE1.2                       N/A        14 Mar 12:46:04        N/A
        # 1234.0002.0004 static  BE1.2                       N/A        N/A                    N/A

        title_found = False
        header_processed = False
        field_indice = []

        def _retrieve_fields(line,field_indice):
            res = []
            for idx,(start,end) in enumerate(field_indice):
                if idx == len(field_indice) - 1:
                    res.append(line[start:].strip())
                else:
                    res.append(line[start:end].strip())
            return res

        lines = out.splitlines()
        for idx,line in enumerate(lines):
            if idx == len(lines) - 1:
                break
            line = line.rstrip()
            if not header_processed:
                # 1. check proper title header exist
                if re.match(r"^Mac Address\s+Type\s+Learned from/Filtered on\s+LC learned\s+Resync Age/Last Change\s+Mapped to",line):
                    title_found = True
                    continue
                # 2. get dash header line
                if title_found and re.match(r"^(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)",line):
                    match = re.match(r"^(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)( +)(-+)",line)
                    start = 0
                    for field in match.groups():
                        if '-' in field:
                            end = start + len(field)
                            field_indice.append((start,end))
                            start = end
                        else:
                            start += len(field)
                            end += len(field)
                    header_processed = True
                    continue
            else:
                mac,mac_type,learned_from,lc_learned,resync_age,mapped_to = _retrieve_fields(line,field_indice)
                result['entries'].append({
                    'mac' : mac,
                    'mac_type' : mac_type,
                    'learned_from' : learned_from,
                    'lc_learned' : lc_learned,
                    'resync_age' : resync_age,
                    'mapped_to' : mapped_to,
                })

        return result


class ShowL2vpnForwardingProtectionMainInterface(MetaParser):
    """Parser for show l2vpn forwarding protection main-interface location <location>"""
    # TODO schema

    def __init__(self,location=None,**kwargs):
        assert location is not None
        self.location = location
        super().__init__(**kwargs)

    cli_command = 'show l2vpn forwarding protection main-interface location {location}'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(location=self.location))
        else:
            out = output

        result = {
            'entries' : []
        }

        ## Sample Output

        # Main Interface ID                Instance   State
        # -------------------------------- ---------- ------------
        # VFI:ves-vfi-1                    0          FORWARDING
        # VFI:ves-vfi-1                    1          BLOCKED
        # VFI:ves-vfi-2                    0          FORWARDING
        # VFI:ves-vfi-2                    1          FORWARDING
        # VFI:ves-vfi-3                    0          FORWARDING
        # VFI:ves-vfi-3                    1          BLOCKED
        # VFI:ves-vfi-4                    0          FORWARDING
        # VFI:ves-vfi-4                    1          FORWARDING
        # PW:10.25.40.40,10001             0          FORWARDING
        # PW:10.25.40.40,10001             1          BLOCKED
        # PW:10.25.40.40,10007             0          FORWARDING
        # PW:10.25.40.40,10007             1          FORWARDING
        # PW:10.25.40.40,10011             0          FORWARDING
        # PW:10.25.40.40,10011             1          FORWARDING
        # PW:10.25.40.40,10017             0          FORWARDING

        title_found = False
        header_processed = False
        field_indice = []

        def _retrieve_fields(line,field_indice):
            res = []
            for idx,(start,end) in enumerate(field_indice):
                if idx == len(field_indice) - 1:
                    res.append(line[start:].strip())
                else:
                    res.append(line[start:end].strip())
            return res

        lines = out.splitlines()
        for idx,line in enumerate(lines):
            if idx == len(lines) - 1:
                break
            line = line.rstrip()
            if not header_processed:
                # 1. check proper title header exist
                if re.match(r"^Main Interface ID\s+Instance\s+State",line):
                    title_found = True
                    continue
                # 2. get dash header line
                if title_found and re.match(r"^(-+)( +)(-+)( +)(-+)",line):
                    match = re.match(r"^(-+)( +)(-+)( +)(-+)",line)
                    start = 0
                    for field in match.groups():
                        if '-' in field:
                            end = start + len(field)
                            field_indice.append((start,end))
                            start = end
                        else:
                            start += len(field)
                            end += len(field)
                    header_processed = True
                    continue
            else:
                interface,instance_id,state = _retrieve_fields(line,field_indice)
                result['entries'].append({
                    'interface' : interface,
                    'instance_id' : instance_id,
                    'state' : state,
                })

        return result

# vim: ft=python ts=8 sw=4 et
