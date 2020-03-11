# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/application-security-incidents/generate-report' resources
# =============================================


class AnalyticsApplicationsecurityincidentsGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsApplicationsecurityincidentsGeneratereport(
    AnalyticsApplicationsecurityincidentsGeneratereportSchema
):
    """ To F5 resource for /mgmt/tm/analytics/application-security-incidents/generate-report
    """

    cli_command = (
        "/mgmt/tm/analytics/application-security-incidents/generate-report"
    )

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
