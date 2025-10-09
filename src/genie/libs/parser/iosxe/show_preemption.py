import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.libs.parser.utils.common import Common

# =============================
# Schema for:
#  * 'show preemption summary'
# =============================
class ShowPreemptionSummarySchema(MetaParser):
    """Schema for show preemption Summary"""
    schema = {
        "interfaces": {
            Any() : {
                "preemption_supported": str,
                "preemption_configured": str,
                "preemption_operational": str,
            }
        }   
    }


# =============================
# Parser for:
#  * 'show preemption summary'
# =============================
class ShowPreemptionSummary(ShowPreemptionSummarySchema):
    """Parser for show preemption Summary
    show preemption summary 
 
    ------------------------------------------------------------------------------------------
    Interface       Preemption Supported      Premption Configured      Preemption Operational
    ------------------------------------------------------------------------------------------
    Gi1/1           yes                       no                        no                       
    Gi1/2           yes                       no                        no                       
    Gi1/3           yes                       no                        no                       
    Gi1/4           yes                       no                        no                       
    Gi1/5           yes                       no                        no                       
    Gi1/6           yes                       no                        no                       
    Gi1/7           yes                       no                        no                       
    Gi1/8           yes                       no                        no                       
    Gi1/9           yes                       no                        no                       
    Gi1/10          yes                       no                        no                       
    Gi1/11          yes                       no                        no                       
    Ap1/1           no                        --                        --                       
    Gi2/1           yes                       no                        no                       
    Gi2/2           yes                       no                        no                       
    Gi2/3           yes                       no                        no                       
    Gi2/4           yes                       no                        no                       
    Gi2/5           yes                       no                        no                       
    Gi2/6           yes                       no                        no                       
    Gi2/7           yes                       no                        no                       
"""
    cli_command = ['show preemption summary']

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0])
        else:
            output=output

        # Matches interface name, preemption supported, configured and operational
        # Interface       Preemption Supported      Premption Configured      Preemption Operational
        p_preemption_summ= re.compile(r"^(?P<interface>\w+\/\d+\/?\d*)\s+(?P<p_supp>\w+|-+)\s+(?P<p_conf>\w+|-+)\s+(?P<p_oper>\w+|-+)\s*$")

        result_dict = {}
        interface_dict = {}

        ## Iterating through the output and populating the dictionary with the interface name as the key
        ## and values as preemption supported, configured and operational
        for line in output.splitlines():
            line = line.strip()
            
            ## Match the line with the regex for interface name, preemption supported, 
            ## configured and operational
            ## Eg: Gi1/1           yes                     no                      no
            match = p_preemption_summ.match(line)

            if match:
                result_dict = interface_dict.setdefault("interfaces", {})
                
                # convert interface to full name
                interface = Common.convert_intf_name(match.groupdict()["interface"])

                result_dict[interface] = {
                    "preemption_supported": match.groupdict()["p_supp"],
                    "preemption_configured": match.groupdict()["p_conf"],
                    "preemption_operational": match.groupdict()["p_oper"],
                }
        return interface_dict
    
