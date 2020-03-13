# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/rule-profiler' resources
# =============================================


class LtmRuleprofilerSchema(MetaParser):

    schema = {}


class LtmRuleprofiler(LtmRuleprofilerSchema):
    """ To F5 resource for /mgmt/tm/ltm/rule-profiler
    """

    cli_command = "/mgmt/tm/ltm/rule-profiler"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
