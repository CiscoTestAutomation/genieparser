"""show_vxlan.py

NXOS revision parser for the following show commands:
    * show nve ethernet-segment
    * show nve ethernet-segment esi <esi_id>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# =====================================================================================
#   Schema for 'show nve ethernet-segment' and 'show nve ethernet-segment esi <esi_id>' 
# =====================================================================================
class ShowNveEthernetSegmentSchema(MetaParser):
    """Schema for:
          show nve ethernet-segment"""

    schema ={
        'nve':{
            Any():{
                'ethernet_segment': {
                    'esi': {
                        Any(): {
                            'esi': str,
                            'if_name': str,
                            'es_state': str,
                            'po_state': str,
                            'nve_if_name': str,
                            'nve_state': str,
                            'host_reach_mode': str,
                            Optional('active_vlans'): list,
                            Optional('df_vlans'): list,
                            Optional('active_vnis'): list,
                            Optional('df_bd_list'): list,
                            Optional('df_vni_list'): list,
                            'num_es_mem': int,
                            'local_ordinal': int,
                            'df_timer_st': str,
                            'config_status': str,
                            'df_list': list,
                            'es_rt_added': bool,
                            'ead_rt_added': bool,
                            'esi_type': str,
                            'esi_df_election_mode': str,
                        },
                    },
                },
            },
        }
    }

# ======================================================================================
#   Parser for 'show nve ethernet-segment' and 'show nve ethernet-segment esi <esi_id>'
# ======================================================================================
class ShowNveEthernetSegment(ShowNveEthernetSegmentSchema):
    """parser for:
        show nve ethernet-segment"""

    cli_command = ['show nve ethernet-segment', 'show nve ethernet-segment esi {esi_id}']

    def cli(self, esi_id="", output=None):
        # excute command to get output
        if output is None:
            if esi_id:
                cmd = self.cli_command[1].format(esi_id=esi_id)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        result_dict = {}
        # ========================================================================================
        # ESI: 0300.0000.0186.a000.0309
        # Parent interface: nve1
        # ES State: Up
        # Port-channel state: N/A
        # NVE Interface: nve1
        # NVE State: Up
        # Host Learning Mode: control-plane
        # Active Vlans: 1,1001-2000,2501-2550,2601-2650,2701-2750,2801-2850,2901-2950
        # DF Vlans: 1001,1004,1007,1010,1013,1016,1019,1022,1025,1028,1031,1034,1037,1040,1043,2948
        # Active VNIs: 10001-10200,10501-11000,12501-13000,22001-22200,24001-24100
        # DF BDs: 8193,8196,8199,8202,8205,8208,8211,8214,8217,8220,8223,8226,8229,8232,12998
        # DF VNIs: 12551,12554,12557,12560,12563,12566,12569,12572,12575,12578,12581,12584,12587
        # Number of ES members: 3
        # My ordinal: 2
        # DF timer start time: 00:00:00
        # Config State: N/A
        # DF List: 100:100:100::1 100:100:100::2 100:100:100::7
        # ES route added to L2RIB: True
        # EAD/ES routes added to L2RIB: False
        # ESI type: Ether-segment
        # ESI DF election mode: Modulo
        # ========================================================================================

        
        # ESI: 0300.0000.0186.a000.0309
        p1 = re.compile(r'^ESI:\s+(?P<esi>[\w\.]+)$')

        # Parent interface: nve1
        p2 = re.compile(r'^Parent\s+interface:\s+(?P<parent_intf>[\w\.\/-]+)$')

        # ES State: Up
        p3 = re.compile(r'^ES\s+State:\s+(?P<es_state>[\w\/]+)$')

        # Port-channel state: N/A
        p4 = re.compile(r'^Port-channel\s+state:\s+(?P<po_state>[\w\/]+)$')

        # NVE Interface: nve1
        p5 = re.compile(r'^NVE\s+Interface:\s+(?P<nve_intf>[\w\.\/]+)$')

        # NVE State: Up
        p6 = re.compile(r'^NVE\s+State:\s+(?P<nve_state>[\w\/]+)$')

        # Host Learning Mode: control-plane
        p7 = re.compile(r'^Host\s+Learning\s+Mode:\s+(?P<host_learning_mode>[\w\-]+)$')

        # Active Vlans: 1,1001-2000,2501-2550,2601-2650,2701-2750,2801-2850,2901-2950
        p8 = re.compile(r'^Active\s+Vlans:\s+(?P<active_vlans>[\d\-\,]+)$')

        # DF Vlans: 1001,1004,1007,1010,1013,1016,1019,1022,1025,1028,1031,1034,1037,1040,1043,2948
        p9 = re.compile(r'^DF\sVlans:\s+(?P<df_vlans>[\d\-\,]+)$')

        # Active VNIs: 10001-10200,10501-11000,12501-13000,22001-22200,24001-24100
        p10 = re.compile(r'^Active\s+VNIs:\s+(?P<active_vnis>[\d\-\,]+)$')

        # DF BDs: 8193,8196,8199,8202,8205,8208,8211,8214,8217,8220,8223,8226,8229,8232,12998
        p11 = re.compile(r'^DF\s+BDs:\s+(?P<df_bds>[\d\-\,]+)$')

        # DF VNIs: 12551,12554,12557,12560,12563,12566,12569,12572,12575,12578,12581,12584,12587
        p12 = re.compile(r'^DF\s+VNIs:\s+(?P<df_vnis>[\d\-\,]+)$')

        # Number of ES members: 3
        p13 = re.compile(r'^Number\s+of\s+ES\s+members:\s+(?P<num_es_mem>[\d]+)?$')

        # My ordinal: 2
        p14 = re.compile(r'^My\s+ordinal:\s+(?P<local_ordinal>[\d]+)$')

        # DF timer start time: 00:00:00
        p15 = re.compile(r'^DF\s+timer\s+start\s+time:\s+(?P<df_timer_start_time>[\w\:]+)$')

        # Config State: N/A
        p16 = re.compile(r'^Config\s+State:\s+(?P<config_status>[\w\/-]+)$')

        # DF List: 100:100:100::1 100:100:100::2 100:100:100::7
        p17 = re.compile(r'^DF\s+List:\s+(?P<df_list>[\d\s\.:]+)$')

        # ES route added to L2RIB: True
        p18 = re.compile(r'^ES\s+route\s+added\s+to\s+L2RIB:\s+(?P<is_es_added_to_l2rib>[\w]+)$')

        # EAD/ES routes added to L2RIB: False
        p19 = re.compile(r'^EAD\/ES\s+routes\s+added\s+to\s+L2RIB:\s+(?P<ead_rt_added>[\w]+)$')

        # ESI type: Ether-segment
        p20 = re.compile(r'^ESI\s+type:\s+(?P<esi_type>[\w\s-]+)$')

        # ESI DF election mode: Modulo
        p21 = re.compile(r'^ESI\s+DF\s+election\s+mode:\s+(?P<esi_df_election_mode>[\w\s-]+)$')

        for line in output.splitlines():
            line = line.strip()

            # ESI: 0300.0000.0186.a000.0309
            m = p1.match(line)
            if m:
                group = m.groupdict()
                esi = group.pop('esi')
                continue

            # Parent interface: nve1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if_name = group.pop('parent_intf')
                continue

            # ES State: Up
            m = p3.match(line)
            if m:
                group = m.groupdict()
                es_state = group.pop('es_state').lower()
                continue

            # Port-channel state: N/A
            m = p4.match(line)
            if m:
                group = m.groupdict()
                po_state =  group.pop('po_state').lower()
                continue

            # NVE Interface: nve1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                nve_if_name = group.pop('nve_intf')
                esi_dict = result_dict.setdefault('nve', {}).setdefault(nve_if_name, {}).\
                                       setdefault('ethernet_segment', {}).setdefault('esi', {}).\
                                       setdefault(esi, {})
                esi_dict.update({
                    'esi': esi,
                    'nve_if_name': nve_if_name,
                    'po_state': po_state,
                    'if_name': if_name,
                    'es_state': es_state
                })
                continue

            # NVE State: Up
            m = p6.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'nve_state': group.pop('nve_state').lower()})
                continue

            # Host Learning Mode: control-plane
            m = p7.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'host_reach_mode': group.pop('host_learning_mode').lower()})
                continue

            # Active Vlans: 1,1001-2000,2501-2550,2601-2650,2701-2750,2801-2850,2901-2950
            m = p8.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'active_vlans': [i.strip() for i in group.pop('active_vlans').split(",")]})
                continue

            # DF Vlans: 1001,1004,1007,1010,1013,1016,1019,1022,1025,1028,1031,1034,1037,1040,1043,2948
            m = p9.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_vlans': [i.strip() for i in group.pop('df_vlans').split(",")]})
                continue

            # Active VNIs: 10001-10200,10501-11000,12501-13000,22001-22200,24001-24100
            m = p10.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'active_vnis': [i.strip() for i in group.pop('active_vnis').split(",")]})
                continue

            # DF BDs: 8193,8196,8199,8202,8205,8208,8211,8214,8217,8220,8223,8226,8229,8232,12998
            m = p11.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_bd_list': [i.strip() for i in group.pop('df_bds').split(",")]})
                continue

            # DF VNIs: 12551,12554,12557,12560,12563,12566,12569,12572,12575,12578,12581,12584,12587
            m = p12.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_vni_list': [i.strip() for i in group.pop('df_vnis').split(",")]})
                continue

            # Number of ES members: 3
            m = p13.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'num_es_mem': int(group.pop('num_es_mem'))})
                continue

            # My ordinal: 2
            m = p14.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'local_ordinal': int(group.pop('local_ordinal'))})
                continue

            # DF timer start time: 00:00:00
            m = p15.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_timer_st': group.pop('df_timer_start_time')})
                continue

            # Config State: N/A
            m = p16.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'config_status': group.pop('config_status').lower()})
                continue

            # DF List: 100:100:100::1 100:100:100::2 100:100:100::7
            m = p17.match(line)
            if m:
                group = m.groupdict()
                df_list_str = group.pop('df_list')
                if df_list_str == 'Empty':
                    esi_dict.update({'df_list': []})
                else:
                    esi_dict.update({'df_list': [i.strip() for i in df_list_str.split()]})
                continue

            # ES route added to L2RIB: True
            m = p18.match(line)
            if m:
                group = m.groupdict()
                esi_dict['es_rt_added'] = 'False' != group.pop('is_es_added_to_l2rib')
                continue

            # EAD/ES routes added to L2RIB: False
            m = p19.match(line)
            if m:
                group = m.groupdict()
                esi_dict['ead_rt_added'] = 'False' != group.pop('ead_rt_added')
                continue

            # ESI type: Ether-segment
            m = p20.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'esi_type': group.pop('esi_type')})
                continue

            # ESI DF election mode: Modulo
            m = p21.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'esi_df_election_mode': group.pop('esi_df_election_mode')})
                continue

        return result_dict
    
