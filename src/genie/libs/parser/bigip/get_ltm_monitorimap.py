# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/monitor/imap' resources
# =============================================


class LtmMonitorImapSchema(MetaParser):

    schema = {}


class LtmMonitorImap(LtmMonitorImapSchema):
    """ To F5 resource for /mgmt/tm/ltm/monitor/imap
    """

    cli_command = "/mgmt/tm/ltm/monitor/imap"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
