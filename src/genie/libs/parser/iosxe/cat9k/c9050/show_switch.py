"""IOSXE C9050 parser for ``show switch stack-ports summary``."""

from genie.libs.parser.iosxe.cat9k.c9350 import show_switch as c9350


class ShowSwitchStackPortSummarySchema(c9350.ShowSwitchStackPortSummarySchema):
    """Schema for C9050 ``show switch stack-ports summary`` output."""

    pass


class ShowSwitchStackPortSummary(c9350.ShowSwitchStackPortSummary):
    """Parser for C9050 ``show switch stack-ports summary`` output."""

    pass
