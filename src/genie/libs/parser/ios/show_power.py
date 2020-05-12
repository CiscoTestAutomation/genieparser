"""show_platform.py

"""
from genie.libs.parser.iosxe.show_power import ShowStackPower as ShowStackPower_iosxe,\
                                               ShowPowerInline as ShowPowerInline_iosxe


class ShowStackPower(ShowStackPower_iosxe):
    """Parser for show stack-power"""
    pass


class ShowPowerInline(ShowPowerInline_iosxe):
    """Parser for show power inline
                  show power inline <interface>"""
    pass