# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/rate-shaping' resources
# =============================================


class NetRateshapingSchema(MetaParser):

    schema = {}


class NetRateshaping(NetRateshapingSchema):
    """ To F5 resource for /mgmt/tm/net/rate-shaping
    """

    cli_command = "/mgmt/tm/net/rate-shaping"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
