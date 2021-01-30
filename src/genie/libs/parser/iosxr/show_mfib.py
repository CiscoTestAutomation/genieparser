"""show_mfib.py

IOSXR parsers for the following show commands:
    * show mfib route summary
    * show mfib route summary location {location}
    * show mfib vrf {vrf} route summary
    * show mfib vrf {vrf} route summary location {location}
    * show mfib platform evpn bucket location {location}
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


# ==========================================================================
# Schema for 'show mfib route summary'
# ==========================================================================
class ShowMfibRouteSummarySchema(MetaParser):
    """ Schema for show mfib [vrf <vrf>] route summary. """

    schema = {
        'vrf':
            {Any():
                 {'no_g_routes': int,
                  'no_sg_routes': int,
                  Optional('num_vrfs'): int
                  },
             },
    }


# ==========================================================================
# Parser for 'show mfib route summary'
# ==========================================================================
class ShowMfibRouteSummary(ShowMfibRouteSummarySchema):
    """
    Parser for show mfib [vrf <vrf>] route summary.

    Parameters
    ----------
    device : Router
        Device to be parsed.

    Returns
    -------
    parsed_dict : dict
        Contains the CLI output parsed into a dictionary.

    Examples
    --------
    >>> show_mfib_route_summary(uut1, vrf='all')

    {'vrf':
        {'all':
            {'no_g_routes': 20,
             'no_sg_routes': 176,
             'num_vrfs': 4
            }
        }
    }

    """

    cli_command = ["show mfib route summary",
                   "show mfib vrf {vrf} route summary",
                   "show mfib route summary location {location}",
                   "show mfib vrf {vrf} route summary location {location}"]

    def cli(self, vrf='', location='', output=None):

        if output is None:
            if vrf and location:
                cmd = self.cli_command[3].format(vrf=vrf, location=location)
            elif vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            elif location:
                cmd = self.cli_command[2].format(location=location)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # IP Multicast Forwarding Information Base Summary for VRF vpn1
        p1 = re.compile(r"IP +Multicast +Forwarding +Information +Base +"
                        r"Summary +for +(?:ALL +VRFs|VRF +(?P<vrf>\S+))"
                        r"(?: +\(num +VRFs: +(?P<num_vrfs>\d+)\))?")

        # No. of (*,G) routes = 20
        p2 = re.compile(r"No\. +of +\(\*,G\) +routes += +(?P<no_g_routes>\d+)")

        # No. of (S,G) routes = 176
        p3 = re.compile(r"No\. +of +\(S,G\) +routes += +(?P<no_sg_routes>\d+)")

        for line in out.splitlines():
            line = line.strip()

            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                vrf = group['vrf'] if group['vrf'] else "all"
                vrf_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf, {})

                if vrf == "all":
                    vrf_dict['num_vrfs'] = int(group['num_vrfs'])
                continue

            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                vrf_dict['no_g_routes'] = int(group['no_g_routes'])
                continue

            m3 = p3.match(line)
            if m3:
                group = m3.groupdict()
                vrf_dict['no_sg_routes'] = int(group['no_sg_routes'])
                continue

        return parsed_dict


# ==========================================================================
# Schema for 'show mfib platform evpn bucket location {location}'
# ==========================================================================
class ShowMfibPlatformEvpnBucketLocationSchema(MetaParser):
    """ Schema for show mfib platform evpn bucket location {location}. """

    schema = {
        'bucket_id':
            {Any():
                 {'esi_interface': str,
                  'handle': str,
                  'stale': str,
                  'state': str
                  },
             },
    }


# ==========================================================================
# Parser for 'show mfib platform evpn bucket location {location}'
# ==========================================================================
class ShowMfibPlatformEvpnBucketLocation(ShowMfibPlatformEvpnBucketLocationSchema):
    """
    Parser for show mfib platform evpn bucket location {location}.

    Parameters
    ----------
    device : Router
        Device to be parsed.
    location : str
        Hardware location.

    Returns
    -------
    parsed_dict : dict
        Contains the CLI output parsed into a dictionary.

    Examples
    --------
    >>> device.parse("show mfib platform evpn bucket location 0/0/CPU0")

    {'bucket_id':
        {0:
            {'esi_interface': 'Bundle-Ether1',
             'handle': '0x4000660',
             'stale': 'F',
             'state': 'DF'}
            },
        1:
            {'esi_interface': 'Bundle-Ether1',
             'handle': '0x4000660',
             'stale': 'F',
             'state': 'NDF'}
            },
        2: ...
        }
    }

    """

    cli_command = "show mfib platform evpn bucket location {location}"

    def cli(self, location='', output=None):

        if output is None:
            cmd = self.cli_command.format(location=location)
            out = self.device.execute(cmd)
        else:
            out = output

        parsed_dict = {}

        # ESI Interface     Handle     Bucket ID   State   Stale
        p1 = re.compile(r"ESI Interface +Handle +Bucket ID +State +Stale")

        # Bundle-Ether1        0x4000660          0       DF     F
        p2 = re.compile(r"(?P<esi_interface>\S+) +(?P<handle>0x[a-fA-F\d]+) +"
                        r"(?P<bucket_id>\d+) +(?P<state>\S+) +(?P<stale>\S+)")

        for line in out.splitlines():
            line = line.strip()

            m1 = p1.match(line)
            if m1:
                parsed_dict.setdefault('bucket_id', {})
                continue

            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                bucket_id = int(group['bucket_id'])
                bucket_dict = parsed_dict['bucket_id'].setdefault(bucket_id, {})
                bucket_dict['esi_interface'] = group['esi_interface']
                bucket_dict['handle'] = group['handle']
                bucket_dict['stale'] = group['stale']
                bucket_dict['state'] = group['state']
                continue

        return parsed_dict
