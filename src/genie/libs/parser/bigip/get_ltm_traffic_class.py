# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/traffic-class' resources
# =============================================


class LtmTrafficclassSchema(MetaParser):

    schema = {}


class LtmTrafficclass(LtmTrafficclassSchema):
    """ To F5 resource for /mgmt/tm/ltm/traffic-class
    """

    cli_command = "/mgmt/tm/ltm/traffic-class"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
