"""show_platform_software_fed.py

    * 'show platform software fed switch {switch_var} access-security table usage'

"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import ListOf, Any
from genie.libs.parser.utils.common import Common

log = logging.getLogger(__name__)

class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema(MetaParser):
    """Schema for 'show platform software fed switch {switch_var} access-security table usage'"""

    schema = {
        'feature': {
            str: {
                'asic': {
                    int: ListOf({
                        'mask': str,
                        'maximum': int,
                        'in_use': int,
                        'total_allocated': int,
                        'total_freed': int
                    })
                }
            }
        }
    }
                                
class ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsage(ShowPlatformSoftwareFedSwitchActiveAccessSecurityTableUsageSchema):
    """Parser for 'show platform software fed switch {switch_var} access-security table usage'"""

    cli_command = 'show platform software fed switch {switch_var} access-security table usage'

    def cli(self, switch_var, output=None):
        if output is None:
            cmd = self.cli_command.format(switch_var=switch_var)

        output = self.device.execute(cmd)

        # Initialize parsed dictionary
        ret_dict = {}

        # Dot1x-MAC-Drop    Port-VLAN-MAC       0     4096      0  0       0
        p1 = re.compile(
            r'^(?P<feature>[\w\-]+)\s+(?P<mask>[\w\-]+)\s+(?P<asic>\d+)\s+'
            r'(?P<maximum>\d+)\s+(?P<in_use>\d+)\s+(?P<total_allocated>\d+)\s+'
            r'(?P<total_freed>\d+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            # Dot1x-MAC-Drop    Port-VLAN-MAC       0     4096      0  0       0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                feature_dict = ret_dict.setdefault('feature', {}).setdefault(group['feature'], {})
                asic_dict = feature_dict.setdefault('asic', {}).setdefault(int(group['asic']), [])
                asic_dict.append({
                    'mask': group['mask'],
                    'maximum': int(group['maximum']),
                    'in_use': int(group['in_use']),
                    'total_allocated': int(group['total_allocated']),
                    'total_freed': int(group['total_freed'])
                })

        return ret_dict

# ============================================================================
#  Schema for
#  * 'show platform software fed switch active acl bind db summary'
#  * 'show platform software fed switch active acl bind db feature racl summary'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbSummarySchema(MetaParser):
    """Schema for  'show platform software fed switch active acl bind db summary'
    'show platform software fed switch active acl bind db feature racl summary'
    """

    schema = {
        "interface": {
            Any(): {
                "feature": {
                    Any(): ListOf({
                        "protocol": str,
                        "status": str,
                        "cg_id": int,
                        "direction": str,
                    })
                }
            },
        },
    }

# ============================================================================
#  Parser for
#  * 'show platform software fed switch active acl bind db summary'
#  * 'show platform software fed switch active acl bind db feature racl summary'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbSummary(
    ShowPlatformSoftwareFedActiveAclBindDbSummarySchema
):
    """
    Parser for
    * 'show platform software fed switch active acl bind db summary'
    * 'show platform software fed switch active acl bind db feature racl summary'
    """

    cli_command = [
        "show platform software fed {switch} {switch_var} acl bind db summary",
        "show platform software fed {switch_var} acl bind db summary",
        "show platform software fed {switch_var} acl bind db feature {feature_name} summary",
        "show platform software fed {switch} {switch_var} acl bind db feature {feature_name} summary",
    ]

    def cli(self, switch_var, switch=None, feature_name=None, output=None):
        if output is None:
            if switch:
                if feature_name:
                    cmd = self.cli_command[3].format(switch=switch, switch_var=switch_var,feature_name=feature_name)
                else:
                    cmd = self.cli_command[0].format(switch_var=switch_var,switch=switch)
            else:
                if feature_name:
                    cmd = self.cli_command[2].format(switch_var=switch_var,feature_name=feature_name)
                else:
                    cmd = self.cli_command[1].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
        # Gi1/0/25    Racl          IPv4          Ingress     17           Success
        p1 = re.compile(
            r"^(?P<interface>[\w\-\.\/]+)\s+(?P<feature>\w+)\s+(?P<protocol>\w+)?\s+(?P<direction>\w+)\s+(?P<cg_id>\d+)\s+(?P<status>\w+)$"
        )

        for line in output.splitlines():
            line = line.strip()

            # Gi1/0/26.11  Racl          IPv4          Egress      13           Success
            # Gi1/0/25    Racl          IPv4          Ingress     17           Success
            m = p1.match(line)
            if m:
                group = m.groupdict()
                feature_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(group['interface']), {})
                acl_dict = feature_dict.setdefault('feature', {}).setdefault(group['feature'], [])
                acl_dict.append({
                    'cg_id': int(group['cg_id']),
                    'protocol': group['protocol'],
                    'direction': group['direction'],
                    'status': group['status']
                })
                continue

        return ret_dict

# ============================================================================
#  Schema for
#  * 'show platform software fed active acl bind db detail'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbDetailSchema(MetaParser):
    """Schema for 'show platform software fed active acl bind db detail'"""

    schema = {
        "interface": {
            Any(): {
                "direction": {
                    Any(): {
                        "feature": {
                            Any(): ListOf({
                                "protocol": str,
                                "cg_id": int,
                                "cg_name": str,
                                "status": str,
                                "src_og_lkup_hdl": int,
                                "dst_og_lkup_hdl": int,
                            }),
                        },
                    },
                },
            },
        },
    }

# ============================================================================
#  Parser for
#  * 'show platform software fed active acl bind db detail'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclBindDbDetail(
    ShowPlatformSoftwareFedActiveAclBindDbDetailSchema
):
    """
    Parser for
    * 'show platform software fed active acl bind db detail'
    """

    cli_command = [
        "show platform software fed {switch} {switch_var} acl bind db detail",
        "show platform software fed {switch_var} acl bind db detail",
    ]

    def cli(self, switch_var, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, switch_var=switch_var)
            else:
                cmd = self.cli_command[1].format(switch_var=switch_var)
            output = self.device.execute(cmd)

        # initial return dictionary
        ret_dict = {}

        # Interface Name: Hu1/0/2
        p1 = re.compile(r"^Interface Name:\s+(?P<interface>[\w\/\.\-]+)$")

        # Direction: Egress
        p2 = re.compile(r"^Direction:\s+(?P<direction>[\w\_]+)$")

        # Feature         : Pbr
        p3 = re.compile(r"^Feature\s+:\s(?P<feature>[\w]+)$")

        # Protocol        : IPv4
        p4 = re.compile(r"^Protocol\s+:\s(?P<protocol>[\w]+)$")

        # CG ID           : 1
        p5 = re.compile(r"^CG ID\s+:\s(?P<cg_id>[\d]+)$")

        # CG Name         : v4_rmap2
        # CG Name         : PACLv6in!PACLv4in:filterACL6!filterACL4:
        p6 = re.compile(r"^CG Name\s+:\s(?P<cg_name>[\w\_\-\!\:]+)$")

        # Status          : Success
        p7 = re.compile(r"^Status\s+:\s(?P<status>[\w]+)$")

        # Src_og_lkup_hdl : 0
        p8 = re.compile(r"^Src_og_lkup_hdl\s+:\s(?P<src_og_lkup_hdl>[\d]+)$")

        # Dst_og_lkup_hdl : 0
        p9 = re.compile(r"^Dst_og_lkup_hdl\s+:\s(?P<dst_og_lkup_hdl>[\d]+)$")

        for line in output.splitlines():
            line = line.strip()

            # Interface Name: Hu1/0/2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                int_dict = ret_dict.setdefault("interface", {}).setdefault(Common.convert_intf_name(group["interface"]), {})
                continue

            # Direction: Egress
            m = p2.match(line)
            if m:
                direction = m.groupdict()["direction"]
                dir_dict = int_dict.setdefault("direction", {}).setdefault(direction, {})
                continue

            # Feature         : Pbr
            m = p3.match(line)
            if m:
                group = m.groupdict()
                direction_list = dir_dict.setdefault("feature", {}).setdefault(group["feature"], [])
                continue

            # Protocol        : IPv4
            m = p4.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list.append({"protocol": dict_val["protocol"]})
                continue

            # CG ID           : 1
            m = p5.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"cg_id": int(dict_val["cg_id"])})
                continue

            # CG Name         : v4_rmap2
            m = p6.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"cg_name": dict_val["cg_name"]})
                continue

            # Status          : Success
            m = p7.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"status": dict_val["status"]})
                continue

            # Src_og_lkup_hdl : 0
            m = p8.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"src_og_lkup_hdl": int(dict_val["src_og_lkup_hdl"])})
                continue

            # Dst_og_lkup_hdl : 0
            m = p9.match(line)
            if m:
                dict_val = m.groupdict()
                direction_list[-1].update({"dst_og_lkup_hdl": int(dict_val["dst_og_lkup_hdl"])})
                continue

        return ret_dict
