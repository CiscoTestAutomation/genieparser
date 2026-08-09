"""starOS implementation of show_config_errors_verbose.py
Author: Luis Antonio Villalobos (luisvill)

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema, Optional


class ShowConfigErrors(MetaParser):
    schema = {
        'config_errors': {
            Any(): {
                'Errors': str,
                'Warnings': str
            }
        }
    }


class ShowErrorsVerbose(ShowConfigErrors):
    """Parser for show configuration errors verbose"""

    cli_command = 'show configuration errors verbose'

    """
    ######################################################################################
    #                   Displaying Diameter Configuration errors
    ######################################################################################
    Total 0 error(s) in this section !

    Info    : No routes configured under endpoint : GY_EMBLACOM

    Info    : No routes configured under endpoint : Gx

    Info    : No routes configured under endpoint : Gx_Labo

    Info    : No routes configured under endpoint : Gx_PrePro

    Info    : No routes configured under endpoint : Gy_Py

    Info    : No routes configured under endpoint : Gy_Py_labo

    Info    : No routes configured under endpoint : Gy_vPy

    Info    : No routes configured under endpoint : Gx-PY

    Info    : No Routes configured under any endpoint

    Total 9 warning(s) in this section!

    ######################################################################################
    #                   Displaying Active-charging system errors
    ######################################################################################
    Error   : Group of Ruledef  <PY-gor_block_tunnel_fraude_post> has application type as POST PROCESSING which is not allowed
    Error   : group-of-ruledefs <UY-SVA_HTTP_RG99_HE-1> is not used in any rulebase. It can be a dynamically enabled ADC group and could be ignored.
    Error   : Ruledef <AUP-GM-I-1> is not used in any rulebase or group-of-ruledefs. It can be a dynamically enabled ADC ruledef and could be ignored.
    Error   : Ruledef <AUP-GM-I-2> is not used in any rulebase or group-of-ruledefs. It can be a dynamically enabled ADC ruledef and could be ignored.
    Error   : Ruledef <AUP-GM-I-3> is not used in any rulebase or group-of-ruledefs. It can be a dynamically enabled ADC ruledef and could be ignored.
    Error   : Ruledef <AUP-GM-I-4> is not used in any rulebase or group-of-ruledefs. It can be a dynamically enabled ADC ruledef and could be ignored.
    Error   : Ruledef <AUP-GM-I-6> is not used in any rulebase or group-of-ruledefs. It can be a dynamically enabled ADC ruledef and could be ignored.
    Error   : Ruledef <AUP-GM-I-7> is not used in any rulebase or group-of-ruledefs. It can be a dynamically enabled ADC ruledef and could be ignored.
    Error   : Post-processing group-of-ruledefs <gor_block_tunnel_fraude_post> is used in the rulebase <RB_PY_NOMINATIVIDAD> but not defined in the active-charging service <CLARO>.
    Error   : Post-processing group-of-ruledefs <gor_block_tunnel_fraude_post_2> is used in the rulebase <RB_PY_NOMINATIVIDAD> but not defined in the active-charging service <CLARO>.
    Total 10 error(s) in this section !

    Warning : Charging Ruledef <AUP-YOUTUBE-2-TLS-SNI> uses multiple "sni" lines but does not have a "multi-line-or all-lines".
    Warning : Charging Ruledef <AUP-YOUTUBE-21> uses multiple "server-domain-name" lines but does not have a "multi-line-or all-lines".
    Warning : Charging Ruledef <AUP-YOUTUBE-22> uses multiple "server-domain-name" lines but does not have a "multi-line-or all-lines".
    Warning : Charging Ruledef <AUP-YOUTUBE-9> uses multiple "server-port" lines but does not have a "multi-line-or all-lines".
    Warning : Charging Ruledef <PY-block_tunnel_fraude-2> uses multiple "payload-length" lines but does not have a "multi-line-or all-lines".
    Warning : Charging Ruledef <PY-block_tunnel_fraude-5> uses multiple "payload-length" lines but does not have a "multi-line-or all-lines".
    Warning : Charging Ruledef <PY-block_tunnel_fraude-8> uses multiple "payload-length" lines but does not have a "multi-line-or all-lines".
    Warning : Post-Processing Ruledef <PY-block_tunnel_fraude_post-2> uses multiple "payload-length" lines but does not have a "multi-line-or all-lines".
    Warning : Post-Processing Ruledef <PY-block_tunnel_fraude_post-5> uses multiple "payload-length" lines but does not have a "multi-line-or all-lines".
    Warning : Post-Processing Ruledef <PY-block_tunnel_fraude_post-8> uses multiple "payload-length" lines but does not have a "multi-line-or all-lines".
    Warning : Default rule (i.e. a ruledef with just the "ip any-match = TRUE" expression) is specified in the rulebase <RB_PY_MMS>, but not at lowest priority action command.
    Warning : Default rule (i.e. a ruledef with just the "ip any-match = TRUE" expression) is specified in the rulebase <RB_PY_WAP>, but not at lowest priority action command.
    Total 12 warning(s) in this section!

    ######################################################################################
    #                   Displaying CSCF-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying PDSN-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying HA-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying FA-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying LNS-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying LAC-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Closed-rp-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying IPSG-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SAMOG-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Global AAA-configuration errors
    ######################################################################################
    Total 0 error(s) in this section !

    Warning %:  NAS-IP is not configured in Group <default> , Context <Ga>.

    Warning %:  NAS-IP is not configured in Group <default> , Context <Gi>.

    Warning %:  NAS-IP is not configured in Group <default> , Context <Gi-Internet>.

    Warning %:  NAS-IP is not configured in Group <default> , Context <Gi-VVM>.

    Warning %:  NAS-IP is not configured in Group <default> , Context <Gi-wap>.

    Warning %:  NAS-IP is not configured in Group <default> , Context <Pgw>.

    Warning %:  NAS-IP is not configured in Group <default> , Context <local>.

    Warning %:  NAS-IP is not configured in Group <default> , Context <radius-wap>.

    Warning %: Charging-agent IP <0.0.0.0> of default GTPP group is NOT ACTIVE, context <local>

    Warning %: Charging-agent IP <0.0.0.0> of default GTPP group is NOT ACTIVE, context <Pgw>

    Warning %: Charging-agent IP <0.0.0.0> of default GTPP group is NOT ACTIVE, context <Gi>

    Warning %: Charging-agent IP <0.0.0.0> of default GTPP group is NOT ACTIVE, context <Gi-VVM>

    Warning %: Charging-agent IP <0.0.0.0> of default GTPP group is NOT ACTIVE, context <radius-wap>

    Warning %: Charging-agent IP <0.0.0.0> of default GTPP group is NOT ACTIVE, context <Gi-wap>

    Warning %: Charging-agent IP <0.0.0.0> of default GTPP group is NOT ACTIVE, context <Gi-Internet>

    Total 15 warning(s) in this section!

    ######################################################################################
    #                   Displaying IMSA-configuration errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Local Subscriber-configuration errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Policy Group system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying GGSN-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying APN-configuration errors
    ######################################################################################
    Error   : Rulebase <Internet-py> configured for APN <igprs.asr5k.com.py.emblacom> dictates generation of eGCDRs/PGWCDR's but associated GTPP group <default> does not have a valid GTPP dictionary configuration. 

    Total 1 error(s) in this section !

    Warning   : Mediation context <radius-wap> different than context <Gi-wap> for APN <mmsasu.claro.com.py>

    Warning   : Mediation context <radius-wap> different than context <Gi-wap> for APN <wapasu.claro.com.py>

    Total 2 warning(s) in this section!

    ######################################################################################
    #                   Displaying PDIF-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying PDG-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying FNG-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying IMSSH-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Credit Control-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SGSN-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SGTP-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying IUPS-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying MAP-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying CAMEL-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Sccp-Network system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SGSN-Mode system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Operator-Policy system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Call-Control-Profile system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying APN-Profile system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying IMEI-Profile system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying APN-Remap-Table system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Gs-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying IPMS errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying MME HSS service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying GPRS-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying CS-Network system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying PS-Network system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying HNBGW-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying cbs-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying MME Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying HSGW-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying IMSUE-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Accounting policy system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying QCI mapping system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying PGW-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SGW-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying EGTP-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying User-Plane-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Subscriber-map system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying PCC-Policy Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying PCC-Quota Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying PCC Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Event Notification Interface errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying DNS Client system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Warning   : DNS client is not configured for context <local>
    Warning   : DNS client is not configured for context <Pgw>
    Warning   : DNS client is not configured for context <Gi>
    Warning   : DNS client is not configured for context <Ga>
    Warning   : DNS client is not configured for context <Gi-VVM>
    Warning   : DNS client is not configured for context <radius-wap>
    Warning   : DNS client is not configured for context <Gi-wap>
    Warning   : DNS client is not configured for context <Gi-Internet>
    Total 8 warning(s) in this section!

    ######################################################################################
    #                   Displaying Local policy Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying IPNE Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SGS Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying HENBGW Access Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying HENBGW Network Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying ALCAP-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SAEGW-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SS7RD system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying EPDG-service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying CGW-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Peer Map Rules system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying WSG system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Qos Marking
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SLS Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying SBc Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying EMBMS-Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Throttling Override Policy errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying S102 Service system errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying BFD Linkagg Peer errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying Linkagg errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying FE (Forwarding Element) errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying UE Overload Control Profile config errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!

    ######################################################################################
    #                   Displaying UE Overload Action Profile config errors
    ######################################################################################
    Total 0 error(s) in this section !

    Total 0 warning(s) in this section!
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output       
        # initial return dictionary
        config_errors_dict = {}
        result_dict = {}

        # Define the regex pattern for matching the rows with values
        errors_regex = re.compile(
            r'^Total\s+(?P<errors>\d+)\s+error\S+\s+in this section',
            re.MULTILINE)
        warnings_regex = re.compile(
            r'^Total\s+(?P<warnings>\d+)\s+warning\S+\s+in this section',
            re.MULTILINE)
        displaying_regex = re.compile(
            r'^.\s+Displaying\s+(?P<name>(.*))',
            re.MULTILINE)   
        # For Loop to get all the values from output
        # Split a string into a list where each line is a list item
        for match in out.splitlines():
            # Matching values in first_regex
            first = displaying_regex.match(match)
            if first:
                if 'config_errors' not in config_errors_dict:
                    result_dict = config_errors_dict.setdefault(
                        'config_errors', {}
                    )
                # Asigning matchings to variables
                displaying = first.groupdict()['name'].strip()

                # Adding values as keys to dictionary
                result_dict[displaying] = {}
            second = errors_regex.match(match)
            if second:
                if 'config_errors' not in config_errors_dict:
                    result_dict = config_errors_dict.setdefault(
                        'config_errors', {}
                    )
                # Asigning matchings to variables
                errors = second.groupdict()['errors'].strip()
                # Adding values to dictionary
                result_dict[displaying]['Errors'] = errors
            third = warnings_regex.match(match)
            if third:
                if 'config_errors' not in config_errors_dict:
                    result_dict = config_errors_dict.setdefault(
                        'config_errors', {}
                    )
                # Asigning matchings to variables
                warnings = third.groupdict()['warnings'].strip()
                # Adding values to dictionary
                result_dict[displaying]['Warnings'] = warnings
        return (config_errors_dict)
