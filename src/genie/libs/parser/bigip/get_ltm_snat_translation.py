# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/snat-translation' resources
# =============================================


class LtmSnattranslationSchema(MetaParser):

    schema = {}


class LtmSnattranslation(LtmSnattranslationSchema):
    """ To F5 resource for /mgmt/tm/ltm/snat-translation
    """

    cli_command = "/mgmt/tm/ltm/snat-translation"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
