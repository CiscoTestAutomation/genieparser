# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/prober-pool' resources
# =============================================


class GtmProberpoolSchema(MetaParser):

    schema = {}


class GtmProberpool(GtmProberpoolSchema):
    """ To F5 resource for /mgmt/tm/gtm/prober-pool
    """

    cli_command = "/mgmt/tm/gtm/prober-pool"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
