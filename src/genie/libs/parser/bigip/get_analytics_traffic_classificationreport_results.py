# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/traffic-classification/report-results' resources
# =============================================


class AnalyticsTrafficclassificationReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsTrafficclassificationReportresults(
    AnalyticsTrafficclassificationReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/traffic-classification/report-results
    """

    cli_command = "/mgmt/tm/analytics/traffic-classification/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
