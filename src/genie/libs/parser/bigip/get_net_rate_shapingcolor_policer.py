# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/rate-shaping/color-policer' resources
# =============================================


class NetRateshapingColorpolicerSchema(MetaParser):

    schema = {}


class NetRateshapingColorpolicer(NetRateshapingColorpolicerSchema):
    """ To F5 resource for /mgmt/tm/net/rate-shaping/color-policer
    """

    cli_command = "/mgmt/tm/net/rate-shaping/color-policer"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
