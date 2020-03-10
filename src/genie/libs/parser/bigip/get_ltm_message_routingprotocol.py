# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/message-routing/generic/protocol' resources
# =============================================


class LtmMessageroutingProtocolSchema(MetaParser):

    schema = {}


class LtmMessageroutingProtocol(LtmMessageroutingProtocolSchema):
    """ To F5 resource for /mgmt/tm/ltm/message-routing/generic/protocol
    """

    cli_command = "/mgmt/tm/ltm/message-routing/generic/protocol"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
