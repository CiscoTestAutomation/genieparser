# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/virtual/generate-report' resources
# =============================================


class AnalyticsVirtualGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsVirtualGeneratereport(AnalyticsVirtualGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/virtual/generate-report
    """

    cli_command = "/mgmt/tm/analytics/virtual/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
