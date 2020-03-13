# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/wideip/mx' resources
# =============================================


class GtmWideipMxSchema(MetaParser):

    schema = {}


class GtmWideipMx(GtmWideipMxSchema):
    """ To F5 resource for /mgmt/tm/gtm/wideip/mx
    """

    cli_command = "/mgmt/tm/gtm/wideip/mx"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
