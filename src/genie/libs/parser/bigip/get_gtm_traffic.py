# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/traffic' resources
# =============================================


class GtmTrafficSchema(MetaParser):

    schema = {}


class GtmTraffic(GtmTrafficSchema):
    """ To F5 resource for /mgmt/tm/gtm/traffic
    """

    cli_command = "/mgmt/tm/gtm/traffic"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
