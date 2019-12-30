# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/tcp/report-results' resources
# =============================================


class AnalyticsTcpReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsTcpReportresults(AnalyticsTcpReportresultsSchema):
    """ To F5 resource for /mgmt/tm/analytics/tcp/report-results
    """

    cli_command = "/mgmt/tm/analytics/tcp/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
