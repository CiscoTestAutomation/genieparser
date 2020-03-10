# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/cos/traffic-priority' resources
# =============================================


class NetCosTrafficprioritySchema(MetaParser):

    schema = {}


class NetCosTrafficpriority(NetCosTrafficprioritySchema):
    """ To F5 resource for /mgmt/tm/net/cos/traffic-priority
    """

    cli_command = "/mgmt/tm/net/cos/traffic-priority"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
