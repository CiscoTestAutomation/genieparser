# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/bot-defense-event/generate-report' resources
# =============================================


class AnalyticsBotdefenseeventGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsBotdefenseeventGeneratereport(
    AnalyticsBotdefenseeventGeneratereportSchema
):
    """ To F5 resource for /mgmt/tm/analytics/bot-defense-event/generate-report
    """

    cli_command = "/mgmt/tm/analytics/bot-defense-event/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
