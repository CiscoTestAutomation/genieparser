# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/access/profile-rewrite/stats' resources
# =============================================


class AccessProfilerewriteStatsSchema(MetaParser):

    schema = {}


class AccessProfilerewriteStats(AccessProfilerewriteStatsSchema):
    """ To F5 resource for /mgmt/tm/access/profile-rewrite/stats
    """

    cli_command = "/mgmt/tm/access/profile-rewrite/stats"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
