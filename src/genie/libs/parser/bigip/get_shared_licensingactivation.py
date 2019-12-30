# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/shared/licensing/activation' resources
# =============================================


class SharedLicensingActivationSchema(MetaParser):

    schema = {}


class SharedLicensingActivation(SharedLicensingActivationSchema):
    """ To F5 resource for /mgmt/tm/shared/licensing/activation
    """

    cli_command = "/mgmt/tm/shared/licensing/activation"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
