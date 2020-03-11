# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/afm-sweeper/generate-report' resources
# =============================================


class AnalyticsAfmsweeperGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsAfmsweeperGeneratereport(
    AnalyticsAfmsweeperGeneratereportSchema
):
    """ To F5 resource for /mgmt/tm/analytics/afm-sweeper/generate-report
    """

    cli_command = "/mgmt/tm/analytics/afm-sweeper/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
