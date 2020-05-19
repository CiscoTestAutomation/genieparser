# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/tcp/generate-report' resources
# =============================================


class AnalyticsTcpGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsTcpGeneratereport(AnalyticsTcpGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/tcp/generate-report
    """

    cli_command = "/mgmt/tm/analytics/tcp/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
