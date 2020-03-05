# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/application-security-anomalies/generate-report' resources
# =============================================


class AnalyticsApplicationsecurityanomaliesGeneratereportSchema(MetaParser):

    schema = {}


class AnalyticsApplicationsecurityanomaliesGeneratereport(
    AnalyticsApplicationsecurityanomaliesGeneratereportSchema
):
    """ To F5 resource for /mgmt/tm/analytics/application-security-anomalies/generate-report
    """

    cli_command = (
        "/mgmt/tm/analytics/application-security-anomalies/generate-report"
    )

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
