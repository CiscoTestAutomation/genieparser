import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ==============================
# Schema for:
#  * 'show wireless cts summary'
# ==============================
class ShowWirelessCtsSummarySchema(MetaParser):
    """Schema for show wireless cts summary."""

    schema = {
        "local_mode_cts_configuration": {
            "policy_profile_name": {
                Optional(Any()): {
                    Optional("sgacl_enforcement"): str,
                    Optional("inline-tagging"): str,
                    Optional("default_sgt"): int
                }
            }
        },
        "flex_mode_cts_configuration": {
            "policy_profile_name": {
                Optional(Any()): {
                    Optional("sgacl_enforcement"): str,
                    Optional("inline-tagging"): str
                }
            }
        } 
    }


# ==============================
# Parser for:
#  * 'show wireless cts summary'
# ==============================
class ShowWirelessCtsSummary(ShowWirelessCtsSummarySchema):
    """Parser for show wireless cts summary"""

    cli_command = 'show wireless cts summary'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        else:
            output=output

        #Local Mode CTS Configuration
        #
        #Policy Profile Name               SGACL Enforcement     Inline-Tagging   Default-Sgt      
        #----------------------------------------------------------------------------------------
        #wip-b60                        DISABLED              DISABLED         0                
        #wip-b70                        DISABLED              DISABLED         0                
        #wip-b80                        DISABLED              DISABLED         0                
        #lizzard_b60                    DISABLED              DISABLED         0                
        #lizzard_b70                    DISABLED              DISABLED         0                
        #lizzard_b80                    DISABLED              DISABLED         0                
        #internet-b60                    DISABLED              DISABLED         0                
        #internet-b70                    DISABLED              DISABLED         0                
        #internet-b80                    DISABLED              DISABLED         0                
        #lizzard_b70_1                  DISABLED              DISABLED         0                
        #lizzard_b70_6                  DISABLED              DISABLED         0                
        #lizzard_b70_8                  DISABLED              DISABLED         0                
        #lizzard_b80_0                  DISABLED              DISABLED         0                
        #lizzard_b80_1                  DISABLED              DISABLED         0                
        #lizzard_b80_2                  DISABLED              DISABLED         0                
        #lizzard_b80_3                  DISABLED              DISABLED         0                
        #lizzard_b80_4                  DISABLED              DISABLED         0                
        #lizzard_b80_5                  DISABLED              DISABLED         0                
        #lizzard_b80_6                  DISABLED              DISABLED         0                
        #lizzard_b80_7                  DISABLED              DISABLED         0                
        #lizzard_b80_8                  DISABLED              DISABLED         0                
        #lizzard_b60_1_2                DISABLED              DISABLED         0                
        #lizzard_b70_3_4                DISABLED              DISABLED         0                
        #lizzard_b70_5_6                DISABLED              DISABLED         0                
        #lizzard_b70_7_8                DISABLED              DISABLED         0                
        #
        #
        #Flex Mode CTS Configuration
        #
        #Flex Profile Name                 SGACL Enforcement     Inline-Tagging   
        #-----------------------------------------------------------------------
        #default-flex-profile              DISABLED              DISABLED         
        #
        #
        #Local Mode CTS Configuration
        #
        #Policy Profile Name               SGACL Enforcement     Inline-Tagging   Default-Sgt      
        #----------------------------------------------------------------------------------------
        #lizzard_b60_3_4_5              DISABLED              DISABLED         0                
        #default-policy-profile            DISABLED              DISABLED         0                
        #lizzard_b60_cafeteria          DISABLED              DISABLED         0                
        #lizzard_b70_cafeteria          DISABLED              DISABLED         0                
        #internet-b70-launchpad          DISABLED              DISABLED         0                
        #lizzard_b70_eventcenter        DISABLED              DISABLED         0                
        #
        #
        #Flex Mode CTS Configuration

        # Local Mode CTS Configuration
        p_local = re.compile(r"Local\s+Mode\s+CTS\s+Configuration$")

        # Policy Profile Name               SGACL Enforcement     Inline-Tagging   Default-Sgt 
        p_local_header = re.compile(r"^Policy\s+Profile\s+Name\s+SGACL\s+Enforcement\s+Inline-Tagging\s+Default-Sgt$")

        # ----------------------------------------------------------------------------------------
        p_hyphen_delimiter = re.compile(r"^-+$")

        # wip-b60                        DISABLED              DISABLED         0
        p_local_policy = re.compile(r"^(?P<name>\S+)\s+(?P<sgacl>\S+)\s+(?P<tag>\S+)\s+(?P<sgt>\d+)$")

        # Flex Mode CTS Configuration
        p_flex = re.compile(r"^Flex\s+Mode\s+CTS\s+Configuration$")

        # Flex Profile Name                 SGACL Enforcement     Inline-Tagging
        p_flex_header = re.compile(r"^Flex\s+Profile\s+Name\s+SGACL\s+Enforcement\s+Inline-Tagging$")

        # default-flex-profile              DISABLED              DISABLED
        p_flex_policy = re.compile(r"(?P<name>\S+)\s+(?P<sgacl>\S+)\s+(?P<tag>\S+)$")


        wireless_cts_summary_dict = {}

        for line in output.splitlines():
            line = line.strip()
            # Local Mode CTS Configuration
            if p_local.match(line):
                continue
            # Policy Profile Name               SGACL Enforcement     Inline-Tagging   Default-Sgt
            elif p_local_header.match(line):
                if not wireless_cts_summary_dict.get("local_mode_cts_configuration"):
                    wireless_cts_summary_dict.update({ "local_mode_cts_configuration": {} })
                continue
            # ----------------------------------------------------------------------------------------
            elif p_hyphen_delimiter.match(line):
                continue
            # north-policy-profile              DISABLED              DISABLED         0
            elif p_local_policy.match(line):
                match = p_local_policy.match(line)
                group = match.groupdict()
                if not wireless_cts_summary_dict["local_mode_cts_configuration"].get("policy_profile_name"):
                    wireless_cts_summary_dict["local_mode_cts_configuration"].update({ "policy_profile_name": {} })
                wireless_cts_summary_dict["local_mode_cts_configuration"]["policy_profile_name"].update({ group["name"] : {} })
                wireless_cts_summary_dict["local_mode_cts_configuration"]["policy_profile_name"][group["name"]].update({ "sgacl_enforcement": group["sgacl"],
                                                                                                                        "inline-tagging": group["tag"],
                                                                                                                        "default_sgt": int(group["sgt"]) 
                                                                                                                        })
                continue
            # Flex Mode CTS Configuration
            elif p_flex.match(line):
                continue
            # Flex Profile Name                 SGACL Enforcement     Inline-Tagging
            elif p_flex_header.match(line):
                if not wireless_cts_summary_dict.get("flex_mode_cts_configuration"):
                    wireless_cts_summary_dict.update({ "flex_mode_cts_configuration": {} })
                continue
            # default-flex-profile              DISABLED              DISABLED
            elif p_flex_policy.match(line):
                match = p_flex_policy.match(line)
                group = match.groupdict()
                if not wireless_cts_summary_dict["flex_mode_cts_configuration"].get("policy_profile_name"):
                    wireless_cts_summary_dict["flex_mode_cts_configuration"].update({ "policy_profile_name": {} })
                wireless_cts_summary_dict["flex_mode_cts_configuration"]["policy_profile_name"].update({ group["name"] : {} })
                wireless_cts_summary_dict["flex_mode_cts_configuration"]["policy_profile_name"][group["name"]].update({ "sgacl_enforcement": group["sgacl"],
                                                                                                                        "inline-tagging": group["tag"]
                                                                                                                        })
                continue

        return wireless_cts_summary_dict
