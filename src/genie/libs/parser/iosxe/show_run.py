''' show_run.py

IOSXE parsers for the following show commands:
	* 'show run policy-map {name}'
	* 'show running-config interface {interface}'
'''

# Python
import re
import xmltodict
import collections
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common

# =================================================
# Schema for:
#   * 'show run policy-map {name}'
# ==================================================
class ShowRunPolicyMapSchema(MetaParser):

	schema = {
		'policy_map': {
			Any(): {
				'class': {
					Any(): {
						Optional('qos_set'): {
							Optional('ip precedence'): str,
							Optional('qos-group'): str,
							},
						Optional('police'): {
							Optional('cir_bps'): str,
							Optional('pir_bps'): str,
							Optional('cir_bc_bytes'): str,
							Optional('cir_be_bytes'): str,
							Optional('conformed'): str,
							Optional('exceeded'): str,
							},
						Optional('bandwidth_percent'): str,
						Optional('priority_level'): str,
						Optional('target_shape_rate'): str,
						Optional('service_policy'): str,
						Optional('service_policy_input'): str,
						Optional('service_policy_output'): str,
					},
				}
			},
		}
	}


# ===================================
# Parser for:
#   * 'show run policy-map {name}'
# ===================================
class ShowRunPolicyMap(ShowRunPolicyMapSchema):
	
	''' Parser for
		* "show run policy-map {name}"
	'''

	cli_command = ['show run policy-map {name}']

	def cli(self, name, output=None):
		if output is None:
			cmd = self.cli_command[0].format(name=name)
			# Execute command on device
			out = self.device.execute(cmd)
		else:
			out = output

		# Init vars
		config_dict = {}

		# police cir 400000 conform-action transmit  exceed-action drop
		# police cir 100000 pir  70000 conform-action transmit  exceed-action drop
		# police cir 8000000 bc 4000 be 1000 conform-action transmit  exceed-action transmit  violate-action drop
		p1 = re.compile(r'^police +cir +(?P<cir_bps>(\d+))( +pir +(?P<pir_bps>(\d+)))?'
			'( +bc +(?P<cir_bc_bytes>(\d+)))?( +be +(?P<cir_be_bytes>(\d+)))?'
			' +conform-action +(?P<conformed>(\w+)) +exceed-action +(?P<exceeded>(\w+))'
			'( +violate-action +(?P<violated>(\w+)))?$')

		# policy-map L3VPN-out_child
		p1_1 = re.compile(r'^policy-map +(?P<policy_map>([\w\-\_]+))$')

 		# class ARP_in
		p1_2 = re.compile(r'^class +(?P<class_name>([\w\-\_]+))$')

		# shape average 10000000
		# shape average 80000 320 0
		p2 = re.compile(r'^shape +average +(?P<target_shape_rate>(\d+))$')

		# set ip precedence 4
		p3 = re.compile(r'^set +ip +precedence +(?P<ip_precedence>(\w+))$')

		# set qos-group 4
		p4 = re.compile(r'^set +qos-group +(?P<qos_group>(\w+))$')

		# bandwidth percent 25
		p5 = re.compile(r'^bandwidth percent +(?P<bandwidth_percent>(\d+))$')

		# priority level 2
		p6 = re.compile(r'^priority +level +(?P<priority_level>(\d+))$')

		# service-policy input L3VPN-0_in
		p7 = re.compile(r'^service-policy( +(?P<direction>(\w+)))? +(?P<service_policy>([\w\-\_]+))$')

		for line in out.splitlines():

			line = line.strip()

			m = p1_1.match(line)
			if m:
				group = m.groupdict()
				policy_map = m.groupdict()['policy_map']
				config_dict.setdefault('policy_map', {})
				config_dict['policy_map'].setdefault(policy_map, {})
				continue

			m = p1_2.match(line)
			if m:
				group = m.groupdict()
				class_name = m.groupdict()['class_name']
				if 'class' not in config_dict['policy_map']:
					config_dict['policy_map'][policy_map].setdefault('class', {})
				config_dict['policy_map'][policy_map]['class'].setdefault(class_name, {})
				continue

			m = p1.match(line)
			if m:
				group = m.groupdict()
				if 'police' not in config_dict['policy_map'][policy_map]['class'][class_name]:
					config_dict['policy_map'][policy_map]['class'][class_name].setdefault('police', {})
				config_dict['policy_map'][policy_map]['class'][class_name]['police'].update(
					{k: v for k, v in group.items() if v})
				continue

			m = p2.match(line)
			if m:
				group = m.groupdict()
				config_dict['policy_map'][policy_map]['class'][class_name].update(
					{k: v for k, v in group.items() if v})
				continue

			m = p3.match(line)
			if m:
				group = m.groupdict()
				if 'qos_set' not in config_dict['policy_map'][policy_map]['class'][class_name]:
					config_dict['policy_map'][policy_map]['class'][class_name].setdefault('qos_set', {})
				config_dict['policy_map'][policy_map]['class'][class_name]['qos_set'].update(
					{k.replace('_', ' '): v for k, v in group.items() if v})
				continue

			m = p4.match(line)
			if m:
				group = m.groupdict()
				if 'qos_set' not in config_dict['policy_map'][policy_map]['class'][class_name]:
					config_dict['policy_map'][policy_map]['class'][class_name].setdefault('qos_set', {})
				config_dict['policy_map'][policy_map]['class'][class_name]['qos_set'].update(
					{k.replace('_', '-'): v for k, v in group.items() if v})
				continue

			m = p5.match(line)
			if m:
				group = m.groupdict()
				config_dict['policy_map'][policy_map]['class'][class_name].update(
					{k: v for k, v in group.items() if v})
				continue

			m = p6.match(line)
			if m:
				group = m.groupdict()
				config_dict['policy_map'][policy_map]['class'][class_name].update(
					{k: v for k, v in group.items() if v})
				continue

			m = p7.match(line)
			if m:
				group = m.groupdict()
				if m.groupdict()['direction']:
					if m.groupdict()['direction'] == 'input':
						config_dict['policy_map'][policy_map]['class'][class_name]['service_policy_input'] = m.groupdict()['service_policy']
					else:
						config_dict['policy_map'][policy_map]['class'][class_name]['service_policy_output'] = m.groupdict()['service_policy']
				else:
					config_dict['policy_map'][policy_map]['class'][class_name]['service_policy'] = m.groupdict()['service_policy']
				continue

		return config_dict


# ==================================================
# Schema for:
#   * show running-config interface {interface}
# ==================================================
class ShowRunInterfaceSchema(MetaParser):

	schema = {
		'interfaces': {
			Any(): {
				Optional('authentication_control_direction'): str,
                Optional('authentication_event_fail_action'): str,
                Optional('authentication_fallback'): str,
                Optional('authentication_host_mode'): str,
                Optional('authentication_order'): str,
                Optional('authentication_periodic'): bool,
                Optional('authentication_port_control'): str,
                Optional('authentication_priority'): str,
                Optional('authentication_timer_inactivity'): str,
                Optional('authentication_timer_reauthenticate_server'): bool,
                Optional('authentication_violation'): str,
				Optional('carrier_delay'): list,
				Optional('shutdown'): bool,
				Optional('encapsulation_dot1q'): str,
                Optional('description'): str,
                Optional('dot1x_pae_authenticator'): bool,
                Optional('dot1x_timeout_quiet_period'): str,
                Optional('dot1x_timeout_server_timeout'): str,
                Optional('dot1x_timeout_tx_period'): str,
                Optional('ip_arp_inspection_limit_rate'): str,
                Optional('ip_dhcp_snooping_limit_rate'): str,
				Optional('ip_ospf'): {
                    Any(): {
                        'area': str,
                    },
                },
				Optional('ipv4'): {
                    'ip': str,
                    'netmask': str,
                },
				Optional('ipv6'): list,
                Optional('ipv6_ospf'): {
                    Any(): {
                        'area': str,
                    },
				},
				Optional('ipv6_enable'): bool,
                Optional('ipv6_ospfv3'): {
                    Any(): {
                        'area': str,
                    },
                },
                Optional('load_interval'): str,
                Optional('mab'): bool,
				Optional('negotiation_auto'): bool,
                Optional('snmp_trap_link_status'): bool,
                Optional('snmp_trap_mac_notification_change_added'): bool,
                Optional('snmp_trap_mac_notification_change_removed'): bool,
                Optional('spanning_tree_bpduguard'): str,
                Optional('spanning_tree_portfast'): bool,
                Optional('switchport_access_vlan'): str,
                Optional('switchport_mode'): str,
                Optional('switchport_nonegotiate'): str,
				Optional('vrf'): str,
			}
		}
	}


# ==================================================
# Parser for:
#   * show running-config interface {interface}
# ==================================================
class ShowRunInterface(ShowRunInterfaceSchema):
	
	''' Parser for
		* show running-config interface {interface}
	'''

	cli_command = 'show running-config interface {interface}'

	def cli(self, interface, output=None):

		if output is None:
			# Execute command on device
			output = self.device.execute(self.cli_command.format(interface=interface))

		# Init vars
		config_dict = {}

		# interface GigabitEthernet0
		p1 = re.compile(r'^interface +(?P<interface>[\S]+)$')

		# description "Boot lan interface"
		# description ISE Controlled Port
		p2 = re.compile(r'^description +(?P<description>[\S\s]+)$')

		# vrf forwarding Mgmt-intf
		# ip vrf forwarding oam
		p3 = re.compile(r'^(ip )?vrf +forwarding +(?P<vrf>[\S\s]+)$')

		# ip address 10.1.21.249 255.255.255.0
		p4 = re.compile(r'^ip +address +(?P<ip>[\S]+) +(?P<netmask>[\S]+)$')

		# ipv6 address 2001:db8:4:1::1/64
 		# ipv6 address 2001:db8:400:1::2/112
		p5 = re.compile(r'^ipv6 address +(?P<ipv6>[\S\s]+)$')

		# shutdown
		p6 = re.compile(r'^(?P<shutdown>shutdown)$')

		# encapsulation dot1Q 201
		p7 = re.compile(r'^encapsulation +dot1Q +(?P<dot1q>[\d]+)$')

		# carrier-delay up 60
 		# carrier-delay down 60
		p8 = re.compile(r'^carrier-delay +(?P<carrier_delay>[\S\s]+)$')

		# negotiation auto
		# no negotiation auto
		p9 = re.compile(r'^(?P<negotiation>no +)?negotiation +auto$')

		# cdp enable
		p10 = re.compile(r'^cdp +(?P<cdp>enable)$')

		# no keepalive
		p11 = re.compile(r'^(?P<keepalive>no +)?keepalive$')

		# switchport access vlan 70
		p12 = re.compile(r'^switchport +access +vlan +(?P<vlan>[\d]+)$')

		# switchport mode access
		p13 = re.compile(r'^switchport +mode +(?P<switchport_mode>[\S\s]+)$')

		# switchport nonegotiate
		p14 = re.compile(r'^switchport +(?P<nonegotiate>nonegotiate)$')

		# ip arp inspection limit rate 1024
		p15 = re.compile(r'^ip +arp +inspection +limit +rate +(?P<rate>[\d]+)$')

		# load-interval 30
		p16 = re.compile(r'^load-interval +(?P<load_interval>\d+)$')

		# authentication control-direction in
		p17 = re.compile(r'^authentication +control-direction +(?P<direction>\w+)$')

		# authentication event fail action next-method
		p18 = re.compile(r'^authentication +event +fail +action +(?P<action>[\S\s]+)$')

		# authentication host-mode multi-auth
		p19 = re.compile(r'^authentication +host-mode +(?P<host_mode>[\S\s]+)$')

		# authentication order dot1x mab
		p20 = re.compile(r'^authentication +order +(?P<order>[\S\s]+)$')

		# authentication priority dot1x mab
		p21 = re.compile(r'^authentication +priority +(?P<priority>[\S\s]+)$')

		# authentication port-control auto
		p22 = re.compile(r'^authentication +port-control +(?P<port_control>[\S\s]+)$')

		# authentication periodic
		p23 = re.compile(r'^(?P<periodic>authentication periodic)$')

		# authentication timer reauthenticate server
		p24 = re.compile(r'^(?P<reauth>authentication +timer +reauthenticate +server)$')

		# authentication timer inactivity 65535
		p24_1 = re.compile(r'^authentication +timer +inactivity +(?P<inactivity>\d+)$')

		# authentication violation restrict
		p25 = re.compile(r'^authentication +violation +(?P<violation>[\S\s]+)$')

		# authentication fallback dot1x
		p26 = re.compile(r'^authentication +fallback +(?P<fallback>[\S\s]+)$')

		# mab
		p27 = re.compile(r'^(?P<mab>mab)$')

		# snmp trap mac-notification change added
		p28 = re.compile(r'^snmp +trap +mac-notification +change +added$')

		# snmp trap mac-notification change removed
		p29 = re.compile(r'^snmp +trap +mac-notification +change +removed$')

		# no snmp trap link-status
		p30 = re.compile(r'^no +snmp +trap +link-status$')

		# dot1x pae authenticator
		p31 = re.compile(r'^dot1x +pae +authenticator$')

		# dot1x timeout quiet-period 5
		p32 = re.compile(r'^dot1x +timeout +quiet-period +(?P<quiet_period>\d+)$')

		# dot1x timeout server-timeout 10
		p33 = re.compile(r'^dot1x +timeout +server-timeout +(?P<server_timeout>\d+)$')

		# dot1x timeout tx-period 5
		p34 = re.compile(r'^dot1x +timeout +tx-period +(?P<tx_period>\d+)$')

		# spanning-tree portfast
		p35 = re.compile(r'^spanning-tree +portfast$')

		# spanning-tree bpduguard enable
		p36 = re.compile(r'^spanning-tree +bpduguard +(?P<bpduguard>[\S\s]+)$')

		# ip dhcp snooping limit rate 100
		p37 = re.compile(r'^ip +dhcp +snooping +limit +rate +(?P<rate>[\d]+)$')

		# ipv6 enable
		p38 = re.compile(r'^ipv6 enable$')

		# ip ospf 2 area 0
		# ipv6 ospf 1 area 0
		p39 = re.compile(r'^(?P<ip>ip|ipv6) +ospf +(?P<ospf>\d+) +area +(?P<area>[\d]+)$')

		# ospfv3 1 ipv6 area 0
		p40 = re.compile(r'^ospfv3 +(?P<rate>[\d]+) +ipv6 +area +(?P<area>[\d]+)$')

		# channel-group 1 mode active
		p41 = re.compile(r'^channel-group +(?P<group>[\d]+) +mode +(?P<mode>[\w]+)$')

		for line in output.splitlines():
			line = line.strip()

			# interface GigabitEthernet0
			m = p1.match(line)
			if m:
				interface = m.groupdict()['interface']
				intf_dict = config_dict.setdefault('interfaces', {}).setdefault(interface, {})
				continue
			
			# description ISE Controlled Port
			m = p2.match(line)
			if m:
				description = m.groupdict()['description']
				intf_dict.update({'description': description})
				continue
			
			# vrf forwarding Mgmt-intf
			m = p3.match(line)
			if m:
				vrf = m.groupdict()['vrf']
				intf_dict.update({'vrf': vrf})
				continue

			# # ip address 10.1.21.249 255.255.255.0
			m = p4.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'ipv4':{
									'ip': group['ip'],
									'netmask': group['netmask']},
								})
				continue
			
			# ipv6 address 2001:db8:4:1::1/64
			m = p5.match(line)
			if m:
				group = m.groupdict()
				intf_dict.setdefault('ipv6', []).append(group['ipv6'])
				continue

			# shutdown
			m = p6.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'shutdown': True})
				continue

			# encapsulation dot1Q 201
			m = p7.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'encapsulation_dot1q': group['dot1q']})
				continue

			# carrier-delay up 60
 			# carrier-delay down 60
			m = p8.match(line)
			if m:
				group = m.groupdict()
				intf_dict.setdefault('carrier_delay', []).append(group['carrier_delay'])
				continue

			# negotiation auto
			# no negotiation auto
			m = p9.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'negotiation_auto': group['negotiation'] is None})
				continue

			# cdp enable
			m = p10.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'cdp': group['cdp']})
				continue

			# no keepalive
			m = p11.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'keepalive': group['keepalive'] is None})
				continue

			# switchport access vlan 70
			m = p12.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'switchport_access_vlan': group['vlan']})
				continue

			# switchport mode access
			m = p13.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'switchport_mode': group['switchport_mode']})
				continue
			
			# switchport nonegotiate
			m = p14.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'switchport_nonegotiate': group['nonegotiate']})
				continue
			
			# ip arp inspection limit rate 1024
			m = p15.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'ip_arp_inspection_limit_rate': group['rate']})
				continue

			# load-interval 30
			m = p16.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'load_interval': group['load_interval']})
				continue
			
			# authentication control-direction
			m = p17.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_control_direction': group['direction']})
				continue

			# authentication event fail action next-method
			m = p18.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_event_fail_action': group['action']})
				continue

			# authentication host-mode multi-auth
			m = p19.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_host_mode': group['host_mode']})
				continue

			# authentication order dot1x mab
			m = p20.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_order': group['order']})
				continue

			# authentication priority dot1x mab
			m = p21.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_priority': group['priority']})
				continue

			# authentication port-control auto
			m = p22.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_port_control': group['port_control']})
				continue

			# authentication periodic
			m = p23.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_periodic': True})
				continue

			# authentication timer reauthenticate server
			m = p24.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_timer_reauthenticate_server': True})
				continue

			# authentication timer inactivity 65535
			m = p24_1.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_timer_inactivity': group['inactivity']})
				continue

			# authentication violation restrict
			m = p25.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_violation': group['violation']})
				continue

			# authentication fallback dot1x
			m = p26.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'authentication_fallback': group['fallback']})
				continue

			# mab
			m = p27.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'mab': True})
				continue

			# snmp trap mac-notification change added
			m = p28.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'snmp_trap_mac_notification_change_added': True})
				continue

			# snmp trap mac-notification change removed
			m = p29.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'snmp_trap_mac_notification_change_removed': True})
				continue

			# no snmp trap link-status
			m = p30.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'snmp_trap_link_status': False})
				continue

			# dot1x pae authenticator
			m = p31.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'dot1x_pae_authenticator': True})
				continue

			# dot1x timeout quiet-period 5
			m = p32.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'dot1x_timeout_quiet_period': group['quiet_period']})
				continue

			# dot1x timeout server-timeout 10
			m = p33.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'dot1x_timeout_server_timeout': group['server_timeout']})
				continue

			# dot1x timeout tx-period 5
			m = p34.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'dot1x_timeout_tx_period': group['tx_period']})
				continue

			# spanning-tree portfast
			m = p35.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'spanning_tree_portfast': True})
				continue

			# spanning-tree bpduguard enable
			m = p36.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'spanning_tree_bpduguard': group['bpduguard']})
				continue

			# ip dhcp snooping limit rate 100
			m = p37.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'ip_dhcp_snooping_limit_rate': group['rate']})
				continue

			# ipv6 enable
			p38 = re.compile(r'^ipv6 enable$')
			m = p38.match(line)
			if m:
				group = m.groupdict()
				intf_dict.update({'ipv6_enable': True})
				continue

			# ip ospf 2 area 0
			# ipv6 ospf 1 area 0
			p39 = re.compile(r'^(?P<ip>ip|ipv6) +ospf +(?P<ospf>\d+) +area +(?P<area>[\d]+)$')
			m = p39.match(line)
			if m:
				group = m.groupdict()
				ip = group['ip']
				ospf = group['ospf']
				area = group['area']
				intf_dict.setdefault('{}_ospf'.format(ip), {}).setdefault(ospf, {}).update({'area': area})
				continue

			# ospfv3 1 ipv6 area 0
			p40 = re.compile(r'^ospfv3 +(?P<ospfv3>[\d]+) +(?P<ip>ip|ipv6) +area +(?P<area>[\d]+)$')
			m = p40.match(line)
			if m:
				group = m.groupdict()
				ip = group['ip']
				ospf = group['ospfv3']
				area = group['area']
				intf_dict.setdefault('{}_ospfv3'.format(ip), {}).setdefault(ospf, {}).update({'area': area})
				continue

			# channel-group 1 mode active
			p41 = re.compile(r'^channel-group +(?P<group>[\d]+) +mode +(?P<mode>[\w]+)$')
			m = p41.match(line)
			if m:
				group = m.groupdict()
				chg = group['group']
				mode = group['mode']
				intf_dict.setdefault('channel-group', {}).setdefault(chg, {}).update({'mode': mode})
				continue

		return config_dict
