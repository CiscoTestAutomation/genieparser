# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/pem/generate-report' resources
# =============================================


class AnalyticsPemGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsPemGeneratereport(AnalyticsPemGeneratereportSchema):
    """ To F5 resource for /mgmt/tm/analytics/pem/generate-report
    """

    cli_command = "/mgmt/tm/analytics/pem/generate-report"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
