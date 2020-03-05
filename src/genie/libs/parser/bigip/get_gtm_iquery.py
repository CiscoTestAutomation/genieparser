# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/gtm/iquery' resources
# =============================================


class GtmIquerySchema(MetaParser):

    schema = {}


class GtmIquery(GtmIquerySchema):
    """ To F5 resource for /mgmt/tm/gtm/iquery
    """

    cli_command = "/mgmt/tm/gtm/iquery"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
