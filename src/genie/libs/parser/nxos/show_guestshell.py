"""show_guestshell.py

NX-OS parser for the following show command:
    * show guestshell
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser


# ============================
# Schema for "show guestshell"
# ============================
class ShowGuestshellSchema(MetaParser):
    """Schema for "show guestshell"."""

    schema = {
        'state': str,
        'info': {
            'package_location': str,
            'version' : str,
            'description' : str,
            'signing_key_type': str,
        },
        'resource_reservation': {
            'disk': int,
            'memory': int,
            'cpu': int,
        }
    }


# ============================
# Parser for "show guestshell"
# ============================
class ShowGuestshell(ShowGuestshellSchema):
    """Parser for "show guestshell"."""

    cli_command = "show guestshell"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        guestshell_dict = {}

        # State                 : Activated
        p1 = re.compile(r'^State +: +(?P<state>.+)$')

        # Package information
        #   Name                : guestshell.ova
        #   Path                : /isanboot/bin/guestshell.ova
        p2 = re.compile(r'^Path +: +(?P<path>.+)$')

        # Application
        #   Name              : GuestShell
        #   Installed version : 2.4(0.0)
        #   Description       : Cisco Systems Guest Shell
        p3 = re.compile(r'^Installed +version +: +(?P<version>.+)$')
        p4 = re.compile(r'^Description +: +(?P<description>.+)$')

        # Signing
        #   Key type          : Cisco release key
        #   Method            : SHA-1
        p5 = re.compile(r'^Key +type +: +(?P<key_type>.+)$')

        # Licensing
        #   Name              : None
        #   Version           : None
        # Resource reservation
        #   Disk                : 1000 MB
        #   Memory              : 500 MB
        #   CPU                 : 1% system CPU
        p6 = re.compile(r'^Disk +: +(?P<disk>\d+) +MB$')
        p7 = re.compile(r'^Memory +: +(?P<memory>\d+) +MB$')
        p8 = re.compile(r'^CPU +: +(?P<cpu>\d+)% system CPU')

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                guestshell_dict['state'] = match.groupdict()['state'].lower()
                continue

            match = p2.match(line)
            if match:
                path = match.groupdict()['path']
                if 'info' not in guestshell_dict:
                    guestshell_dict['info'] = {}
                guestshell_dict['info']['package_location'] = path
                continue

            match = p3.match(line)
            if match:
                version = match.groupdict()['version']
                if 'info' not in guestshell_dict:
                    guestshell_dict['info'] = {}
                guestshell_dict['info']['version'] = version
                continue

            match = p4.match(line)
            if match:
                description = match.groupdict()['description']
                if 'info' not in guestshell_dict:
                    guestshell_dict['info'] = {}
                guestshell_dict['info']['description'] = description
                continue

            match = p5.match(line)
            if match:
                key_type = match.groupdict()['key_type']
                if 'info' not in guestshell_dict:
                    guestshell_dict['info'] = {}
                guestshell_dict['info']['signing_key_type'] = key_type
                continue

            match = p6.match(line)
            if match:
                disk = int(match.groupdict()['disk'])
                if 'resource_reservation' not in guestshell_dict:
                    guestshell_dict['resource_reservation'] = {}
                guestshell_dict['resource_reservation']['disk'] = disk
                continue

            match = p7.match(line)
            if match:
                memory = int(match.groupdict()['memory'])
                if 'resource_reservation' not in guestshell_dict:
                    guestshell_dict['resource_reservation'] = {}
                guestshell_dict['resource_reservation']['memory'] = memory
                continue

            match = p8.match(line)
            if match:
                cpu = int(match.groupdict()['cpu'])
                if 'resource_reservation' not in guestshell_dict:
                    guestshell_dict['resource_reservation'] = {}
                guestshell_dict['resource_reservation']['cpu'] = cpu
                continue

        return guestshell_dict
