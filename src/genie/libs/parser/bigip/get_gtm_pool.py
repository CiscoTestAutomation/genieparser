# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/pool' resources
# =============================================


class GtmPoolSchema(MetaParser):

    schema = {}


class GtmPool(GtmPoolSchema):
    """ To F5 resource for /mgmt/tm/gtm/pool
    """

    cli_command = "/mgmt/tm/gtm/pool"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
