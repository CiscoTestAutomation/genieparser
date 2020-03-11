# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/sys/license' resources
# =============================================


class SysLicenseSchema(MetaParser):

    schema = {}


class SysLicense(SysLicenseSchema):
    """ To F5 resource for /mgmt/tm/sys/license
    """

    cli_command = "/mgmt/tm/sys/license"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
