"""show_pstackwise.py
   supported commands:
     * 'show stackwise-virtual dual-active-detection'
     * 'show stackwise-virtual dual-active-detection Pagp'
     * 'show stackwise-virtual bandwidth'
     * 'show stackwise-virtual'
     * 'show stackwise-virtual switch {number} link'
     * 'show stackwise-virtual link'
     * 'show stackwise-virtual neighbors'

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# =================================================
# Schema for:
#  * 'show_stackwise_virtual_dual_active_detection'
# =================================================
class ShowStackwiseVirtualDualActiveDetectionSchema(MetaParser):
    """Schema for show_stackwise_virtual_dual_active_detection."""

    schema = {
        Optional("in_dad_recovery"): str,
        Optional("recovery_reload"): str,
        Optional('recovery_mode_triggered_by'): str,
        Optional('triggered_Time'): str,
        "dad_port": {
            "switches": {
                int: {
                    str: {
                        "status": str
                    }
                }
            }
        }
    }


# =================================================
# Parser for:
#  * 'show_stackwise_virtual_dual_active_detection'
# =================================================
class ShowStackwiseVirtualDualActiveDetection(ShowStackwiseVirtualDualActiveDetectionSchema):
    """Parser for show stackwise-virtual dual-active-detection"""

    cli_command = 'show stackwise-virtual dual-active-detection'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        dad_dict = {}

        # In dual-active recovery mode: No
        p1 = re.compile(".*In\s+dual\-active\s+recovery\s+mode:\s+(?P<in_dad_recovery>\S+)")
        # Recovery mode triggered by: fast-hello
        p2 = re.compile(".*Recovery\s+mode\s+triggered\s+by\:\s+(?P<recovery_mode_triggered_by>\S+)")
        # Triggered Time: 06:07:37.000 UTC Tue Jan 25 2022
        p3 = re.compile(".*Triggered\s+Time\:\s+(?P<triggered_Time>.*)")
        # Recovery Reload: Enabled
        p4 = re.compile(".*Recovery\s+Reload:\s+(?P<recovery_reload>\S+)")
        # 1       FortyGigabitEthernet1/0/3       up
        p5 = re.compile(r"^(?P<switch_id>\d+)\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)
        #         FortyGigabitEthernet1/0/4       up
        p6 = re.compile(r"^\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if clean_line_strip.startswith(remove_lines):
                    clean_lines.remove(clean_line)
            return clean_lines

        remove_lines = ('----', 'Switch', 'Dual')
        out = filter_lines(raw_output=out, remove_lines=remove_lines)
        switch_id = ''

        for line in out:

            match1 = p1.match(line)
            if match1:
                dad_dict["in_dad_recovery"] = match1.group("in_dad_recovery")
                continue
            match2 = p2.match(line)
            if match2:
                dad_dict["recovery_mode_triggered_by"] = match2.group("recovery_mode_triggered_by")
                continue
            match3 = p3.match(line)
            if match3:
                dad_dict["triggered_Time"] = match3.group("triggered_Time")
                continue
            match4 = p4.match(line)
            if match4:
                dad_dict["recovery_reload"] = match4.group("recovery_reload")
                continue
            if not dad_dict.get('dad_port'):
                dad_dict['dad_port'] = {}
            if not dad_dict['dad_port'].get('switches'):
                dad_dict['dad_port']['switches'] = {}
            match5 = p5.match(line)
            if match5:
                groups = match5.groupdict()
                switch_id = int(groups['switch_id'])
                dad_dict['dad_port']['switches'].update({switch_id: {groups['dad_port']: {'status': groups['status']}}})
            match6 = p6.match(line)
            if match6:
                groups = match6.groupdict()
                dad_dict['dad_port']['switches'][switch_id].update({groups['dad_port']: {'status': groups['status']}})

        return dad_dict

# ===========================
# Schema for:
#  * 'show stackwise-virtual dual-active-detection Pagp'
# ===========================
class ShowStackwiseVirtualDualActiveDetectionPagpSchema(MetaParser):
    """Schema for show stackwise-virtual dual-active-detection pagp"""

    schema = {
		"pagp_dad_enabled": str,
        "in_dad_recovery": str,
        "recovery_reload": str,
        'channel_group': {
            int:{
                'port': {
                    str:{
                        "dad_capable": str,
                        "partner_name": str,
                        "partner_port": str,
                        "partner_version": str,
                    },
                },
            },
        },
        Optional("recovery_mode_triggered_by"): str,
        Optional("pagp_channel_group"): int,
        Optional("interface"): str,
        Optional("triggered_Time"): str,
        Optional("received_id"): str,
        Optional("expected_id"): str,
    }

# =================================================
# Parser for:
#  * 'show_stackwise_virtual_dual_active_detection Pagp'
# =================================================
class ShowStackwiseVirtualDualActiveDetectionPagp(ShowStackwiseVirtualDualActiveDetectionPagpSchema):
    """Parser for show stackwise-virtual dual-active-detection Pagp"""

    cli_command = ["show stackwise-virtual dual-active-detection pagp"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            out = output

        # Pagp dual-active detection enabled: Yes
        p1 = re.compile("^Pagp\s+dual\-active\s+detection\s+enabled\:\s+(?P<pagp_dad_enabled>\S+)$")
        # In dual-active recovery mode: No
        p2 = re.compile("^In\s+dual\-active\s+recovery\s+mode:\s+(?P<in_dad_recovery>\S+)$")
        # Triggered by: e-pagp
        p3 = re.compile("^Triggered\s+by\:\s+(?P<recovery_mode_triggered_by>\S+)$")
        # Triggered on group 1, Interface: Hu1/0/11
        p4 = re.compile("^Triggered\s+on\s+group\s+(?P<channel_group>\d+)\,\s+Interface\:\s+(?P<interface>\S+)")
        # Triggered Time: 06:07:37.000 UTC Tue Jan 25 2022
        p5 = re.compile("^Triggered\s+Time\:\s+(?P<triggered_Time>.*)$")
        # Received id: f87a.4137.a600
        p6 = re.compile("^Received\s+id\:\s+(?P<received_id>.*)$")
        # Expected id: f87a.4137.9e00
        p7 = re.compile("^Expected\s+id\:\s+(?P<expected_id>.*)$")
        # Recovery Reload: Enabled
        p8 = re.compile("^Recovery\s+Reload:\s+(?P<recovery_reload>\S+)$")
        # Channel group 1
        p9 = re.compile("^Channel\s+group\s+(?P<channel_group>\d+)$")
		# Hu1/0/11    Yes             Nyquist-Peer-1       Fo1/1/1       1.1
        p10 = re.compile("^(?P<port>\S+)\s+(?P<status>\S+)\s+(?P<partner_name>\S+)\s+(?P<partner_port>\S+)\s+(?P<partner_version>\S+)$")

        channel_group = ''
        pagp_dad_obj = {}

        for line in output.splitlines():
            line = line.strip()
            # remove headers
            if re.search(r"\s+Dual\-Active\s+Partner\s+Partner\s+Partner.*", line):
                continue
            # remove headers
            if re.search(r"Port\s+Detect\s+Capable\s+Name\s+Port\s+Version.*", line):
                continue

            match1 = p1.match(line)
            if match1:
                pagp_dad_obj["pagp_dad_enabled"] = match1.group("pagp_dad_enabled")
                continue
            match2 = p2.match(line)
            if match2:
                pagp_dad_obj["in_dad_recovery"] = match2.group("in_dad_recovery")
                continue
            match3 = p3.match(line)
            if match3:
                pagp_dad_obj["recovery_mode_triggered_by"] = match3.group("recovery_mode_triggered_by")
                continue
            match4 = p4.match(line)
            if match4:
                pagp_dad_obj["pagp_channel_group"] = int(match4.group("channel_group"))
                pagp_dad_obj["interface"] = match4.group("interface")
                continue
            match5 = p5.match(line)
            if match5:
                pagp_dad_obj["triggered_Time"] = match5.group("triggered_Time")
                continue
            match6 = p6.match(line)
            if match6:
                pagp_dad_obj["received_id"] = match6.group("received_id")
                continue
            match7 = p7.match(line)
            if match7:
                pagp_dad_obj["expected_id"] = match7.group("expected_id")
                continue
            match8 = p8.match(line)
            if match8:
                pagp_dad_obj["recovery_reload"] = match8.group("recovery_reload")
                continue
            match9 = p9.match(line)
            if match9:
                pagp_dad_obj['channel_group'] = {}
                channel_group = int(match9.group("channel_group"))
                pagp_dad_obj['channel_group'][channel_group] = {}
                pagp_dad_obj['channel_group'][channel_group]['port'] = {}
            if channel_group != '':
                match10 = p10.match(line)
                if match10:
                    port = match10.group("port")
                    pagp_dad_obj['channel_group'][channel_group]['port'][port] = {}
                    if port:
                        pagp_dad_obj['channel_group'][channel_group]['port'][port].update({ "dad_capable": match10.group("status")})
                        pagp_dad_obj['channel_group'][channel_group]['port'][port].update({ "partner_name": match10.group("partner_name")})
                        pagp_dad_obj['channel_group'][channel_group]['port'][port].update({ "partner_port": match10.group("partner_port")})
                        pagp_dad_obj['channel_group'][channel_group]['port'][port].update({ "partner_version": match10.group("partner_version")})
                    continue
                else:
                    continue

        return pagp_dad_obj


class ShowStackwiseVirtualBandwidthSchema(MetaParser):
    """
    Schema for show stackwise-virtual bandwidth
    """
    schema = {
        'switch': {
            int: {
                'bandwidth': str,
            }
        }
    }


class ShowStackwiseVirtualBandwidth(ShowStackwiseVirtualBandwidthSchema):
    """ Parser for show stackwise-virtual bandwidth"""

    cli_command = 'show stackwise-virtual bandwidth'

    def cli(self, output=None):
        # excute command to get output
        if not output:
            output = self.device.execute(self.cli_command)

        # initial variables
        ret_dict = {}

        # 1        200G
        p1 = re.compile('^(?P<switch>\d+)\s+(?P<bandwidth>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # 1        200G
            m = p1.match(line)
            if m:
                group = m.groupdict()
                root_dict = ret_dict.setdefault('switch',{}).setdefault(int(group['switch']),{})
                root_dict['bandwidth'] = group['bandwidth']
                continue

        return ret_dict

      
class ShowStackwiseVirtualSchema(MetaParser):
    """Schema for show stackwise-virtual."""

    schema = {
        "domain": int,
        "enabled": bool,
        Optional("switches"): {
            int: {
            Optional("stackwise_virtual_link"): {
                int: {
                  "ports": list,
              },
            },
          }
        },
    }


class ShowStackwiseVirtual(ShowStackwiseVirtualSchema):
    """Parser for show stackwise-virtual"""

    cli_command = ["show stackwise-virtual"]

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output = output

        # Stackwise Virtual Configuration:
        # --------------------------------
        # Stackwise Virtual : Enabled
        # Domain Number : 1
        #
        # Switch  Stackwise Virtual Link  Ports
        # ------  ----------------------  ------
        # 1       1                       TenGigabitEthernet1/0/47
        #                                 TenGigabitEthernet1/0/48
        # 2       1                       TenGigabitEthernet2/0/47
        #                                 TenGigabitEthernet2/0/48

        # Stackwise Virtual : Enabled
        enabled_capture = "(?P<enabled>Enabled|Disabled)"
        p_enabled = re.compile("Stackwise\s+Virtual\s+:\s+{enabled_capture}".format(enabled_capture=enabled_capture))

        # Domain Number : 100
        domain_capture = "(?P<domain>\d+)"
        p_domain = re.compile("Domain\s+Number\s+:\s+{domain_capture}".format(domain_capture=domain_capture))

        # 1       1                       TenGigabitEthernet1/0/47"
        switch_capture = "(?P<switch>\d+)"
        vlink_capture = "(?P<vlink>\d+)"
        p6 = "(?P<port>\S+)"
        p10 = re.compile("{switch_capture}\s+{vlink_capture}\s+{p6}".format(switch_capture=switch_capture, vlink_capture=vlink_capture, p6=p6))

        #                                 TenGigabitEthernet1/0/47"
        p_st_int = re.compile("\s{10,}(?P<port>\S+)\s*$")

        stackwise_obj = {}
        for line in output.splitlines():

            # remove headers and empty lines
            if re.search(r"^\s*$", line) or line.startswith("-----"):
                continue

            # remove erroneous line
            elif re.search(r"Stackwise\s+Virtual\s+Configuration:", line):
                continue

            # remove headers
            elif re.search(r"Switch\s+Stackwise\s+Virtual\s+Link\s+Ports", line):
                continue

            elif p_enabled.match(line):
                match = p_enabled.match(line)
                enabled = True if match.group("enabled") == "Enabled" else False
                stackwise_obj["enabled"] = enabled
                continue

            elif p_domain.match(line):
                match = p_domain.match(line)
                stackwise_obj["domain"] = int(match.group("domain"))
                continue

            elif p10.match(line):
                match = p10.match(line)
                switch = int(match.group("switch"))
                port = match.group("port")
                vlink = match.group("vlink")
                if not stackwise_obj.get("switches"):
                    stackwise_obj["switches"] = {}
                stackwise_obj["switches"].update({switch: {"stackwise_virtual_link": { int(vlink): { "ports": [port]}}}})
                continue

            elif p_st_int.match(line):
                match = p_st_int.match(line)
                port = match.group("port")
                stackwise_obj["switches"][switch]["stackwise_virtual_link"][int(vlink)]["ports"].append(port)
                continue

        return stackwise_obj


class ShowStackwiseLinkSchema(MetaParser):
    """Schema for show stackwise-virtual switch 1 link."""

    schema = {
       'svl_info': {
           Any(): {
               'switch': int,
               'svl': int,
               'ports': str,
               'link_status': str,
               'protocol_status': str
           }
       }
    }


class ShowStackwiseLink(ShowStackwiseLinkSchema):
    """Parser for show stackwise-virtual switch 1 link"""

    cli_command = ["show stackwise-virtual switch {number} link"]

    def cli(self, number="", output=None):
        if output is None:
            # get output from device
            output = self.device.execute(self.cli_command[0].format(number=number))

        # initial return dictionary
        ret_dict = {}
        index = 0

        # initial regexp pattern
        # Switch SVL Ports Link-Status Protocol-Status
        # ------ --- ----- ----------- ---------------
        # 1 1 HundredGigE1/0/26 U R
        p1 = re.compile(r'^(?P<switch>\d+)+\s+(?P<SVL>\d+)+\s+(?P<port>\S+)+\s+(?P<link_status>\w+)+\s+(?P<protocol_status>\w+)$')

        for line in output.splitlines():
            line = line.strip()

            # Last configuration file parsed
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index += 1
                svl_info = ret_dict.setdefault('svl_info', {}).setdefault(index, {})
                svl_info.update({'switch': int(group['switch'])})
                svl_info.update({'svl': int(group['SVL'])})
                svl_info.update({'ports': group['port']})
                svl_info.update({'link_status': group['link_status']})
                svl_info.update({'protocol_status': group['protocol_status']})
                continue

        return ret_dict

class ShowStackwiseVirtualLinkSchema(MetaParser):
    """Schema for show stackwise-virtual link"""

    schema = {
        'switch':{
                int:{
                    'svl':{
                        int:{
                            Optional('ports'):{
                                Any():{
                                    'link_status':str,
                                    'protocol_status':str,
                                }
                            }
                        }
                    }    
                }
            }
        }

class ShowStackwiseVirtualLink(ShowStackwiseVirtualLinkSchema):
    """Parser for show stackwise-virtual link"""
 
    cli_command = 'show stackwise-virtual link'
   
    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output
       
        ret_dict = {}
        #                        1              1         HundredGigE1/0/1                U               P
        #                                                 HundredGigE1/0/6                U               P        
        p1 = re.compile(r'^(?P<switch>\d+) +(?P<svl>\d+) +(?P<ports>\S+) +(?P<link_status>\S+) +(?P<protocol_status>\S+)$')
        p2 = re.compile(r'^(?P<ports>\S+) +(?P<link_status>\S+) +(?P<protocol_status>\S+)$')

        for line in out.splitlines():
            line = re.sub('\t', '   ', line)
            line = line.strip()
            #                       1       1       HundredGigE1/0/1                U               P
            #                                       HundredGigE1/0/6                U               P
            m =  p1.match(line)
            if m:
               group = m.groupdict()
               #svl_port_dict = ret_dict.setdefault('svl_port', {})
               switches_dict = ret_dict.setdefault('switch',{})  
               switch_id_dict = switches_dict.setdefault(int(group['switch']),{})
               svl_dict = switch_id_dict.setdefault('svl',{})
               svl_id_dict = svl_dict.setdefault(int(group['svl']),{})
               port_dict = svl_id_dict.setdefault('ports',{})
               port_id_dict = port_dict.setdefault(str(group['ports']),{})
               port_id_dict.update({  
                    'link_status' : str(group['link_status']),
                    'protocol_status' : str(group['protocol_status'])
                })
               continue
            m =  p2.match(line)
            if m:
                group = m.groupdict()
                #    port_dict = svl_id_dict.setdefault('ports',{})
                port_id_dict = port_dict.setdefault(str(group['ports']),{})
                port_id_dict.update({  
                        'link_status' : str(group['link_status']),
                        'protocol_status' : str(group['protocol_status'])
                    })
                continue
        return ret_dict
      
class ShowStackwiseVirtualNeighborsSchema(MetaParser):
    '''Schema for show stackwise-virtual neighbors '''

    schema = {
        'switch':{
            int:{ 
                'svl':{  
                    int:{  
                        'local_port':{
                            str:{
                                'remote_port':str
                            }
                        }
                    }
                }
            }
        }
    }

class ShowStackwiseVirtualNeighbors(ShowStackwiseVirtualNeighborsSchema):   
    '''Parser for show stackwise-virtual neighbors'''

    cli_command = 'show stackwise-virtual neighbors'

    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output

        ret_dict = {}

        # 1               1          HundredGigE1/1/0/19     HundredGigE2/1/0/23              
        p1 = re.compile(r'^(?P<switch>\d+)\s+(?P<svl>\d+)\s+(?P<local_port>[\w/]+)\s+(?P<remote_port>[\w/]+)$')
        # HundredGigE1/5/0/17     HundredGigE2/1/0/24 
        p2 = re.compile(r'^(?P<local_port>[\w/]+)\s+(?P<remote_port>[\w/]+)$')        
        # FiftyGigE1/6/0/33   
        p3 = re.compile(r'^(?P<local_port>[\w/]+)$')

        for line in out.splitlines():
            line = re.sub('\t', '   ', line)
            line = line.strip()
            # 1               1          HundredGigE1/1/0/19     HundredGigE2/1/0/23                
            m =  p1.match(line)
            if m:
               group = m.groupdict()
               switches_dict = ret_dict.setdefault('switch',{})  
               switch_id_dict = switches_dict.setdefault(int(group['switch']),{})
               svl_dict = switch_id_dict.setdefault('svl',{}) 
               svl_id_dict = svl_dict.setdefault(int(group['svl']),{})
               lo_port_dict = svl_id_dict.setdefault('local_port',{})
               lo_port_id_dict = lo_port_dict.setdefault(str(group['local_port']),{})
               lo_port_id_dict['remote_port'] = group['remote_port']
               continue
            # HundredGigE1/5/0/17     HundredGigE2/1/0/24 
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lo_port_id_dict = lo_port_dict.setdefault(str(group['local_port']),{})
                lo_port_id_dict['remote_port'] = group['remote_port']
                continue
            # FiftyGigE1/6/0/33  
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lo_port_id_dict = lo_port_dict.setdefault(str(group['local_port']),{})
                lo_port_id_dict['remote_port'] = str(None)
                continue
        return ret_dict
