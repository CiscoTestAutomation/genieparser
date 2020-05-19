# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/path' resources
# =============================================


class GtmPathSchema(MetaParser):

    schema = {}


class GtmPath(GtmPathSchema):
    """ To F5 resource for /mgmt/tm/gtm/path
    """

    cli_command = "/mgmt/tm/gtm/path"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
