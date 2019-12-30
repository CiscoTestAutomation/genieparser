# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/ike-msg-stat' resources
# =============================================


class NetIkemsgstatSchema(MetaParser):

    schema = {}


class NetIkemsgstat(NetIkemsgstatSchema):
    """ To F5 resource for /mgmt/tm/net/ike-msg-stat
    """

    cli_command = "/mgmt/tm/net/ike-msg-stat"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
