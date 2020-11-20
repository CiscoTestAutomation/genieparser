from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ======================================================
# Schema for 'show vrrp'
# ======================================================

class ShowVrrpSchema(MetaParser):

    schema = {
        'interface': {
            Any(): {
                'group': {
                    int: {
                        Optional('auth_text'): str,
                        'advertise_interval_secs': float,
                        'master_advertisement_interval_secs': float,
                        'master_down_interval_secs': float,
                        'master_router_ip': str,
                        Optional('master_router'): str,
                        'master_router_priority': int,
                        'preemption': str,
                        'priority': int,
                        'virtual_ip_address': str,
                        'virtual_mac_address': str,
                        Optional('description'): str,
                        'state': str,
                        Optional('vrrp_delay'): float,
                        Optional('vrrs_name'): {
                            str: {
                                 Optional('track_object'): { 
                                    int: {
                                        Optional('decrement'): int,
                                        Optional('state'): str,
                                         }
                                        
                                                                  }
                                }
                                                    }
               

                    }
                }
            }
        }
    }


class ShowVrrp(ShowVrrpSchema):
    """Parser for show vrrp on IOS-XE
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = 'show vrrp'

    def cli(self, output=None):

        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Defines the regex for the first line of device output, which is:
        # Ethernet1/0 - Group 1
        p1 = re.compile(
            r'^(?P<interface>[\w,\/]+) - +Group (?P<grp_number>\d+)$')

        #State is Master
        p2 = re.compile(r'State is (?P<state>(Master|UP|Init))')

        # Virtual IP address is 10.2.0.10
        p3 = re.compile(r'^Virtual +IP +address is (?P<vir_ip>[\d,\.]+)')

        # Virtual MAC address is 0000.5e00.0101
        p4 = re.compile(
            r'^Virtual +MAC +address +is (?P<vir_mac_addr>[\w,\.]+)')

        # Advertisement interval is 3.000 sec
        p5 = re.compile(
            r'^Advertisement +interval +is (?P<advrt_int>[\w,\.]+) +sec')

        #Preemption is enabled
        p6 = re.compile(r'^Preemption +is (?P<state>\w+)')

        # Preemption enabled
        p7 = re.compile(r'^Preemption (?P<state>\w+)')

        # min delay is 0.000 sec
        p8 = re.compile(r'^min +delay +is (?P<delay>[\w,\.]+) +sec')

        #Priority is 115
        p9 = re.compile(r'^Priority +is (?P<priority>\w+)')

        # Priority 100
        p10 = re.compile(r'^Priority (?P<priority>\w+)')

        # VRRS Group name DC_LAN
        p11 = re.compile(r'^VRRS +Group +name (?P<vrrs_grp_name>[\w,\_]+)')

        # Track object 1 state down decrement 15
        p12 = re.compile(
            r'Track +object (?P<obj_name>\w+) +state (?P<obj_state>(Up|Down)) +decrement (?P<value>\w+)')

        # Authentication text "hash"
        p13 = re.compile(r'Authentication +text \"(?P<type>[\w,\"]+)\"')

        # Master Router is 10.2.0.1 (local), priority is 100
        p14 = re.compile(
            r'^Master +Router +is (?P<mast_ip_addr>[\w,\.]+) \((?P<server>\S+)\), +priority +is (?P<digit>\d+)')

        # Master Advertisement interval is 3.000 sec
        p15 = re.compile(
            r'^Master +Advertisement +interval +is (?P<mast_adv_interval>[\d,\.]+) +sec')

        # Master Down interval is 9.609 sec
        p16 = re.compile(
            r'^Master +Down +interval +is (?P<mast_down_interval>[\d,\.]+) +sec')

        # Master Router is 192.168.1.233, priority is 120
        p17 = re.compile(
            r'^Master +Router +is (?P<mast_ip_addr>[\w,\.]+)+, +priority +is (?P<digit>\d+)')

        # DC-LAN Subnet
        p18 = re.compile(r'(?P<vrrp_grp_name>[\w,\W]+)')

        for line in out.splitlines():

            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = (group['interface'])
                vrrp_grp = int(group['grp_number'])
                vrrp_dict = result_dict.setdefault('interface', {}).setdefault(
                    interface, {}).setdefault('group', {}).setdefault(vrrp_grp, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'state': str(group['state'])})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'virtual_ip_address': str(group['vir_ip'])})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'virtual_mac_address': str(group['vir_mac_addr'])})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'advertise_interval_secs': float(group['advrt_int'])})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'preemption': str(group['state'])})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'preemption': str(group['state'])})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'vrrp_delay': float(group['delay'])})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'priority': int(group['priority'])})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'priority': int(group['priority'])})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                vrf_group_name = group['vrrs_grp_name']
                vrf_dict = vrrp_dict.setdefault('vrrs_name',{}).setdefault(vrf_group_name,{})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                track_object_number = int(group['obj_name'])
                state = str(group['obj_state'])
                decrement = int(group['value'])
                vrp_obj_dict = vrf_dict.setdefault('track_object',{}).setdefault(track_object_number,{})
                vrp_obj_dict['decrement']= decrement
                vrp_obj_dict['state']= state
                continue
             
            m = p13.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update({'auth_text': str(group['type'])})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_router_ip': str(group['mast_ip_addr'])})
                vrrp_dict.update({'master_router': str(group['server'])})
                vrrp_dict.update(
                    {'master_router_priority': int(group['digit'])})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_advertisement_interval_secs': float(group['mast_adv_interval'])})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_down_interval_secs': float(group['mast_down_interval'])})
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'master_router_ip': str(group['mast_ip_addr'])})
                vrrp_dict.update(
                    {'master_router_priority': int(group['digit'])})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                vrrp_dict.update(
                    {'description': str(group['vrrp_grp_name'])})
                continue

        return result_dict
