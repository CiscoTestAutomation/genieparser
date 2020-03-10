# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/wideip/cname' resources
# =============================================


class GtmWideipCnameSchema(MetaParser):

    schema = {}


class GtmWideipCname(GtmWideipCnameSchema):
    """ To F5 resource for /mgmt/tm/gtm/wideip/cname
    """

    cli_command = "/mgmt/tm/gtm/wideip/cname"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
