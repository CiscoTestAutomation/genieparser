# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/asm-attack-signatures/installations' resources
# =============================================


class Live_updateAsmattacksignaturesInstallationsSchema(MetaParser):

    schema = {}


class Live_updateAsmattacksignaturesInstallations(
    Live_updateAsmattacksignaturesInstallationsSchema
):
    """ To F5 resource for /mgmt/tm/live-update/asm-attack-signatures/installations
    """

    cli_command = "/mgmt/tm/live-update/asm-attack-signatures/installations"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
