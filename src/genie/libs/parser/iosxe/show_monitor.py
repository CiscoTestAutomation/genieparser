# Python
import re
import xmltodict
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common


# =========================================
# Schema for 'show monitor'
# =========================================
class ShowMonitorSchema(MetaParser):

    ''' Schema for "show monitor" '''

    schema = {
        'session':
            {Any():
                 {'type':str,
                  'status':str,
                  Optional('source_ports'):
                      {Any(): str,
                       },
                  Optional('destination_ports'): str,
                  Optional('destination_ip_address'): str,
                  Optional('destination_erspan_id'): str,
                  Optional('origin_ip_address'): str,
                  Optional('source_erspan_id'): str,
                  Optional('source_ip_address'): str,
                  'mtu': int,
                  },
             },
    }


# =========================================
# Parser for 'show monitor'
# =========================================
class ShowMonitor(ShowMonitorSchema):
    ''' Parser for
      "show monitor"
      "show monitor session all

    '''

    cli_command = ['show monitor', 'show monitor session {session}']

    def cli(self, session="", output=None):
        if output is None:
            if session:
                cmd = self.cli_command[-1].format(session=session)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
            #out = self.device.execute(self.cli_command.format(session=session))
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Session 1
        p1 = re.compile('Session +(?P<session>(\d+))')

        # Type                   : ERSPAN Source Session
        p2 = re.compile('^Type +: +(?P<type>([a-zA-Z\s]+))$')

        # Status                 : Admin Enabled
        p3 = re.compile('^Status +: +(?P<status>([a-zA-Z\s]+))$')

        # Source Ports           :
        p4_1 = re.compile('^Source +Ports +:$')

        #    TX Only            : Gi0/1/4
        #    Both               : Gi0/1/4
        p4_2 = re.compile('(?P<key>(TX Only|Both)) *: +(?P<intf>(\S+))$')

        # Destination IP Address : 172.18.197.254
        p5 = re.compile('^Destination +IP +Address +: +(?P<destination_ip_address>([0-9\.\:]+))$')

        # MTU                    : 1464
        p6 = re.compile('^MTU +: +(?P<mtu>([0-9]+))$')

        # Destination ERSPAN ID  : 1
        p7 = re.compile('^Destination +ERSPAN +ID +: +(?P<destination_erspan_Id>([0-9]+))$')

        # Origin IP Address      : 172.18.197.254
        p8 = re.compile('^Origin +IP +Address +: +(?P<origin_ip_address>([0-9\.\:]+))$')

        # Destination Ports      : Gi0/1/6 Gi0/1/2
        p9 = re.compile('^Destination +Ports +: +(?P<destination_ports>([a-zA-Z0-9\/\s]+))$')

        # Source IP Address      : 172.18.197.254
        p10 = re.compile('^Source +IP +Address +: +(?P<source_ip_address>([0-9\.\:]+))$')

        # Source ERSPAN ID       : 1
        p11 = re.compile('^Source +ERSPAN +ID +: +(?P<source_erspan_Id>([0-9]+))$')

        for line in out.splitlines():
            line = line.strip()

            # Session 1
            m = p1.match(line)
            if m:
                session = m.groupdict()['session']
                session_dict = ret_dict.setdefault('session', {}).setdefault(session, {})
                continue

            # Type                   : ERSPAN Source Session
            m = p2.match(line)
            if m:
                session_dict['type'] = str(m.groupdict()['type'])
                continue

            # Status                 : Admin Enabled
            m = p3.match(line)
            if m:
                session_dict['status'] = str(m.groupdict()['status'])
                continue

            # Source Ports           :
            m = p4_1.match(line)
            if m:
                src_ports_dict = session_dict.setdefault('source_ports', {})
                continue

            #    TX Only            : Gi0/1/4
            #    Both               : Gi0/1/4
            m = p4_2.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace(" ", "_")
                # Set keys
                src_ports_dict[key] = group['intf']
                continue

            # Destination IP Address : 172.18.197.254
            m = p5.match(line)
            if m:
                session_dict['destination_ip_address'] = str(m.groupdict()['destination_ip_address'])
                continue

            # MTU                    : 1464
            m = p6.match(line)
            if m:
                session_dict['mtu'] = int(m.groupdict()['mtu'])
                continue

            # Destination ERSPAN ID  : 1
            m = p7.match(line)
            if m:
                session_dict['destination_erspan_id'] = str(m.groupdict()['destination_erspan_Id'])
                continue

            # Origin IP Address      : 172.18.197.254
            m = p8.match(line)
            if m:
                session_dict['origin_ip_address'] = str(m.groupdict()['origin_ip_address'])
                continue

            # Destination Ports      : Gi0/1/6 Gi0/1/2
            m = p9.match(line)
            if m:
                session_dict['destination_ports'] = str(m.groupdict()['destination_ports'])
                continue
            # Source IP Address      : 172.18.197.254
            m = p10.match(line)
            if m:
                session_dict['source_ip_address'] = str(m.groupdict()['source_ip_address'])
                continue

            # Source ERSPAN ID       : 1
            m = p11.match(line)
            if m:
                session_dict['source_erspan_id'] = str(m.groupdict()['source_erspan_Id'])
                continue

        return ret_dict
