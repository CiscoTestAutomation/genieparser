# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/access/acl-stats' resources
# =============================================


class AccessAclstatsSchema(MetaParser):

    schema = {}


class AccessAclstats(AccessAclstatsSchema):
    """ To F5 resource for /mgmt/tm/access/acl-stats
    """

    cli_command = "/mgmt/tm/access/acl-stats"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
