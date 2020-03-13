# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/bwc/probe' resources
# =============================================


class NetBwcProbeSchema(MetaParser):

    schema = {}


class NetBwcProbe(NetBwcProbeSchema):
    """ To F5 resource for /mgmt/tm/net/bwc/probe
    """

    cli_command = "/mgmt/tm/net/bwc/probe"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
