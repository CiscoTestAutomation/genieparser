# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/shared/licensing/registration' resources
# =============================================


class SharedLicensingRegistrationSchema(MetaParser):

    schema = {}


class SharedLicensingRegistration(SharedLicensingRegistrationSchema):
    """ To F5 resource for /mgmt/tm/shared/licensing/registration
    """

    cli_command = "/mgmt/tm/shared/licensing/registration"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
