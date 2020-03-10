# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cm/cert' resources
# =============================================


class CmCertSchema(MetaParser):

    schema = {}


class CmCert(CmCertSchema):
    """ To F5 resource for /mgmt/tm/cm/cert
    """

    cli_command = "/mgmt/tm/cm/cert"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
