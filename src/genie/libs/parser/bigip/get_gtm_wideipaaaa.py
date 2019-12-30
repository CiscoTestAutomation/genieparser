# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/wideip/aaaa' resources
# =============================================


class GtmWideipAaaaSchema(MetaParser):

    schema = {}


class GtmWideipAaaa(GtmWideipAaaaSchema):
    """ To F5 resource for /mgmt/tm/gtm/wideip/aaaa
    """

    cli_command = "/mgmt/tm/gtm/wideip/aaaa"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
