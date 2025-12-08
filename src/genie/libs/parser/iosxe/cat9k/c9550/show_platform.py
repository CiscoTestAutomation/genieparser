import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

from genie.libs.parser.iosxe.cat9k.c9350.show_platform import(
   ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema as ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema_C9550,
   ShowPlatformSoftwareFedActiveAclInfoDbDetail as ShowPlatformSoftwareFedActiveAclInfoDbDetail_C9550,
   ShowPlatformTcamUtilizationSchema as ShowPlatformTcamUtilizationSchema_C9550,
   ShowPlatformTcamUtilization as ShowPlatformTcamUtilization_C9550,
   ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear as ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear_C9550,
   ShowPlatformHardwareFedQosSchedulerSdkInterface as ShowPlatformHardwareFedQosSchedulerSdkInterface_C9550
)

from genie.libs.parser.iosxe.cat9k.c9500.show_platform import(
   ShowPlatformHardwareChassisPowerSupplyDetailAllSchema as ShowPlatformHardwareChassisPowerSupplyDetailAllSchema_C9550,
   ShowPlatformHardwareChassisPowerSupplyDetailAll as ShowPlatformHardwareChassisPowerSupplyDetailAll_C9550
)

class ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema(ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema_C9550):
    ...


# ==========================================================
#  Parser for 'ShowPlatformSoftwareFedActiveAclInfoDbDetail'
# ==========================================================
class ShowPlatformSoftwareFedActiveAclInfoDbDetail(ShowPlatformSoftwareFedActiveAclInfoDbDetail_C9550):
    ...

class ShowPlatformTcamUtilizationSchema(ShowPlatformTcamUtilizationSchema_C9550):
    ...


# ==========================================================
#  Parser for 'ShowPlatformTcamUtilization'
# ==========================================================
class ShowPlatformTcamUtilization(ShowPlatformTcamUtilization_C9550):
    ...

class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear(ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear_C9550):
    ...

class ShowPlatformHardwareFedQosSchedulerSdkInterface(ShowPlatformHardwareFedQosSchedulerSdkInterface_C9550):
    ...

class ShowPlatformHardwareFedQosSchedulerSdkInterface(ShowPlatformHardwareFedQosSchedulerSdkInterface_C9550):
    ...

class ShowPlatformHardwareChassisPowerSupplyDetailAll(ShowPlatformHardwareChassisPowerSupplyDetailAll_C9550):
    ...

class ShowPlatformHardwareChassisFantrayDetailSchema(MetaParser):
    """Schema for show platform hardware chassis fantray detail"""
    
    schema = {
        'fantrays': {
            Any(): {
                'inlet_rpm': int,
                'outlet_rpm': int,
                'pwm_percentage': int
            }
        }
    }

# ==========================================================
#  Parser for 'ShowPlatformHardwareChassisFantrayDetail'
# ==========================================================
class ShowPlatformHardwareChassisFantrayDetail(ShowPlatformHardwareChassisFantrayDetailSchema):
    """Parser for show platform hardware chassis fantray detail
    """

    cli_command = ['show platform hardware chassis fantray detail', 
                   'show platform hardware chassis fantray detail switch {switch_mode}']

    def cli(self, switch_mode="",output=None):
        if output is None:
            if switch_mode:
                output = self.device.execute(self.cli_command[1].format(switch_mode=switch_mode))
            else:
                output = self.device.execute(self.cli_command[0])

        # Initialize return dictionary
        ret_dict = {}

        # FT1:
        # Inlet:4031 RPM, Outlet:5203 RPM, PWM:30%
        p1 = re.compile(r'^(?P<fantray>FT\d+):$')
        p2 = re.compile(r'^Inlet:(?P<inlet_rpm>\d+)\s+RPM,\s+Outlet:(?P<outlet_rpm>\d+)\s+RPM,\s+PWM:(?P<pwm>\d+)%$')

        current_fantray = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Match fantray identifier (FT1:, FT2:, etc.)
            m = p1.match(line)
            if m:
                current_fantray = m.groupdict()['fantray']
                if 'fantrays' not in ret_dict:
                    ret_dict['fantrays'] = {}
                ret_dict['fantrays'][current_fantray] = {}
                continue

            # Match RPM and PWM data
            m = p2.match(line)
            if m and current_fantray:
                group = m.groupdict()
                ret_dict['fantrays'][current_fantray].update({
                    'inlet_rpm': int(group['inlet_rpm']),
                    'outlet_rpm': int(group['outlet_rpm']),
                    'pwm_percentage': int(group['pwm'])
                })
                continue

        return ret_dict
