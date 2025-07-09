''' show_access-list.py
Parser for the following show commands:
    * show access-list
'''

# Python
import re
import ipaddress

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

# ==============================
# Schema for 'show access-list'
# ==============================
class ShowAccessListSchema(MetaParser):
    """Schema for
        * show access-list
    """

    schema = {
        'acl': {
            Any(): {
                'aces': {
                    Any(): {
                        'comments': list,
                        'elements': {
                            Any(): {
                                'destinations': list,
                                'sources': list,
                                'proto': str,
                                'port_range': tuple,
                                'hitcnt': int,
                                'action': str,
                            }
                        }
                    }
                }
            }
        }
    }

# ==============================
# Parser for 'show access-list'
# ==============================

def acl_no_sub_elements(lines, n):
    """return true if this is a single line acl with no expanded sub-elements"""
    # Check if the next line is a not a sub-element
    # First check if we are at a config line at the end of this ACL
    # If so this is a one line ACL with no sub-elements and to be included
    if n + 1 == len(lines):
        return True

    if not is_element(lines[n + 1]):
        return True


def get_port_number(port_name):
    """return the port as an integer"""
    x = ''' aol                              5120
  bgp                              179
  chargen                          19
  cifs                             3020
  citrix-ica                       1494
  cmd                              514
  ctiqbe                           2748
  daytime                           13
  discard                            9
  domain                            53
  echo                               7
  exec                              512
  finger                            79
  ftp                               21
  ftp-data                           20
  gopher                             70
  h323                              1720
  hostname                          101
  http                              80
  https                             443
  ident                             113
  imap4                             143
  irc                               194
  kerberos                          88
  klogin                            543
  kshell                            544
  ldap                              389
  ldaps                             636
  login                             513
  lotusnotes                        1352
  lpd                                515
  netbios-ssn                        139
  nfs                             2049
  nntp                            119
  ntp                               123
  pcanywhere-data                 5631
  pim-auto-rp                     496
  pop2                            109
  pop3                            110
  pptp                            1723
  rsh                             514
  rtsp                            554
  sip                             5060
  smtp                            25
  sqlnet                          1522
  ssh                             22
  sunrpc                          111
  syslog                          514
  snmp                            162
  snmptrap                     161
  tacacs                          49
  talk                            517
  telnet                          23
  uucp                            540
  whois                           43
  www                             80'''

    x = {y.split()[0]: int(y.split()[1]) for y in x.splitlines()}
    if port_name in x:
        return x[port_name]
    else:
        try:
            return int(port_name)
        except ValueError:
            return port_name


def rule_hitcnt(line):
    """return the hit count as an integer"""
    if 'hitcnt' in line:
        x = re.search(r'hitcnt=(\d+)', line)
        if x:
            # Convert hit count to int and return
            return int(x.group(1))


def is_element(line):
    """return true for any rule elements beneath a rule config line"""
    if line[:11] != 'access-list':
        return True


def range_subnets(ip1, ip2):
    """return the subnets the cover the range of IPs"""
    x = ipaddress.summarize_address_range(ipaddress.ip_address(ip1), ipaddress.ip_address(ip2))
    return list(x)


def get_rule_terms(line):
    """return source and destination ip, network or range"""

    # Get the action - permit or deny
    action = line.split()[5]

    # First sub out "any" with 0.0.0.0/0
    line = re.sub('any4', '0.0.0.0 0.0.0.0', line)
    line = re.sub('any', '0.0.0.0 0.0.0.0', line)

    # Service Port matching Regexes
    svc_port = re.compile(r'eq\s\S+\s\(hitcnt')
    svc_range = re.compile(r'range \S+\s\S+\s\(hitcnt')
    svc_port_gt = re.compile(r'gt\s\S+\s\(hitcnt')

    # Protocol Regex
    svc_proto = re.compile(r'tcp|udp|icmp|ip')

    # Source and destination Regexes
    host_host = re.compile(r"host (\d+\.){3}\d+ host (\d+\.){3}\d+")
    host_net = re.compile(r"host (\d+\.){3}\d+ (\d+\.){3}\d+ (\d+\.){3}\d+")
    net_host = re.compile(r"(\d+\.){3}\d+ (\d+\.){3}\d+ host (\d+\.){3}\d+")
    net_net = re.compile(r"(\d+\.){3}\d+ (\d+\.){3}\d+ (\d+\.){3}\d+ (\d+\.){3}\d+")

    # Source and destination ranges Regexes
    host_range = re.compile(r"host (\d+\.){3}\d+ range (\d+\.){3}\d+ (\d+\.){3}\d+")
    range_host = re.compile(r"range (\d+\.){3}\d+ (\d+\.){3}\d+ host (\d+\.){3}\d+")
    net_range = re.compile(r"(\d+\.){3}\d+.*(\d+\.){3}\d+ range (\d+\.){3}\d+ (\d+\.){3}\d+")
    range_net = re.compile(r"range (\d+\.){3}\d+ (\d+\.){3}\d+ (\d+\.){3}\d+ (\d+\.){3}\d+")
    range_range = re.compile(r"range (\d+\.){3}\d+ (\d+\.){3}\d+ range (\d+\.){3}\d+ (\d+\.){3}\d+")

    m_range_host = range_host.search(line)
    m_host_range = host_range.search(line)
    m_net_range = net_range.search(line)
    m_range_net = range_net.search(line)
    m_range_range = range_range.search(line)

    m_host_host = host_host.search(line)
    m_host_net = host_net.search(line)
    m_net_host = net_host.search(line)
    m_net_net = net_net.search(line)

    m_svc_range = svc_range.search(line)
    m_svc_port = svc_port.search(line)
    m_svc_proto = svc_proto.search(line)
    m_svc_port_gt = svc_port_gt.search(line)

    # Set the port range var based on what matches for the service port.
    # Set the port_range var to a tuple of ints for.
    # if one port then same int for start and end - e.g. (80, 80)
    if m_svc_range:
        port_range = tuple(get_port_number(x) for x in
                           [m_svc_range.group(0).split()[1], m_svc_range.group(0).split()[2]])
    elif m_svc_port:
        port_range = tuple(get_port_number(x) for x in
                           [m_svc_port.group(0).split()[1], m_svc_port.group(0).split()[1]])
    elif m_svc_port_gt:
        port_range = tuple([get_port_number(m_svc_port_gt.group(0).split()[1]), get_port_number('65536')])

    # If nothing matches set to 0, 0
    else:
        print('No Match Port', line)
        port_range = (0, 0)

    # Check if the protocol was found
    if m_svc_proto:
        proto = m_svc_proto.group(0)
    else:
        print('No Match Proto', line)
        proto = 'None'

    # Set the dest and src vars - list of IP network objects
    # Convert ranges to a list of IP network objects
    # !!! Keep these in the correct order since some matches at the bottom
    # Can overlap with matches at the top !!!
    if m_host_host:
        split_it = m_host_host.group(0).split()
        dest = [ipaddress.ip_network(split_it[-1], '/32')]
        src = [ipaddress.ip_network(split_it[1])]
    elif m_range_host:
        split_it = m_range_host.group(0).split()
        dest = [ipaddress.ip_network(split_it[-1], '/32')]
        src = range_subnets(split_it[1], split_it[2])
    elif m_range_net:
        split_it = m_range_net.group(0).split()
        dest = [ipaddress.ip_network('/'.join(split_it[-2:]))]
        src = range_subnets(split_it[1], split_it[2])
    elif m_range_range:
        split_it = m_range_range.group(0).split()
        dest = range_subnets(split_it[-2], split_it[-1])
        src = range_subnets(split_it[1], split_it[2])
    elif m_host_net:
        split_it = m_host_net.group(0).split()
        dest = [ipaddress.ip_network('/'.join(split_it[-2:]))]
        src = [ipaddress.ip_network(split_it[1], '/32')]
    elif m_host_range:
        split_it = m_host_range.group(0).split()
        dest = range_subnets(split_it[-2], split_it[-1])
        src = [ipaddress.ip_network(split_it[1], '/32')]
    elif m_net_host:
        split_it = m_net_host.group(0).split()
        dest = [ipaddress.ip_network(split_it[-1])]
        src = [ipaddress.ip_network('/'.join(split_it[:2]))]
    elif m_net_net:
        split_it = m_net_net.group(0).split()
        dest = [ipaddress.ip_network('/'.join(split_it[-2:]))]
        src = [ipaddress.ip_network('/'.join(split_it[:2]))]
    elif m_net_range:
        split_it = m_net_range.group(0).split()
        dest = range_subnets(split_it[-2], split_it[-1])
        src = [ipaddress.ip_network('/'.join(split_it[:2]))]
    else:
        print('No Match', line)
        dest = []
        src = []
    return [str(x) for x in src], [str(x) for x in dest], proto, port_range, rule_hitcnt(line), action


def get_remarks(lines, n):
    """returns the comments related to this ACE config line"""
    # Traverse back through the lines to get all comments above
    # decrement line counter
    n = n - 1
    if 'remark' in lines[n]:
        return [lines[n]] + get_remarks(lines, n)
    else:
        return []


def add_element(add_2_dict, line, line_key, acl):
    """Adds in the ACE element to the dictionary"""
    src_s, dst_s, proto, port_range, hitcnt, action = get_rule_terms(line)
    add_2_dict.setdefault('acl', {}). \
        setdefault(acl, {}). \
        setdefault('aces', {}). \
        setdefault(line_key, {}). \
        setdefault('elements', {}). \
        setdefault(line, {})

    add_2_dict['acl'][acl]['aces'][line_key]['elements'][line] \
        ['sources'] = src_s
    add_2_dict['acl'][acl]['aces'][line_key]['elements'][line] \
        ['destinations'] = dst_s
    add_2_dict['acl'][acl]['aces'][line_key]['elements'][line] \
        ['proto'] = proto
    add_2_dict['acl'][acl]['aces'][line_key]['elements'][line] \
        ['port_range'] = port_range
    add_2_dict['acl'][acl]['aces'][line_key]['elements'][line] \
        ['hitcnt'] = hitcnt
    add_2_dict['acl'][acl]['aces'][line_key]['elements'][line] \
        ['action'] = action


def is_ace(line):
    """check if the line is an ace"""
    if 'hitcnt=' in line:
        return True


# The parser class inherits from the schema class
class ShowAccessList(ShowAccessListSchema):
    ''' Parser for "show access-list"'''

    cli_command = 'show access-list'

    # Defines a function to run the cli_command
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Initializes the Python dictionary variable
        parsed_dict = {}

        # Defines the "for" loop, to pattern match each line of output
        lines = out.splitlines()
        for n, line in enumerate(lines):
            # Check if this line is an ACE
            if is_ace(line):
                # Check if this is the config level ACE
                if not is_element(line):
                    # If this is the config part of the ACE use this as the key
                    line_key = line
                    # Get the ACL Name - one per interface and/or global
                    acl = line.split()[1]

                    # Add in this line as a key and get the comments.
                    parsed_dict.setdefault('acl', {}). \
                        setdefault(acl, {}). \
                        setdefault('aces', {}). \
                        setdefault(line_key, {})
                    # Reverse the order of the comments since
                    # The get_remarks func returns them backwards.
                    parsed_dict['acl'][acl]['aces'][line_key]\
                        ['comments'] = get_remarks(lines, n)[::-1]

                    # Check if this rule has no sub elements
                    # If so add all details here
                    if acl_no_sub_elements(lines, n):
                        add_element(parsed_dict, line, line_key, acl)
                else:
                    # if this is an ACE element
                    # Then parse out details
                    add_element(parsed_dict, line.strip(), line_key, acl)

        return parsed_dict
