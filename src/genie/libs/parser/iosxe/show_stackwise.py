"""show_pstackwise.py
   supported commands:
     * 'show stackwise-virtual dual-active-detection'
     * 'show stackwise-virtual bandwidth'
     * 'show stackwise-virtual'
     * 'show stackwise-virtual switch {number} link'

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
        dad_dict = {'switches': {}}
        # Dual-Active-Detection Configuration:
        # -------------------------------------
        # Switch  Dad port                        Status
        # ------  ------------                    ---------
        # 1       FortyGigabitEthernet1/0/3       up
        #         FortyGigabitEthernet1/0/4       up
        # 2       FortyGigabitEthernet2/0/3       up
        #         FortyGigabitEthernet2/0/4       up
        #         p1 = re.compile(r"^(?P<switch_id>\d+)\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)
        #         p2 = re.compile(r"^\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)
        #

        dad_dict = {}

        # 1       FortyGigabitEthernet1/0/3       up
        switch_id_capture = re.compile(r"^(?P<switch_id>\d+)\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))",
                                         re.MULTILINE)
        #         FortyGigabitEthernet1/0/4       up
        port_capture = re.compile(r"^\s+(?P<dad_port>\S+)\s+(?P<status>(up|down))", re.MULTILINE)

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
            match = switch_id_capture.match(line)
            # 1       FortyGigabitEthernet1/0/3       up
            if not dad_dict.get('dad_port'):
                dad_dict['dad_port'] = {}
            if not dad_dict['dad_port'].get('switches'):
                dad_dict['dad_port']['switches'] = {}
            if match:
                groups = match.groupdict()
                switch_id = int(groups['switch_id'])
                dad_dict['dad_port']['switches'].update({switch_id: {groups['dad_port']: {'status': groups['status']}}})
            port_match = port_capture.match(line)
            #         FortyGigabitEthernet1/0/4       up
            if port_match:
                groups = port_match.groupdict()
                dad_dict['dad_port']['switches'][switch_id].update({groups['dad_port']: {'status': groups['status']}})
        return dad_dict


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

class ShowStackwiseVirtualLinkSchema(MetaParser):
    """Schema for show stackwise-virtual link"""

    schema = {
        'switch' : {
            Any():{
                'svl' : int,
                'ports' : str,
                'link_status' : str,
                'protocol_status' : str
            }
        }
    }

class ShowStackwiseVirtualLink(ShowStackwiseVirtualLinkSchema):
    """Parser for show stackwise-virtual link"""
  
    cli_command = 'show stackwise-virtual link'
    
    def cli(self, output=None):
        out = self.device.execute(self.cli_command) if output is None else output
        
        ret_dict = {}
        #                        1              1        HundredGigE1/1/0/13          U                        R
        pr = re.compile(r'^(?P<switch>\d+) + (?P<svl>\d+) +  (?P<ports>\S+) + (?P<link_status>\S+) + (?P<protocol_status>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            #                        1                 1        HundredGigE1/0/3          U                       R
            m =  pr.match(line)
            if m:
               group = m.groupdict()
               switch_dict = ret_dict.setdefault('switch', {})
               stackw_dict = switch_dict.setdefault(int(group['switch']),{})     
               stackw_dict.update({  
                    'svl': int(group['svl']),
                    'ports' : str(group['ports']),
                    'link_status' : str(group['link_status']),
                    'protocol_status' : str(group['protocol_status'])
                }) 
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
        port_capture = "(?P<port>\S+)"
        p_st_all = re.compile("{switch_capture}\s+{vlink_capture}\s+{port_capture}".format(switch_capture=switch_capture, vlink_capture=vlink_capture, port_capture=port_capture))

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

            elif p_st_all.match(line):
                match = p_st_all.match(line)
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
