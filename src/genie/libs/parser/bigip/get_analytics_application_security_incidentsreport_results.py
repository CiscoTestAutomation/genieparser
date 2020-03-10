# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/analytics/application-security-incidents/report-results' resources
# =============================================


class AnalyticsApplicationsecurityincidentsReportresultsSchema(MetaParser):

    schema = {}


class AnalyticsApplicationsecurityincidentsReportresults(
    AnalyticsApplicationsecurityincidentsReportresultsSchema
):
    """ To F5 resource for /mgmt/tm/analytics/application-security-incidents/report-results
    """

    cli_command = (
        "/mgmt/tm/analytics/application-security-incidents/report-results"
    )

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
