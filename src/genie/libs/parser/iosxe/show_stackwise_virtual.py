import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional


# ===========================
# Schema for:
#  * 'show stackwise-virtual'
# ===========================
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


# ===========================
# Parser for:
#  * 'show stackwise-virtual'
# ===========================
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
