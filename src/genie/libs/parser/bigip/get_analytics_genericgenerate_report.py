# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/generic/generate-report' resources
# =============================================


class AnalyticsGenericGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsGenericGeneratereport(AnalyticsGenericGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/generic/generate-report
    """

    cli_command = "/mgmt/tm/analytics/generic/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
