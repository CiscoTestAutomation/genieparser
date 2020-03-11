# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/wideip/a' resources
# =============================================


class GtmWideipASchema(MetaParser):

    schema = {}


class GtmWideipA(GtmWideipASchema):
    """ To F5 resource for /mgmt/tm/gtm/wideip/a
    """

    cli_command = "/mgmt/tm/gtm/wideip/a"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
