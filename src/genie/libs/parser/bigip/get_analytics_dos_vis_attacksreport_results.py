# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/dos-vis-attacks/report-results' resources
# =============================================


class AnalyticsDosvisattacksReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsDosvisattacksReportresults(
    AnalyticsDosvisattacksReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/dos-vis-attacks/report-results
    """

    cli_command = "/mgmt/tm/analytics/dos-vis-attacks/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
