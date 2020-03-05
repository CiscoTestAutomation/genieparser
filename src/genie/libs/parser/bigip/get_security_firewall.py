# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/security/firewall' resources
# =============================================


class SecurityFirewallSchema(MetaParser):

    schema = {}


class SecurityFirewall(SecurityFirewallSchema):
    """ To F5 resource for /mgmt/tm/security/firewall
    """

    cli_command = "/mgmt/tm/security/firewall"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
