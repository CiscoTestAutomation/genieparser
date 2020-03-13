# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/asm-enforced-entities/generate-report' resources
# =============================================


class AnalyticsAsmenforcedentitiesGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsAsmenforcedentitiesGeneratereport(
    AnalyticsAsmenforcedentitiesGeneratereportSchema
):
    """ To F5 resource for /mgmt/tm/analytics/asm-enforced-entities/generate-report
    """

    cli_command = "/mgmt/tm/analytics/asm-enforced-entities/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
