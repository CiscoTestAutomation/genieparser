# Global Imports
import json
from collections import defaultdict

# Metaparser
from genie.metaparser import MetaParser

# =============================================
# Collection for '/mgmt/tm/live-update/asm-attack-signatures/update-files' resources
# =============================================


class Live_updateAsmattacksignaturesUpdatefilesSchema(MetaParser):

    schema = {}


class Live_updateAsmattacksignaturesUpdatefiles(
    Live_updateAsmattacksignaturesUpdatefilesSchema
):
    """ To F5 resource for /mgmt/tm/live-update/asm-attack-signatures/update-files
    """

    cli_command = "/mgmt/tm/live-update/asm-attack-signatures/update-files"

    def rest(self):

        response = self.device.get(self.cli_command)

        response_json = response.json()

        if not response_json:
            return {}

        return response_json
