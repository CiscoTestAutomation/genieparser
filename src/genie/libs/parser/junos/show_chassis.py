
''' show_chassis.py

Parser for the following show commands:
    * show chassis fpc detail
    * show chassis environment routing-engine
    * show chassis firmware
    * show chassis firmware no-forwarding
    * show chassis fpc
    * show chassis routing-engine
    * show chassis routing-engine no-forwarding
    * show chassis hardware
    * show chassis hardware detail
    * show chassis hardware detail no-forwarding
    * show chassis hardware extensive
    * show chassis hardware extensive no-forwarding
'''
# python
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, SchemaTypeError, Schema, Or)

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
        p1 = re.compile(r'^Slot +(?P<slot>\d+) +information:$')

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


class ShowChassisHardwareSchema(MetaParser):
        
    """schema = {
    Optional("@xmlns:junos"): str,
    "chassis-inventory": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": [
                {
                    "chassis-sub-module": [
                        {
                            "chassis-sub-sub-module": {
                                "description": str,
                                "name": str,
                                "part-number": str,
                                "serial-number": str
                            },
                            "description": str,
                            "name": str,
                            "part-number": str,
                            "serial-number": str,
                            "version": str
                        }
                    ],
                    "description": str,
                    "name": str
                }
            ],
            "description": str,
            "name": str,
            "serial-number": str
        }
    }
}"""

    def validate_inner_chassis_hardware_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('inner chassis hardware is not a list')
        chassis_inner_hardware_schema = Schema(
                        {
                            Optional("chassis-sub-sub-module"): {
                                "description": str,
                                "name": str,
                                "part-number": str,
                                "serial-number": str
                            },
                            Optional("description"): str,
                            "name": str,
                            Optional("part-number"): str,
                            Optional("serial-number"): str,
                            Optional("version"): str
                        }
                    
        )
        # Validate each dictionary in list
        for item in value:
            chassis_inner_hardware_schema.validate(item)
        return value


    def validate_chassis_hardware_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('chassis hardware is not a list')
        chassis_hardware_schema = Schema({
            Optional("chassis-sub-module"): Use(ShowChassisHardware.validate_inner_chassis_hardware_list),
            Optional("description"): str,
            "name": str
        })
        # Validate each dictionary in list
        for item in value:
            chassis_hardware_schema.validate(item)
        return value

    schema = {
    Optional("@xmlns:junos"): str,
    "chassis-inventory": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": Use(validate_chassis_hardware_list),
            "description": str,
            "name": str,
            "serial-number": str
            }
        }
    }

class ShowChassisHardware(ShowChassisHardwareSchema):
    """ Parser for:
    * show chassis hardware
    """

    cli_command = 'show chassis hardware'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Hardware inventory:
        p1 = re.compile(r'^Hardware +(?P<style>\S+):$')

        #FPC 0                                                    Virtual FPC
        p2 = re.compile(r'^(?P<name>(\S+\s\d+)) +(?P<description>\S+\s\S+)$')

        #Routing Engine 0                                         RE-VMX
        p3 = re.compile(r'^(?P<name>\S+\s+\S+\s+\d+) +(?P<description>\S+)$')

        #CPU            Rev. 1.0 RIOT-LITE    BUILTIN
        p4 = re.compile(r'^(?P<name>\S+) +(?P<version>[\S\.\d]+ [\S\.\d]+) '
                        r'+(?P<part_number>[\S\-]+) +(?P<serial_number>\S+)$')

        #MIC 0                                                  Virtual
        p5 = re.compile(r'^(?P<name>\S+ \d+) +(?P<description>\S+)$')

        #PIC 0                 BUILTIN      BUILTIN           Virtual
        p6 = re.compile(r'^(?P<name>\S+ \d+) +(?P<part_number>\S+) '
                        r'+(?P<serial_number>\S+) +(?P<description>\S+)$')

        #Chassis                                VM5D4C6B3599      VMX
        p7 = re.compile(r'^(?P<name>\S+) +(?P<serial_number>\S+) '
                        r'+(?P<description>\S+)$')

        #Midplane
        p8 = re.compile(r'^(?P<name>\S+)$')

        ret_dict = {}

        for line in out.splitlines()[1:]:
            line = line.strip()

            #Hardware inventory:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                chassis_inventory_dict = ret_dict.setdefault("chassis-inventory", {})\
                                                            .setdefault("chassis", {})

                chassis_inventory_dict["@junos:style"] = group["style"]
                
                chassis_entry_list = chassis_inventory_dict.setdefault("chassis-module", [])

                continue

            #FPC 0                                                    Virtual FPC
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if(group["name"] == "CB 0"):
                    entry_dict = {}
                    entry_dict["description"] = group["description"]
                    entry_dict["name"] = group["name"]

                    chassis_entry_list.append(entry_dict)
                else:
                    chassis_inner_dict1 = {}
                    chassis_inner_dict1["description"] = group["description"]
                    chassis_inner_dict1["name"] = group["name"]
                continue

            #Routing Engine 0                                         RE-VMX
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["description"] = group["description"]
                entry_dict["name"] = group["name"]

                chassis_entry_list.append(entry_dict)
                continue

            #CPU            Rev. 1.0 RIOT-LITE    BUILTIN
            m = p4.match(line)
            if m:
                group = m.groupdict()
                chassis_inner_list = []
                chassis_inner_dict = {}
                chassis_inner_dict["name"] = group["name"]
                chassis_inner_dict["part-number"] = group["part_number"]
                chassis_inner_dict["serial-number"] = group["serial_number"]
                chassis_inner_dict["version"] = group["version"]

                chassis_inner_list.append(chassis_inner_dict)
                continue

            #MIC 0                                                  Virtual
            m = p5.match(line)
            if m:
                group = m.groupdict()
                chassis_inner_dict2 = {}
                chassis_inner_dict2["description"] = group["description"]
                chassis_inner_dict2["name"] = group["name"]
                continue

            #PIC 0                 BUILTIN      BUILTIN           Virtual
            m = p6.match(line)
            if m:
                group = m.groupdict()
                chassis_inner_inner_dict = {}
                chassis_inner_inner_dict["description"] = group["description"]
                chassis_inner_inner_dict["name"] = group["name"]
                chassis_inner_inner_dict["part-number"] = group["part_number"]
                chassis_inner_inner_dict["serial-number"] = group["serial_number"]

                chassis_inner_dict2["chassis-sub-sub-module"] = chassis_inner_inner_dict
                chassis_inner_list.append(chassis_inner_dict2)

                chassis_inner_dict1["chassis-sub-module"] = chassis_inner_list

                chassis_entry_list.append(chassis_inner_dict1)
                continue

            #Chassis                                VM5D4C6B3599      VMX
            m = p7.match(line)
            if m:
                group = m.groupdict()
                chassis_inventory_dict["description"] = group["description"]
                chassis_inventory_dict["name"] = group["name"]
                chassis_inventory_dict["serial-number"] = group["serial_number"]
                continue

            #Midplane
            m = p8.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["name"] = group["name"]
                chassis_entry_list.append(entry_dict)
                continue

        return ret_dict


class ShowChassisHardwareDetailSchema(MetaParser):
        
    """schema = {
    Optional("@xmlns:junos"): str,
    "chassis-inventory": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": [
                {
                    "chassis-re-disk-module": {
                        "description": str,
                        "disk-size": str,
                        "model": str,
                        "name": str,
                        "serial-number": str
                    },
                    "chassis-sub-module": [
                        {
                            "chassis-sub-sub-module": {
                                "description": str,
                                "name": str,
                                "part-number": str,
                                "serial-number": str
                            },
                            "description": str,
                            "name": str,
                            "part-number": str,
                            "serial-number": str,
                            "version": str
                        }
                    ],
                    "description": str,
                    "name": str
                }
            ],
            "description": str,
            "name": str,
            "serial-number": str
        }
    }
}"""

    def validate_inner_chassis_hardware_detail_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('inner chassis module is not a list')
        chassis_inner_hardware_schema = Schema(
                        {
                            Optional("chassis-sub-sub-module"): {
                                "description": str,
                                "name": str,
                                "part-number": str,
                                "serial-number": str
                            },
                            Optional("description"): str,
                            "name": str,
                            Optional("part-number"): str,
                            Optional("serial-number"): str,
                            Optional("version"): str
                        }
                    
        )
        # Validate each dictionary in list
        for item in value:
            chassis_inner_hardware_schema.validate(item)
        return value


    def validate_chassis_hardware_detail_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('chassis module is not a list')
        chassis_hardware_detail_schema = Schema({
            Optional("chassis-re-disk-module"): {
                        "description": str,
                        "disk-size": str,
                        "model": str,
                        "name": str,
                        "serial-number": str
                    },
            Optional("chassis-sub-module"): Use(ShowChassisHardwareDetail.validate_inner_chassis_hardware_detail_list),
            Optional("description"): str,
            "name": str,
            Optional("serial-number"): str
        })
        # Validate each dictionary in list
        for item in value:
            chassis_hardware_detail_schema.validate(item)
        return value

    schema = {
    Optional("@xmlns:junos"): str,
    "chassis-inventory": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": Use(validate_chassis_hardware_detail_list),
            "description": str,
            "name": str,
            "serial-number": str
            }
        }
    }

class ShowChassisHardwareDetail(ShowChassisHardwareDetailSchema):
    """ Parser for:
    * show chassis hardware detail
    """

    cli_command = 'show chassis hardware detail'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Hardware inventory:
        p1 = re.compile(r'^Hardware +(?P<style>\S+):$')

        #FPC 0                                                    Virtual FPC
        p2 = re.compile(r'^(?P<name>(\S+\s\d+)) +(?P<description>\S+\s\S+)$')

        #Routing Engine 0                                         RE-VMX
        p3 = re.compile(r'^(?P<name>\S+\s+\S+\s+\d+) +(?P<description>\S+)$')

        #cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
        p4 = re.compile(r'^(?P<name>\S+) +(?P<disk_size>\d+) '
                         r'+MB +(?P<model>\S+\s+\S+\s+\S+\s+\S+) '
                         r'+(?P<serial_number>\d+) +(?P<description>'
                         r'\S+\s+\S+)$')

        #CPU            Rev. 1.0 RIOT-LITE    BUILTIN
        p5 = re.compile(r'^(?P<name>\S+) +(?P<version>[\S\.\d]+ [\S\.\d]+) '
                        r'+(?P<part_number>[\S\-]+) +(?P<serial_number>\S+)$')

        #MIC 0                                                  Virtual
        p6 = re.compile(r'^(?P<name>\S+ \d+) +(?P<description>\S+)$')

        #PIC 0                 BUILTIN      BUILTIN           Virtual
        p7 = re.compile(r'^(?P<name>\S+ \d+) +(?P<part_number>\S+) '
                        r'+(?P<serial_number>\S+) +(?P<description>\S+)$')

        #Chassis                                VM5D4C6B3599      VMX
        p8 = re.compile(r'^(?P<name>\S+) +(?P<serial_number>\S+) '
                        r'+(?P<description>\S+)$')

        #Midplane
        p9 = re.compile(r'^(?P<name>\S+)$')

        ret_dict = {}

        for line in out.splitlines()[1:]:
            line = line.strip()

            #Hardware inventory:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                chassis_inventory_dict = ret_dict.setdefault("chassis-inventory", {})\
                                                            .setdefault("chassis", {})
                chassis_inventory_dict["@junos:style"] = group["style"]
                
                chassis_entry_list = chassis_inventory_dict.setdefault("chassis-module", [])

                continue

            #FPC 0                                                    Virtual FPC
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if(group["name"] == "CB 0"):
                    entry_dict = {}
                    entry_dict["description"] = group["description"]
                    entry_dict["name"] = group["name"]

                    chassis_entry_list.append(entry_dict)
                else:
                    chassis_inner_dict1 = {}
                    chassis_inner_dict1["description"] = group["description"]
                    chassis_inner_dict1["name"] = group["name"]
                continue

            #Routing Engine 0                                         RE-VMX
            m = p3.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["description"] = group["description"]
                entry_dict["name"] = group["name"]

                
                continue

            #cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
            m = p4.match(line)
            if m:
                group = m.groupdict()
                re_disk_entry_dict = {}
                re_disk_entry_dict["description"] = group["description"]
                re_disk_entry_dict["disk-size"] = group["disk_size"]
                re_disk_entry_dict["model"] = group["model"]
                re_disk_entry_dict["name"] = group["name"]
                re_disk_entry_dict["serial-number"] = group["serial_number"]

                entry_dict["chassis-re-disk-module"] = re_disk_entry_dict
                chassis_entry_list.append(entry_dict)
                continue

            #CPU            Rev. 1.0 RIOT-LITE    BUILTIN
            m = p5.match(line)
            if m:
                group = m.groupdict()
                chassis_inner_list = []
                chassis_inner_dict = {}
                chassis_inner_dict["name"] = group["name"]
                chassis_inner_dict["part-number"] = group["part_number"]
                chassis_inner_dict["serial-number"] = group["serial_number"]
                chassis_inner_dict["version"] = group["version"]

                chassis_inner_list.append(chassis_inner_dict)
                continue

            #MIC 0                                                  Virtual
            m = p6.match(line)
            if m:
                group = m.groupdict()
                chassis_inner_dict2 = {}
                chassis_inner_dict2["description"] = group["description"]
                chassis_inner_dict2["name"] = group["name"]
                continue

            #PIC 0                 BUILTIN      BUILTIN           Virtual
            m = p7.match(line)
            if m:
                group = m.groupdict()
                chassis_inner_inner_dict = {}
                chassis_inner_inner_dict["description"] = group["description"]
                chassis_inner_inner_dict["name"] = group["name"]
                chassis_inner_inner_dict["part-number"] = group["part_number"]
                chassis_inner_inner_dict["serial-number"] = group["serial_number"]

                chassis_inner_dict2["chassis-sub-sub-module"] = chassis_inner_inner_dict
                chassis_inner_list.append(chassis_inner_dict2)

                chassis_inner_dict1["chassis-sub-module"] = chassis_inner_list

                chassis_entry_list.append(chassis_inner_dict1)
                continue

            #Chassis                                VM5D4C6B3599      VMX
            m = p8.match(line)
            if m:
                group = m.groupdict()
                chassis_inventory_dict["description"] = group["description"]
                chassis_inventory_dict["name"] = group["name"]
                chassis_inventory_dict["serial-number"] = group["serial_number"]
                continue

            #Midplane
            m = p9.match(line)
            if m:
                group = m.groupdict()
                entry_dict = {}
                entry_dict["name"] = group["name"]
                chassis_entry_list.append(entry_dict)
                continue

        return ret_dict


class ShowChassisHardwareDetailNoForwarding(ShowChassisHardwareDetail):
    """ Parser for:
            - show chassis hardware detail no-forwarding
    """

    cli_command = [
        'show chassis hardware detail no-forwarding'
    ]

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)

class ShowChassisHardwareExtensiveSchema(MetaParser):
        
    """schema = {
    Optional("@xmlns:junos"): str,
    "chassis-inventory": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": [
                {
                    "chassis-re-disk-module": {
                        "description": str,
                        "disk-size": str,
                        "model": str,
                        "name": str,
                        "serial-number": str
                    },
                    "chassis-sub-module": [
                        {
                            "chassis-sub-sub-module": {
                                "description": str,
                                "name": str,
                                "part-number": str,
                                "serial-number": str
                            },
                            "description": str,
                            "name": str,
                            "part-number": str,
                            "serial-number": str,
                            "version": str
                        }
                    ],
                    "description": str,
                    "name": str
                }
            ],
            "description": str,
            "i2c-information": {
                "assembly-flags": str,
                "assembly-identifier": str,
                "assembly-version": str,
                "board-information-record": str,
                "eeprom-version": str,
                "i2c-data": list,
                "i2c-identifier": str,
                "i2c-version": str,
                "jedec-code": str,
                "manufacture-date": str,
                "part-number": str,
                "serial-number": str
            },
            "name": str,
            "serial-number": str
        }
    }
}"""

    def validate_inner_chassis_hardware_detail_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('inner chassis module is not a list')
        chassis_inner_hardware_schema = Schema(
                        {
                            Optional("chassis-sub-sub-module"): {
                                "description": str,
                                "name": str,
                                "part-number": str,
                                "serial-number": str
                            },
                            Optional("description"): str,
                            Optional("i2c-information"): {
                            "assembly-flags": str,
                            "assembly-identifier": str,
                            "assembly-version": str,
                            "board-information-record": str,
                            "eeprom-version": str,
                            Optional("i2c-data"): list,
                            Optional("i2c-identifier"): Or(str, None),
                            "i2c-version": Or(str, None),
                            "jedec-code": str,
                            "manufacture-date": str,
                            "part-number": Or(str, None),
                            Optional("serial-number"): Or(str,None)
                        },
                            "name": str,
                            Optional("part-number"): str,
                            Optional("serial-number"): str,
                            Optional("version"): str
                        }
                    
        )
        # Validate each dictionary in list
        for item in value:
            chassis_inner_hardware_schema.validate(item)
        return value


    def validate_chassis_hardware_extensive_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaTypeError('chassis module is not a list')
        chassis_hardware_detail_schema = Schema({
            Optional("chassis-re-disk-module"): {
                        "description": str,
                        "disk-size": str,
                        "model": str,
                        "name": str,
                        "serial-number": str
                    },
            Optional("chassis-sub-module"): Use(ShowChassisHardwareExtensive.validate_inner_chassis_hardware_detail_list),
            Optional("description"): str,
            Optional("i2c-information"): {
                "assembly-flags": str,
                "assembly-identifier": str,
                "assembly-version": str,
                "board-information-record": str,
                "eeprom-version": str,
                Optional("i2c-data"): list,
                Optional("i2c-identifier"): Or(str, None),
                "i2c-version": Or(str, None),
                "jedec-code": str,
                "manufacture-date": str,
                "part-number": Or(str, None),
                Optional("serial-number"): Or(str,None)
            },
            "name": str,
            Optional("serial-number"): str
        })
        # Validate each dictionary in list
        for item in value:
            chassis_hardware_detail_schema.validate(item)
        return value

    schema = {
    Optional("@xmlns:junos"): str,
    "chassis-inventory": {
        Optional("@xmlns"): str,
        "chassis": {
            Optional("@junos:style"): str,
            "chassis-module": Use(validate_chassis_hardware_extensive_list),
            "description": str,
            Optional("i2c-information"): {
                "assembly-flags": str,
                "assembly-identifier": str,
                "assembly-version": str,
                "board-information-record": str,
                "eeprom-version": str,
                Optional("i2c-data"): list,
                Optional("i2c-identifier"): Or(str, None),
                "i2c-version": Or(str, None),
                "jedec-code": str,
                "manufacture-date": str,
                "part-number": Or(str, None),
                Optional("serial-number"): Or(str, None)
            },
            "name": str,
            "serial-number": str
            }
        }
    }

class ShowChassisHardwareExtensive(ShowChassisHardwareExtensiveSchema):
    """ Parser for:
    * show chassis hardware extensive
    """

    cli_command = 'show chassis hardware extensive'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        #Hardware inventory:
        p1 = re.compile(r'^Hardware +(?P<style>\S+):$')

        #Jedec Code:   0x7fb0            EEPROM Version:    0x02
        p2 = re.compile(r'^Jedec Code: +(?P<jedec_code>\S+) '
                        r'+EEPROM Version: +(?P<eeprom_version>\S+)$')

        
        #S/N:               VM5D4C6B3599
        p3 = re.compile(r'^S/N: +(?P<serial_number>\S+)$')

        

        #Assembly ID:  0x0567            Assembly Version:  00.00
        p4 = re.compile(r'^Assembly ID: +(?P<assembly_identifier>\S+) '
                        r'+Assembly Version: +(?P<assembly_version>\S+)$')

        

        

        #Date:         00-00-0000        Assembly Flags:    0x00
        p5 = re.compile(r'^Date: +(?P<manufacture_date>\S+) +Assembly Flags: '
                        r'+(?P<assembly_flags>\S+)$')

        

        #ID: VMX
        p6 = re.compile(r'^ID: +(?P<i2c_identifier>[\S\s]+)$')

        

        #Board Information Record:
        p7 = re.compile(r'^(?P<address_type>\ABoard Information Record):$')

        

        #I2C Hex Data:
        p8 = re.compile(r'^(?P<address_type>\AI2C Hex Data:)$')

        

        #Address 0x00: 7f b0 02 00 fa 4e 01 00 52 65 76 2e 20 31 2e 30
        p9 = re.compile(r'^(?P<address_info>\AAddress[\s\S]+)$')



        #FPC 0                                                    Virtual FPC
        #CB 0                                                     VMX SCB
        p10 = re.compile(r'^(?P<name>(\S+\s\d+)) +(?P<description>\S+\s\S+)$')




        #Routing Engine 0                                         RE-VMX
        p11 = re.compile(r'^(?P<name>\S+\s+\S+\s+\d+) +(?P<description>\S+)$')



        #cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
        p12 = re.compile(r'^(?P<name>\S+) +(?P<disk_size>\d+) '
                         r'+MB +(?P<model>\S+\s+\S+\s+\S+\s+\S+) '
                         r'+(?P<serial_number>\d+) +(?P<description>'
                         r'\S+\s+\S+)$')

        #CPU            Rev. 1.0 RIOT-LITE    BUILTIN
        p13 = re.compile(r'^(?P<name>\S+) +(?P<version>[\S\.\d]+ '
                         r'[\S\.\d]+) +(?P<part_number>[\S\-]+) +'
                         r'(?P<serial_number>\S+)$')

        #MIC 0                                                  Virtual
        p14 = re.compile(r'^(?P<name>\S+ \d+) +(?P<description>\S+)$')

        #PIC 0                 BUILTIN      BUILTIN           Virtual
        p15 = re.compile(r'^(?P<name>\S+ \d+) +(?P<part_number>\S+) '
                         r'+(?P<serial_number>\S+) +(?P<description>\S+)$')

        
        #Version:      Rev. 1.0
        p111 = re.compile(r'^Version: +(?P<version>[\S\s]+)$')

        
        #Chassis                                VM5D4C6B3599      VMX
        p16 = re.compile(r'^(?P<name>\S+) +(?P<serial_number>\S+) +'
                         r'(?P<description>\S+)$')

        #Midplane
        p17 = re.compile(r'^(?P<name>\S+)$')

        ret_dict = {}

        for line in out.splitlines()[1:]:
            line = line.strip()

            #Hardware inventory:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                current_item = " "
                chassis_inventory_dict = ret_dict.setdefault("chassis-inventory", {})\
                                                            .setdefault("chassis", {})
                chassis_inventory_dict["@junos:style"] = group["style"]
                
                chassis_entry_list = chassis_inventory_dict.setdefault("chassis-module", [])

                continue

            #Jedec Code:   0x7fb0            EEPROM Version:    0x02
            m = p2.match(line)
            if m:
                group = m.groupdict()
                i2c_dict = {}
                i2c_dict["jedec-code"] = group["jedec_code"]
                i2c_dict["eeprom-version"] = group["eeprom_version"]
                continue

            #S/N:               VM5D4C6B3599
            m = p3.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["serial-number"] = group["serial_number"]
                continue



            #Assembly ID:  0x0567            Assembly Version:  00.00
            m = p4.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["assembly-identifier"] = group["assembly_identifier"]
                i2c_dict["assembly-version"] = group["assembly_version"]
                continue


            #Date:         00-00-0000        Assembly Flags:    0x00
            m = p5.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["manufacture-date"] = group["manufacture_date"]
                i2c_dict["assembly-flags"] = group["assembly_flags"]
                continue

            #Version:      Rev. 1.0
            m = p111.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["i2c-version"] = group["version"]
                continue


            #ID: VMX
            m = p6.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["i2c-identifier"] = group["i2c_identifier"]
                continue


            #Board Information Record:
            m = p7.match(line)
            if m:
                group = m.groupdict()
                complete_address = ""
                address_type = group["address_type"]                
                continue

            #I2C Hex Data:
            m = p8.match(line)
            if m:
                group = m.groupdict()
                complete_address = []
                address_type = group["address_type"]                
                continue

            #Address 0x00: 7f b0 02 00 fa 4e 01 00 52 65 76 2e 20 31 2e 30
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if(address_type == "Board Information Record"):
                    i2c_dict["board-information-record"] = group["address_info"]
                else:
                    #complete_address += group["address_info"] + '\n' + ('    ')*5
                    complete_address.append(group["address_info"])
                continue
            

            #FPC 0                                                    Virtual FPC
            m = p10.match(line)
            if m:
                group = m.groupdict()
                if(group["name"] == "CB 0"):                  
                    outter_dict = {}
                    current_item = group["name"]
                    outter_dict["description"] = group["description"]
                    outter_dict["name"] = group["name"]
                else:                    
                    if(current_item == "CB 0"):
                        i2c_dict["i2c-data"] = complete_address
                        if "part-number" not in i2c_dict:
                            i2c_dict["part-number"] = None
                        if "i2c-version" not in i2c_dict:
                            i2c_dict["i2c-version"] = None
                        if "serial-number" not in i2c_dict:
                            i2c_dict["serial-number"] = None
                        
                        outter_dict["i2c-information"] = i2c_dict
                        chassis_entry_list.append(outter_dict)

                    current_item = group["name"]
                    outter_dict = {}
                    outter_dict["description"] = group["description"]
                    outter_dict["name"] = group["name"]
                continue

            #Routing Engine 0                                         RE-VMX
            m = p11.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["i2c-data"] = complete_address
                if(current_item == "Chassis"):
                    if "part-number" not in i2c_dict:
                        i2c_dict["part-number"] = None
                    if "i2c-version" not in i2c_dict:
                        i2c_dict["i2c-version"] = None
                    
                    
                    chassis_inventory_dict["i2c-information"] = i2c_dict

                current_item = group["name"]
                
                outter_dict = {}
                outter_dict["description"] = group["description"]
                outter_dict["name"] = group["name"]

                
                continue

            #cd0   27649 MB  VMware Virtual IDE Har 00000000000000000001 Hard Disk
            m = p12.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["i2c-data"] = complete_address

                if(current_item == "Routing Engine 0"):
                    if "part-number" not in i2c_dict:
                        i2c_dict["part-number"] = None
                    if "i2c-version" not in i2c_dict:
                        i2c_dict["i2c-version"] = None
                    if "serial-number" not in i2c_dict:
                        i2c_dict["serial-number"] = None

                    outter_dict["i2c-information"] = i2c_dict

                re_disk_entry_dict = {}
                re_disk_entry_dict["description"] = group["description"]
                re_disk_entry_dict["disk-size"] = group["disk_size"]
                re_disk_entry_dict["model"] = group["model"]
                re_disk_entry_dict["name"] = group["name"]
                re_disk_entry_dict["serial-number"] = group["serial_number"]

                outter_dict["chassis-re-disk-module"] = re_disk_entry_dict
                chassis_entry_list.append(outter_dict)
                continue

            #CPU            Rev. 1.0 RIOT-LITE    BUILTIN
            m = p13.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["i2c-data"] = complete_address
                if(current_item == "FPC 0"):
                    if "part-number" not in i2c_dict:
                        i2c_dict["part-number"] = None
                    if "i2c-version" not in i2c_dict:
                        i2c_dict["i2c-version"] = None
                    if "serial-number" not in i2c_dict:
                        i2c_dict["serial-number"] = None

                    outter_dict["i2c-information"] = i2c_dict

                current_item = group["name"]
                chassis_inner_list = []
                chassis_inner_dict = {}
                chassis_inner_dict["name"] = group["name"]
                chassis_inner_dict["part-number"] = group["part_number"]
                chassis_inner_dict["serial-number"] = group["serial_number"]
                chassis_inner_dict["version"] = group["version"]
                continue

            #MIC 0                                                  Virtual
            m = p14.match(line)
            if m:
                group = m.groupdict()
                i2c_dict["i2c-data"] = complete_address
                if(current_item == "CPU"):
                    if "part-number" not in i2c_dict:
                        i2c_dict["part-number"] = None
                    if "i2c-version" not in i2c_dict:
                        i2c_dict["i2c-version"] = None
                    if "serial-number" not in i2c_dict:
                        i2c_dict["serial-number"] = chassis_inner_dict["serial-number"]
                    if "i2c-identifier" not in i2c_dict:
                        i2c_dict["i2c-identifier"] = None
                    
                    chassis_inner_dict["i2c-information"] = i2c_dict
                
                current_item = group["name"]

                chassis_inner_dict2 = {}
                chassis_inner_dict2["description"] = group["description"]
                chassis_inner_dict2["name"] = group["name"]
                continue

            #PIC 0                 BUILTIN      BUILTIN           Virtual
            m = p15.match(line)
            if m:
                group = m.groupdict()
                chassis_inner_inner_dict = {}

                i2c_dict["i2c-data"] = complete_address

                if(current_item == "MIC 0"):
                    if "part-number" not in i2c_dict:
                        i2c_dict["part-number"] = None
                    if "i2c-version" not in i2c_dict:
                        i2c_dict["i2c-version"] = None
                    if "serial-number" not in i2c_dict:
                        i2c_dict["serial-number"] = None

                    chassis_inner_dict2["i2c-information"] = i2c_dict

                chassis_inner_inner_dict["description"] = group["description"]
                chassis_inner_inner_dict["name"] = group["name"]
                chassis_inner_inner_dict["part-number"] = group["part_number"]
                chassis_inner_inner_dict["serial-number"] = group["serial_number"]

                chassis_inner_dict2["chassis-sub-sub-module"] = chassis_inner_inner_dict
                chassis_inner_list.append(chassis_inner_dict2)
                chassis_inner_list.append(chassis_inner_dict)

                outter_dict["chassis-sub-module"] = chassis_inner_list

                chassis_entry_list.append(outter_dict)
                continue

            #Chassis                                VM5D4C6B3599      VMX
            m = p16.match(line)
            if m:
                group = m.groupdict()
                current_item = group["name"]

                chassis_inventory_dict["description"] = group["description"]
                chassis_inventory_dict["name"] = group["name"]
                chassis_inventory_dict["serial-number"] = group["serial_number"]
                chassis_entry_dict = {}
                continue

            #Midplane
            m = p17.match(line)
            if m:
                group = m.groupdict()
                if(current_item == "CPU"):
                    if "part-number" not in i2c_dict:
                        i2c_dict["part-number"] = None
                    if "i2c-version" not in i2c_dict:
                        i2c_dict["i2c-version"] = None

                    chassis_inventory_dict["i2c-information"] = i2c_dict
                entry_dict = {}
                entry_dict["name"] = group["name"]
                chassis_entry_list.append(entry_dict)
                continue

        return ret_dict


class ShowChassisHardwareExtensiveNoForwarding(ShowChassisHardwareExtensive):
    """ Parser for:
            - show chassis hardware extensive no-forwarding
    """

    cli_command = [
        'show chassis hardware extensive no-forwarding'
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

    cli_command = 'show chassis routing-engine no-forwarding'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output

        return super().cli(output=out)
        
