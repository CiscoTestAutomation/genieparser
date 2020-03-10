# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/dhcpv6' resources
# =============================================


class LtmProfileDhcpv6Schema(MetaParser):

    schema = {}


class LtmProfileDhcpv6(LtmProfileDhcpv6Schema):
    """ To F5 resource for /mgmt/tm/ltm/profile/dhcpv6
    """

    cli_command = "/mgmt/tm/ltm/profile/dhcpv6"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
