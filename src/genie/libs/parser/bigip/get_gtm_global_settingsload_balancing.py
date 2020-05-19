# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/global-settings/load-balancing' resources
# =============================================


class GtmGlobalsettingsLoadbalancingSchema(MetaParser):

    schema = {}


class GtmGlobalsettingsLoadbalancing(GtmGlobalsettingsLoadbalancingSchema):
    """ To F5 resource for /mgmt/tm/gtm/global-settings/load-balancing
    """

    cli_command = "/mgmt/tm/gtm/global-settings/load-balancing"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
