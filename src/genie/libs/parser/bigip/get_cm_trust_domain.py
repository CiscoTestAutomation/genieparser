# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/cm/trust-domain' resources
# =============================================


class CmTrustdomainSchema(MetaParser):

    schema = {}


class CmTrustdomain(CmTrustdomainSchema):
    """ To F5 resource for /mgmt/tm/cm/trust-domain
    """

    cli_command = "/mgmt/tm/cm/trust-domain"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
