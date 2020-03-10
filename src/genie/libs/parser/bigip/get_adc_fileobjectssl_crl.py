# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/adc/fileobject/ssl-crl' resources
# =============================================


class AdcFileobjectSslcrlSchema(MetaParser):

    schema = {}


class AdcFileobjectSslcrl(AdcFileobjectSslcrlSchema):
    """ To F5 resource for /mgmt/tm/adc/fileobject/ssl-crl
    """

    cli_command = "/mgmt/tm/adc/fileobject/ssl-crl"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
