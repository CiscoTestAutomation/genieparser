
''' show_chassis.py

Parser for the following show commands:
    * show chassis fpc detail
    * show chassis environment routing-engine
    * show chassis firmware
    * show chassis firmware no-forwarding
    * show chassis fpc
    * show chassis routing-engine
    * show chassis routing-engine no-forwarding
'''
# python
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema)

class ShowChassisFpcDetailSchema(MetaParser):

    schema = {
    Optional("@xmlns:junos"): str,
    "fpc-information": {
        Optional("@junos:style"): str,
        Optional("@xmlns"): str,
        "fpc": {
            "fips-capable": str,
            "fips-mode": str,
            "memory-ddr-dram-size": str,
            "memory-dram-size": str,
            "memory-rldram-size": str,
            "slot": str,
            "start-time": {
                "#text": str,
                Optional("@junos:seconds"): str
            },
            "state": str,
            "temperature": {
                "#text": str,
                Optional("@junos:celsius"): str
            },
            "up-time": {
                "#text": str,
                Optional("@junos:seconds"): str
            }
        }
    }
}


class ShowChassisFpcDetail(ShowChassisFpcDetailSchema):
    """ Parser for:
    * show chassis fpc detail
    """

    cli_command = 'show chassis fpc detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Slot 0 information:
        p1 = re.compile(r'^Slot (?P<slot>\d+) +information:$')

        #State                               Online
        p2 = re.compile(r'^State +(?P<state>\S+)$')

        #Temperature                      Testing
        p3 = re.compile(r'^Temperature +(?P<temperature>\S+)$')

        #Total CPU DRAM                  511 MB
        p4 = re.compile(r'^Total CPU DRAM +(?P<memory_dram_size>\d+)\sMB$')

        #Total RLDRAM                     10 MB
        p5 = re.compile(r'^Total RLDRAM +(?P<memory_rldram_size>\d+)\sMB$')

        #Total DDR DRAM                    0 MB
        p6 = re.compile(r'^Total DDR DRAM +(?P<memory_ddr_dram_size>\d+)\sMB$')

        #FIPS Capable                        False
        p7 = re.compile(r'^FIPS Capable +(?P<fips_capable>\S+)$')

        #FIPS Mode                           False
        p8 = re.compile(r'^FIPS Mode +(?P<fips_mode>\S+)$')

        #Start time                          2019-08-29 09:09:16 UTC
        p9 = re.compile(r'^Start time +(?P<start_time>[\d\-\:A-Za-z ]+)$')

        #Uptime                              208 days, 22 hours, 50 minutes, 26 seconds
        p10 = re.compile(r'^Uptime +(?P<up_time>[\d\-\,A-Za-z ]+)$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #Slot 0 information:
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("fpc-information", {})\
                    .setdefault("fpc", {})
                group = m.groupdict()

                ospf_area.update({'slot' : group['slot']})
                continue

            #State                               Online
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_area.update({'state' : group['state']})
                continue

           #Temperature                      Testing
            m = p3.match(line)
            if m:
                group = m.groupdict()
                temperature_dict = {}
                temperature_dict["#text"] = group["temperature"]
                ospf_area.update({'temperature' : temperature_dict})
                continue

            #Total CPU DRAM                  511 MB
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ospf_area.update({'memory-dram-size' : group['memory_dram_size']})
                continue

            #Total RLDRAM                     10 MB
            m = p5.match(line)
            if m:
                group = m.groupdict()
                ospf_area.update({'memory-rldram-size' : group['memory_rldram_size']})
                continue

            #Total DDR DRAM                    0 MB
            m = p6.match(line)
            if m:
                group = m.groupdict()
                ospf_area.update({'memory-ddr-dram-size' : group['memory_ddr_dram_size']})
                continue

            #FIPS Capable                        False
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ospf_area.update({'fips-capable' : group['fips_capable']})
                continue

            #FIPS Mode                           False
            m = p8.match(line)
            if m:
                group = m.groupdict()
                ospf_area.update({'fips-mode' : group['fips_mode']})
                continue

            #Start time                          2019-08-29 09:09:16 UTC
            m = p9.match(line)
            if m:
                group = m.groupdict()
                start_time_dict = {}
                start_time_dict["#text"] = group["start_time"]
                ospf_area.update({'start-time' : start_time_dict})
                continue

            #Uptime                              208 days, 22 hours, 50 minutes, 26 seconds
            m = p10.match(line)
            if m:
                group = m.groupdict()
                up_time_dict = {}
                up_time_dict["#text"] = group["up_time"]
                ospf_area.update({'up-time' : up_time_dict})
                continue

        return ret_dict

class ShowChassisEnvironmentRoutingEngineSchema(MetaParser):

    schema = {
    Optional("@xmlns:junos"): str,
    "environment-component-information": {
        Optional("@xmlns"): str,
        "environment-component-item": {
            "name": str,
            "state": str
        }
    }
}


class ShowChassisEnvironmentRoutingEngine(ShowChassisEnvironmentRoutingEngineSchema):
    """ Parser for:
    * show chassis environment routing-engine
    """

    cli_command = 'show chassis environment routing-engine'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Routing Engine 0 status:
        p1 = re.compile(r'^(?P<name>[\S\s]+) +status:$')

        #State                      Online Master
        p2 = re.compile(r'^State +(?P<name>[\S\s]+)$')


        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #Routing Engine 0 status:
            m = p1.match(line)
            if m:
                ospf_area = ret_dict.setdefault("environment-component-information", {})\
                    .setdefault("environment-component-item", {})
                group = m.groupdict()

                ospf_area.update({'name' : group['name']})
                continue

            #State                      Online Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ospf_area.update({'state' : group['name']})
                continue

        return ret_dict


class ShowChassisFirmwareSchema(MetaParser):

    """ schema = {
    Optional("@xmlns:junos"): str,
    "firmware-information": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": {
                "firmware": [
                    {
                        "firmware-version": str,
                        "type": str
                    }
                ],
                "name": str
            }
        }
    }
} """

    def validate_chassis_firmware_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('firmware is not a list')
        chassis_firmware_schema = Schema({
            "firmware-version": str,
                        "type": str
        })
        # Validate each dictionary in list
        for item in value:
            chassis_firmware_schema.validate(item)
        return value

    schema = {
        "firmware-information": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": {
                "firmware": Use(validate_chassis_firmware_list),
                "name": str
                }
            }
        }
    }

class ShowChassisFirmware(ShowChassisFirmwareSchema):
    """ Parser for:
    * show chassis firmware
    """

    cli_command = 'show chassis firmware'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Part                     Type       Version
        p0 = re.compile(r'^Part +Type +Version$')

        #FPC 0                    ROM        PC Bios
        p1 = re.compile(r'^(?P<name>\S+\s+\d+) +(?P<type>\S+) +(?P<firmware>\S+\s+\S+)$')

        #O/S        Version 19.2R1.8 by builder on 2019-06-21 17:52:23 UTC
        p2 = re.compile(r'^(?P<type>\S+) +(?P<firmware>[\s\S]+)$')


        ret_dict = {}

        for line in out.splitlines()[1:]:
            line = line.strip()

            #Part                     Type       Version
            m = p0.match(line)
            if m:
                continue

            #FPC 0                    ROM        PC Bios
            m = p1.match(line)
            if m:
                
                firmware_chassis_dict = ret_dict.setdefault("firmware-information", {})\
                    .setdefault("chassis", {}).setdefault("chassis-module", {})

                firmware_entry_list = firmware_chassis_dict.setdefault("firmware", [])

                group = m.groupdict()
                entry_dict = {}
                entry_dict["firmware-version"] = group["firmware"]
                entry_dict["type"] = group["type"]
                
                firmware_chassis_dict["name"] = group["name"]
                firmware_entry_list.append(entry_dict)
                continue

            #O/S        Version 19.2R1.8 by builder on 2019-06-21 17:52:23 UTC
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["firmware-version"] = group["firmware"]
                entry_dict["type"] = group["type"]

                firmware_entry_list.append(entry_dict)
                continue

        return ret_dict


class ShowChassisFirmwareNoForwarding(ShowChassisFirmware):
    """ Parser for:
            - show chassis firmware no-forwarding
    """

    cli_command = [
        'show chassis firmware no-forwarding'
    ]

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)


class ShowChassisFpcSchema(MetaParser):

    """ schema = {
    Optional("@xmlns:junos"): str,
    "fpc-information": {
        Optional("@junos:style"): str,
        Optional("@xmlns"): str,
        "fpc": [
            {
                "cpu-15min-avg": str,
                "cpu-1min-avg": str,
                "cpu-5min-avg": str,
                "cpu-interrupt": str,
                "cpu-total": str,
                "memory-buffer-utilization": str,
                "memory-dram-size": str,
                "memory-heap-utilization": str,
                "slot": str,
                "state": str,
                "temperature": {
                    "#text": str,
                    Optional("@junos:celsius"): str
                    }
                }
            ]
        }
    }
    """
    

    def validate_chassis_fpc_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('fpc is not a list')
        chassis_fpc_schema = Schema({
                Optional("cpu-15min-avg"): str,
                Optional("cpu-1min-avg"): str,
                Optional("cpu-5min-avg"): str,
                Optional("cpu-interrupt"): str,
                Optional("cpu-total"): str,
                Optional("memory-buffer-utilization"): str,
                Optional("memory-dram-size"): str,
                Optional("memory-heap-utilization"): str,
                "slot": str,
                "state": str,
                Optional("temperature"): {
                    "#text": str,
                    Optional("@junos:celsius"): str
                }
        })
        # Validate each dictionary in list
        for item in value:
            chassis_fpc_schema.validate(item)
        return value

    schema = {
    Optional("@xmlns:junos"): str,
    "fpc-information": {
        Optional("@junos:style"): str,
        Optional("@xmlns"): str,
        "fpc": Use(validate_chassis_fpc_list)
        }
    }

class ShowChassisFpc(ShowChassisFpcSchema):
    """ Parser for:
    * show chassis fpc
    """

    cli_command = 'show chassis fpc'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #0  Online           Testing   3         0        2      2      2    511        31          0
        p1 = re.compile(r'^(?P<slot>\d+) +(?P<state>\S+) '
                        r'+(?P<text>\S+) +(?P<cpu_total>\d+) '
                        r'+(?P<cpu_interrupt>\d+) +(?P<cpu_1min>\d+) '
                        r'+(?P<cpu_5min>\d+) +(?P<cpu_15min>\d+) +'
                        r'(?P<dram>\d+) +(?P<heap>\d+) +(?P<buffer>\d+)$')

        #2  Empty
        p2 = re.compile(r'^(?P<slot>\d+) +(?P<state>\S+)$')


        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #0  Online           Testing   3         0        2      2      2    511        31          0
            m = p1.match(line)
            if m:
                
                fpc_chassis_list = ret_dict.setdefault("fpc-information", {})\
                    .setdefault("fpc", [])

                group = m.groupdict()
                fpc_entry_dict = {}
                fpc_entry_dict["slot"] = group["slot"]
                fpc_entry_dict["state"] = group["state"]

                fpc_temp_dict = {}
                fpc_temp_dict["#text"] = group["text"]
                fpc_entry_dict["temperature"] = fpc_temp_dict

                fpc_entry_dict["cpu-total"] = group["cpu_total"]
                fpc_entry_dict["cpu-interrupt"] = group["cpu_interrupt"]

                fpc_entry_dict["cpu-1min-avg"] = group["cpu_1min"]
                fpc_entry_dict["cpu-5min-avg"] = group["cpu_5min"]
                fpc_entry_dict["cpu-15min-avg"] = group["cpu_15min"]

                fpc_entry_dict["memory-dram-size"] = group["dram"]
                fpc_entry_dict["memory-heap-utilization"] = group["heap"]
                fpc_entry_dict["memory-buffer-utilization"] = group["buffer"]

                fpc_chassis_list.append(fpc_entry_dict)
                continue

            #2  Empty
            m = p2.match(line)
            if m:
                group = m.groupdict()
                fpc_entry_dict = {}
                fpc_entry_dict["slot"] = group["slot"]
                fpc_entry_dict["state"] = group["state"]

                fpc_chassis_list.append(fpc_entry_dict)
                continue

        return ret_dict


class ShowChassisRoutingEngineSchema(MetaParser):

    schema = {
    Optional("@xmlns:junos"): str,
    "route-engine-information": {
        Optional("@xmlns"): str,
        "route-engine": {
            "cpu-background-5sec": str,
            "cpu-background-1min": str,
            "cpu-background-5min": str,
            "cpu-background-15min": str,
            "cpu-idle-5sec": str,
            "cpu-idle-1min": str,
            "cpu-idle-5min": str,
            "cpu-idle-15min": str,
            "cpu-interrupt-5sec": str,
            "cpu-interrupt-1min": str,
            "cpu-interrupt-5min": str,
            "cpu-interrupt-15min": str,
            "cpu-system-5sec": str,
            "cpu-system-1min": str,
            "cpu-system-5min": str,
            "cpu-system-15min": str,
            "cpu-user-5sec": str,
            "cpu-user-1min": str,
            "cpu-user-5min": str,
            "cpu-user-15min": str,
            "last-reboot-reason": str,
            "load-average-fifteen": str,
            "load-average-five": str,
            "load-average-one": str,
            "mastership-priority": str,
            "mastership-state": str,
            "memory-buffer-utilization": str,
            "memory-dram-size": str,
            "memory-installed-size": str,
            "model": str,
            "slot": str,
            "start-time": {
                "#text": str,
                Optional("@junos:seconds"): str
            },
            Optional("status"): str,
            "up-time": {
                "#text": str,
                Optional("@junos:seconds"): str
                }
            }
        }
    }
   

class ShowChassisRoutingEngine(ShowChassisRoutingEngineSchema):
    """ Parser for:
    * show chassis routing-engine
    """

    cli_command = 'show chassis routing-engine'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Slot 0:
        p1 = re.compile(r'^Slot +(?P<slot>\d+):$')

        #Current state                  Master
        p2 = re.compile(r'^Current state +(?P<mastership_state>\S+)$')

        #Election priority              Master (default)
        p3 = re.compile(r'^Election priority +(?P<mastership_priority>[\S\s]+)$')

        #DRAM                      2002 MB (2048 MB installed)
        p4 = re.compile(r'^DRAM +(?P<memory_dram_size>\S+\s\S+) +(?P<memory_installed_size>[\S\s]+)$')

        #Memory utilization          19 percent
        p5 = re.compile(r'^Memory utilization +(?P<memory_buffer_utilization>\d+) +percent$')

        #5 sec CPU utilization:
        p6 = re.compile(r'^(?P<state>\d+\s+\S+) +CPU utilization:$')

        #User                       1 percent
        p7 = re.compile(r'^User +(?P<user>\d+) +percent$')

        #Background                 0 percent
        p8 = re.compile(r'^Background +(?P<background>\d+) +percent$')

        #Kernel                     1 percent
        p9 = re.compile(r'^Kernel +(?P<system>\d+) +percent$')

        #Interrupt                  0 percent
        p10 = re.compile(r'^Interrupt +(?P<interrupt>\d+) +percent$')

        #Idle                      98 percent
        p11 = re.compile(r'^Idle +(?P<idle>\d+) +percent$')

        #Model                          RE-VMX
        p12 = re.compile(r'^Model +(?P<system>\S+)$')

        #Start time                     2019-08-29 09:02:22 UTC
        p13 = re.compile(r'^Start time +(?P<start_time>[\S\s]+)$')

        #Uptime                         208 days, 23 hours, 14 minutes, 9 seconds
        p14 = re.compile(r'^Uptime +(?P<uptime>[\S\s]+)$')

        #Last reboot reason             Router rebooted after a normal shutdown.
        p15 = re.compile(r'^Last reboot reason +(?P<last_reboot_reason>[\S\s]+)$')

        #0.72       0.46       0.40
        p16 = re.compile(r'^(?P<load_average_one>[\d\.]+) '
                         r'+(?P<load_average_five>[\d\.]+) '
                         r'+(?P<load_average_fifteen>[\d\.]+)$')


        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #Slot 0:
            m = p1.match(line)
            if m:
                current_state = " "
                
                route_engine_dict = ret_dict.setdefault("route-engine-information", {})\
                    .setdefault("route-engine", {})

                group = m.groupdict()
                route_engine_entry_dict = {}

                route_engine_dict["slot"] = group["slot"]
                continue

            #Current state                  Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["mastership-state"] = group["mastership_state"]
                continue

            #Election priority              Master (default)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["mastership-priority"] = group["mastership_priority"]
                continue

            #DRAM                      2002 MB (2048 MB installed)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["memory-dram-size"] = group["memory_dram_size"]
                route_engine_dict["memory-installed-size"] = group["memory_installed_size"]
                continue

            #Memory utilization          19 percent
            m = p5.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["memory-buffer-utilization"] = group["memory_buffer_utilization"]
                continue

            #5 sec CPU utilization:
            m = p6.match(line)
            if m:
                group = m.groupdict()
                current_state = group["state"]
                tag = '-'+group["state"].replace(' ','')
                continue
            
            #User                       1 percent
            m = p7.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["cpu-user"+tag] = group["user"]
                continue

            #Background                 0 percent
            m = p8.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["cpu-background"+tag] = group["background"]
                continue

            #Kernel                     1 percent
            m = p9.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["cpu-system"+tag] = group["system"]
                continue

            #Interrupt                  0 percent
            m = p10.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["cpu-interrupt"+tag] = group["interrupt"]
                continue

            #Idle                      98 percent
            m = p11.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["cpu-idle"+tag] = group["idle"]
                continue

            #Model                          RE-VMX
            m = p12.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["model"] = group["system"]
                continue

            #Start time                     2019-08-29 09:02:22 UTC
            m = p13.match(line)
            if m:
                group = m.groupdict()
                start_time_dict = {}
                start_time_dict["#text"] = group["start_time"]

                route_engine_dict["start-time"] = start_time_dict
                continue

            #Uptime                         208 days, 23 hours, 14 minutes, 9 seconds
            m = p14.match(line)
            if m:
                group = m.groupdict()
                up_time_dict = {}
                up_time_dict["#text"] = group["uptime"]

                route_engine_dict["up-time"] = up_time_dict
                continue

            #Last reboot reason             Router rebooted after a normal shutdown.
            m = p15.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["last-reboot-reason"] = group["last_reboot_reason"]
                continue

            #0.72       0.46       0.40
            m = p16.match(line)
            if m:
                group = m.groupdict()
                route_engine_dict["load-average-one"] = group["load_average_one"]
                route_engine_dict["load-average-five"] = group["load_average_five"]
                route_engine_dict["load-average-fifteen"] = group["load_average_fifteen"]
                continue


        return ret_dict


class ShowChassisRoutingEngineNoForwarding(ShowChassisRoutingEngine):
    """ Parser for:
            - show chassis routing-engine no-forwarding
    """

    cli_command = [
        'show chassis routing-engine no-forwarding'
    ]

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)