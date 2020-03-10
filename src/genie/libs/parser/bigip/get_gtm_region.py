# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/region' resources
# =============================================


class GtmRegionSchema(MetaParser):

    schema = {}


class GtmRegion(GtmRegionSchema):
    """ To F5 resource for /mgmt/tm/gtm/region
    """

    cli_command = "/mgmt/tm/gtm/region"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
