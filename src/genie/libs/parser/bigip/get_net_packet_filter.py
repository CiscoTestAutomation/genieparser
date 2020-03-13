# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/packet-filter' resources
# =============================================


class NetPacketfilterSchema(MetaParser):

    schema = {}


class NetPacketfilter(NetPacketfilterSchema):
    """ To F5 resource for /mgmt/tm/net/packet-filter
    """

    cli_command = "/mgmt/tm/net/packet-filter"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
