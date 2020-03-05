# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/rate-shaping/drop-policy' resources
# =============================================


class NetRateshapingDroppolicySchema(MetaParser):

    schema = {}


class NetRateshapingDroppolicy(NetRateshapingDroppolicySchema):
    """ To F5 resource for /mgmt/tm/net/rate-shaping/drop-policy
    """

    cli_command = "/mgmt/tm/net/rate-shaping/drop-policy"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
