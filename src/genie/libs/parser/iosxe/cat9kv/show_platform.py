''' show_platform.py
IOSXE parsers for the following show commands:

    * 'show switch'
    '''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And, ListOf
from genie.libs.parser.utils.common import Common


class ShowSwitchSchema(MetaParser):
    """Schema for show switch"""
    schema = {
        'switch': {
            'mac_address': str,
            Optional('mac_persistency_wait_time'): str,
            Optional('stack'): {
                Any(): {
                    'role': str,
                    'mac_address': str,
                    'priority': str,
                    Optional('hw_ver'): str,
                    'state': str
                }
            }
        }
    }


class ShowSwitch(ShowSwitchSchema):
    """Parser for show switch."""
    cli_command = 'show switch'

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern

        # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
        p1 = re.compile(r'^([Ss]witch)?(Chassis)?\/[Ss]tack +[Mm]ac +[Aa]ddress +\: +'
                        r'(?P<switch_mac_address>[\w\.]+) *(?P<local>[\w\s\-]+)?$')

        # Mac persistency wait time: Indefinite
        p2 = re.compile(r'^[Mm]ac +persistency +wait +time\: +'
                        r'(?P<mac_persistency_wait_time>[\w\.\:]+)$')

        #                                              H/W   Current
        # Switch#   Role    Mac Address     Priority Version  State
        # -----------------------------------------------------------
        # *1       Active   689c.e2ff.b9d9     3      V04     Ready
        #  2       Standby  689c.e2ff.b9d9     14             Ready
        #  3       Member   bbcc.fcff.7b00     15     0       V-Mismatch
        p3 = re.compile(r'^\*?(?P<switch>\d+) +(?P<role>\w+) +'
                           r'(?P<mac_address>[\w\.]+) +'
                           r'(?P<priority>\d+) +'
                           r'(?P<hw_ver>[\w\d]+)? +'
                           r'(?P<state>[\w\s-]+)$')

        for line in output.splitlines():
            line = line.strip()

            # Switch/Stack Mac Address : 0057.d2ff.e71b - Local Mac Address
            m = p1.match(line)
            if m:
                switch_dict = ret_dict.setdefault('switch', {})
                switch_dict['mac_address'] = m.groupdict()['switch_mac_address']
                continue

            # Mac persistency wait time: Indefinite
            m = p2.match(line)
            if m:
                switch_dict['mac_persistency_wait_time'] = m.groupdict()['mac_persistency_wait_time'].lower()
                continue

            #                                              H/W   Current
            # Switch#   Role    Mac Address     Priority Version  State
            # -----------------------------------------------------------
            # *1       Active   689c.e2ff.b9d9     3      V04     Ready
            #  2       Standby  689c.e2ff.b9d9     14             Ready
            m = p3.match(line)
            if m:
                group = m.groupdict()
                stack = group['switch']
                match_dict = {k: v.lower()for k, v in group.items() if k in ['role', 'state']}
                match_dict.update({k: v for k, v in group.items() if k in ['priority', 'mac_address', 'hw_ver'] and v})
                switch_dict.setdefault('stack', {}).setdefault(stack, {}).update(match_dict)
                continue

        return ret_dict


# =================================================================
# Schema for 'show platform software fed switch active stp-vlan 1 '
# =================================================================


class ShowPlatformSoftwareFedSwitchActiveStpVlanSchema(MetaParser):
    """Schema for show platform software fed switch active stp-vlan {vlan_id}"""

    schema = {
        "hw_flood_list": ListOf(str),
        "interface": {
            Any(): {
                "pvlan_mode": str,
                "stp_state": str,
                "stp_state_hw": str,
                "vtp_pruned": str,
                "untagged": str,
                "ingress": str,
                "egress": str,
                "gid": str,
                "mac_learn": str
            }
        },
    }


# =================================================================
# Parser for 'show platform software fed switch active stp-vlan {vlan_id}'
# =================================================================


class ShowPlatformSoftwareFedSwitchActiveStpVlan(
    ShowPlatformSoftwareFedSwitchActiveStpVlanSchema
):
    """Parser for show platform software fed switch active stp-vlan {vlan_id}"""

    cli_command = [
        "show platform software fed switch {switch_num} stp-vlan {vlan_id}",
        "show platform software fed active stp-vlan {vlan_id}",
    ]

    def cli(self, vlan_id="", switch_num=None, output=None):
        if output is None:
            self.cli_command = (
                self.cli_command[0].format(switch_num=switch_num, vlan_id=vlan_id)
                if switch_num
                else self.cli_command[1].format(vlan_id=vlan_id)
            )
            output = self.device.execute(self.cli_command)

        #                    Interface   pvlan_mode   stp_state  vtp pruned          Untagged          Ingress           Egress
        p1 = re.compile(
            r"^(?P<interface>\S+) +(?P<pvlan_mode>\S+) +(?P<stp_state>\S+) +(?P<stp_state_hw>\S+) +"
            r"(?P<vtp_pruned>\S+) +(?P<untagged>\w+) +(?P<ingress>\w+) +(?P<egress>\w+) +(?P<gid>\d+) +(?P<mac_learn>\S+)$"
        )

        # HW flood list: : Gi2/0/23, Gi2/0/10, Gi2/0/12, Gi2/0/14, Gi2/0/16, Ap2/0/1
        p2 = re.compile(r"^HW flood list\:\s+:(?P<hw_flood_list>[\w\s\,/\.]*)$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # TenGigabitEthernet2/0/23         none    disabled          No               Yes         blocking         blocking
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                key_chain_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(dict_val["interface"]), {}
                )
                key_chain_dict["pvlan_mode"] = dict_val["pvlan_mode"]
                key_chain_dict["stp_state"] = dict_val["stp_state"]
                key_chain_dict["stp_state_hw"] = dict_val["stp_state_hw"]
                key_chain_dict["vtp_pruned"] = dict_val["vtp_pruned"]
                key_chain_dict["untagged"] = dict_val["untagged"]
                key_chain_dict["ingress"] = dict_val["ingress"]
                key_chain_dict["egress"] = dict_val["egress"]
                key_chain_dict["gid"] = dict_val["gid"]
                key_chain_dict["mac_learn"] = dict_val["mac_learn"]
                continue

            # HW flood list: : Gi2/0/23, Gi2/0/10, Gi2/0/12, Gi2/0/14, Gi2/0/16, Ap2/0/1
            m = p2.match(line)
            if m:
                ret_dict["hw_flood_list"] = (
                    m.groupdict()["hw_flood_list"].replace(" ", "").split(",")
                    if len(m.groupdict()["hw_flood_list"]) > 0
                    else []
                )
                continue

        return ret_dict
