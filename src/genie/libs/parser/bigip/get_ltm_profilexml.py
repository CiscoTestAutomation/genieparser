# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/xml' resources
# =============================================


class LtmProfileXmlSchema(MetaParser):

    schema = {}


class LtmProfileXml(LtmProfileXmlSchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/xml
    """

    cli_command = "/mgmt/tm/ltm/profile/xml"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
