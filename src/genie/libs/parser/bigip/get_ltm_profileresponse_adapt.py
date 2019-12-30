# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/response-adapt' resources
# =============================================


class LtmProfileResponseadaptSchema(MetaParser):

    schema = {}


class LtmProfileResponseadapt(LtmProfileResponseadaptSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/response-adapt
    """

    cli_command = "/mgmt/tm/ltm/profile/response-adapt"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
