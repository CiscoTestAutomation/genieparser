# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/asm-memory/generate-report' resources
# =============================================


class AnalyticsAsmmemoryGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsAsmmemoryGeneratereport(AnalyticsAsmmemoryGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/asm-memory/generate-report
    """

    cli_command = "/mgmt/tm/analytics/asm-memory/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
