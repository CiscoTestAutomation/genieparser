""" show_vtp.py

IOSXE parsers for the following show commands:
    * show vtp status
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser

# import iosxe parser
from genie.libs.parser.iosxe.show_vtp import ShowVtpStatus as ShowVtpStatus_iosxe
from genie.libs.parser.iosxe.show_vtp import ShowVtpPassword as ShowVtpPassword_iosxe


# =============================================
# Parser for 'show vtp password'
# =============================================
class ShowVtpPassword(ShowVtpPassword_iosxe):
    """Parser for show vtp password"""
    pass


# =============================================
# Parser for 'show vtp status'
# =============================================
class ShowVtpStatus(ShowVtpStatus_iosxe):
    """Parser for show vtp status """
    pass
