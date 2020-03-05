# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/net/bwc/policy' resources
# =============================================


class NetBwcPolicySchema(MetaParser):

    schema = {}


class NetBwcPolicy(NetBwcPolicySchema):
    """ To F5 resource for /mgmt/tm/net/bwc/policy
    """

    cli_command = "/mgmt/tm/net/bwc/policy"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
