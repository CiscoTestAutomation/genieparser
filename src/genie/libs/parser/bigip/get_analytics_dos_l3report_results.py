# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/dos-l3/report-results' resources
# =============================================


class AnalyticsDosl3ReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsDosl3Reportresults(AnalyticsDosl3ReportresultsSchema):
    """ To F5 resource for /mgmt/tm/analytics/dos-l3/report-results
    """

    cli_command = "/mgmt/tm/analytics/dos-l3/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
