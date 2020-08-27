import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================
# Schema for:
#  * 'show cts rbacl'
# ======================
class ShowCtsRbaclSchema(MetaParser):
    """Schema for show cts rbacl."""

    schema = {
        "cts_rbacl": {
            "ip_ver_support": str,
            "name": {
                str: {
                    "ip_protocol_version": str,
                    "refcnt": int,
                    "flag": str,
                    "stale": bool,
                    "aces": {
                        Optional(int): {
                            Optional("action"): str,
                            Optional("protocol"): str,
                            Optional("direction"): str,
                            Optional("port"): int
                        }
                    }
                }
            }
        }
    }


# ======================
# Parser for:
#  * 'show cts rbacl'
# ======================
class ShowCtsRbacl(ShowCtsRbaclSchema):
    """Parser for show cts rbacl"""

    cli_command = 'show cts rbacl'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        cts_rbacl_dict = {}
        # CTS RBACL Policy
        # ================
        # RBACL IP Version Supported: IPv4 & IPv6
        #   name   = TCP_51005-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51005
        #
        #   name   = TCP_51060-02
        #   IP protocol version = IPV4
        #   refcnt = 4
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51060
        #
        #   name   = TCP_51144-01
        #   IP protocol version = IPV4
        #   refcnt = 10
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51144
        #
        #   name   = TCP_51009-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        #   RBACL ACEs:
        #     permit tcp dst eq 51009



        # RBACL IP Version Supported: IPv4 & IPv6
        ip_ver_capture = re.compile(r"^RBACL\s+IP\s+Version\s+Supported:\s(?P<ip_ver_support>.*$)")
        #   name   = TCP_13131-01
        #   IP protocol version = IPV4
        #   refcnt = 2
        #   flag   = 0x41000000
        #   stale  = FALSE
        rbacl_capture = re.compile(r"^(?P<rbacl_key>.*)(?==)=\s+(?P<rbacl_value>.*$)")
        #     permit tcp dst eq 13131
        rbacl_ace_capture = re.compile(
            r"^(?P<action>(permit|deny))\s+(?P<protocol>\S+)(\s+(?P<direction>dst|src)\s+((?P<port_condition>)\S+)\s+(?P<port>\d+)|)")

        remove_lines = ('CTS RBACL Policy', '================', 'RBACL ACEs:')
        
                # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)
        rbacl_name = ''
        rbacl_ace_index = 1
        for line in out:
            # RBACL IP Version Supported: IPv4 & IPv6
            ip_ver_match = ip_ver_capture.match(line)
            if ip_ver_match:
                groups = ip_ver_match.groupdict()
                ip_ver_support = groups['ip_ver_support']
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                    cts_rbacl_dict['cts_rbacl']['name'] = {}
                cts_rbacl_dict['cts_rbacl']['ip_ver_support'] = ip_ver_support
                continue
            #   name   = TCP_13131-01
            #   IP protocol version = IPV4
            #   refcnt = 2
            #   flag   = 0x41000000
            #   stale  = FALSE
            elif rbacl_capture.match(line):
                groups = rbacl_capture.match(line).groupdict()
                rbacl_key = groups['rbacl_key'].strip().lower().replace(' ', '_')
                rbacl_value = groups['rbacl_value']
                if rbacl_value.isdigit():
                    rbacl_value = int(rbacl_value)
                if rbacl_value == "TRUE" or rbacl_value == "FALSE":
                    if rbacl_value == "TRUE":
                        rbacl_value = True
                    else:
                        rbacl_value = False
                if not cts_rbacl_dict.get('cts_rbacl', {}):
                    cts_rbacl_dict['cts_rbacl'] = {}
                if rbacl_key == 'name':
                    rbacl_name = rbacl_value
                    cts_rbacl_dict['cts_rbacl']['name'][rbacl_name] = {}
                    rbacl_ace_index = 1
                else:
                    cts_rbacl_dict['cts_rbacl']['name'][rbacl_name].update({rbacl_key: rbacl_value})
                continue
            #     permit tcp dst eq 13131
            elif rbacl_ace_capture.match(line):
                groups = rbacl_ace_capture.match(line).groupdict()
                ace_group_dict = {}
                cts_rbacl_dict['cts_rbacl']['name'][rbacl_name]['aces'] = {}
                if groups['action']:
                    ace_group_dict.update({'action': groups['action']})
                if groups['protocol']:
                    ace_group_dict.update({'protocol': groups['protocol']})
                if groups['direction']:
                    ace_group_dict.update({'direction': groups['direction']})
                if groups['port_condition']:
                    ace_group_dict.update({'port_condition': groups['port_condition']})
                if groups['port']:
                    ace_group_dict.update({'port': int(groups['port'])})
                if not cts_rbacl_dict['cts_rbacl']['name'][rbacl_name]['aces'].get(rbacl_ace_index, {}):
                    cts_rbacl_dict['cts_rbacl']['name'][rbacl_name]['aces'][rbacl_ace_index] = ace_group_dict
                rbacl_ace_index = rbacl_ace_index + 1
                continue
        return cts_rbacl_dict
        
# ==================
# Schema for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacsSchema(MetaParser):
    """Schema for show cts pacs."""

    schema = {
        "aid": str,
        "pac_info": {
            "aid": str,
            "pac_type": str,
            "i_id": str,
            "a_id_info": str,
            "credential_lifetime": str,
        },
        "pac_opaque": str,
        "refresh_timer": str
    }


# ==================
# Parser for:
#  * 'show cts pacs'
# ==================
class ShowCtsPacs(ShowCtsPacsSchema):
    """Parser for show cts pacs"""

    cli_command = 'show cts pacs'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # AID: 1100E046659D4275B644BF946EFA49CD
        # PAC-Info:
        #   PAC-type = Cisco Trustsec
        #   AID: 1100E046659D4275B644BF946EFA49CD
        #   I-ID: gw1
        #   A-ID-Info: Identity Services Engine
        #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
        # PAC-Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
        # Refresh timer is set for 6w3d

        cts_pacs_dict = {}

        # AID: 1100E046659D4275B644BF946EFA49CD
        aid_capture = re.compile(r"^AID:\s+(?P<aid>\S+)")
        #   PAC-type = Cisco Trustsec
        pac_type_capture = re.compile(r"^PAC-type\s=\s(?P<pac_type>.*$)")
        #     I-ID: gw1
        iid_capture = re.compile(r"^I-ID:\s+(?P<iid>\S+)")
        #   A-ID-Info: Identity Services Engine
        aid_info_capture = re.compile(r"^A-ID-Info:\s+(?P<aid_info>.*$)")
        #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
        credential_lifetime_capture = re.compile(
            r"^Credential\s+Lifetime:\s+(?P<time>\d+:\d+:\d+)\s+(?P<time_zone>\S+)\s+(?P<day>\S+)\s+(?P<month>\S+)\s+(?P<date>\d+)\s+(?P<year>\d+)")
        # PAC - Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
        pac_opaque_capture = re.compile(r"^PAC-Opaque:\s+(?P<pac_opaque>.*$)")
        # Refresh timer is set for 6w3d
        refresh_timer_capture = re.compile(r"^Refresh\s+timer\s+is\s+set\s+for\s+(?P<refresh_timer>\S+)")

        remove_lines = ('PAC-Info:')

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # print(clean_line)
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)


        for line in out:
            # AID: 1100E046659D4275B644BF946EFA49CD
            aid_match = aid_capture.match(line)
            if aid_match:
                groups = aid_match.groupdict()
                aid = groups['aid']
                if not cts_pacs_dict.get('aid', {}):
                    cts_pacs_dict['aid'] = aid
                if not cts_pacs_dict.get('pac_info', {}):
                    cts_pacs_dict['pac_info'] = {}
                    cts_pacs_dict['pac_info']['aid'] = aid
                continue
            #   PAC-type = Cisco Trustsec
            pac_type_match = pac_type_capture.match(line)
            if pac_type_match:
                groups = pac_type_match.groupdict()
                pac_type = groups['pac_type']
                if not cts_pacs_dict.get('pac_info', {}):
                    cts_pacs_dict['pac_info'] = {}
                cts_pacs_dict['pac_info']['pac_type'] = pac_type
                continue
            #     I-ID: gw1
            iid_match = iid_capture.match(line)
            if iid_match:
                groups = iid_match.groupdict()
                iid = groups['iid']
                cts_pacs_dict['pac_info']['i_id'] = iid
                continue
            #   A-ID-Info: Identity Services Engine
            aid_info_match = aid_info_capture.match(line)
            if aid_info_match:
                groups = aid_info_match.groupdict()
                aid_info = groups['aid_info']
                cts_pacs_dict['pac_info']['a_id_info'] = aid_info
                continue
            #   Credential Lifetime: 19:56:32 PDT Sun Sep 06 2020
            credential_lifetime_match = credential_lifetime_capture.match(line)
            if credential_lifetime_match:
                groups = credential_lifetime_match.groupdict()
                time = groups['time']
                time_zone = groups['time_zone']
                day = groups['day']
                month = groups['month']
                date = groups['date']
                year = groups['year']
                full_date = f"{day}, {month}/{date}/{year}"
                cts_pacs_dict['pac_info']['credential_lifetime'] = full_date
                continue
            # PAC - Opaque: 000200B80003000100040010207FCE2A590A44BA0DE959740A348AF00006009C00030100F57E4D71BDE3BD2850B2B63C92E18122000000135EDA996F00093A805A004010F4EDAF81FB6900D03013E907ED81BFB83EE273B8E563BE48DC16B2E9164B1AA6711281937B734E8C449280FCEAF4BE668545B5A55BE20C6346C42AFFCA87FFDDA0AC6A480F9AEE147541EE51FB67CDE0580FD8A746978C78C2CB9E7855BB1667469896AB18902424344AC094B3162EF09488CDB0D6A95139
            pac_opaque_match = pac_opaque_capture.match(line)
            if pac_opaque_match:
                groups = pac_opaque_match.groupdict()
                pac_opaque = groups['pac_opaque']
                cts_pacs_dict['pac_opaque'] = pac_opaque
                continue
            # Refresh timer is set for 6w3d
            refresh_timer_match = refresh_timer_capture.match(line)
            if refresh_timer_match:
                groups = refresh_timer_match.groupdict()
                refresh_timer = groups['refresh_timer']
                cts_pacs_dict['refresh_timer'] = refresh_timer
                continue
        return cts_pacs_dict

