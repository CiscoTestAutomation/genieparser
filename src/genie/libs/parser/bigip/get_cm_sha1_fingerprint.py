# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cm/sha1-fingerprint' resources
# =============================================


class CmSha1fingerprintSchema(MetaParser):

    schema = {}


class CmSha1fingerprint(CmSha1fingerprintSchema):
    """ To F5 resource for /mgmt/tm/cm/sha1-fingerprint
    """

    cli_command = "/mgmt/tm/cm/sha1-fingerprint"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
