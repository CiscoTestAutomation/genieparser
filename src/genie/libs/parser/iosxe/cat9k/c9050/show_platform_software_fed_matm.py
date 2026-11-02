"""IOSXE C9050 parser for the FED MATM MAC-table command."""

from genie.libs.parser.iosxe.cat9k.c9350 import (
    show_platform_software_fed_matm as c9350,
)


class ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema(
    c9350.ShowPlatformSoftwareFedSwitchActiveMatmMactableSchema
):
    """Schema for C9050 FED MATM MAC-table output."""

    pass


class ShowPlatformSoftwareFedSwitchActiveMatmMactable(
    c9350.ShowPlatformSoftwareFedSwitchActiveMatmMactable
):
    """Parser for the C9050 FED MATM MAC-table command."""

    pass
