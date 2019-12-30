# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/dns/report-results' resources
# =============================================


class AnalyticsDnsReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsDnsReportresults(AnalyticsDnsReportresultsSchema):
    """ To F5 resource for /mgmt/tm/analytics/dns/report-results
    """

    cli_command = "/mgmt/tm/analytics/dns/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
