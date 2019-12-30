# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/snatpool' resources
# =============================================


class LtmSnatpoolSchema(MetaParser):

    schema = {}


class LtmSnatpool(LtmSnatpoolSchema):
    """ To F5 resource for /mgmt/tm/ltm/snatpool
    """

    cli_command = "/mgmt/tm/ltm/snatpool"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
