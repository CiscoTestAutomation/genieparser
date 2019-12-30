# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/access/profile-rewrite-stats' resources
# =============================================


class AccessProfilerewritestatsSchema(MetaParser):

    schema = {}


class AccessProfilerewritestats(AccessProfilerewritestatsSchema):
    """ To F5 resource for /mgmt/tm/access/profile-rewrite-stats
    """

    cli_command = "/mgmt/tm/access/profile-rewrite-stats"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
