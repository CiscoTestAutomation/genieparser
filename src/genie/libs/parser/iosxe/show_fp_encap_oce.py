''' show_fp_encap_oce.py

IOSXE parsers for the following show commands:

    * show platform software evpn Fp active encap-oce index <oce_index> detail

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any

# ====================================
# Parser for 'show platform software evpn Fp active encap-oce index <oce_index> detail'
# ====================================
class ShowFpEncapOceSchema(MetaParser):
    """Schema for show platform software evpn Fp active encap-oce index <oce_index> detail"""

    schema = {
        'oce':{
            Optional('evpn_encap_oce'):{
                'number_of_children': int,
                Optional('flags'): str,
                Optional('atom_flags'): str,
                'next_hop': str,
                Optional('efi_name'): str,
                Optional('next_hw_oce_ptr'): str
            },
            Optional('vxlan_header_oce'):{
                'number_of_children': int,
                Optional('next_hw_oce_ptr'): str,
                Optional('encap_str'): str
            },
            'adjacency':{
                'number_of_children': int,
                'adj_type': str,
                Optional('encap_len'): int,
                'l3_mtu': int,
                Optional('adj_flags'): str,
                Optional('fixup_flags'): str,
                Optional('output_uidb'): int,
                'interface_name': str,
                'next_hop_address': str,
                Optional('lisp_fixup_hw_ptr'): str,
                Optional('next_hw_oce_ptr'): str,
                Optional('fixup_flags_2'): str,
                'encap': str,
                Optional('adj_gre'): bool,
                Optional('adj_flag_2'): bool
            }
        }
    }


class ShowFpEncapOce(ShowFpEncapOceSchema):
    """Parser for show platform software evpn Fp active encap-oce index <oce_index> detail"""

    cli_command = 'show platform software evpn Fp active encap-oce index {oce_index} detail'

    def cli(self, oce_index=None, output=None):

        cli = self.cli_command

        if output is None:
            cli = self.cli_command.format(oce_index=oce_index)
            output = self.device.execute(cli)

        # initial return dictionary
        ret_dict = {}

        # OCE Type: EVPN Encap OCE, Number of children: 1
        p1 = re.compile(r'^OCE +Type: +(?P<oce_type>[\d\w ]+), +Number +of +children: +(?P<number_of_children>[\d]+)$')
        # Flags: 0x02
        p2 = re.compile(r'^Flags: +(?P<flags>[\w\d]+)$')
        # Atom flags: 0000
        p3 = re.compile(r'^Atom +flags: +(?P<atom_flags>[\w\d]+)$')
        # Next hop: 2.2.2.3
        p4 = re.compile(r'^Next +hop: +(?P<next_hop>[\.\d]+)$')
        # EFI Name: nve1.VNI20111
        p5 = re.compile(r'^EFI +Name: +(?P<efi_name>[\w\d\.]+)$')
        # Next hw oce ptr: 0xe8bc9120
        p6 = re.compile(r'^Next +hw +oce +ptr: +(?P<next_hw_oce_ptr>[\w\d]+)$')
        # Fixup_Flags_2: 0xd0000
        p7 = re.compile(r'^Fixup_Flags_2: +(?P<fixup_flags_2>[\w\d]+)$')
        # Adj Type: IPV4 Adjacency
        p8 = re.compile(r'^Adj +Type: +(?P<adj_type>[\w\d ]+)$')
        # Encap Len: 28
        p9 = re.compile(r'^Encap +Len: +(?P<encap_len>[\d]+)$')
        # L3 MTU: 9216
        p10 = re.compile(r'^L3 +MTU: +(?P<l3_mtu>[\d]+)$')
        # Adj Flags: 0x0000
        p11 = re.compile(r'^Adj +Flags: +(?P<adj_flags>[\w\d]+)$')
        # Interface Name: Tunnel1
        p12 = re.compile(r'^Interface +Name: +(?P<interface_name>\w+)$')
        # Next Hop Address: 2.2.2.3
        p13 = re.compile(r'^Next +Hop +Address: +(?P<next_hop_address>[\.\d]+)$')
        # Output UIDB: 262090
        p14 = re.compile(r'^Output +UIDB: +(?P<output_uidb>[\d]+)$')
        # Lisp Fixup HW Ptr: 0x4966a3a0
        p15 = re.compile(r'^Lisp +Fixup +HW +Ptr: +(?P<lisp_fixup_hw_ptr>[\w\d]+)$')
        # Next HW OCE Ptr: 00000000
        p16 = re.compile(r'^Next +HW +OCE +Ptr: +(?P<next_hw_oce_ptr>[\w\d]+)$')
        # Encap str: 8000000 6212400
        p17 = re.compile(r'^Encap +str: +(?P<encap_str>[\d ]+)$')
        # Encap: 45 00 00 00 00 00 00 00 ff 11 ed 5e 63 63 03 64
        p18 = re.compile(r'^Encap: +(?P<encap>[\d\w ]+)$')
        # 63 63 04 64 12 b5 12 b5 00 00 00 00
        p19 = re.compile(r'^(?P<encap2>[\da-fA-F ]+)$')
        # Fixup Flags: 0x0001
        p20 = re.compile(r'^Fixup +Flags: +(?P<fixup_flags>[\d\w]+)$')
        # ADJ_GRE
        p21 = re.compile(r'^ADJ_GRE$')
        # ADJ_FLAG_2_ROUTE_PTR
        p22 = re.compile(r'^ADJ_FLAG_2_ROUTE_PTR$')

        for line in output.splitlines():
            line = line.strip()

            # OCE Type: EVPN Encap OCE, Number of children: 1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                oce_type = group['oce_type'].replace(' ', '_').lower()
                final_dict = ret_dict.setdefault('oce', {}).\
                    setdefault(oce_type, {})
                final_dict['number_of_children'] = int(group['number_of_children'])
                continue

            # Flags: 0x02
            m = p2.match(line)
            if m:
                group = m.groupdict()
                final_dict['flags'] = group['flags']
                continue

            # Atom flags: 0000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                final_dict['atom_flags'] = group['atom_flags']
                continue

            # Next hop: 2.2.2.3
            m = p4.match(line)
            if m:
                group = m.groupdict()
                final_dict['next_hop'] = group['next_hop']
                continue

            # EFI Name: nve1.VNI20111
            m = p5.match(line)
            if m:
                group = m.groupdict()
                final_dict['efi_name'] = group['efi_name']
                continue

            # Next hw oce ptr: 0xe8bc9120
            m = p6.match(line)
            if m:
                group = m.groupdict()
                final_dict['next_hw_oce_ptr'] = group['next_hw_oce_ptr']
                continue

            # Fixup_Flags_2: 0xd0000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                final_dict['fixup_flags_2'] = group['fixup_flags_2']
                continue

            # ADJ_FLAG_2_ROUTE_PTR
            m = p22.match(line)
            if m:
                final_dict['adj_flag_2'] = True
                continue

            # Adj Type: IPV4 Adjacency
            m = p8.match(line)
            if m:
                group = m.groupdict()
                final_dict['adj_type'] = group['adj_type']
                continue

            # Encap Len: 28
            m = p9.match(line)
            if m:
                group = m.groupdict()
                final_dict['encap_len'] = int(group['encap_len'])
                continue

            # L3 MTU: 9216
            m = p10.match(line)
            if m:
                group = m.groupdict()
                final_dict['l3_mtu'] = int(group['l3_mtu'])
                continue

            # Adj Flags: 0x0000
            m = p11.match(line)
            if m:
                group = m.groupdict()
                final_dict['adj_flags'] = group['adj_flags']
                continue

            # Interface Name: Tunnel1
            m = p12.match(line)
            if m:
                group = m.groupdict()
                final_dict['interface_name'] = group['interface_name']
                continue

            # Next Hop Address: 2.2.2.3
            m = p13.match(line)
            if m:
                group = m.groupdict()
                final_dict['next_hop_address'] = group['next_hop_address']
                continue

            # Output UIDB: 262090
            m = p14.match(line)
            if m:
                group = m.groupdict()
                final_dict['output_uidb'] = int(group['output_uidb'])
                continue

            # Lisp Fixup HW Ptr: 0x4966a3a0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                final_dict['lisp_fixup_hw_ptr'] = group['lisp_fixup_hw_ptr']
                continue

            # Next HW OCE Ptr: 00000000
            m = p16.match(line)
            if m:
                group = m.groupdict()
                final_dict['next_hw_oce_ptr'] = group['next_hw_oce_ptr']
                continue

            # Encap str: 8000000 6212400
            m = p17.match(line)
            if m:
                group = m.groupdict()
                final_dict['encap_str'] = group['encap_str']
                continue

            # Encap: 45 00 00 00 00 00 00 00 ff 11 ed 5e 63 63 03 64
            m = p18.match(line)
            if m:
                group = m.groupdict()
                final_dict['encap'] = group['encap']
                continue
        
            # 63 63 04 64 12 b5 12 b5 00 00 00 00
            m = p19.match(line)
            if m:
                group = m.groupdict()
                final_dict['encap'] = final_dict['encap'] + ' ' + group['encap2']
                continue

            # Fixup Flags: 0x0001
            m = p20.match(line)
            if m:
                group = m.groupdict()
                final_dict['fixup_flags'] = group['fixup_flags']
                continue

            # ADJ_GRE
            m = p21.match(line)
            if m:
                final_dict['adj_gre'] = True
                continue

        return ret_dict
