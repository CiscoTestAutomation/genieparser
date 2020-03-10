# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/wideip/naptr' resources
# =============================================


class GtmWideipNaptrSchema(MetaParser):

    schema = {}


class GtmWideipNaptr(GtmWideipNaptrSchema):
    """ To F5 resource for /mgmt/tm/gtm/wideip/naptr
    """

    cli_command = "/mgmt/tm/gtm/wideip/naptr"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
