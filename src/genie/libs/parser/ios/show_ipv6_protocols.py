''' show_protocols.py

IOS parsers for the following show commands:
    * show ipv6 protocols
'''

from genie.libs.parser.iosxe.show_ipv6_protocols import ShowIpv6Protocols as \
												   ShowIpv6Protocols_iosxe, \
												   ShowIpv6ProtocolsSectionRip as \
												   ShowIpv6ProtocolsSectionRip_iosxe


class ShowIpv6Protocols(ShowIpv6Protocols_iosxe):
	''' Parser for "show ipv6 protocols" '''
	pass


class ShowIpv6ProtocolsSectionRip(ShowIpv6ProtocolsSectionRip_iosxe):
	"""Parser for :
		show ipv6 protocols | sec rip
		show ipv6 protocols vrf {vrf} | sec rip
	"""
	pass
