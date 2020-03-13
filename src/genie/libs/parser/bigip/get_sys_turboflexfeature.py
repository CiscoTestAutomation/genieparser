# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/turboflex/profile/feature' resources
# =============================================


class SysTurboflexFeatureSchema(MetaParser):

    schema = {}


class SysTurboflexFeature(SysTurboflexFeatureSchema):
    """ To F5 resource for /mgmt/tm/sys/turboflex/profile/feature
    """

    cli_command = "/mgmt/tm/sys/turboflex/profile/feature"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
