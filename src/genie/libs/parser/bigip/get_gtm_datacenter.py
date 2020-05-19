# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/datacenter' resources
# =============================================


class GtmDatacenterSchema(MetaParser):

    schema = {}


class GtmDatacenter(GtmDatacenterSchema):
    """ To F5 resource for /mgmt/tm/gtm/datacenter
    """

    cli_command = "/mgmt/tm/gtm/datacenter"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
