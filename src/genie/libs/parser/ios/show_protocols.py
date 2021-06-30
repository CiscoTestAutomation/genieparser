''' show_protocols.py

IOS parsers for the following show commands:
    * show ip protocols
'''

from genie.libs.parser.iosxe.show_protocols import ShowIpProtocols as \
												   ShowIpProtocols_iosxe, \
												   ShowIpProtocolsSectionRip as \
												   ShowIpProtocolsSectionRip_iosxe, \
												   ShowIpv6ProtocolsSectionRip as \
												   ShowIpv6ProtocolsSectionRip_iosxe, \
                                                   ShowIpv6Protocols as \
                                                   ShowIpv6Protocols_iosxe


class ShowIpProtocols(ShowIpProtocols_iosxe):
	''' Parser for "show ip protocols" '''
	pass


class ShowIpProtocolsSectionRip(ShowIpProtocolsSectionRip_iosxe):
	"""
	Parser for :
		'show ip protocols | sec rip'
		'show ip protocols vrf {vrf} | sec rip'
	"""
	pass


class ShowIpv6ProtocolsSectionRip(ShowIpv6ProtocolsSectionRip_iosxe):
	"""Parser for :
		show ipv6 protocols | sec rip
		show ipv6 protocols vrf {vrf} | sec rip
	"""
	pass


class ShowIpv6Protocols(ShowIpv6Protocols_iosxe):
	''' Parser for "show ipv6 protocols" '''
	pass
