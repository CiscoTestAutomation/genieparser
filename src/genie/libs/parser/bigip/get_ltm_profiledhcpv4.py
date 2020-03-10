# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/dhcpv4' resources
# =============================================


class LtmProfileDhcpv4Schema(MetaParser):

    schema = {}


class LtmProfileDhcpv4(LtmProfileDhcpv4Schema):
    """ To F5 resource for /mgmt/tm/ltm/profile/dhcpv4
    """

    cli_command = "/mgmt/tm/ltm/profile/dhcpv4"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
