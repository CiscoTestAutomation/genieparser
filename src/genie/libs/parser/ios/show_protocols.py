''' show_protocols.py

IOS parsers for the following show commands:
    * show ip protocols
'''

from genie.libs.parser.iosxe.show_protocols import ShowIpProtocols as ShowIpProtocols_iosxe


class ShowIpProtocols(ShowIpProtocols_iosxe):
    ''' Parser for "show ip protocols" '''
    pass