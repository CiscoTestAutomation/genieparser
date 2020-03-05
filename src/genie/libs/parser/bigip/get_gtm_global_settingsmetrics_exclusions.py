# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/global-settings/metrics-exclusions' resources
# =============================================


class GtmGlobalsettingsMetricsexclusionsSchema(MetaParser):

    schema = {}


class GtmGlobalsettingsMetricsexclusions(
    GtmGlobalsettingsMetricsexclusionsSchema
):
    """ To F5 resource for /mgmt/tm/gtm/global-settings/metrics-exclusions
    """

    cli_command = "/mgmt/tm/gtm/global-settings/metrics-exclusions"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
