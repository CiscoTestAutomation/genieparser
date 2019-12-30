# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/ike-evt-stat' resources
# =============================================


class NetIkeevtstatSchema(MetaParser):

    schema = {}


class NetIkeevtstat(NetIkeevtstatSchema):
    """ To F5 resource for /mgmt/tm/net/ike-evt-stat
    """

    cli_command = "/mgmt/tm/net/ike-evt-stat"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
