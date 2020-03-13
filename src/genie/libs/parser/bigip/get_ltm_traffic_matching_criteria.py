# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/traffic-matching-criteria' resources
# =============================================


class LtmTrafficmatchingcriteriaSchema(MetaParser):

    schema = {}


class LtmTrafficmatchingcriteria(LtmTrafficmatchingcriteriaSchema):
    """ To F5 resource for /mgmt/tm/ltm/traffic-matching-criteria
    """

    cli_command = "/mgmt/tm/ltm/traffic-matching-criteria"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
