# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/ltm/profile/certificate-authority' resources
# =============================================


class LtmProfileCertificateauthoritySchema(MetaParser):

    schema = {}


class LtmProfileCertificateauthority(LtmProfileCertificateauthoritySchema):
    """ To F5 resource for /mgmt/tm/ltm/profile/certificate-authority
    """

    cli_command = "/mgmt/tm/ltm/profile/certificate-authority"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
