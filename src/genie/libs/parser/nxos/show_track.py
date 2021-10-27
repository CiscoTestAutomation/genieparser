"""show_track.py
NXOS parser for the following show commands:
* 'show track'
"""

import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# =======================
# Schema for 'show track'
# =======================
class ShowTrackSchema(MetaParser):
    """ Schema for:
       * 'show track' 
       * 'show track {id}' 
    """
    schema = {
        'track': {
            Any(): {
                Optional('type') : str,
                Optional('instance'): str,
                Optional('address'): str,
                'state': str,
                Optional('secs_remaining'): float,
                Optional('sublist') : str,
                Optional('subtrack') : str,
                'change_count': int,
                'last_change': str,
                Optional('threshold_down'): str,
                Optional('threshold_up'): str,
                Optional('tracked_by'): {
                    Optional(Any()): {   #increasing index 0, 1, 2, 3, ...
                        Optional('name'): str,
                        Optional('interface'): str,
                        Optional('id'): str,
                     }
                },
                Optional('track_list_members'):{
                    Optional(Any()): {
                        Optional('object_id') : str,
                        Optional('weight') : str,	
                        Optional('percentage') : str,
                        Optional('obj_state') : str,
                    }
                },
                Optional('delay_up_secs'): float,
                Optional('delay_down_secs'): float,
                Optional('delay_up_millisecs'): float,
                Optional('delay_down_millisecs'): float,
                Optional('VPN_vrf_Routing'): str,
            },
        },
    }


# =======================
# Parser for 'show track'
# =======================
class ShowTrack(ShowTrackSchema):
    """ Parser for 'show track' 'show track {id}'"""

    cli_command = [
        'show track',
        'show track {track_id}'
    ]

    def cli(self, track_id = ' ', output=None):
        if output is None:
            if track_id:
               cmd = self.cli_command[1].format(track_id=track_id)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        #Init vars
        parsed_dict = {}
       
        #Track N 
        p0 = re.compile(r'Track (?P<track_id>\d+)') 

        # Interface Ethernet1/4 IP Routing
        # IP Route 10.1.1.1/32 Reachability
        # IPv6 Route 10:1::1:1/32 Reachability
        # IP SLA 121 Reachability
        p1 = re.compile(r'^(?P<type>IP Route|Interface|IP SLA|IPv6 Route|List)\s+((?P<address>[\d.]+(\/\d+))|(?P<name>([\d\w.:]+()\/\d+|loopback[\d]+|\d+)))*\s+((?P<parameter>[\w \-]+))')

        # IP Routing is DOWN
        # Line Protocol is delayed DOWN (20 secs remaining)
        p2 = re.compile(r'^(?P<parameter>[\w ]+) +is +(?P<state>UP|DOWN|delayed DOWN|delayed UP)( \((?P<secs_remaining>\d+) secs remaining\))*')

        # 1 changes, last change 00:01:04
        p3 = re.compile(r'^(?P<change_count>\d+) +changes, +last +change'
                        r' +(?P<last_change>[\d\w:]+)')
   
        # Threshold weight up 20 down 10
        # Threshold percentage up 20% down 10%
        p4  = re.compile(r'^(?P<parameter>[\w ]+) +up +(?P<threshold_up>[\d]+%*) +down +(?P<threshold_down>[\d]+%*)')

        # Track List  12
        # VRRPV3 Vlan2 2
        # HSRP Vlan2 2   
        p5 = re.compile(r'^((?P<name>[a-zA-Z3]{3,6}) +'
            r'(?P<interface>[A-Za-z0-9\/.]{3,}) +(?P<group_id>\d+))|(?P<route>Route Map Configuration)')

        # Delay up 20 secs, down 10 secs
        # Delay up 10000 milliseconds, down 10000 milliseconds 
        p6 = re.compile(r'^(Delay )(up (?P<delay_up_secs>[\d]+\s+)secs,*)*(up (?P<delay_up_millisecs>[\d]+\s+)milliseconds,)*(\s*down (?P<delay_down_secs>[\d]+) secs)*( down (?P<delay_down_millisecs>[\d]+) milliseconds)*')

        # object 10 weight 10 UP
        # object 1 (100%) DOWN
        p7 = re.compile(r'^(object)\s+(?P<object_id>[\d]+)\s(weight (?P<weight>[\d]+))*((?P<percent>\([\d%]+\)))*\s*(?P<obj_state>[\w \-]+)')

        # VPN Routing/Forwarding table "management"
        # VPN Routing/Forwarding table "vrf2"
        p8 = re.compile(r'^(VPN Routing\/Forwarding table )\"(?P<vrf_table>[\w]+)')

        for line in output.splitlines():
            line = line.strip()
            
            #Track n   
            m = p0.match(line)
            if m:
               group = m.groupdict()
               type_dict1 = parsed_dict.setdefault('track', {})
               track_id1 = group['track_id']
               type_dict = type_dict1.setdefault(track_id1,{})
               continue

            # Interface Ethernet1/4 IP Routing
            # IP Route 10.1.1.1/32 Reachability
            # IPv6 Route 10:1::1:1/32 Reachability
            # IP SLA 121 Reachability 
            m = p1.match(line)
            if m:
               group = m.groupdict()
               type_name = group['type']
               if group['type']:
                    type_dict['type'] = group['type']
               if group['name']:
                    type_dict['instance'] = group['name']
               if group['address']:
                    type_dict['address'] = group['address']
               continue

            # IP Routing is DOWN
            # Line Protocol is delayed DOWN (20 secs remaining)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if type_dict['type'] == 'List':
                   str1 = (group['parameter']).split()
                   sublist = str1[-1]
                   type_dict['sublist'] = sublist
                else:
                   type_dict['subtrack'] = group['parameter']

                type_dict['state'] = group['state']
                if group['secs_remaining']:
                   type_dict['secs_remaining'] = float(group['secs_remaining'])
                continue

            # 1 changes, last change 00:01:04 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                type_dict['change_count'] = int(group['change_count'])
                type_dict['last_change'] = group['last_change']
                continue

            # Threshold weight up 20 down 10
            # Threshold percentage up 20% down 10%
            m = p4.match(line)
            if m:
               group = m.groupdict()
               if group['threshold_down']:
                    type_dict['threshold_down'] = group['threshold_down']
               if group['threshold_up']:
                    type_dict['threshold_up'] = group['threshold_up']
               continue

            # Track List  12
            # VRRPV3 Vlan2 2
            # HSRP Vlan2 2
            m = p5.match(line)
            if m:
                group = m.groupdict()
                tracked_by_dict = type_dict.setdefault('tracked_by', {})
                tracker_index = len(tracked_by_dict) + 1
                tracker_dict = tracked_by_dict.setdefault(tracker_index, {})
                if group['route']:
                   tracker_dict['name'] = group['route']
                elif group['name'] == 'Track':
                   tracker_dict['name'] = group['name']+group['interface']
                   if group['group_id']:
                      tracker_dict['id'] = group['group_id']
                else:
                   tracker_dict['name'] = group['name']
                   if group['interface']:
                      tracker_dict['interface'] = group['interface']
                   if group['group_id']:
                      tracker_dict['id'] = group['group_id']
                continue


            # Delay up 20 secs, down 10 secs
            # Delay up 10000 milliseconds, down 10000 milliseconds
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if group['delay_up_secs']:
                   type_dict['delay_up_secs'] = float(group['delay_up_secs']) 
                if group['delay_down_secs']:
                   type_dict['delay_down_secs'] = float(group['delay_down_secs'])
                if group['delay_up_millisecs']:
                   type_dict['delay_up_millisecs'] = float(group['delay_up_millisecs'])
                if group['delay_down_millisecs']:
                   type_dict['delay_down_millisecs'] = float(group['delay_down_millisecs'])
                continue

            # object 10 weight 10 UP
            # object 1 (100%) DOWN
            m = p7.match(line)
            if m:
               group = m.groupdict()
               track_list_members_dict = type_dict.setdefault('track_list_members', {})
               tracker_list_index = len(track_list_members_dict) + 1
               track_list_dict = track_list_members_dict.setdefault(tracker_list_index,{})
               track_list_dict['object_id'] = group['object_id']
               if group['weight']:
                  track_list_dict['weight'] = group['weight']
               if group['percent']:
                  track_list_dict['percentage'] = group['percent']
               if group['obj_state']:
                  track_list_dict['obj_state'] = group['obj_state']
               continue
  
            # VPN Routing/Forwarding table "management"
            # VPN Routing/Forwarding table "vrf2"    
            m = p8.match(line)
            if m:
               group = m.groupdict()
               if group['vrf_table']:
                  type_dict['VPN_vrf_Routing'] = group['vrf_table']
               continue   

        return parsed_dict


# =======================
# Schema for 'show track brief'
# =======================
class ShowTrackBriefSchema(MetaParser):
  """ Schema for :
      * 'show track brief' 
      * 'show track interface brief'
      * 'show track ip route brief'
      * 'show track ipv6 route brief'
      * 'show track ip sla brief'
      * 'show track list boolean and brief'
      * 'show track list boolean or brief'
      * 'show track list threshold percentage brief'
      * 'show track list threshold weight brief'
  """
  schema = {
        'track':{
            Any():{ 
                'tracktype': str,
                'instance': str,
                'parameter': str,
                'state': str,
                'last_change': str
            },
        }
    }


# ===================================
# Parser for:
#   * 'show track brief'
#   * 'show track interface brief'
#   * 'show track ip route brief'
#   * 'show track ipv6 route brief'
#   * 'show track ip sla brief'
# ===================================
class ShowTrackBrief(ShowTrackBriefSchema):
   """ Parser for:
       * 'show track brief'
       * 'show track interface brief'
       * 'show track ip route brief'
       * 'show track ipv6 route brief'
       * 'show track ip sla brief'
   """
   cli_command = [
      'show track brief',
      'show track {track_type} brief'
   ]

   def cli(self, track_type = '', output=None):
       if not output:
          if track_type:
             cmd = self.cli_command[1].format(track_type = track_type)
          else:
             cmd = self.cli_command[0]
          output = self.device.execute(cmd)
       else:
          output = output 

       track_table_dict = {}
       result_dict = {}

       #Track Type       Instance                 Parameter         State    Last Change
       #1     Interface    Ethernet1/4         IP Routing             DOWN    1w2d
       #2     Interface    Ethernet1/2         IPv6 Routing           DOWN    1w2d
       #3     Interface    Ethernet1/3         Line Protocol          DOWN    1w2d
       #4     IP Route     10.1.1.1/32         Reachability           DOWN    1w1d
       #5     IP SLA       121                 Reachability           DOWN    1w1d
       #6     IP SLA       120                 State                  DOWN    1w1d
       #7     IPv6 Route   10:1::1:1/32        Reachability           DOWN    1w1d
       #8     IPv6 Route   10:1::1:2/32        Reachability           DOWN    1w1d
       #9     List         -----               Boolean and            DOWN    never
       #10    List         -----               Boolean or             UP      1w0d
       #11    List         -----               Threshold percentage   DOWN    1w0d
       #12    List         -----               Threshold weight       DOWN    1w0d
       #13    Interface    loopback1           Line Protocol          DOWN    1w0d
       #20    Interface    loopback200         IP Routing             DOWN    1d10h
       #21    Interface    loopback0           IP Routing             DOWN    1d10h

       p1 = re.compile(r'(?P<trc>\d+)\s+(?P<typ> (Interface|IP Route|IP SLA|IPv6 Route|List))\s+(?P<inst>([\d\w.|:]+()\/\d+|[\d]+|[\w-]+))\s+(?P<par>((IP|IPv6)\sRouting|Reachability|State|Boolean(\sand|\sor)|Threshold(\spercentage|\sweight)|Line Protocol))\s+(?P<ste>[\w]+)\s+(?P<chg>[\w]+)')
  
       for line in output.splitlines():
          line = line.strip()

          m = p1.match(line)
          if m:
             group = m.groupdict()
             track_number = group['trc']
             result_dict = track_table_dict.setdefault('track', {}).setdefault(track_number, {})
             result_dict['tracktype'] = group['typ']
             result_dict['instance'] = group['inst']
             result_dict['parameter'] = group['par']
             result_dict['state'] = group['ste']
             result_dict['last_change'] = group['chg']
             continue
             
       return track_table_dict

# ===================================================
# Parser for:
#    * 'show track list boolean and brief'
#    * 'show track list boolean or brief'
#    * 'show track list threshold percentage brief'
#    * 'show track list threshold weight brief'
# ===================================================
class ShowTrackListBrief(ShowTrackBrief):
    """ parser for :
        * 'show track list boolean and brief'
        * 'show track list boolean or brief'
        * 'show track list threshold percentage brief'
        * 'show track list threshold weight brief'
    """
    cli_command = [
        'show track list {sub_type} brief'
    ]

    def cli(self, sub_type='', output=None):
       if not output:
          if sub_type:
             cmd = self.cli_command[0].format(sub_type = sub_type)
             output = self.device.execute(cmd)
       else:
          output = output

       return super().cli(output = output)
