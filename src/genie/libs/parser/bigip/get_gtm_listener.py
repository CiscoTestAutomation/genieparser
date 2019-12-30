# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/listener' resources
# =============================================


class GtmListenerSchema(MetaParser):

    schema = {}


class GtmListener(GtmListenerSchema):
    """ To F5 resource for /mgmt/tm/gtm/listener
    """

    cli_command = "/mgmt/tm/gtm/listener"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
