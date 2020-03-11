# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/disk-info/generate-report' resources
# =============================================


class AnalyticsDiskinfoGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsDiskinfoGeneratereport(AnalyticsDiskinfoGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/disk-info/generate-report
    """

    cli_command = "/mgmt/tm/analytics/disk-info/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
