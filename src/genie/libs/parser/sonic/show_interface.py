"""
Sonic parsers for the following show commands:

    * show interfaces transceiver eeprom

"""
# Python
import re
import os
# Metaparser
from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
from genie.metaparser.util.schemaengine import Schema, Any, Optional, ListOf


class ShowInterfacesTransceiverEepromSchema(MetaParser):

    """
    Schema for
        * show interfaces transceiver eeprom
    """

    schema = {
            Any(): 
                {
                'oper_status': str,
                Optional('application_advertisment'):{
                    Optional('application_type'):str,
                    Optional('host_assign'):str,
                    Optional('cable_type'):str,
                    Optional('media_assign'):str,
                },
                Optional('connector'): str,
                Optional('encoding'): str,
                Optional('identifier'): str,
                Optional('extended_identifier'): str,
                Optional('extended_rate_compliance'): str,
                Optional('cable_length'): float,
                Optional('input_rate_mps'): int,
                Optional('compliance'):{
                    Any():{
                        Optional('specification'):str,
                        Optional('compliance_code'):str,
                        Optional('fiber'):{
                            Optional('length'):str,
                            Optional('speed'):str,
                            Optional('transmisson_media'): str,
                            Optional('transmission_technology'):str,
                            
                        }
                    }
                },
                Optional('vendor'):{
                    Optional('date'): str,
                    Optional('lot'): str,
                    Optional('name'):str,
                    Optional('oui'):str,
                    Optional('pn'): str,
                    Optional('rev'): str,
                    Optional('sn'): str

                }
            }
    }
        

class ShowInterfacesTransceiverEeprom(ShowInterfacesTransceiverEepromSchema):

    """
    Parser for
        * show interfaces transceiver eeprom
    """

    cli_command = "show interfaces transceiver eeprom"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # Ethernet0: SFP EEPROM detected
        p1 = re.compile(r'^(?P<name>[\w\/\.\-\:]+): SFP EEPROM +(?P<status>.+)$')

        # Application Advertisement: 400G CR8 - Host Assign (0x1) - Copper cable - Media Assign (Unknown)
        p2 = re.compile(r'^Application Advertisement: (?P<application_type>[\dA-Z\s]+) - Host Assign \((?P<host_assign>0x[0-9a-fA-F]+)\) - (?P<media_type>\w+) cable - Media Assign \((?P<media_assign>\w+)\)$')

        # Application Advertisement: N/A
        p2_1 = re.compile(r'^Application Advertisement: N/A$')

        # Connector: No separable connector
        p3 = re.compile(r'^Connector: (?P<connector>.+)$')

        # Encoding: N/A
        p4 = re.compile(r'^Encoding: (?P<encoding>.*)$')

        # Extended Identifier: Power Class 1 (1.5W Max)
        p5 = re.compile(r'^Extended Identifier: (?P<identifier>.+)$')

        # Extended RateSelect Compliance: N/A
        p6 =  re.compile(r'^Extended RateSelect Compliance: (?P<compliance>.+)$')

        # Identifier: QSFP-DD Double Density 8X Pluggable Transceiver
        p7 = re.compile(r'^Identifier: (?P<identifier>.+)$')

        # Length Cable Assembly(m): 2.0
        p8 = re.compile(r'^Length Cable Assembly\(m\): (?P<length>\d+(\.\d+)?)$')

        #  Nominal Bit Rate(100Mbs): 0
        p9 = re.compile(r'^Nominal Bit Rate\(100Mbs\): (?P<rate>\d+)$')

        # Vendor Date Code(YYYY-MM-DD Lot): 2020-07-17 00
        p10 = re.compile(r'^Vendor Date Code\(YYYY-MM-DD Lot\): (?P<date>\d{4}-\d{2}-\d{2}) (?P<lot>\d+)$')
        
        # Vendor Name: CISCO-LEONI
        p11 =  re.compile(r'^Vendor Name: (?P<vendor_name>.+)$')

        # Vendor OUI: a8-b0-ae
        p12 =  re.compile(r'^Vendor OUI: (?P<vendor_oui>.+)$')

        # Vendor PN: L45593-K218-C20
        p13 = re.compile(r'^Vendor PN: (?P<vendor_pn>.+)$')

        # Vendor Rev: 00
        # Vendor Rev: A
        p14 = re.compile(r'^Vendor Rev: (?P<vendor_rev>.+)$')
        
        # Vendor SN: LCC2429H3GD-A
        p15 = re.compile(r'^Vendor SN: (?P<vendor_sn>.+)$')

        # Specification compliance: passive_copper_media_interface
        p16 = re.compile(r'^Specification compliance: (?P<spec_compliance>.+)$')

        # Specification compliance:
        p16_1 = re.compile(r'^Specification compliance:$')

        # 10/40G Ethernet Compliance Code: Extended
        # Gigabit Ethernet Compliant Codes: Unknown
        p17 = re.compile(r'^(?P<compliance>.+) Compliance Code[s]?: (?P<compliance_code>.+)$')

        # Extended Specification Compliance: 100G AOC (Active Optical Cable) or 25GAUI C2M AOC
        p18 = re.compile(r'^Extended Specification Compliance: (?P<ext_spec_compliance>.+)$')

        # Fibre Channel Link Length: Unknown
        p19 = re.compile(r'^Fibre Channel Link Length: (?P<link_length>.+)$')

        # Fibre Channel Speed: Unknown
        p20 = re.compile(r'^Fibre Channel Speed: (?P<link_speed>.+)$')

        # Fibre Channel Transmission Media: Unknown
        p21 = re.compile(r'^Fibre Channel Transmission Media: (?P<link_media>.+)$')

        # Fibre Channel Transmitter Technology: Unknown
        p22 = re.compile(r'^Fibre Channel Transmitter Technology: (?P<link_tech>.+)$')


        for line in output.splitlines():
            line = line.strip()

            # Ethernet0: SFP EEPROM detected
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                intf_name =  Common.convert_intf_name(match_dict['name'])
                intf_dict = ret_dict.setdefault(intf_name, {})
                intf_dict['oper_status'] = match_dict['status']
                continue

            # Application Advertisement: 400G CR8 - Host Assign (0x1) - Copper cable - Media Assign (Unknown)
            m = p2.match(line)
            if m:
                match_dict = m.groupdict()
                app_dict = intf_dict.setdefault('application_advertisment', {})
                app_dict['application_type'] = match_dict['application_type']
                app_dict['host_assign'] = match_dict['host_assign']
                app_dict['cable_type'] = match_dict['media_type']
                app_dict['media_assign'] = match_dict['media_assign']
                continue

            # Application Advertisement: N/A
            m = p2_1.match(line)
            if m:
                match_dict = m.groupdict()
                app_dict = intf_dict.setdefault('application_advertisment', {})
                app_dict['application_type'] = 'NA'
                continue

            # Connector: No separable connector
            m = p3.match(line)
            if m:
                match_dict = m.groupdict()
                intf_dict['connector'] = match_dict['connector']
                continue

            # Encoding: N/A
            m = p4.match(line)
            if m:
                match_dict = m.groupdict()
                intf_dict['encoding'] = match_dict['encoding']
                continue

            # Extended Identifier: Power Class 1 (1.5W Max)
            m = p5.match(line)
            if m:
                match_dict = m.groupdict()
                intf_dict['extended_identifier'] = match_dict['identifier']
                continue

            # Extended RateSelect Compliance: N/A 
            m = p6.match(line)
            if m:
                match_dict = m.groupdict()
                intf_dict['extended_rate_compliance'] = match_dict['compliance']
                continue

            # Identifier: QSFP-DD Double Density 8X Pluggable Transceiver
            m = p7.match(line)
            if m:
                match_dict = m.groupdict()
                intf_dict['identifier'] = match_dict['identifier']
                continue

            # Length Cable Assembly(m): 2.0
            m = p8.match(line)
            if m:
                match_dict = m.groupdict()
                intf_dict['cable_length'] = float(match_dict['length'])
                continue

            #  Nominal Bit Rate(100Mbs): 0            m = p9.match(line)
            m = p9.match(line)
            if m:
                match_dict = m.groupdict()
                intf_dict['input_rate_mps'] = int(match_dict['rate'])
                continue

            # Vendor Date Code(YYYY-MM-DD Lot): 2020-07-17 00
            m = p10.match(line)
            if m:
                match_dict = m.groupdict()
                vendor_dict = intf_dict.setdefault('vendor', {})
                vendor_dict['date'] = match_dict['date']
                vendor_dict['lot'] = match_dict['lot']
                continue

            # Vendor Name: CISCO-LEONI
            m = p11.match(line)
            if m:
                match_dict = m.groupdict()
                vendor_dict['name'] = match_dict['vendor_name']
                continue

            # Vendor OUI: a8-b0-ae
            m = p12.match(line)
            if m:
                match_dict = m.groupdict()
                vendor_dict['oui'] = match_dict['vendor_oui']
                continue

            # Vendor PN: L45593-K218-C20
            m = p13.match(line)
            if m:
                match_dict = m.groupdict()
                vendor_dict['pn'] = match_dict['vendor_pn']
                continue

            # Vendor Rev: 00
            # Vendor Rev: A
            m = p14.match(line)
            if m:
                match_dict = m.groupdict()
                vendor_dict['rev'] = match_dict['vendor_rev']
                continue
                # Vendor Rev: 00

            # Vendor SN: LCC2429H3GD-A
            m = p15.match(line)
            if m:
                match_dict = m.groupdict()
                vendor_dict['rev'] = match_dict['vendor_sn']
                continue

            # Specification compliance: passive_copper_media_interface  
            m = p16.match(line)
            if m:
                match_dict = m.groupdict()
                compliance = match_dict['spec_compliance']
                spec_compliance_dict = intf_dict.setdefault('compliance', {}).setdefault(compliance, {})
                spec_compliance_dict['specification'] = match_dict['spec_compliance']
                continue

            # Specification compliance: passive_copper_media_interface  
            m = p16_1.match(line)
            if m:
                spec_compliance_dict = intf_dict.setdefault('compliance', {})
                continue

            # Gigabit Ethernet Compliant Codes: Unknown
            m = p17.match(line)
            if m:
                match_dict = m.groupdict()
                compliance = match_dict['compliance']
                spec_compliance_dict = intf_dict.setdefault('compliance', {}).setdefault(compliance, {})
                spec_compliance_dict['compliance_code'] = match_dict['compliance_code']
                continue

            # Extended Specification Compliance: 100G AOC (Active Optical Cable) or 25GAUI C2M AOC
            m = p18.match(line)
            if m:
                match_dict = m.groupdict()
                spec_compliance_dict['specification'] = match_dict['ext_spec_compliance']
                continue

            # Fibre Channel Link Length: Unknown
            m = p19.match(line)
            if m:
                match_dict = m.groupdict()
                fib_dict = spec_compliance_dict.setdefault('fiber', {})
                fib_dict['length'] = match_dict['link_length']
                continue

            # Fibre Channel Speed: Unknown
            m = p20.match(line)
            if m:
                match_dict = m.groupdict()
                fib_dict['speed'] = match_dict['link_speed']
                continue

            # Fibre Channel Transmission Media: Unknown
            m = p21.match(line)
            if m:
                match_dict = m.groupdict()
                fib_dict['transmisson_media'] = match_dict['link_media']
                continue

            # Fibre Channel Transmitter Technology: Unknown
            m = p22.match(line)
            if m:
                match_dict = m.groupdict()
                fib_dict['transmission_technology'] = match_dict['link_tech']
                continue
        return ret_dict
