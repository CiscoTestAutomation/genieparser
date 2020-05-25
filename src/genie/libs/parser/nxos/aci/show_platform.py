"""aci implementation of show_platform.py

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use


class ShowPlatformInternalHalPolicyRedirdstSchema(MetaParser):
    """Schema for 'vsh_lc -c "show platform internal hal policy redirdst group_id {group_id} {address_family} src_ip {src_ip} dst_ip {dst_ip} protocol {protocol}'"""

    schema = {
        'group_id': {
            Any(): {
                'src_ip': str,
                'dst_ip': str,
                'protocol': str,
                Optional('rewrite_mac'): str,
                Optional('rewrite_vnid'): str,
                Optional('outgoing_l2_ifindex'): str,
                Optional('outgoing_ifname'): str,
                Optional('packets_hash'): str,
            }
        }
    }


class ShowPlatformInternalHalPolicyRedirdst(ShowPlatformInternalHalPolicyRedirdstSchema):
    """Parser for 'vsh_lc -c "show platform internal hal policy redirdst group_id {group_id} {address_family} src_ip {src_ip} dst_ip {dst_ip} protocol {protocol}'"""

    cli_command = 'vsh_lc -c "show platform internal hal policy ' \
                  'redirdst group_id {group_id} {address_family} ' \
                  'src_ip {src_ip} dst_ip {dst_ip} protocol ' \
                  '{protocol}"'

    def cli(self, group_id, address_family, src_ip, dst_ip, protocol, output=None):
        if output is None:
            cmd = self.cli_command.format(
                group_id=group_id,
                address_family=address_family,
                src_ip=src_ip,
                dst_ip=dst_ip,
                protocol=protocol
            )
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        ret_dict = {}

        # initial regexp pattern
        # Group Id                                                 : 0x224 
        p1 = re.compile(r'^Group +Id +: +(?P<group_id>\S+)$')

        # Src IP                                                    : 10.1.1.1/32 
        p2 = re.compile(r'^Src +IP +: +(?P<src_ip>\S+)$')

        # Dst +IP +: +(?P<dst_ip>\S+)
        p3 = re.compile(r'^Dst +IP +: +(?P<dst_ip>\S+)$')

        # Protocol                                                  : 0x1
        p4 = re.compile(r'^Protocol +: +(?P<protocol>\S+)$')

        # Rewrite MAC                                               : 00:00:00:ff:02:03 
        p5 = re.compile(r'^Rewrite +MAC +: +(?P<rewrite_mac>\S+)$')

        # Rewrite VNID                                              : 0xf08007
        p6 = re.compile(r'^Rewrite +VNID +: +(?P<rewrite_vnid>\S+)$')

        # Outgoing L2 IfIndex                                       : 0x1801001e
        p7 = re.compile(r'^Outgoing +L2 +IfIndex +: +(?P<outgoing_l2_ifindex>\S+)$')

        # Outgoing IfName                                           : Tunnel30
        p8 = re.compile(r'^Outgoing +IfName +: +(?P<outgoing_ifname>\S+)$')

        # Packet's Hash                                             : 0x29d2 
        p9 = re.compile(r'^Packet\'s +Hash +: +(?P<packets_hash>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Group Id                                                 : 0x224 
            m = p1.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict = ret_dict.setdefault('group_id', {}). \
                    setdefault(group['group_id'], {})
                continue

            # Src IP                                                    : 10.1.1.1/32 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'src_ip': group['src_ip']})
                continue

            # Dst IP                                                    : 10.69.9.9/32 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'dst_ip': group['dst_ip']})
                continue

            # Protocol                                                  : 0x1 
            m = p4.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'protocol': group['protocol']})
                continue

            # Rewrite MAC                                               : 00:00:00:ff:02:03 
            m = p5.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'rewrite_mac': group['rewrite_mac']})
                continue

            # Rewrite VNID                                              : 0xf08007 
            m = p6.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'rewrite_vnid': group['rewrite_vnid']})
                continue

            # Outgoing L2 IfIndex                                       : 0x1801001e 
            m = p7.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'outgoing_l2_ifindex': group['outgoing_l2_ifindex']})
                continue

            # Outgoing IfName                                           : Tunnel30 
            m = p8.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'outgoing_ifname': group['outgoing_ifname']})
                continue
            
            # Packet's Hash                                             : 0x29d2 
            m = p9.match(line)
            if m:
                group = m.groupdict()
                groud_id_dict.update({'packets_hash': group['packets_hash']})
                continue

        return ret_dict