# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/link' resources
# =============================================


class GtmLinkSchema(MetaParser):

    schema = {}


class GtmLink(GtmLinkSchema):
    """ To F5 resource for /mgmt/tm/gtm/link
    """

    cli_command = "/mgmt/tm/gtm/link"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
