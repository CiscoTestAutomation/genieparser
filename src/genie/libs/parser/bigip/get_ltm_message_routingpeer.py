# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/message-routing/diameter/peer' resources
# =============================================


class LtmMessageroutingPeerSchema(MetaParser):

    schema = {}


class LtmMessageroutingPeer(LtmMessageroutingPeerSchema):
    """ To F5 resource for /mgmt/tm/ltm/message-routing/diameter/peer
    """

    cli_command = "/mgmt/tm/ltm/message-routing/diameter/peer"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
