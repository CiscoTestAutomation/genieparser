"""show_platform_software_fed_matm.py
    * 'show platform software fed switch active matm macTable'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And


from genie.libs.parser.iosxe.cat9k.c9550.show_platform_software_fed_matm import (
    ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema as ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema_9350,
    ShowPlatformSoftwareFedSwitchActiveMatmMactable as ShowPlatformSoftwareFedSwitchActiveMatmMactable_9350)

class ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema(ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema_9350):
    """Schema for show platform software fed switch active matm macTable"""
    ...

# ======================================================
# Parser for 'show platform software fed switch active matm macTable'
# ======================================================

class ShowPlatformSoftwareFedSwitchActiveMatmMactable(ShowPlatformSoftwareFedSwitchActiveMatmMactable_9350):
    ...