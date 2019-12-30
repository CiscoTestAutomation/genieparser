# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/dns/analytics' resources
# =============================================


class LtmDnsAnalyticsSchema(MetaParser):

    schema = {}


class LtmDnsAnalytics(LtmDnsAnalyticsSchema):
    """ To F5 resource for /mgmt/tm/ltm/dns/analytics
    """

    cli_command = "/mgmt/tm/ltm/dns/analytics"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
