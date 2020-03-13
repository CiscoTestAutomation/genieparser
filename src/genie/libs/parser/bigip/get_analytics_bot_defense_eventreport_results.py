# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/bot-defense-event/report-results' resources
# =============================================


class AnalyticsBotdefenseeventReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsBotdefenseeventReportresults(
    AnalyticsBotdefenseeventReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/bot-defense-event/report-results
    """

    cli_command = "/mgmt/tm/analytics/bot-defense-event/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
