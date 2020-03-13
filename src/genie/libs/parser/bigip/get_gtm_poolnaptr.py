# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/pool/naptr' resources
# =============================================


class GtmPoolNaptrSchema(MetaParser):

    schema = {}


class GtmPoolNaptr(GtmPoolNaptrSchema):
    """ To F5 resource for /mgmt/tm/gtm/pool/naptr
    """

    cli_command = "/mgmt/tm/gtm/pool/naptr"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
