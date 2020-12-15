
''' show_chassis.py

Parser for the following show commands:
    * show chassis alarms
    * show chassis fpc detail
    * show chassis fpc pic-status
    * show chassis environment routing-engine
    * show chassis environment 
    * show chassis environment fpc
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
    * show chassis power
'''
# python
import re

from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any,
        Optional, Use, Schema, Or)

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
            raise SchemaError('firmware is not a list')
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
            raise SchemaError('inner chassis hardware is not a list')
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
            raise SchemaError('chassis hardware is not a list')
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

    ''' 
    Schema for 'show chassis hardware detail'
    schema = {
        "chassis-inventory": {
            "chassis": {
                "chassis-module": [
                    {
                        Optional("chassis-re-dimm-module"): [
                            {
                                "die-rev": str,
                                "mfr-id": str,
                                "name": str,
                                "part-number": str,
                                "pcb-rev": str,
                            }
                        ],
                        Optional("chassis-re-disk-module"): [
                            {
                            "description": str,
                            "disk-size": str,
                            "model": str,
                            "name": str,
                            "serial-number": str
                            },
                        ],
                        Optional("chassis-re-usb-module"): [
                            {
                            "description": str,
                            "name": str,
                            "product": str,
                            "product-number": str,
                            "vendor": str,
                            },
                        ],
                        Optional("chassis-sub-module"): [
                            {
                                "chassis-sub-sub-module": {
                                    "description": str,
                                    "name": str,
                                    "part-number": str,
                                    "serial-number": str,
                                    Optional("chassis-sub-sub-sub-module"): [
                                        "description": str,
                                        "name": str,
                                        "part-number": str,
                                        "serial-number": str,
                                        Optional("version"): str
                                    ]
                                },
                                Optional("description"): str,
                                "name": str,
                                "part-number": str,
                                "serial-number": str,
                                "version": str
                            }
                        ],
                        "description": str,
                        "name": str,
                        Optional("part-number"): str,
                        Optional("serial-number"): str,
                        Optional("version"): str,
                    }
                ],
                "description": str,
                "name": str,
                "serial-number": str
            }
        }
    }
    '''
    # ------------------------------------------------------
    # Optional("chassis-re-dimm-module")
    # ------------------------------------------------------
    def validate_chassis_re_dimm_list(value):
        if not isinstance(value, list):
            raise SchemaError('chassis re dimm is not a list')

        chassis_re_dimm_schema = Schema(
           {"die-rev": str,
            "mfr-id": str,
            "name": str,
            "part-number": str,
            "pcb-rev": str,}
        )

        # Validate each dictionary in list
        for item in value:
            chassis_re_dimm_schema.validate(item)
        return value

    # ------------------------------------------------------
    # Optional("chassis-re-disk-module")
    # ------------------------------------------------------
    def validate_chassis_re_disk_list(value):
        if not isinstance(value, list):
            raise SchemaError('chassis re disk is not a list')

        chassis_re_disk_schema = Schema(
            {
                "description": str,
                "disk-size": str,
                "model": str,
                "name": str,
                "serial-number": str
            }
        )

        # Validate each dictionary in list
        for item in value:
            chassis_re_disk_schema.validate(item)
        return value        

    # ------------------------------------------------------
    # Optional("chassis-re-usb-module")
    # ------------------------------------------------------
    def validate_chassis_re_usb_list(value):
        if not isinstance(value, list):
            raise SchemaError('chassis re usb is not a list')

        chassis_re_usb_schema = Schema(
            {
                Optional("description"): str,
                "name": str,
                "product": str,
                "product-number": str,
                "vendor": str,
            }
        )

        # Validate each dictionary in list
        for item in value:
            chassis_re_usb_schema.validate(item)
        return value         

    # ------------------------------------------------------
    # Optional("chassis-sub-module")
    # ------------------------------------------------------
    def validate_chassis_sub_module_list(value):
        
        # ------------------------------------------------------
        # Optional("chassis-sub-sub-sub-module")
        # ------------------------------------------------------
        def validate_chassis_sub_sub_sub_module_list(value):
            # Pass list as value
            if not isinstance(value, list):
                raise SchemaError('inner chassis sub sub sub module is not a list')

            chassis_sub_sub_sub_module_schema = Schema(
                            {
                                Optional("description"): str,
                                Optional("name"): str,
                                Optional("part-number"): str,
                                Optional("serial-number"): str,
                                Optional("version"): str
                            }
                        )
            # Validate each dictionary in list
            for item in value:
                chassis_sub_sub_sub_module_schema.validate(item)
            return value
        

        # Pass list as value
        if not isinstance(value, list):
            raise SchemaError('inner chassis sub sub sub module is not a list')

        # ------------------------------------------------------
        # Optional("chassis-sub-sub-module")
        # ------------------------------------------------------
        def validate_chassis_sub_sub_module_list(value):
            # Pass list as value
            if not isinstance(value, list):
                raise SchemaError('inner chassis sub sub module is not a list')

            chassis_sub_sub_module_schema = Schema(
                            {
                                Optional("description"): str,
                                Optional("name"): str,
                                Optional("part-number"): str,
                                Optional("serial-number"): str,
                                Optional("chassis-sub-sub-sub-module"): Use(validate_chassis_sub_sub_sub_module_list)
                            },
                        )
            # Validate each dictionary in list
            for item in value:
                chassis_sub_sub_module_schema.validate(item)
            return value
        

        # Pass list as value
        if not isinstance(value, list):
            raise SchemaError('inner chassis sub sub module is not a list')

        chassis_sub_module_schema = Schema(
                        {
                            Optional("chassis-sub-sub-module"): Use(validate_chassis_sub_sub_module_list),
                            Optional("description"): str,
                            Optional("name"): str,
                            Optional("part-number"): str,
                            Optional("serial-number"): str,
                            Optional("version"): str
                        }
                    
        )
        # Validate each dictionary in list
        for item in value:
            chassis_sub_module_schema.validate(item)
        return value


    def validate_chassis_hardware_detail_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaError('chassis module is not a list')
        chassis_hardware_detail_schema = Schema({
            Optional("chassis-re-dimm-module"): Use(ShowChassisHardwareDetail.validate_chassis_re_dimm_list),
            Optional("chassis-re-disk-module"): Use(ShowChassisHardwareDetail.validate_chassis_re_disk_list),
            Optional("chassis-re-usb-module"): Use(ShowChassisHardwareDetail.validate_chassis_re_usb_list),
            Optional("chassis-sub-module"): Use(ShowChassisHardwareDetail.validate_chassis_sub_module_list),
            Optional("description"): str,
            Optional("name"): str,
            Optional("part-number"): str,
            Optional("serial-number"): str,
            Optional("version"): str,
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
            Optional("chassis-module"): Use(validate_chassis_hardware_detail_list),
            Optional("description"): str,
            Optional("name"): str,
            Optional("serial-number"): str
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

        # Hardware inventory:
        p1 = re.compile(r'^Hardware +(?P<style>\S+):$')

        # Chassis                                VM5D4C6B3599      VMX
        p_chassis = re.compile(r'^(?P<name>Chassis) +(?P<serial_number>[A-Z\d]+)'
                               r' +(?P<description>\S+)$')

        # -------------------------------------------------------------------------------------
        # For general chassis modules, for example:
        # -------------------------------------------------------------------------------------
        # Midplane         REV 64   750-040240   ABAC9716          Lower Backplane
        # Midplane 1       REV 06   711-032386   ABAC9742          Upper Backplane
        p_module0 = re.compile(r'(?P<name>Midplane( \d+)?) +(?P<version>\w+ \d+)'
                               r' +(?P<part_number>[\d\-]+) +(?P<serial_number>[A-Z\d]+) '
                               r'+(?P<description>[\s\S]+)$')
        
        # Routing Engine 0 REV 01   740-052100   9009237267        RE-S-1800x4
        # Routing Engine 0                                         RE-VMX
        # CB 0                                                     VMX SCB
        # FPC 0                                                    Virtual FPC
        # SPMB 0           REV 04   711-041855   ABDC5673          PMB Board
        # SFB 0            REV 06   711-044466   ABCY8621          Switch Fabric Board
        # ADC 9            REV 21   750-043596   ABDC2129          Adapter Card
        # Fan Tray 0       REV 01   760-052467   ACAY4748          172mm FanTray - 6 Fans
        # FPM Board        REV 13   760-040242   ABDD0194          Front Panel Display
        # PDM 3            REV 01   740-050036   1EFD3390136       DC Power Dist Module
        p_module1 = re.compile(r'^(?P<name>(Routing Engine|CB|FPC|SPMB|SFB|ADC|Fan Tray|FPM|PDM|PSM|PMP) (\d+|Board))( +(?P<version>\w+ \d+)'
                               r' +(?P<part_number>[\d\-]+) +(?P<serial_number>[A-Z\d]+))? '
                               r'+(?P<description>[\s\S]+)$')

        # Midplane
        p_module2 = re.compile(r'^(?P<name>Midplane)$')
        

        # -------------------------------------------------------------------------------------
        # For chassis-re-disk-module, for example:
        # -------------------------------------------------------------------------------------
        # ad0    3919 MB  604784               000060095234B000018D Compact Flash
        # ad1   28496 MB  StorFly - VSFA18PI032G- P1T12003591504100303 Disk 1
        p_re_disk = re.compile(r'^(?P<name>\w+) +(?P<disk_size>\d+) +MB +(?P<model>[\s\S]+) '
                               r'+(?P<serial_number>[A-Z\d]{20}) +(?P<description>[\s\S]+)$')


        # -------------------------------------------------------------------------------------
        # For chassis-re-usb-module, for example:
        # -------------------------------------------------------------------------------------
        # usb0 (addr 1)  EHCI root hub 0       Intel             uhub0
        # usb0 (addr 2)  product 0x0020 32     vendor 0x8087     uhub1
        p_re_usb = re.compile(r'^(?P<name>usb\d +\(addr +\d\)) +(?P<product>[\s\S]+) '
                              r'+(?P<product_number>\d+) +(?P<vendor>[\s\S]+) '
                              r'+(?P<description>[a-z0-9]+)$')


        # -------------------------------------------------------------------------------------
        # For chassis-re-dimm-module, for example:
        # -------------------------------------------------------------------------------------
        # DIMM 0         VL33B1G63F-K9SQ-KC DIE REV-0 PCB REV-0  MFR ID-ce80
        p_re_dimm = re.compile(r'^(?P<name>[A-Z\s\d]+) +(?P<part_number>[A-Z\d\-]+) '
                               r'+(?P<die_rev>DIE REV-\d+) +(?P<pcb_rev>PCB REV-\d+) '
                               r'+(?P<mfr_id>MFR ID\-\w+)$')


        # -------------------------------------------------------------------------------------
        # For chassis-sub-module, for example:
        # -------------------------------------------------------------------------------------
        # CPU            REV 12   711-045719   ABDF7304          RMPC PMB
        # MIC 0          REV 19   750-049457   ABDJ2346          2X100GE CFP2 OTN 
        # XLM 0          REV 14   711-046638   ABDF2862          MPC6E XL
        p_sub_module = re.compile(r'^(?P<name>CPU|(MIC|XLM)\s\d+) +(?P<version>\w+ \d+)'
                                  r' +(?P<part_number>[\d\-]+) +(?P<serial_number>[A-Z\d]+) '
                                  r'+(?P<description>[\s\S]+)$')

        # CPU            Rev. 1.0 RIOT-LITE    BUILTIN     
        p_sub_module_2 = re.compile(r'(?P<name>CPU) +(?P<version>[\s\S]+) +(?P<part_number>[A-Z\-]+)'
                                    r' +(?P<serial_number>[A-Z]+)')

        # MIC 0                                                  Virtual     
        p_sub_module_3 = re.compile(r'(?P<name>MIC\s\d+) +(?P<description>\S+)')


        # -------------------------------------------------------------------------------------
        # For chassis-sub-sub-module, for example:
        # -------------------------------------------------------------------------------------
        # PIC 0                 BUILTIN      BUILTIN           2X100GE CFP2 OTN
        p_sub_sub_module = re.compile(r'^(?P<name>PIC\s\d+) +(?P<part_number>[A-Z]+) '
                                      r'+(?P<serial_number>[A-Z]+) +(?P<description>[\s\S]+)$')


        # -------------------------------------------------------------------------------------
        # For chassis-sub-sub-sub-module, for example:
        # -------------------------------------------------------------------------------------
        # Xcvr 0     REV 01   740-052504   UW811XC           CFP2-100G-LR4
        # Xcvr 5              NON-JNPR     AGM1049Q4E4       SFP-T
        # Xcvr 8     l*       NON-JNPR     AGM17082139       SFP-T
        # Xcvr 9     }        NON-JNPR     AGM1708212S       SFP-T
        p_sub_sub_sub_module = re.compile(r'^(?P<name>Xcvr\s\d+)( +(?P<version>(\w+ \d+)|(\S+)))?'
                                          r' +(?P<part_number>[\d\-]+|NON-JNPR) +(?P<serial_number>[A-Z\d]+)'
                                          r' +(?P<description>[\s\S]+)$')                                      

        res = {}

        for line in out.splitlines():
            line = line.strip()
            
            #Hardware inventory:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                res = {
                    "chassis-inventory":{
                        "chassis":{

                        }
                    }
                }
                chassis_inventory_dict = res["chassis-inventory"]["chassis"]

                chassis_inventory_dict["@junos:style"] = group["style"]
                chassis_inventory_dict["chassis-module"] = []
                
                chassis_modules_list = chassis_inventory_dict["chassis-module"] 

                continue

            # Chassis                                VM5D4C6B3599      VMX
            m = p_chassis.match(line)
            if m:
                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        chassis_inventory_dict[k] = v.strip()
                continue

            # -------------------------------------------------------------------------------------
            # For general chassis modules, for example:
            # -------------------------------------------------------------------------------------
            # Midplane         REV 64   750-040240   ABAC9716          Lower Backplane
            # Midplane 1       REV 06   711-032386   ABAC9742          Upper Backplane
            
            # Routing Engine 0 REV 01   740-052100   9009237267        RE-S-1800x4
            # Routing Engine 0                                         RE-VMX
            # CB 0                                                     VMX SCB
            # FPC 0                                                    Virtual FPC
            # SPMB 0           REV 04   711-041855   ABDC5673          PMB Board
            # SFB 0            REV 06   711-044466   ABCY8621          Switch Fabric Board
            # ADC 9            REV 21   750-043596   ABDC2129          Adapter Card
            # Fan Tray 0       REV 01   760-052467   ACAY4748          172mm FanTray - 6 Fans            
            # FPM Board        REV 13   760-040242   ABDD0194          Front Panel Display

            # Midplane
            m = p_module0.match(line) or p_module1.match(line) or p_module2.match(line)
            if m:
                module_dict = {}
                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        module_dict[k] = v.strip()
                
                chassis_modules_list.append(module_dict)
                
                continue
                

            # -------------------------------------------------------------------------------------
            # For chassis-re-disk-module, for example:
            # -------------------------------------------------------------------------------------
            # ad0    3919 MB  604784               000060095234B000018D Compact Flash
            # ad1   28496 MB  StorFly - VSFA18PI032G- P1T12003591504100303 Disk 1                
            m = p_re_disk.match(line)
            if m:
                if "chassis-re-disk-module" not in module_dict:
                    module_dict["chassis-re-disk-module"] = []

                re_disk_module_list = module_dict["chassis-re-disk-module"]

                re_disk_module_item = {}

                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        re_disk_module_item[k] = v.strip()

                re_disk_module_list.append(re_disk_module_item)
                continue


            # -------------------------------------------------------------------------------------
            # For chassis-re-usb-module, for example:
            # -------------------------------------------------------------------------------------
            # usb0 (addr 1)  EHCI root hub 0       Intel             uhub0
            # usb0 (addr 2)  product 0x0020 32     vendor 0x8087     uhub1
            m = p_re_usb.match(line)
            if m:
                if "chassis-re-usb-module" not in module_dict:
                    module_dict["chassis-re-usb-module"] = []

                re_usb_module_list = module_dict["chassis-re-usb-module"]

                re_usb_module_item = {}

                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        re_usb_module_item[k] = v.strip()

                re_usb_module_list.append(re_usb_module_item)
                continue

            # -------------------------------------------------------------------------------------
            # For chassis-re-dimm-module, for example:
            # -------------------------------------------------------------------------------------
            # DIMM 0         VL33B1G63F-K9SQ-KC DIE REV-0 PCB REV-0  MFR ID-ce80        
            m = p_re_dimm.match(line)
            if m:
                if "chassis-re-dimm-module" not in module_dict:
                    module_dict["chassis-re-dimm-module"] = []

                re_usb_dimm_list = module_dict["chassis-re-dimm-module"]

                re_usb_dimm_item = {}

                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        re_usb_dimm_item[k] = v.strip()

                re_usb_dimm_list.append(re_usb_dimm_item)
                continue

            # -------------------------------------------------------------------------------------
            # For chassis-sub-module, for example:
            # -------------------------------------------------------------------------------------
            # CPU            REV 12   711-045719   ABDF7304          RMPC PMB
            # MIC 0          REV 19   750-049457   ABDJ2346          2X100GE CFP2 OTN 
            # XLM 0          REV 14   711-046638   ABDF2862          MPC6E XL
            # MIC 0                                                  Virtual
            # CPU            Rev. 1.0 RIOT-LITE    BUILTIN 
            m = p_sub_module.match(line) or p_sub_module_2.match(line) or p_sub_module_3.match(line)
            if m:
                if "chassis-sub-module" not in module_dict:
                    module_dict["chassis-sub-module"] = []

                re_sub_module_list = module_dict["chassis-sub-module"]
                last_sub_sub_item = {}

                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        last_sub_sub_item[k] = v.strip()
                
                re_sub_module_list.append(last_sub_sub_item)
                continue

            # -------------------------------------------------------------------------------------
            # For chassis-sub-sub-module, for example:
            # -------------------------------------------------------------------------------------
            # PIC 0                 BUILTIN      BUILTIN           2X100GE CFP2 OTN
            m = p_sub_sub_module.match(line)
            if m:
                # find the sub module
                last_sub_item = module_dict["chassis-sub-module"][-1]
                
                if "chassis-sub-sub-module" not in last_sub_item:
                    last_sub_item["chassis-sub-sub-module"] = []
                    
                re_sub_sub_module_item_list = last_sub_item["chassis-sub-sub-module"]

                re_sub_sub_module_list_item = {}
                
                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        re_sub_sub_module_list_item[k] = v.strip()
                re_sub_sub_module_item_list.append(re_sub_sub_module_list_item)
                
                continue
                

            # -------------------------------------------------------------------------------------
            # For chassis-sub-sub-sub-module, for example:
            # -------------------------------------------------------------------------------------
            # Xcvr 0     REV 01   740-052504   UW811XC           CFP2-100G-LR4
            m = p_sub_sub_sub_module.match(line)
            if m:
                # the last appended item
                last_sub_sub_item = module_dict["chassis-sub-module"][-1]["chassis-sub-sub-module"][-1]
                
                if "chassis-sub-sub-sub-module" not in last_sub_sub_item:
                    last_sub_sub_item["chassis-sub-sub-sub-module"] = []

                re_sub_sub_sub_module_list = last_sub_sub_item["chassis-sub-sub-sub-module"]

                re_sub_sub_sub_module_item = {}

                for k,v in m.groupdict().items():
                    k = k.replace('_', '-')
                    if v:
                        re_sub_sub_sub_module_item[k] = v.strip()
                
                re_sub_sub_sub_module_list.append(re_sub_sub_sub_module_item)
                continue
        
        return res

                

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
            raise SchemaError('inner chassis module is not a list')
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
            raise SchemaError('chassis module is not a list')
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
            raise SchemaError('fpc is not a list')
        chassis_fpc_schema = Schema({
                Optional("cpu-15min-avg"): str,
                Optional("cpu-1min-avg"): str,
                Optional("cpu-5min-avg"): str,
                Optional("cpu-interrupt"): str,
                Optional("cpu-total"): str,
                Optional("memory-buffer-utilization"): str,
                Optional("memory-dram-size"): str,
                Optional("memory-heap-utilization"): str,
                Optional("comment"): str,
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

        # 0  Online           Testing   3         0        2      2      2    511        31          0
        # 0  Present          Testing
        p1 = re.compile(r'^(?P<slot>\d+) +(?P<state>\S+) '
                        r'+(?P<text>\S+)( +(?P<cpu_total>\d+) '
                        r'+(?P<cpu_interrupt>\d+)( +(?P<cpu_1min>\d+) '
                        r'+(?P<cpu_5min>\d+) +(?P<cpu_15min>\d+))? +'
                        r'(?P<dram>\d+) +(?P<heap>\d+) +(?P<buffer>\d+))?$')

        #2  Empty
        p2 = re.compile(r'^(?P<slot>\d+) +(?P<state>\S+)$')
        
        # 0  Offline         ---Offlined by cli command---
        p3 = re.compile(r'^(?P<slot>\d+)\s+(?P<state>\S+)\s+---(?P<comment>Offlined\s+by\s+cli\s+command)---$')

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

                if group["cpu_total"]:
                    fpc_entry_dict["cpu-total"] = group["cpu_total"]

                if group["cpu_interrupt"]:
                    fpc_entry_dict["cpu-interrupt"] = group["cpu_interrupt"]

                if group["cpu_1min"]:
                    fpc_entry_dict["cpu-1min-avg"] = group["cpu_1min"]
                if group["cpu_5min"]:
                    fpc_entry_dict["cpu-5min-avg"] = group["cpu_5min"]
                if group["cpu_15min"]:
                    fpc_entry_dict["cpu-15min-avg"] = group["cpu_15min"]

                if group["dram"]:
                    fpc_entry_dict["memory-dram-size"] = group["dram"]
                
                if group["heap"]:
                    fpc_entry_dict["memory-heap-utilization"] = group["heap"]
                
                if group["buffer"]:
                    fpc_entry_dict["memory-buffer-utilization"] = group["buffer"]

                fpc_chassis_list.append(fpc_entry_dict)
                continue

            #2  Empty
            m = p2.match(line)
            if m:
                group = m.groupdict()
                fpc_chassis_list = ret_dict.setdefault("fpc-information", {})\
                    .setdefault("fpc", [])

                fpc_entry_dict = {}
                fpc_entry_dict["slot"] = group["slot"]
                fpc_entry_dict["state"] = group["state"]

                fpc_chassis_list.append(fpc_entry_dict)
                continue
            
            # 0  Offline         ---Offlined by cli command---
            m = p3.match(line)
            if m:
                group = m.groupdict()
                fpc_chassis_list = ret_dict.setdefault("fpc-information", {})\
                    .setdefault("fpc", [])
                fpc_entry_dict = {}
                fpc_entry_dict["slot"] = group["slot"]
                fpc_entry_dict["state"] = group["state"]
                fpc_entry_dict["comment"] = group["comment"]
                fpc_chassis_list.append(fpc_entry_dict)
                continue

        return ret_dict

class ShowChassisRoutingEngineSchema(MetaParser):

    schema = {
    Optional("@xmlns:junos"): str,
    "route-engine-information": {
        Optional("@xmlns"): str,
        "route-engine": [{
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
            }],
        Optional("re-state"): str
        }
    }


    def validate_chassis_routing_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaError('routing engine is not a list')
        chassis_routing_schema = Schema({
                Optional("cpu-background"): str,
                Optional("cpu-background-5sec"): str,
                Optional("cpu-background-1min"): str,
                Optional("cpu-background-5min"): str,
                Optional("cpu-background-15min"): str,
                Optional("cpu-idle"): str,
                Optional("cpu-idle-5sec"): str,
                Optional("cpu-idle-1min"): str,
                Optional("cpu-idle-5min"): str,
                Optional("cpu-idle-15min"): str,
                Optional("cpu-interrupt"): str,
                Optional("cpu-interrupt-5sec"): str,
                Optional("cpu-interrupt-1min"): str,
                Optional("cpu-interrupt-5min"): str,
                Optional("cpu-interrupt-15min"): str,
                Optional("cpu-system"): str,
                Optional("cpu-system-5sec"): str,
                Optional("cpu-system-1min"): str,
                Optional("cpu-system-5min"): str,
                Optional("cpu-system-15min"): str,
                Optional("cpu-temperature"):{
                    "#text": str
                },
                Optional("cpu-user"): str,
                Optional("cpu-user-5sec"): str,
                Optional("cpu-user-1min"): str,
                Optional("cpu-user-5min"): str,
                Optional("cpu-user-15min"): str,
                Optional("last-reboot-reason"): str,
                Optional("load-average-fifteen"): str,
                Optional("load-average-five"): str,
                Optional("load-average-one"): str,
                Optional("mastership-priority"): str,
                "mastership-state": str,
                Optional("memory-buffer-utilization"): str,
                Optional("memory-dram-size"): str,
                Optional("memory-installed-size"): str,
                Optional("model"): str,
                Optional("serial-number"): str,
                "slot": str,
                Optional("start-time"): {
                    "#text": str,
                    Optional("@junos:seconds"): str
                },
                Optional("status"): str,
                Optional("temperature"):{
                    "#text": str
                },
                Optional("up-time"): {
                    "#text": str,
                    Optional("@junos:seconds"): str
                    }
            })
        # Validate each dictionary in list
        for item in value:
            chassis_routing_schema.validate(item)
        return value

    schema = {
    Optional("@xmlns:junos"): str,
    "route-engine-information": {
        Optional("@xmlns"): str,
        "route-engine": Use(validate_chassis_routing_list),
        Optional("re-state"): str
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

        #Temperature                 42 degrees C / 107 degrees F
        p9_1 = re.compile(r'^Temperature +(?P<cpu_temperature>[\S\s]+)$')

        #Interrupt                  0 percent
        p10 = re.compile(r'^Interrupt +(?P<interrupt>\d+) +percent$')

        #Idle                      98 percent
        p11 = re.compile(r'^Idle +(?P<idle>\d+) +percent$')

        #Model                          RE-VMX
        p12 = re.compile(r'^Model +(?P<system>\S+)$')

        #Serial ID                      9009237474
        p12_1 = re.compile(r'^Serial +ID +(?P<serial_number>\d+)$')

        #Start time                     2019-08-29 09:02:22 UTC
        p13 = re.compile(r'^Start time +(?P<start_time>[\S\s]+)$')

        #CPU temperature             38 degrees C / 100 degrees F
        p13_1 = re.compile(r'^CPU +[tT]emperature +(?P<cpu_temperature>[\S\s]+)$')

        #Uptime                         208 days, 23 hours, 14 minutes, 9 seconds
        p14 = re.compile(r'^Uptime +(?P<uptime>[\S\s]+)$')

        #Last reboot reason             Router rebooted after a normal shutdown.
        p15 = re.compile(r'^Last reboot reason +(?P<last_reboot_reason>[\S\s]+)$')

        #0.72       0.46       0.40
        p16 = re.compile(r'^(?P<load_average_one>[\d\.]+) '
                         r'+(?P<load_average_five>[\d\.]+) '
                         r'+(?P<load_average_fifteen>[\d\.]+)$')

        #{master}
        p17 = re.compile(r'^(?P<re_state>[\{\S\s]+\})$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            #Slot 0:
            m = p1.match(line)
            if m:
                current_state = " "
                
                route_engine_list = ret_dict.setdefault("route-engine-information", {})\
                    .setdefault("route-engine", [])

                group = m.groupdict()
                route_engine_entry_dict = {}
                route_engine_list.append(route_engine_entry_dict)
                tag = ''
                route_engine_entry_dict["slot"] = group["slot"]
                continue

            #Current state                  Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["mastership-state"] = group["mastership_state"]
                continue

            #Election priority              Master (default)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["mastership-priority"] = group["mastership_priority"]
                continue

            #DRAM                      2002 MB (2048 MB installed)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["memory-dram-size"] = group["memory_dram_size"]
                route_engine_entry_dict["memory-installed-size"] = group["memory_installed_size"]
                continue

            #Memory utilization          19 percent
            m = p5.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["memory-buffer-utilization"] = group["memory_buffer_utilization"]
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
                route_engine_entry_dict["cpu-user"+tag] = group["user"]
                continue

            #Background                 0 percent
            m = p8.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["cpu-background"+tag] = group["background"]
                continue

            #Kernel                     1 percent
            m = p9.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["cpu-system"+tag] = group["system"]
                continue

            #Temperature                 42 degrees C / 107 degrees F
            m = p9_1.match(line)
            if m:
                group = m.groupdict()
                temp_dict = {}
                temp_dict["#text"] = group["cpu_temperature"]

                route_engine_entry_dict["temperature"] = temp_dict
                continue

            #Interrupt                  0 percent
            m = p10.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["cpu-interrupt"+tag] = group["interrupt"]
                continue

            #Idle                      98 percent
            m = p11.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["cpu-idle"+tag] = group["idle"]
                continue

            #Model                          RE-VMX
            m = p12.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["model"] = group["system"]
                continue

            #Serial ID                      9009237474
            m = p12_1.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["serial-number"] = group["serial_number"]
                continue

            #Start time                     2019-08-29 09:02:22 UTC
            m = p13.match(line)
            if m:
                group = m.groupdict()
                start_time_dict = {}
                start_time_dict["#text"] = group["start_time"]

                route_engine_entry_dict["start-time"] = start_time_dict
                continue
            
            #CPU temperature             38 degrees C / 100 degrees F
            m = p13.match(line)
            if m:
                group = m.groupdict()
                cpu_temp_dict = {}
                cpu_temp_dict["#text"] = group["cpu_temperature"]

                route_engine_entry_dict["cpu-temperature"] = cpu_temp_dict
                continue

            #Uptime                         208 days, 23 hours, 14 minutes, 9 seconds
            m = p14.match(line)
            if m:
                group = m.groupdict()
                up_time_dict = {}
                up_time_dict["#text"] = group["uptime"]

                route_engine_entry_dict["up-time"] = up_time_dict
                continue

            #Last reboot reason             Router rebooted after a normal shutdown.
            m = p15.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["last-reboot-reason"] = group["last_reboot_reason"]
                continue

            #0.72       0.46       0.40
            m = p16.match(line)
            if m:
                group = m.groupdict()
                route_engine_entry_dict["load-average-one"] = group["load_average_one"]
                route_engine_entry_dict["load-average-five"] = group["load_average_five"]
                route_engine_entry_dict["load-average-fifteen"] = group["load_average_fifteen"]
                continue

            #{master}
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ret_dict["route-engine-information"]["re-state"] = group["re_state"]
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
        
class ShowChassisEnvironmentSchema(MetaParser):

    def validate_environment_item_list(value):
        if not isinstance(value, list):
            raise SchemaError('environment-item is not a list')        
        
        environment_item_schema = Schema({
            Optional('class'): str,
            Optional('comment'): str,
            'name': str,
            'status': str,
            Optional('temperature'): {
                '#text': str,
                '@junos:celsius': str,
            }
        })

        for item in value:
            environment_item_schema.validate(item)
        return value

    schema = {
        'environment-information': {
            'environment-item': Use(validate_environment_item_list)
        }
    }

class ShowChassisEnvironment(ShowChassisEnvironmentSchema):
    """Parser for show chassis environment"""

    cli_command = 'show chassis environment'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output    

        #   Class Item                           Status     Measurement
        #   Temp  PSM 0                          OK         25 degrees C / 77 degrees F
        #   Fans  Fan Tray 0 Fan 1               OK         2760 RPM
        #         PSM 1                          OK         24 degrees C / 75 degrees F
        #         CB 0 IntakeA-Zone0             OK         39 degrees C / 102 degrees F     
        #         PSM 4                          Check        
        #         Fan Tray 2 Fan 2               OK         2640 RPM  
        p1 = re.compile(r'^((?P<class>Temp|Fans) +)?(?P<name>[\s\S]+) '
                        r'+(?P<status>OK|Check)( +(?P<measurement>[\s\S]+))?$')

        # 24 degrees C / 75 degrees F
        celsius_pattern = re.compile(r'(?P<celsius>\d+) degrees C / (?P<fahr>\d+) degrees F')
        
        res = {}
        environment_item_list = []
        class_flag = ''

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                res = {
                    'environment-information': {
                        'environment-item': environment_item_list
                }}

                group = m.groupdict()

                # environment_item schema:
                #         {
                #             Optional('class'): str,
                #             'name': str,
                #             'status': str,
                #             Optional('temperature'): {
                #                 '#text': str,
                #                 '@junos:celsius': str,
                #             }
                #         }
                environment_item = {}

                if group['class']:
                    class_flag = group['class']
                environment_item['class'] = class_flag
                
                environment_item['name'] = group['name'].strip()
                environment_item['status'] = group['status'].strip()

                text = group['measurement']

                if text:
                    #         CB 0 IntakeA-Zone0             OK         39 degrees C / 102 degrees F     
                    if celsius_pattern.match(text):
                        celsius_value = celsius_pattern.match(text).groupdict()['celsius']
                    
                        temperature_dict = {}
                        temperature_dict['@junos:celsius'] = celsius_value
                        temperature_dict['#text'] = text

                        environment_item['temperature'] = temperature_dict
                    
                    # Fan Tray 2 Fan 2               OK         2640 RPM
                    else:
                        environment_item['comment'] = text

                environment_item_list.append(environment_item)

        return res


class ShowChassisEnvironmentFpcSchema(MetaParser):
    '''
    Schema for show chassis environment fpc
    schema = {
        "environment-component-information": {
            "environment-component-item": [
                {
                    "name": str,
                    "power-information": {
                        "power-title": {
                            "power-type": str
                        }
                        "voltage": [
                            {
                                "actual-voltage": str,
                                "reference-voltage": str,
                            },
                        ]
                    },
                    "slave-revision": str,
                    "state": str,
                    "temperature-reading": [
                        {
                            "temperature": {
                                "#text": str,
                                "@junos:celsius": str,
                            },
                            "temperature-name": str,
                        },
                    ]
                }
            ]
        }
    }
    '''

    def validate_environment_item_list(value):
        if not isinstance(value, list):
            raise SchemaError('environment-item is not a list')        
        
        def validate_voltage_list(value):
            if not isinstance(value, list):
                raise SchemaError("voltage is not a list")

            voltage_schema = Schema(
                {
                    "actual-voltage": str,
                    "reference-voltage": str,
                }
            )

            for item in value:
                voltage_schema.validate(item)    
            return value

        def valivalidate_temp_reading_list(value):
            if not isinstance(value, list):
                raise SchemaError("temperature reading is not a list")

            temp_reading_schema = Schema(
                {
                    "temperature": {
                        "#text": str,
                        "@junos:celsius": str,
                    },
                    "temperature-name": str,
                }
            )

            for item in value:
                temp_reading_schema.validate(item)    
            return value

        environment_item_schema = Schema({
            "name": str,
            "power-information": {
                "power-title": {
                    "power-type": str
                },
                "voltage": Use(validate_voltage_list),
            },
            "slave-revision": str,
            "state": str,
            "temperature-reading": Use(valivalidate_temp_reading_list),
        })

        for item in value:
            environment_item_schema.validate(item)
        return value

    schema = {
        'environment-component-information': {
            'environment-component-item': Use(validate_environment_item_list)
        }
    }


class ShowChassisEnvironmentFpc(ShowChassisEnvironmentFpcSchema):
    '''Parser for show chassis environment fpc'''

    cli_command = 'show chassis environment fpc'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Regex
        # FPC 0 status:
        p1 = re.compile(r'^(?P<name>.*) +status:$')

        # State                      Online
        p2 = re.compile(r'^State +(?P<state>\S+)$')

        # Temperature Intake         27 degrees C / 80 degrees F
        # Temperature I3 0 Chip      38 degrees C / 100 degrees F 
        p_temp = re.compile(r'^(?P<temperature_name>[\s\S]+) '
                            r'+(?P<text>(?P<celsius>\d+)\sdegrees\sC.*)')

        # Power
        p_power = re.compile(r'^Power$')

        # 1.2 V PFE 0               1231 mV
        # 1.5 V                     1498 mV
        p_voltage = re.compile(r'(?P<reference_voltage>[\s\S]+) '
                               r'+(?P<actual_voltage>\d+) +mV')

        # I2C Slave Revision         42
        p_slave_revision = re.compile(r'^.* +Slave +Revision +(?P<slave_revision>\S+)$')


        # Read line from output and build parsed output
        res = {}

        for line in out.splitlines():
            line = line.strip()

            # FPC 0 status:
            m = p1.match(line)
            if m:
                if "environment-component-information" not in res:
                    res = {
                        "environment-component-information": {
                            "environment-component-item": []
                        }
                    }

                env_list = res["environment-component-information"]["environment-component-item"]

                env_item = {
                    "name": m.groupdict()["name"]
                }
                continue

            # State                      Online
            m = p2.match(line)
            if m:
                env_item["state"] = m.groupdict()["state"]
                continue

            # Temperature Intake         27 degrees C / 80 degrees F
            # Temperature I3 0 Chip      38 degrees C / 100 degrees F 
            m = p_temp.match(line)
            if m:
                group = m.groupdict()
                
                if "temperature-reading" not in env_item:
                    env_item["temperature-reading"] = []
                
                temp_list = env_item["temperature-reading"]

                temp_item = {
                    "temperature": {
                        "#text": group["text"].strip(),
                        "@junos:celsius": group["celsius"]
                    },
                    "temperature-name": group["temperature_name"].strip()
                }

                temp_list.append(temp_item)

                continue

            # Power
            m = p_power.match(line)
            if m:
                env_item["power-information"] = {
                    "power-title": {
                            "power-type": "Power"
                        },
                }
                continue

            # 1.2 V PFE 0               1231 mV
            # 1.5 V                     1498 mV
            m = p_voltage.match(line)
            if m:
                if "voltage" not in env_item["power-information"]:
                    env_item["power-information"]["voltage"] = []
                
                voltage_list = env_item["power-information"]["voltage"]

                voltage_item = {
                    "actual-voltage": m.groupdict()["actual_voltage"].strip(),
                    "reference-voltage": m.groupdict()["reference_voltage"].strip()
                }

                voltage_list.append(voltage_item)

                continue

            # I2C Slave Revision         42
            m = p_slave_revision.match(line)
            if m:
                env_item["slave-revision"] = m.groupdict()["slave_revision"].strip()
                env_list.append(env_item)
                continue

        return res


class ShowChassisAlarmsSchema(MetaParser):
    """ Schema for show chassis alarms"""
    schema = {
        "alarm-information": {
            "alarm-detail": {
                "alarm-class": str,
                "alarm-description": str,
                "alarm-short-description": str,
                "alarm-time": {
                    "#text": str,
                },
                "alarm-type": str
            },
            "alarm-summary": {
                "active-alarm-count": str
            }
        },
    }

class ShowChassisAlarms(ShowChassisAlarmsSchema):
    """Parser for show chassis alarms"""
    cli_command = 'show chassis alarms'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 1 alarms currently active
        p1 = re.compile(r'^(?P<active_alarms>\d+) +alarms +currently +active$')

        # Alarm time               Class  Description
        # 2020-07-16 13:38:21 EST  Major  PSM 15 Not OK 
        p2 = re.compile(r'^(?P<text>\S+ +\d\d\:\d\d\:\d\d +\S+) '
                        r'+(?P<alarm_class>\S+) +(?P<description>[\s\S]+)$')

        res = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                res = {
                    "alarm-information": {
                        "alarm-summary": {
                            "active-alarm-count": m.groupdict()['active_alarms']
                        }
                    }
                }
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()

                text = group['text']
                alarm_class = group['alarm_class']
                description = group['description']

                res['alarm-information']['alarm-detail'] = {
                    'alarm-class':alarm_class,
                    'alarm-description':description,
                    'alarm-short-description':description,
                    'alarm-time':{
                        '#text':text
                    },
                    "alarm-type": "Chassis"
                }
                continue

        return res


class ShowChassisFabricSummarySchema(MetaParser):

    """
        schema = {
        "fm-state-information": {
            "fm-state-item": [
                {
                    "plane-slot": str,
                    "state": str,
                    "up-time": str
                }
                ]
            }
        }"""

    def validate_chassis_fm_state(value):
        # Pass fm-state-item
        if not isinstance(value, list):
            raise SchemaError('fm-state-item is not a list')
        chassis_routing_schema = Schema({
                "plane-slot": str,
                "state": str,
                "up-time": str
            })
        # Validate each dictionary in list
        for item in value:
            chassis_routing_schema.validate(item)
        return value

    schema = {
    "fm-state-information": {
        "fm-state-item": Use(validate_chassis_fm_state)
        }
    }

class ShowChassisFabricSummary(ShowChassisFabricSummarySchema):
    """ Parser for:
    * show chassis fabric summary
    """

    cli_command = 'show chassis fabric summary'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 0      Online   34 days, 18 hours, 43 minutes, 48 seconds
        p1 = re.compile(r'^(?P<plane_slot>\d+) +(?P<state>\S+) +(?P<up_time>[\S\s]+)$')


        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 0      Online   34 days, 18 hours, 43 minutes, 48 seconds
            m = p1.match(line)
            if m:
                fm_state_information = ret_dict.setdefault("fm-state-information", {})\
                    .setdefault("fm-state-item", [])
                group = m.groupdict()

                fm_state_dict = {}
                for key, value in m.groupdict().items():
                    key = key.replace('_', '-')
                    fm_state_dict[key] = value

                fm_state_information.append(fm_state_dict)
                continue
        
        return ret_dict


class ShowChassisFabricPlaneSchema(MetaParser):

    """
        schema = {
        "fm-plane-state-information": {
            "fmp-plane": [
                {
                    "fru-name": "list",
                    "fru-slot": "list",
                    "pfe-link-status": "list",
                    "pfe-slot": "list",
                    "slot": str,
                    "state": str
                }
            ]
        }
    }"""

    def validate_chassis_fm_state(value):
        # Pass fm-state-item
        if not isinstance(value, list):
            raise SchemaError('routing engine is not a list')
        chassis_routing_schema = Schema({
                "fru-name": list,
                "fru-slot": list,
                "pfe-link-status": list,
                "pfe-slot": list,
                "slot": str,
                "state": str
            })
        # Validate each dictionary in list
        for item in value:
            chassis_routing_schema.validate(item)
        return value

    schema = {
    "fm-plane-state-information": {
        "fmp-plane": Use(validate_chassis_fm_state)
        }
    }

class ShowChassisFabricPlane(ShowChassisFabricPlaneSchema):
    """ Parser for:
    * show chassis fabric plane
    """

    cli_command = 'show chassis fabric plane'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Plane 0
        p1 = re.compile(r'^Plane +(?P<slot>\d+)$')

        # Plane state: ACTIVE
        p2 = re.compile(r'^Plane +state: +(?P<state>\S+)$')

        # FPC 0
        p3 = re.compile(r'^(?P<fpc_name>\S+) +(?P<fpc_slot>\d+)$')

        # PFE 1 :Links ok
        p4 = re.compile(r'^PFE +(?P<pfe>\d+) +:+(?P<links>[\S\s]+)$')


        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Plane 0
            m = p1.match(line)
            if m:
                fm_plane_state_information = ret_dict.setdefault("fm-plane-state-information", {})\
                    .setdefault("fmp-plane", [])
                group = m.groupdict()

                fm_state_dict = {}

                fru_name = fm_state_dict.setdefault("fru-name",[])
                fru_slot = fm_state_dict.setdefault("fru-slot",[])
                pfe_link_status = fm_state_dict.setdefault("pfe-link-status",[])
                pfe_slot = fm_state_dict.setdefault("pfe-slot",[])

                fm_plane_state_information.append(fm_state_dict)

                fm_state_dict.update({'slot' : group['slot']})

                continue

            # Plane state: ACTIVE
            m = p2.match(line)
            if m:
                group = m.groupdict()
                
                fm_state_dict.update({'state' : group['state']})
                continue
            
            # FPC 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                fru_name.append(group['fpc_name'])
                fru_slot.append(group['fpc_slot'])

                continue
            
            # PFE 1 :Links ok
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pfe_link_status.append(group['links'])
                pfe_slot.append(group['pfe'])

                continue
        
        return ret_dict

""" Schema for:
    * show chassis power
"""
class ShowChassisPowerSchema(MetaParser):
    def validate_power_usage_item(value):
        if not isinstance(value, list):
            raise SchemaError('power-usage-item is not a list')        
        
        power_usage_item_schema = Schema({
            "dc-input-detail2": {
                Optional("dc-input-status"): str,
                Optional("str-dc-actual-feed"): str,
                Optional("str-dc-expect-feed"): str
            },
            "dc-output-detail2": {
                "str-dc-current": str,
                "str-dc-load": str,
                "str-dc-power": str,
                "str-dc-voltage": str,
                "str-zone": str
            },
            "name": str,
            "pem-capacity-detail": {
                "capacity-actual": str,
                "capacity-max": str
            },
            "state": str
        })

        for item in value:
            power_usage_item_schema.validate(item)
        return value
    
    def validate_power_usage_zone_information_item(value):
        if not isinstance(value, list):
            raise SchemaError('power-usage-zone-information is not a list')        
        
        power_usage_zone_information_schema = Schema({
            "capacity-actual": str,
            "capacity-actual-usage": str,
            "capacity-allocated": str,
            "capacity-max": str,
            "capacity-remaining": str,
            "str-zone": str
        })

        for item in value:
            power_usage_zone_information_schema.validate(item)
        return value

    schema = {
        Optional("@xmlns:junos"): str,
        "power-usage-information": {
            "power-usage-item": Use(validate_power_usage_item),
            "power-usage-system": {
                "capacity-sys-actual": str,
                "capacity-sys-max": str,
                "capacity-sys-remaining": str,
                "power-usage-zone-information": Use(validate_power_usage_zone_information_item)
            }
        }
    }

class ShowChassisPower(ShowChassisPowerSchema):
    """ Parser for:
    * show chassis power
    """

    cli_command = 'show chassis power'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # PSM 0:
        p1 = re.compile(r'^(?P<name>\S+ +\d+):$')

        # State                      Online Master
        p2 = re.compile(r'^State: +(?P<state>[\S\s]+)$')

        # DC input:  OK (INP0 feed expected, INP0 feed connected)
        p3 = re.compile(r'^DC +input: +(?P<dc_input_status>[\S\s]+)( +\((?P<str_dc_expect_feed>\S+) +'
            r'feed +expected, +(?P<str_dc_actual_feed>\S+) +feed +connected\))?$')
        
        # Capacity:  2100 W (maximum 2500 W)
        p4 = re.compile(r'^Capacity: +(?P<capacity_actual>\d+) +\S+ +\(maximum +(?P<capacity_max>\d+) +\S+\)$')

        # DC output: 489.25 W (Lower Zone, 9.50 A at 51.50 V, 23.30% of capacity)
        p5 = re.compile(r'^DC +output: +(?P<str_dc_power>\S+) +\S+ +\((?P<str_zone>\S+) +'
            r'Zone, +(?P<str_dc_current>\S+) +\S+ +at +(?P<str_dc_voltage>\S+) +\S+, +'
            r'(?P<str_dc_load>\S+)\% +of +capacity\)$')
        
        # Total system capacity: 14700 W (maximum 17500 W)
        p6 = re.compile(r'^Total +system +capacity: +(?P<capacity_sys_actual>\S+) +\S+ +'
            r'\(maximum +(?P<capacity_sys_max>\S+) +\S+\)$')
        
        # Total remaining power: 5074 W
        p7 = re.compile(r'^Total +remaining +power: +(?P<capacity_sys_remaining>\S+) +\S+$')

        # Upper Zone:
        # Lower Zone:
        p8 = re.compile(r'^(?P<str_zone>\S+) +Zone:$')

        # Allocated power:   3332 W (2968 W remaining)
        p9 = re.compile(r'^Allocated +power: +(?P<capacity_allocated>\S+) +\S+ +\((?P<capacity_remaining>\S+) +\S+ +remaining\)$')

        # Actual usage:      925.50 W
        p10 = re.compile(r'^Actual +usage: +(?P<capacity_actual_usage>\S+) +\S+$')

        ret_dict = {}
        power_usage_system_found = False

        for line in out.splitlines():
            line = line.strip()

            # PSM 0:
            m = p1.match(line)
            if m:
                power_usage_information_list = ret_dict.setdefault("power-usage-information", {})\
                    .setdefault("power-usage-item", [])
                power_usage_item_dict = {}
                group = m.groupdict()
                power_usage_information_list.append(power_usage_item_dict)
                power_usage_item_dict.update({'name' : group['name']})
                continue

            # State                      Online Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                power_usage_item_dict.update({'state' : group['state']})
                continue
            
            # DC input:  OK (INP0 feed expected, INP0 feed connected)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                dc_input_detail2_dict = power_usage_item_dict.setdefault('dc-input-detail2', {})
                dc_input_detail2_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Capacity:  2100 W (maximum 2500 W)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if power_usage_system_found:
                    power_usage_zone_information_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                else:
                    pem_capacity_detail_dict = power_usage_item_dict.setdefault('pem-capacity-detail', {})
                    pem_capacity_detail_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # DC output: 489.25 W (Lower Zone, 9.50 A at 51.50 V, 23.30% of capacity)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                dc_output_detail2_dict = power_usage_item_dict.setdefault('dc-output-detail2', {})
                dc_output_detail2_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Total system capacity: 14700 W (maximum 17500 W)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                power_usage_system_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Total remaining power: 5074 W
            m = p7.match(line)
            if m:
                group = m.groupdict()
                power_usage_system_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Upper Zone:
            # Lower Zone:
            m = p8.match(line)
            if m:
                group = m.groupdict()
                power_usage_system_found = True
                power_usage_system_dict = ret_dict.setdefault("power-usage-information", {})\
                    .setdefault("power-usage-system", {})
                power_usage_zone_information_list = power_usage_system_dict.setdefault("power-usage-zone-information", [])
                power_usage_zone_information_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                power_usage_zone_information_list.append(power_usage_zone_information_dict)
                continue
            
            # Allocated power:   3332 W (2968 W remaining)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                power_usage_zone_information_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Actual usage:      925.50 W
            m = p10.match(line)
            if m:
                group = m.groupdict()
                power_usage_zone_information_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
        
        return ret_dict

"""
Schema for:
    * show chassis fpc pic-status
"""
class ShowChassisFpcPicStatusSchema(MetaParser):
    """
    schema = {
        "fpc-information": {
            "fpc": [
                {
                    "description": str,
                    "slot": str,
                    "state": str,
                    "pic": [
                        {
                            "pic-slot": str,
                            "pic-state": str,
                            "pic-type": str,
                        }
                    ]
                }
            ]
        }
    }
    """

    # Validate fpc
    def validate_fpc(value):

        if not isinstance(value, list):
            raise SchemaError('fpc is not a list')
        
        # Validate pic 
        def validate_pic(value):
            if not isinstance(value, list):
                raise SchemaError('pic is not a list')

            pic_schema = Schema({
                "pic-slot": str,
                "pic-state": str,
                "pic-type": str,
            })

            for item in value:
                pic_schema.validate(item)
            return value

        fpc_schema = Schema(
            {
                    "description": str,
                    "slot": str,
                    "state": str,
                    "pic": Use(validate_pic)
                }
        )

        for item in value:
            fpc_schema.validate(item)
        return value

    schema = {
        "fpc-information": {
            "fpc": Use(validate_fpc)
        }
    }

"""
Parser for:
    * show chassis fpc pic-status
"""
class ShowChassisFpcPicStatus(ShowChassisFpcPicStatusSchema):
    cli_command = 'show chassis fpc pic-status'

    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Regex patterns
        # Slot 0   Online       DPCE 2x 10GE R
        p_fpc = re.compile(r'Slot +(?P<slot>\d+) +(?P<state>\S+)'
                           r' +(?P<description>[\s\S]+)')

        # PIC 0  Online       1x 10GE(LAN/WAN)
        p_pic = re.compile(r'PIC +(?P<pic_slot>\d+) '
                           r'+(?P<pic_state>\S+) +(?P<pic_type>[\s\S]+)')

        # Build result dictionary
        res = {}

        for line in out.splitlines():
            line = line.strip()

            # Slot 0   Online       DPCE 2x 10GE R
            m = p_fpc.match(line)
            if m:
                group = m.groupdict()

                if "fpc-information" not in res:
                    res = {
                        "fpc-information": {
                            "fpc": []
                        }
                    }

                fpc_list = res["fpc-information"]["fpc"]

                fpc_item = {}

                for k, v in group.items():
                    fpc_item[k] = v

                fpc_list.append(fpc_item)
                continue

            # PIC 0  Online       1x 10GE(LAN/WAN)
            m = p_pic.match(line)
            if m:
                group = m.groupdict()
                
                if "pic" not in fpc_item:
                    fpc_item["pic"] = []

                pic_list = fpc_item["pic"]

                pic_item = {}

                for k, v in group.items():
                    k = k.replace('_' ,'-')

                    pic_item[k] = v

                pic_list.append(pic_item)
                continue

        return res


class ShowChassisEnvironmentComponentSchema(MetaParser):
    """ Schema for:
            * show chassis environment {component}
    """
    def validate_temperature_reading_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaError('environment-component-item is not a list')
        env_schema = Schema({
                        "temperature": {
                            "#text": str,
                            Optional("@junos:celsius"): str
                        },
                        "temperature-name": str
                    })
        # Validate each dictionary in list
        for item in value:
            env_schema.validate(item)
        return value
    
    def validate_voltage_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaError('environment-component-item is not a list')
        env_schema = Schema({
                            "actual-voltage": str,
                            "reference-voltage": str
                        })
        # Validate each dictionary in list
        for item in value:
            env_schema.validate(item)
        return value
    
    def validate_environment_component_item_list(value):
        # Pass firmware list as value
        if not isinstance(value, list):
            raise SchemaError('environment-component-item is not a list')
        env_schema = Schema({
                "name": str,
                "state": str,
                "bus-revision": str,
                "fpga-revision": str,
                "power-information": {
                    "power-title": {
                        "power-type": str
                    },
                    "voltage": Use(ShowChassisEnvironmentComponentSchema.validate_voltage_list)
                },
                "temperature-reading": Use(ShowChassisEnvironmentComponentSchema.validate_temperature_reading_list)
            })
        # Validate each dictionary in list
        for item in value:
            env_schema.validate(item)
        return value
    
    schema = {
        Optional("@xmlns:junos"): str,
        "environment-component-information": {
            Optional("@xmlns"):
            str,
            "environment-component-item": Use(validate_environment_component_item_list)
        }
    }


class ShowChassisEnvironmentComponent(ShowChassisEnvironmentComponentSchema):
    """ Parser for:
            * show chassis environment {component}
    """
    cli_command = 'show chassis environment {component}'

    def cli(self, component, output=None):
        if not output:
            out = self.device.execute(self.cli_command.format(
                component=component
            ))
        else:
            out = output

        ret_dict = {}

        # CB 0 status:
        p1 = re.compile(r'^(?P<name>\S+ +\d+) +status:$')

        # State                      Online Master
        p2 = re.compile(r'^State +(?P<state>[\S\s]+)$')

        # Power 1
        p3 = re.compile(r'^\w+ +(?P<power_type>\d+)$')

        # 1.0 V                     1005 mV
        p4 = re.compile(r'^(?P<temperature_name>.*) +(?P<text>\d+ +degrees +\w+ +\/ +\d+ +degrees +\w+)$')
        
        # TCBC-Zone0 Temperature     45 degrees C / 113 degrees F
        p5 = re.compile(r'^(?P<reference_voltage>[\d\.]+ +\w+( +\w+)?) +(?P<actual_voltage>\d+) +\w+$')

        # Bus Revision               100
        p6 = re.compile(r'^Bus +Revision +(?P<bus_revision>\d+)$')

        # FPGA Revision              272
        p7 = re.compile(r'^FPGA +Revision +(?P<fpga_revision>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # CB 0 status:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                environment_component_item_list = ret_dict.setdefault('environment-component-information', {}). \
                    setdefault('environment-component-item', [])
                environment_component_item_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                environment_component_item_list.append(environment_component_item_dict)
                continue
            
            # State                      Online Master
            m = p2.match(line)
            if m:
                group = m.groupdict()
                environment_component_item_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Power 1
            m = p3.match(line)
            if m:
                group = m.groupdict()
                power_info_dict = environment_component_item_dict.setdefault('power-information', {})
                power_title_dict = power_info_dict.setdefault('power-title', {}). \
                    setdefault('power-type', group['power_type'])
                continue
            
            # IntakeC-Zone0 Temperature  51 degrees C / 123 degrees F
            m = p4.match(line)
            if m:
                group = m.groupdict()
                temperature_reading_list = environment_component_item_dict.setdefault('temperature-reading', [])
                temperature_name = group['temperature_name']
                text = group['text']
                temperature_reading_dict = {'temperature-name': temperature_name,
                    'temperature': {'#text': text}}
                temperature_reading_list.append(temperature_reading_dict)
                continue
            
            # 1.0 V                     1005 mV
            m = p5.match(line)
            if m:
                group = m.groupdict()
                voltage_list = power_info_dict.setdefault('voltage', [])
                voltage_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                voltage_list.append(voltage_dict)
                continue
            
            # Bus Revision               100
            m = p6.match(line)
            if m:
                group = m.groupdict()
                environment_component_item_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # FPGA Revision              272
            m = p7.match(line)
            if m:
                group = m.groupdict()
                environment_component_item_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
        
        return ret_dict