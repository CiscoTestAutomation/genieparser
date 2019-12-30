# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/port-list' resources
# =============================================


class NetPortlistSchema(MetaParser):

    schema = {}


class NetPortlist(NetPortlistSchema):
    """ To F5 resource for /mgmt/tm/net/port-list
    """

    cli_command = "/mgmt/tm/net/port-list"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
