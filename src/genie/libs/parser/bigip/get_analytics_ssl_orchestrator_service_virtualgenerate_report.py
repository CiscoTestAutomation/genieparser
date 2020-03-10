# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/ssl-orchestrator-service-virtual/generate-report' resources
# =============================================


class AnalyticsSslorchestratorservicevirtualGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsSslorchestratorservicevirtualGeneratereport(
    AnalyticsSslorchestratorservicevirtualGeneratereportSchema
):
    """ To F5 resource for /mgmt/tm/analytics/ssl-orchestrator-service-virtual/generate-report
    """

    cli_command = (
        "/mgmt/tm/analytics/ssl-orchestrator-service-virtual/generate-report"
    )

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
