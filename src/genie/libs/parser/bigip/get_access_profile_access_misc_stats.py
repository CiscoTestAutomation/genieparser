# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/access/profile-access-misc-stats' resources
# =============================================


class AccessProfileaccessmiscstatsSchema(MetaParser):

    schema = {}


class AccessProfileaccessmiscstats(AccessProfileaccessmiscstatsSchema):
    """ To F5 resource for /mgmt/tm/access/profile-access-misc-stats
    """

    cli_command = "/mgmt/tm/access/profile-access-misc-stats"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
