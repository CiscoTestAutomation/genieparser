"""show_platform.py

"""
from genie.libs.parser.iosxe.show_power import ShowStackPower as ShowStackPower_iosxe,\
                                               ShowPowerInlineInterface as ShowPowerInlineInterface_iosxe


class ShowStackPower(ShowStackPower_iosxe):
    """Parser for show stack-power"""
    pass


class ShowPowerInlineInterface(ShowPowerInlineInterface_iosxe):
    """Parser for show power inline <interface>"""
    pass