# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/global-settings/metrics' resources
# =============================================


class GtmGlobalsettingsMetricsSchema(MetaParser):

    schema = {}


class GtmGlobalsettingsMetrics(GtmGlobalsettingsMetricsSchema):
    """ To F5 resource for /mgmt/tm/gtm/global-settings/metrics
    """

    cli_command = "/mgmt/tm/gtm/global-settings/metrics"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
