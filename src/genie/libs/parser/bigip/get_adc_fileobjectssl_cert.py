# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/adc/fileobject/ssl-cert' resources
# =============================================


class AdcFileobjectSslcertSchema(MetaParser):

    schema = {}


class AdcFileobjectSslcert(AdcFileobjectSslcertSchema):
    """ To F5 resource for /mgmt/tm/adc/fileobject/ssl-cert
    """

    cli_command = "/mgmt/tm/adc/fileobject/ssl-cert"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
