# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/message-routing/mqtt/profile/router' resources
# =============================================


class LtmMessageroutingRouterSchema(MetaParser):

    schema = {}


class LtmMessageroutingRouter(LtmMessageroutingRouterSchema):
    """ To F5 resource for /mgmt/tm/ltm/message-routing/mqtt/profile/router
    """

    cli_command = "/mgmt/tm/ltm/message-routing/mqtt/profile/router"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
