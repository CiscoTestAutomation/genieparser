# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/asm-learning-suggestions/report-results' resources
# =============================================


class AnalyticsAsmlearningsuggestionsReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsAsmlearningsuggestionsReportresults(
    AnalyticsAsmlearningsuggestionsReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/asm-learning-suggestions/report-results
    """

    cli_command = "/mgmt/tm/analytics/asm-learning-suggestions/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
