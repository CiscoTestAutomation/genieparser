"""show_fdb.py
   supported commands:
     *  show mac address-table
     *  show mac address-table vlan {vlan}
     *  show mac address-table aging-time
     *  show mac address-table learning
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
# import parser utils
from genie.libs.parser.utils.common import Common
# import iosxe parser
from genie.libs.parser.iosxe.show_fdb import \
                ShowMacAddressTable as ShowMacAddressTable_iosxe,\
                ShowMacAddressTableAgingTime as ShowMacAddressTableAgingTime_iosxe,\
                ShowMacAddressTableLearning as ShowMacAddressTableLearning_iosxe


class ShowMacAddressTable(ShowMacAddressTable_iosxe):
    """Parser for show mac address-table"""
    pass


class ShowMacAddressTableAgingTime(ShowMacAddressTableAgingTime_iosxe):
    """Parser for show mac address-table aging-time"""
    pass


class ShowMacAddressTableLearning(ShowMacAddressTableLearning_iosxe):
    """Parser for show mac address-table learning"""
    pass
