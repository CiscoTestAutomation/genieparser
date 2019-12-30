# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/dos-l3/generate-report' resources
# =============================================


class AnalyticsDosl3GeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsDosl3Generatereport(AnalyticsDosl3GeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/dos-l3/generate-report
    """

    cli_command = "/mgmt/tm/analytics/dos-l3/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
