# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/access/session/kill-sessions' resources
# =============================================


class AccessSessionKillsessionsSchema(MetaParser):

    schema = {}


class AccessSessionKillsessions(AccessSessionKillsessionsSchema):
    """ To F5 resource for /mgmt/tm/access/session/kill-sessions
    """

    cli_command = "/mgmt/tm/access/session/kill-sessions"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
