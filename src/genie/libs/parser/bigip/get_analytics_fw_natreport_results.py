# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/fw-nat/report-results' resources
# =============================================


class AnalyticsFwnatReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsFwnatReportresults(AnalyticsFwnatReportresultsSchema):
    """ To F5 resource for /mgmt/tm/analytics/fw-nat/report-results
    """

    cli_command = "/mgmt/tm/analytics/fw-nat/report-results"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
