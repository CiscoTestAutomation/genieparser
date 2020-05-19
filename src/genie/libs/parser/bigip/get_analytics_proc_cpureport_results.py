# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/proc-cpu/report-results' resources
# =============================================


class AnalyticsProccpuReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsProccpuReportresults(AnalyticsProccpuReportresultsSchema):
    """ To F5 resource for /mgmt/tm/analytics/proc-cpu/report-results
    """

    cli_command = "/mgmt/tm/analytics/proc-cpu/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
