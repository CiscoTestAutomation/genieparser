# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/wideip/srv' resources
# =============================================


class GtmWideipSrvSchema(MetaParser):

    schema = {}


class GtmWideipSrv(GtmWideipSrvSchema):
    """ To F5 resource for /mgmt/tm/gtm/wideip/srv
    """

    cli_command = "/mgmt/tm/gtm/wideip/srv"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
