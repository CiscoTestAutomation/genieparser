# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/bwc/priority-group' resources
# =============================================


class NetBwcPrioritygroupSchema(MetaParser):

    schema = {}


class NetBwcPrioritygroup(NetBwcPrioritygroupSchema):
    """ To F5 resource for /mgmt/tm/net/bwc/priority-group
    """

    cli_command = "/mgmt/tm/net/bwc/priority-group"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
