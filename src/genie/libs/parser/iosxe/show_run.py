''' show_run.py

IOSXE parsers for the following show commands:
	* 'show run policy-map {name}'
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

			# import pdb; pdb.set_trace()
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