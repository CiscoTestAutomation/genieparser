# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/memory-per-process/report-results' resources
# =============================================


class AnalyticsMemoryperprocessReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsMemoryperprocessReportresults(
    AnalyticsMemoryperprocessReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/memory-per-process/report-results
    """

    cli_command = "/mgmt/tm/analytics/memory-per-process/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
