# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/service' resources
# =============================================


class LtmProfileServiceSchema(MetaParser):

    schema = {}


class LtmProfileService(LtmProfileServiceSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/service
    """

    cli_command = "/mgmt/tm/ltm/profile/service"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
