# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/dns/generate-report' resources
# =============================================


class AnalyticsDnsGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsDnsGeneratereport(AnalyticsDnsGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/dns/generate-report
    """

    cli_command = "/mgmt/tm/analytics/dns/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
