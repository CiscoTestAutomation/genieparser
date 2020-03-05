# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/ntlm' resources
# =============================================


class LtmProfileNtlmSchema(MetaParser):

    schema = {}


class LtmProfileNtlm(LtmProfileNtlmSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/ntlm
    """

    cli_command = "/mgmt/tm/ltm/profile/ntlm"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
