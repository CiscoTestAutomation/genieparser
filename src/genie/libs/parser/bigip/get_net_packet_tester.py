# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/packet-tester' resources
# =============================================


class NetPackettesterSchema(MetaParser):

    schema = {}


class NetPackettester(NetPackettesterSchema):
    """ To F5 resource for /mgmt/tm/net/packet-tester
    """

    cli_command = "/mgmt/tm/net/packet-tester"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
