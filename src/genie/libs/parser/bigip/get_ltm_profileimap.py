# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/imap' resources
# =============================================


class LtmProfileImapSchema(MetaParser):

    schema = {}


class LtmProfileImap(LtmProfileImapSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/imap
    """

    cli_command = "/mgmt/tm/ltm/profile/imap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
