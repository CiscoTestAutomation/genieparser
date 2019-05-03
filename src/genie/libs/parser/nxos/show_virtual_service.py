"""show_virtual_service.py

NX-OS parser for the following show commands:
    * show virtual-service list
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ======================================
# Schema for "show virtual-service list"
# ======================================
class ShowVirtualServiceListSchema(MetaParser):
    """Schema for "show virtual-service list"."""

    schema = {
        'service': {
            Any(): {
                'status': str,
                Optional('package'): str,
            },
        },
    }


# ======================================
# Parser for "show virtual-service list"
# ======================================
class ShowVirtualServiceList(ShowVirtualServiceListSchema):
    """Parser for "show virtual-service list"."""

    cli_command = "show virtual-service list"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        services_dict = {}

        # Virtual Service List:
        #
        # Name                    Status             Package Name
        # ----------------------------------------------------------------------
        # guestshell+             Activated          guestshell.ova
        # lxc4                    Not Installed      Not Available
        # sc_sanity_03            Installed          ft_mv_no_onep.ova
        # lxc_upgrade             Activate Failed    c63lxc_no_onep.ova

        p1 = re.compile(r'^(?P<name>(\S+))\s+'
                        '(?P<status>(\S+(?: \S+)?))\s+'
                        '(?P<package>(\S+(?: \S+)?))$')

        for line in output.splitlines():
            line = line.strip()

            match = p1.match(line)
            if match:
                group = match.groupdict()
                name = group['name']
                status = group['status'].lower()
                package = group['package']

                # Avoid false positives matching the output headers:
                if name == "Virtual" and status == "service":
                    continue
                if name == "Name" and status == "status":
                    continue

                service_dict = (services_dict
                                .setdefault('service', {})
                                .setdefault(name, {}))
                service_dict['status'] = status
                if package != "Not Available":
                    service_dict['package'] = package
                continue

        return services_dict
