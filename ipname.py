import os
import re
import sys
from ipaddress import ip_address, IPv4Address, IPv4Network

classA = IPv4Network(("0.0.0.0", "128.0.0.0"))  # or IPv4Network("10.0.0.0\8")
classB = IPv4Network(("128.0.0.0", "192.0.0.0"))  # or IPv4Network("172.16.0.0\12")
classC = IPv4Network(("192.0.0.0", "224.0.0.0"))  # or IPv4Network("192.168.0.0\16")

paths = [
        '/pypi/genieparser/src/genie/libs/parser/iosxr/show_bgp.py',
        '/pypi/genieparser/src/genie/libs/parser/iosxr/tests/test_show_bgp.py',

]

keywords = {
        # KDDI
	'9996': '65109',
	'KDDI': 'CISCO',
	'JST': 'EST',
	# Bell
	'bell.ca': 'cisco.com',
	'-tatooine.net': '-genie',
	'novi2.dev': 'genie.dev',
        # other
        '50996': '65109',
}

review_dict = {}
review_dict.setdefault('private_address', {})

# process each file
def process(file_path):
	if '.py' in file_path and '.pyc' not in file_path and '.json' not in file_path and '.png' not in file_path and '.git' not in file_path:
		print('Checking '+file_path+'...')
		p4 = re.compile(r'(?P<ipaddress>((?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(?:(?<!\.)\b|\.)){4})')

		# from https://www.regextester.com/96774
		p6 = re.compile(r'(?P<v6address>(?:(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){6})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:::(?:(?:(?:[0-9a-fA-F]{1,4})):){5})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){4})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,1}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){3})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,2}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:(?:[0-9a-fA-F]{1,4})):){2})(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,3}(?:(?:[0-9a-fA-F]{1,4})))?::(?:(?:[0-9a-fA-F]{1,4})):)(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,4}(?:(?:[0-9a-fA-F]{1,4})))?::)(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9]))\.){3}(?:(?:25[0-5]|(?:[1-9]|1[0-9]|2[0-4])?[0-9])))))))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,5}(?:(?:[0-9a-fA-F]{1,4})))?::)(?:(?:[0-9a-fA-F]{1,4})))|(?:(?:(?:(?:(?:(?:[0-9a-fA-F]{1,4})):){0,6}(?:(?:[0-9a-fA-F]{1,4})))?::)))))')

		with open(file_path, 'r') as f:
			for line in f.readlines():
				m6 = p6.findall(line)
				if m6:
					for item in m6:
						ipaddress = item
						ipaddress2 = ''
						try:
							a = ip_address(ipaddress)
							#print('IPv6 Address:', ipaddress)
						except:
							#print('Invalid IPv6 Address:', ipaddress)
							continue
						# ignore SNMP MIB which accidentaly match v6 regex
						if 'B::' == ipaddress or 'tcl' in line or 'State::' in line:
							pass
						elif not ip_address(ipaddress).is_private and not ip_address(ipaddress).is_link_local and not ip_address(ipaddress).is_multicast:
							#print('Global IPv6 Address:', ipaddress)
							v6_list = ip_address(ipaddress).exploded.split(':')
							# 20:1:2:3::1
							# 2001:(20+2)**2/65535:(1+3)**2/65535::1
							oct1 = int('0x'+v6_list[0], 16)
							oct2 = int('0x'+v6_list[1], 16)
							oct3 = ((int('0x'+v6_list[2], 16) + oct1)**2)%65535
							oct4 = ((int('0x'+v6_list[3], 16) + oct2)**2)%65535
							v6_list[0] = '2001'
							v6_list[1] = 'db8'
							# 65531 -> 0xfffb -> fffb
							v6_list[2] = hex(oct3)[2::]
							v6_list[3] = hex(oct4)[2::]
							ipaddress2 = ip_address(':'.join(v6_list)).compressed
							if ipaddress.isupper():
								ipaddress2 = ipaddress2.upper()
							print('Converted:', ipaddress, '->', ipaddress2)
						elif ip_address(ipaddress).is_multicast:
							#print('Multicast IPv6 Address:', ipaddress)
							pass
						elif ip_address(ipaddress).is_link_local:
							#print('Link-Local IPv6 Address:', ipaddress)
							pass
						else:
							#print('Private IPv6 Address:', ipaddress)
							pass

						if ipaddress2:
							review_dict.setdefault('private_address', {}).setdefault(file_path, {}).setdefault(ipaddress, ipaddress2)

				m4 = p4.findall(line)
				if m4:
					# import pdb; pdb.set_trace()
					for item in m4:
						ipaddress = item[0]
						# if '102.138.135.49' in ipaddress:
						# 	import pdb; pdb.set_trace()
						try:
							a = ip_address(ipaddress)
						except:
							continue
						# import pdb; pdb.set_trace()
						if not ip_address(ipaddress).is_private:
							# import pdb; pdb.set_trace()
							pp4 = re.compile(r'(?P<ip1>\d+)\.(?P<ip2>\d+)\.(?P<ip3>\d+)\.(?P<ip4>\d+)')
							mm4 = pp4.match(ipaddress)
							if mm4:
								ip1 = int(mm4.groupdict()['ip1'])
								ip2 = int(mm4.groupdict()['ip2'])
								ip3 = int(mm4.groupdict()['ip3'])
								ip4 = int(mm4.groupdict()['ip4'])
	
								ipaddr = IPv4Address(ipaddress)
								ip = ''
								if ipaddr in classA:
									ip = '10.'+str(((ip1+ip2)**2)%255)+'.'+str(ip3)+'.'+str(ip4)
								elif ipaddr in classB:
									ip = '172.16.'+str(((ip1+ip2+ip3)**2)%255)+'.'+str(ip4)
								elif ipaddr in classC:
									ip = '192.168.'+str(((ip1+ip2+ip3)**2)%255)+'.'+str(ip4)
								# else: # disabled
								# 	# Multicast or etc
								# 	ip = ipaddress
								if ip:
									review_dict.setdefault('private_address', {}).setdefault(file_path, {}).setdefault(ipaddress, ip)
				
				for k, v in keywords.items():
					p5 = re.compile(r'.*(?P<kw>'+k+').*')
					m5 = p5.findall(line)
					if m5 and '777775555599' not in line:
						for item in m5:
							# import pdb; pdb.set_trace()
							review_dict.setdefault('private_address', {}).setdefault(file_path, {}).setdefault(k, v)

		# import pdb; pdb.set_trace()

		# import pdb; pdb.set_trace()
		file_output = []
		if file_path in review_dict['private_address']:
			print('Updating '+file_path+'...')
			# import pdb; pdb.set_trace()
			with open(file_path, 'r') as f:
				for line in f.readlines():
					# import pdb; pdb.set_trace()

					for before, after in review_dict['private_address'][file_path].items():
						if before in line:
							line = line.replace(before, after)

					for k, v in keywords.items():
						line = line.replace(k,v)
	
					file_output.append(line)
				
			f2 = open(file_path, 'w')
			f2.writelines(file_output)
			f2.close()		

def recursive_file_check(path):
	if os.path.isdir(path):
		files = os.listdir(path)
		for file in files:
			recursive_file_check(path + "/" + file)
	else:
		process(path)

virtual_env = os.environ['VIRTUAL_ENV']
                
for path in paths:
        output_dict = {}
        recursive_file_check(virtual_env+path)
