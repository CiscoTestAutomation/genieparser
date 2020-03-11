# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/system-monitor/report-results' resources
# =============================================


class AnalyticsSystemmonitorReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsSystemmonitorReportresults(
    AnalyticsSystemmonitorReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/system-monitor/report-results
    """

    cli_command = "/mgmt/tm/analytics/system-monitor/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
