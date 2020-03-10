# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/asm-attack-signatures' resources
# =============================================


class Live_updateAsmattacksignaturesSchema(MetaParser):

    schema = {}


class Live_updateAsmattacksignatures(Live_updateAsmattacksignaturesSchema):
    """ To F5 resource for /mgmt/tm/live-update/asm-attack-signatures
    """

    cli_command = "/mgmt/tm/live-update/asm-attack-signatures"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
