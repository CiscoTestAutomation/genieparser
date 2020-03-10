# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/afm-sweeper/report-results' resources
# =============================================


class AnalyticsAfmsweeperReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsAfmsweeperReportresults(AnalyticsAfmsweeperReportresultsSchema):
    """ To F5 resource for /mgmt/tm/analytics/afm-sweeper/report-results
    """

    cli_command = "/mgmt/tm/analytics/afm-sweeper/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
