# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/routing/profile' resources
# =============================================


class NetRoutingProfileSchema(MetaParser):

    schema = {}


class NetRoutingProfile(NetRoutingProfileSchema):
    """ To F5 resource for /mgmt/tm/net/routing/profile
    """

    cli_command = "/mgmt/tm/net/routing/profile"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
