import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional, Any
# import parser utils
from genie.libs.parser.utils.common import Common


# ==============================================
# Parser for 'show macsec summary'
# ==============================================

class ShowMacsecSummarySchema(MetaParser):
    """
    Schema for 'show macsec summary'

    """

    schema = {
        'interfaces': {
            Any(): {
                'transmit_sc': str,
                'receive_sc': str
            },
        }
    }


# ==========================================================
#  Parser for show macsec summary
# ==========================================================
class ShowMacsecSummary(ShowMacsecSummarySchema):
    """
    parser for
            * show macsec summary
    """

    cli_command = 'show macsec summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Te2/0/13                           1                   1
        # port-channel1                      1                   2
        # Fif1/6/0/32.2001                   1                   2
        p1 = re.compile(r'^(?P<interface>[\w\s\.\-\/]+)\s+(?P<transmit_sc>\d+)\s+(?P<receive_sc>\d+)$')

        ret_dict = {}
        if out != '':
            res_dict = ret_dict.setdefault('interfaces', {})
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name \
                    (intf=group['interface'].strip())
                intf_dict = res_dict.setdefault(interface,{})
                intf_dict['transmit_sc'] = group['transmit_sc']
                intf_dict['receive_sc'] = group['receive_sc']

        return ret_dict


# ====================================================
#  Schema for show macsec post
# ====================================================
class ShowMacsecPostSchema(MetaParser):
    """Schema for 'show macsec post'"""

    schema = {
        'interfaces': {
            Any(): {
                'post_result': str,
            }
        }
    }

# ======================================================
# Parser for 'show macsec post'
# ======================================================
    
class ShowMacsecPost(ShowMacsecPostSchema):
    """Parser for 'show macsec post'"""

    cli_command = 'show macsec post'

    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute(self.cli_command)

        else:
            out = output

        # MACsec Capable Interface                         POST Result
        # --------------------------------------------------------------
        # TenGigabitEthernet0/0/0                             NONE

        p1 = re.compile(r"^\s*(?P<macsec_capable_interface>\S+)\s+(?P<post_result>\S+)\s*$")

        ret_dict = {}


        for line in output.splitlines():
            line = line.strip()  

        # MACsec Capable Interface                         POST Result
        # --------------------------------------------------------------
        # TenGigabitEthernet0/0/0                             NONE
            
            m = p1.match(line)
            if m:
                group = m.groupdict() 
                interface = group['macsec_capable_interface']  
                int_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                int_dict['post_result'] = group['post_result']  
                continue 

        return ret_dict  


# ==============================================
# Schema for 'show macsec interface {interface}'
# ==============================================

class ShowMacsecStatisticsInterfaceSchema(MetaParser):
    schema = {
        'sec_counters': {
                "ingress_untag_pkts": int,
                "ingress_no_tag_pkts": int,
                "ingress_bad_tag_pkts": int,
                "ingress_unknown_sci_pkts": int,
                "ingress_no_sci_pkts": int,
                "ingress_overrun_pkts": int,
                "ingress_validated_octets": int,
                "ingress_decrypted_octets": int ,
                "egress_untag_pkts": int,
                "egress_too_long_pkts": int,
                "egress_protected_octets": int,
                "egress_encrypted_octets": int
        },
        'controlled_counters': {
                'if_in_octects': int,
                'if_in_packets': int,
                'if_in_discard': int,
                'if_in_errors': int,
                'if_out_octects': int,
                'if_out_packets': int,
                'if_out_errors': int
        },
        'transmit_sc_counters': {
            Any(): {   
                'out_pkts_protected': int,
                'out_pkts_encrypted': int
            }
        },
        'receive_sa_counters': {
            Any(): {   
                'sci': str,
                'an': str,
                'in_pkts_unchecked': int,
                'in_pkts_delayed': int,
                'in_pkts_ok': int,
                'in_pkts_invalid': int,
                'in_pkts_not_valid': int,
                'in_pkts_not_using_sa': int,
                'in_pkts_unused_sa': int,
                'in_pkts_late': int
                }
        }
    }

#==============================================
#Parser for 'show macsec statistics interface {interface}'
#==============================================
	
class ShowMacsecStatisticsInterface(ShowMacsecStatisticsInterfaceSchema):

    cli_command = 'show macsec statistics interface {interface}'

    def cli(self, interface, output=None):
        if not output:
            # get output from device
            output = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output
        
        ret_dict = {}

        #  Ingress Untag Pkts:       0
        p1 = re.compile(r'^Ingress\s+Untag\s+Pkts:\s+(?P<ingress_untag_pkts>\d+)$')

        #   Ingress No Tag Pkts:      0
        p2 = re.compile(r'^Ingress\s+No\s+Tag\s+Pkts:\s+(?P<ingress_no_tag_pkts>\d+)$')

        #   Ingress Bad Tag Pkts:     0
        p3 = re.compile(r'^Ingress\s+Bad\s+Tag\s+Pkts:\s+(?P<ingress_bad_tag_pkts>\d+)$')

        #   Ingress Unknown SCI Pkts: 0
        p4 = re.compile(r'^Ingress\s+Unknown\s+SCI\s+Pkts:\s+(?P<ingress_unknown_sci_pkts>\d+)$')

        #   Ingress No SCI Pkts:      0
        p5 = re.compile(r'^Ingress\s+No\s+SCI\s+Pkts:\s+(?P<ingress_no_sci_pkts>\d+)$')

        #   Ingress Overrun Pkts:     0
        p6 = re.compile(r'^Ingress\s+Overrun\s+Pkts:\s+(?P<ingress_overrun_pkts>\d+)$')

        #   Ingress Validated Octets: 0
        p7 = re.compile(r'^Ingress\s+Validated\s+Octets:\s+(?P<ingress_validated_octets>\d+)$')

        #   Ingress Decrypted Octets: 184493007008
        p8 = re.compile(r'^Ingress\s+Decrypted\s+Octets:\s+(?P<ingress_decrypted_octets>\d+)$')

        #   Egress Untag Pkts:        0
        p9 = re.compile(r'^Egress\s+Untag\s+Pkts:\s+(?P<egress_untag_pkts>\d+)$')

        #   Egress Too Long Pkts:     0
        p10 = re.compile(r'^Egress\s+Too\s+Long\s+Pkts:\s+(?P<egress_too_long_pkts>\d+)$')

        #   Egress Protected Octets:  0
        p11 = re.compile(r'^Egress\s+Protected\s+Octets:\s+(?P<egress_protected_octets>\d+)$')

        #   Egress Encrypted Octets:  3519888
        p12 = re.compile(r'^Egress\s+Encrypted\s+Octets:\s+(?P<egress_encrypted_octets>\d+)$')

        #   IF In Octets:             186176188032
        p13 = re.compile(r'^IF\s+In\s+Octets:\s+(?P<if_in_octects>\d+)$')

        #   IF In Packets:            134202116
        p14 = re.compile(r'^IF\s+In\s+Packets:\s+(?P<if_in_packets>\d+)$')

        #   IF In Discard:            0
        p15 = re.compile(r'^IF\s+In\s+Discard:\s+(?P<if_in_discard>\d+)$')

        #   IF In Errors:             0
        p16 = re.compile(r'^IF\s+In\s+Errors:\s+(?P<if_in_errors>\d+)$')

        #   IF Out Octets:            3623448
        p17 = re.compile(r'^IF\s+Out\s+Octets:\s+(?P<if_out_octects>\d+)$')

        #   IF Out Packets:           8630
        p18 = re.compile(r'^IF\s+Out\s+Packets:\s+(?P<if_out_packets>\d+)$')

        #   IF Out Errors:            0
        p19 = re.compile(r'^IF\s+Out\s+Errors:\s+(?P<if_out_errors>\d+)$')

        #Transmit SC Counters (SCI: 44881699B510001C)
        p20 = re.compile(r'^Transmit SC Counters \(SCI: (?P<sci>\w+)\)$')

        #   Out Pkts Protected:       0
        p21 = re.compile(r'^Out\s+Pkts\s+Protected:\s+(?P<out_pkts_protected>\d+)$')

        #   out_pkts_encrypted:       8630
        p22 = re.compile(r'^Out\s+Pkts\s+Encrypted:\s+(?P<out_pkts_encrypted>\d+)$')

        # Receive SA Counters (SCI: A44C119DF89C001E  AN 0)
        p23 = re.compile(r'^Receive\s+SA\s+Counters\s+\(SCI:\s+(?P<sci>\S+)\s+AN\s+(?P<an>\S+)\)$')

        #   In Pkts Unchecked:        0
        p24 = re.compile(r'^In\s+Pkts\s+Unchecked:\s+(?P<in_pkts_unchecked>\d+)$')

        #   In Pkts Delayed:          0
        p25 = re.compile(r'^In\s+Pkts\s+Delayed:\s+(?P<in_pkts_delayed>\d+)$')

        #   In Pkts OK:               103416932
        p26 = re.compile(r'^In\s+Pkts\s+OK:\s+(?P<in_pkts_ok>\d+)$')

        #   In Pkts Invalid:          0
        p27 = re.compile(r'^\s*In\s+Pkts\s+Invalid:\s+(?P<in_pkts_invalid>\d+)$')

        #   In Pkts Not Valid:        0
        p28 = re.compile(r'^In\s+Pkts\s+Not\s+Valid:\s+(?P<in_pkts_not_valid>\d+)$')

        #   In Pkts Not using SA:     0
        p29 = re.compile(r'^In\s+Pkts\s+Not\s+using\s+SA:\s+(?P<in_pkts_not_using_sa>\d+)$')

        #   In Pkts Unused SA:        0
        p30 = re.compile(r'^In\s+Pkts\s+Unused\s+SA:\s+(?P<in_pkts_unused_sa>\d+)$')

        #   In Pkts Late:             0
        p31 = re.compile(r'^In\s+Pkts\s+Late:\s+(?P<in_pkts_late>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            #  Ingress Untag Pkts:       0		
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                sec_counters_dict = ret_dict
                sec_counters_dict = sec_counters_dict.setdefault('sec_counters', {})	   
                sec_counters_dict['ingress_untag_pkts'] = int(groups['ingress_untag_pkts'])
                continue

            #   Ingress No Tag Pkts:      0
            m = p2.match(line)
            if m:
                groups = m.groupdict()	
                sec_counters_dict['ingress_no_tag_pkts'] = int(groups['ingress_no_tag_pkts'])
                continue

            #   Ingress Bad Tag Pkts:     0
            m = p3.match(line)
            if m:
                groups = m.groupdict()	
                sec_counters_dict['ingress_bad_tag_pkts'] = int(groups['ingress_bad_tag_pkts'])
                continue

            #   Ingress Unknown SCI Pkts: 0
            m = p4.match(line)
            if m:
                groups = m.groupdict()	
                sec_counters_dict['ingress_unknown_sci_pkts'] = int(groups['ingress_unknown_sci_pkts'])
                continue

            #   Ingress No SCI Pkts:      0
            m = p5.match(line)
            if m:
                groups = m.groupdict()	
                sec_counters_dict['ingress_no_sci_pkts'] =int( groups['ingress_no_sci_pkts'])
                continue

            #   Ingress Overrun Pkts:     0
            m = p6.match(line)
            if m:
                groups = m.groupdict()	
                sec_counters_dict['ingress_overrun_pkts'] = int(groups['ingress_overrun_pkts'])
                continue

            #   Ingress Validated Octets: 0
            m = p7.match(line)
            if m:
                groups = m.groupdict()	
                sec_counters_dict['ingress_validated_octets'] = int(groups['ingress_validated_octets'])
                continue

            #   Ingress Decrypted Octets: 184493007008
            m = p8.match(line)
            if m:
                groups = m.groupdict()	
                sec_counters_dict['ingress_decrypted_octets'] = int(groups['ingress_decrypted_octets'])
                continue

            #   Egress Untag Pkts:        0    
            m = p9.match(line)
            if m:
                groups = m.groupdict()    
                sec_counters_dict['egress_untag_pkts'] = int(groups['egress_untag_pkts'])
                continue

            #   Egress Too Long Pkts:     0
            m = p10.match(line)
            if m:
                groups = m.groupdict()    
                sec_counters_dict['egress_too_long_pkts'] = int(groups['egress_too_long_pkts'])
                continue

            #   Egress Protected Octets:  0
            m = p11.match(line)
            if m:
                groups = m.groupdict()    
                sec_counters_dict['egress_protected_octets'] = int(groups['egress_protected_octets'])
                continue

            #   Egress Encrypted Octets:  3519888
            m = p12.match(line)
            if m:
                groups = m.groupdict()    
                sec_counters_dict['egress_encrypted_octets'] = int(groups['egress_encrypted_octets'])
                continue

            #   IF In Octets:             186176188032
            m = p13.match(line)
            if m:
                groups = m.groupdict() 
                controlled_counters_dict = ret_dict   
                controlled_counters_dict = controlled_counters_dict.setdefault('controlled_counters',{})
                controlled_counters_dict['if_in_octects'] = int(groups['if_in_octects'])
                continue

            #   IF In Packets:            134202116
            m = p14.match(line)
            if m:
                groups = m.groupdict()    
                controlled_counters_dict['if_in_packets'] = int(groups['if_in_packets'])
                continue

            #   IF In Discard:            0
            m = p15.match(line)
            if m:
                groups = m.groupdict()    
                controlled_counters_dict['if_in_discard'] = int(groups['if_in_discard'])
                continue

            #   IF In Errors:             0
            m = p16.match(line)
            if m:
                groups = m.groupdict()    
                controlled_counters_dict['if_in_errors'] = int(groups['if_in_errors'])
                continue

            #   IF Out Octets:            3623448
            m = p17.match(line)
            if m:
                groups = m.groupdict()    
                controlled_counters_dict['if_out_octects'] = int(groups['if_out_octects'])
                continue

            #   IF Out Packets:           8630
            m = p18.match(line)
            if m:
                groups = m.groupdict()    
                controlled_counters_dict['if_out_packets'] = int(groups['if_out_packets'])
                continue

            #   IF Out Errors:            0
            m = p19.match(line)
            if m:
                groups = m.groupdict()    
                controlled_counters_dict['if_out_errors'] = int(groups['if_out_errors'])
                continue

            #Transmit SC Counters (SCI: 44881699B510001C)
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                sci = groups['sci']
                transmit_sc_counters_dict = ret_dict.setdefault('transmit_sc_counters', {}).setdefault(sci, {})
                continue

            #   Out Pkts Protected:       0
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                transmit_sc_counters_dict['out_pkts_protected'] = int(groups['out_pkts_protected'])
                continue

            #   out_pkts_encrypted:       8630
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                transmit_sc_counters_dict['out_pkts_encrypted'] = int(groups['out_pkts_encrypted'])
                continue

            # Receive SA Counters (SCI: A44C119DF89C001E  AN 0)
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                sci_dict = ret_dict.setdefault('receive_sa_counters', {}).setdefault(groups['sci'], {})
                sci_dict['sci'] = groups['sci']
                sci_dict['an'] = groups['an']


            #   In Pkts Unchecked:        0
            m = p24.match(line)
            if m:
                groups = m.groupdict()    
                sci_dict['in_pkts_unchecked'] = int(groups['in_pkts_unchecked'])
                continue

            #   In Pkts Delayed:          0
            m = p25.match(line)
            if m:
                groups = m.groupdict()
                sci_dict['in_pkts_delayed'] = int(groups['in_pkts_delayed'])
                continue

            #   In Pkts OK:               103416932
            m = p26.match(line)
            if m:
                groups = m.groupdict()
                sci_dict['in_pkts_ok'] = int(groups['in_pkts_ok'])
                continue

            #   In Pkts Invalid:          0
            m = p27.match(line)
            if m:
                groups = m.groupdict()
                sci_dict['in_pkts_invalid'] = int(groups['in_pkts_invalid'])
                continue

            #   In Pkts Not Valid:        0
            m = p28.match(line)
            if m:
                groups = m.groupdict()
                sci_dict['in_pkts_not_valid'] = int(groups['in_pkts_not_valid'])
                continue

            #   In Pkts Not using SA:     0
            m = p29.match(line)
            if m:
                groups = m.groupdict()
                sci_dict['in_pkts_not_using_sa'] = int(groups['in_pkts_not_using_sa'])
                continue
            
            #   In Pkts Unused SA:        0
            m = p30.match(line)
            if m:
                groups = m.groupdict()
                sci_dict['in_pkts_unused_sa'] = int(groups['in_pkts_unused_sa'])
                continue

            #   In Pkts Late:             0
            m = p31.match(line)
            if m:
                groups = m.groupdict()
                sci_dict['in_pkts_late'] = int(groups['in_pkts_late'])
                continue

        return ret_dict