# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/security/firewall/management-ip-rules' resources
# =============================================


class SecurityFirewallManagementiprulesSchema(MetaParser):

    schema = {}


class SecurityFirewallManagementiprules(
    SecurityFirewallManagementiprulesSchema
):
    """ To F5 resource for /mgmt/tm/security/firewall/management-ip-rules
    """

    cli_command = "/mgmt/tm/security/firewall/management-ip-rules"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
