# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/rate-shaping/class' resources
# =============================================


class NetRateshapingClassSchema(MetaParser):

    schema = {}


class NetRateshapingClass(NetRateshapingClassSchema):
    """ To F5 resource for /mgmt/tm/net/rate-shaping/class
    """

    cli_command = "/mgmt/tm/net/rate-shaping/class"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
