# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/tcp-analytics' resources
# =============================================


class LtmProfileTcpanalyticsSchema(MetaParser):

    schema = {}


class LtmProfileTcpanalytics(LtmProfileTcpanalyticsSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/tcp-analytics
    """

    cli_command = "/mgmt/tm/ltm/profile/tcp-analytics"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
