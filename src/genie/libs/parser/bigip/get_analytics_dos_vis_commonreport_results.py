# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/dos-vis-common/report-results' resources
# =============================================


class AnalyticsDosviscommonReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsDosviscommonReportresults(
    AnalyticsDosviscommonReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/dos-vis-common/report-results
    """

    cli_command = "/mgmt/tm/analytics/dos-vis-common/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
