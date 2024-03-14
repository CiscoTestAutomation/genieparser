from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
import re


class DisplayInterfaceSchema(MetaParser):
    schema = {
            Any(): {
                Optional('ip_address'): str,
                Optional('subnet_prefix'): str,
                Optional('subnet_mask'): str,
                Optional('admin_status'): str,
                Optional('crc_errors'): str,
                Optional('line_status'): bool,
                Optional('line_up_since'): str,
                Optional('interface_description'): str,
                Optional('mtu'): int,
                Optional('cellular_info'):
                    {
                        Optional('ip_address'): str,
                        Optional('subnet_prefix'): str,
                        Optional('subnet_mask'): str,
                        Optional('modem_state'): str,
                        Optional('modem_model'): str,
                        Optional('wireless_technology'): str,
                        Optional('rssi'): str,
                        Optional('sinr'): str,
                    },
                Optional('time_last_up'): str,
                Optional('system_info'): str,
                Optional('input_packets'): str,
                Optional('input_bytes'): str,
                Optional('output_packets'): str,
                Optional('output_bytes'): str,
                Optional('output_rate_packets'): str,
                Optional('output_rate_bits'): str,
                Optional('input_rate_bits'): str,
                Optional('input_rate_packets'): str,
                Optional('system_time'): str,
                Optional('port_mode'): str,
                Optional('port_speed'): str,
                Optional('port_negotiation'): str,
                Optional('mac_address'): str,
            }
    }


class DisplayInterface(DisplayInterfaceSchema):
    """parser for display interface
                  display interface <interface>"""

    cli_command = ['display interface', 'display interface {interface}']

    @staticmethod
    def translater_cidr_netmask(cidr):
        """
        # to convert prefix to subnetmask. huawei only shows prefix len
        Translate CIDR to netmask notation.
        :param cidr:
        :return: netmask as string
        """
        return '.'.join(
            [str((m >> (3 - i) * 8) & 0xff) for i, m in enumerate(
                [-1 << (32 - int(cidr))] * 4)]
        )

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        ####### GENERAL
        # Atm0/0/0 current state : UP
        # GigabitEthernet0/0/0 current state : Administratively DOWN
        # LoopBack0 current state : DOWN

        p1 = re.compile(r'^(?P<interface>[\w\/\.\-\:]+) +current +state +:(?P<admin_status>[\w\s]+$)')

        # Line protocol current state : UP
        # Line protocol current state : DOWN
        p2 = re.compile(
            r'^Line +protocol +current +state +: +(?P<line_status>[\w\s]+$)')

        # Last line protocol up time : 2022-01-24 12:00:41
        p3 = re.compile(
            r'^Last line +protocol +up +time +: +(?P<line_up_since>.*$)')

        # ex: Description:145.7.64.247 Backup Link
        p4 = re.compile(r'^Description: *(?P<interface_description>.*)$')

        # Route Port,The Maximum Transmit Unit is 1500
        # Switch Port, TPID : 8100(Hex), The Maximum Transmit Unit is 1500
        p5 = re.compile(r'^.*The Maximum Transmit Unit is (?P<mtu>\d+)')

        # Last physical up time   : 2022-01-24 12:00:41
        p6 = re.compile(r'^Last physical up time \s+:\s+(?P<time_last_up>.*$)')

        # Last physical down time : 2022-01-24 11:56:21
        p7 = re.compile(r'^Last physical down time \s+:\s+(?P<time_last_down>.*$)')

        # Current system time: 2022-01-27 11:41:40+01:00
        p8 = re.compile(r'^Current system time:\s+(?P<system_time>.*$)')

        # Input:  69561 packets, 7394401 bytes
        p9 = re.compile(r'^Input:\s+(?P<input_packets>\d+).*,\s+(?P<input_bytes>\d+)')

        # Output:  69361 packets, 739411401 bytes
        p10 = re.compile(r'^Output:\s+(?P<output_packets>\d+).*,\s+(?P<output_bytes>\d+)')

        # default is 30. people can change that.
        # not sure if i should handle that no usecase for it
        # Last 30 seconds input rate 3856 bits/sec, 3 packets/sec
        p11 = re.compile(r'^Last \d+ seconds input rate (?P<input_rate_bits>\d+) .*,\s+(?P<input_rate_packets>\d+)')

        # Last 30 seconds output rate 4504 bits/sec, 3 packets/sec
        p12 = re.compile(r'^Last \d+ seconds output rate (?P<output_rate_bits>\d+) .*,\s+(?P<output_rate_packets>\d+)')

        # Port Mode: COMMON COPPER
        # Port Mode: AUTO
        p13 = re.compile(r'^Port Mode:\s+(?P<port_mode>.*$)')

        # port speed settings can be 1000/100/10/AUTO
        # we dont need the Loopback part
        # Speed : 1000,  Loopback: NONE
        # Speed : AUTO,  Loopback: NONE
        p14 = re.compile(r'^Speed\s+:\s+(?P<port_speed>\d+|\w+),')

        # Duplex: FULL, Negotiation: ENABLE
        p15 = re.compile(r'^Duplex:\s+(?P<port_speed>\d+|\w+),\s+Negotiation:\s+(?P<port_negotiation>.*$)')

        # IP Sending Frames' Format is PKTFMT_ETHNT_2, Hardware address is c444-7d9c-77c9
        p16 = re.compile(r'^IP Sending Frames\' .*Hardware address is\s+(?P<mac_address>[\d\w]{0,4}-[\d\w]{0,4}-[\d\w]{0,4})$')

        #  note below begins with 2 leading spaces in the cli
        #   CRC:                      0,  Giants:                      0
        p17 = re.compile(r'^.*CRC:\s+(?P<crc_errors>.*(?=,))')

        ####### ROUTED port Interfaces

        # Internet Address is 10.1.1.132/32
        p1_routed = re.compile('^Internet Address is (?P<ip>[0-9\.x]+)\/(?P<prefix_length>[0-9]+)$')

        ####### CELLULAR Interfaces
        # Internet Address is negotiated, 10.124.234.33/32
        p1_cellular = re.compile(r'^Internet Address is negotiated, (?P<ip>[0-9\.x]+)\/(?P<prefix_length>[0-9]+)')

        # Current Network Connection = LTE(LTE)
        p2_cellular = re.compile(r'^Current Network Connection\s+=\s+(?P<wireless_technology>.*$)')

        # Current RSSI = -67 dBm
        p3_cellular = re.compile(r'^Current RSSI\s+=\s+(?P<rssi>.*$)')

        # Current SINR = 17 dB (good)
        p4_cellular = re.compile(r'^Current SINR\s+=\s+(?P<sinr>.*$)')

        # Modem State: Present
        p5_cellular = re.compile(r'^Modem State:\s+(?P<modem_state>.*)$')

        # below mean modem model
        # Model = EP06
        p6_cellular = re.compile(r'^Model\s+=\s+(?P<modem_model>.*)$')

        interface_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # we match an interface name and state and continue with that
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_state = m.groupdict()['admin_status']

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                if 'ellular' in interface:
                    interface_dict[interface]['cellular_info'] = {}

                interface_dict[interface]['admin_status'] = interface_state

            m = p2.match(line)
            if m:
                line_status = m.groupdict()['line_status']
                if 'UP' in line_status:
                    interface_dict[interface]['line_status'] = True
                else:
                    interface_dict[interface]['line_status'] = False

            m = p3.match(line)
            if m:
                interface_dict[interface]['line_up_since'] = m.groupdict()[
                    'line_up_since']

            m = p4.match(line)
            if m:
                interface_dict[interface]['interface_description'] = \
                    m.groupdict()['interface_description']

            m = p5.match(line)
            if m:
                interface_dict[interface]['mtu'] = int(m.groupdict()['mtu'])

            m = p6.match(line)
            if m:
                interface_dict[interface]['time_last_up'] = \
                    m.groupdict()['time_last_up']

            m = p7.match(line)
            if m:
                interface_dict[interface]['time_last_down'] = m.groupdict()[
                    'time_last_down']

            m = p8.match(line)
            if m:
                interface_dict[interface]['system_time'] = m.groupdict()[
                    'system_time']

            m = p9.match(line)
            if m:
                interface_dict[interface]['input_packets'] = m.groupdict()[
                    'input_packets']
                interface_dict[interface]['input_bytes'] = m.groupdict()[
                    'input_bytes']

            m = p10.match(line)
            if m:
                interface_dict[interface]['output_packets'] = m.groupdict()[
                    'output_packets']
                interface_dict[interface]['output_bytes'] = m.groupdict()[
                    'output_bytes']

            m = p11.match(line)
            if m:
                interface_dict[interface]['input_rate_bits'] = m.groupdict()[
                    'input_rate_bits']
                interface_dict[interface]['input_rate_packets'] = m.groupdict()[
                    'input_rate_packets']

            m = p12.match(line)
            if m:
                interface_dict[interface]['output_rate_bits'] = m.groupdict()[
                    'output_rate_bits']
                interface_dict[interface]['output_rate_packets'] = m.groupdict()[
                    'output_rate_packets']

            m = p13.match(line)
            if m:
                interface_dict[interface]['port_mode'] = m.groupdict()[
                    'port_mode']

            m = p14.match(line)
            if m:
                interface_dict[interface]['port_speed'] = m.groupdict()[
                    'port_speed']

            m = p15.match(line)
            if m:
                interface_dict[interface]['port_speed'] = m.groupdict()[
                    'port_speed']
                interface_dict[interface]['port_negotiation'] = m.groupdict()[
                    'port_negotiation']

            m = p16.match(line)
            if m:
                interface_dict[interface]['mac_address'] = m.groupdict()[
                    'mac_address']

            m = p17.match(line)
            if m:
                interface_dict[interface]['crc_errors'] = m.groupdict()[
                    'crc_errors']

            m = p1_routed.match(line)
            if m:
                ip_address = m.groupdict()['ip']
                subnet_prefix = m.groupdict()['prefix_length']
                subnet_mask = self.translater_cidr_netmask(
                    m.groupdict()['prefix_length']
                )

                interface_dict[interface]['ip_address'] = ip_address
                interface_dict[interface]['subnet_prefix'] = subnet_prefix
                interface_dict[interface]['subnet_mask'] = subnet_mask

            m_cellular = p1_cellular.match(line)
            if m_cellular:
                ip_address = m_cellular.groupdict()['ip']
                subnet_prefix = m_cellular.groupdict()['prefix_length']
                subnet_mask = self.translater_cidr_netmask(
                    m_cellular.groupdict()['prefix_length']
                )

                interface_dict[interface]['cellular_info']['ip_address'] \
                    = ip_address
                interface_dict[interface]['cellular_info']['subnet_prefix'] \
                    = subnet_prefix
                interface_dict[interface]['cellular_info']['subnet_mask'] \
                    = subnet_mask

            m_cellular = p2_cellular.match(line)
            if m_cellular:
                interface_dict[
                    interface]['cellular_info']['wireless_technology'] \
                    = m_cellular.groupdict()['wireless_technology']

            m_cellular = p3_cellular.match(line)
            if m_cellular:
                interface_dict[
                    interface]['cellular_info']['rssi'] \
                    = m_cellular.groupdict()['rssi']

            m_cellular = p4_cellular.match(line)
            if m_cellular:
                interface_dict[
                    interface]['cellular_info']['sinr'] \
                    = m_cellular.groupdict()['sinr']

            m_cellular = p5_cellular.match(line)
            if m_cellular:
                interface_dict[
                    interface]['cellular_info']['modem_state'] \
                    = m_cellular.groupdict()['modem_state']

            m_cellular = p6_cellular.match(line)
            if m_cellular:
                interface_dict[
                    interface]['cellular_info']['modem_model'] \
                    = m_cellular.groupdict()['modem_model']

        return(interface_dict)