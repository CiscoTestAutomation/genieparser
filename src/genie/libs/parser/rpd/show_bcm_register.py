'''show_bcm_register.py
RPD CLI parser for the following show command
    * show bcm-register wbfft config
'''

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional

import re


# ===========================================
# Schema for 'show bcm-register wbfft config'
# ===========================================


class ShowBcmRegisterWbfftConfigSchema(MetaParser):
    """ Schema for "show bcm-register wbfft config" """

    schema = {
        "wbfft_trigger_mode": str,
        "enable_utsc": bool,
        "samples_num": int,
        "low_bin_session_id": str,
        "pnm_dest_ip": str,
        "pnm_dest_mac": str,

    }


# ===========================================
# Parser for 'show bcm-register wbfft config'
# ===========================================


class ShowBcmRegisterWbfftConfig(ShowBcmRegisterWbfftConfigSchema):
    """ Parser for "show bcm-register wbfft config" """

    cli_command = "show bcm-register wbfft config"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Init vars
        parsed_dict = {}

        # WBFFT Trigger Mode  : N/A
        p1 = re.compile(r"^WBFFT Trigger Mode\s+:\s(?P<wbfft_trigger_mode>.*)$")

        # Enable UTSC         : False
        p2 = re.compile(r"^Enable UTSC\s+:\s(?P<enable_utsc>.*)$")

        # Samples Num         : 0
        p3 = re.compile(r"^Samples Num\s+:\s(?P<samples_num>.*)$")

        # Low Bin SesID       : 00001000
        p4 = re.compile(r"^Low Bin SesID\s+:\s(?P<low_bin_session_id>.*)$")

        # PNM Dest IP         : 0.0.0.0
        p5 = re.compile(r"^PNM Dest IP\s+:\s(?P<pnm_dest_ip>.*)$")

        # PNM Dest Mac        : 0000.0000.0000
        p6 = re.compile(r"^PNM Dest Mac\s+:\s(?P<pnm_dest_mac>.*)$")

        for line in output.splitlines():
            line = line.strip()

            # WBFFT Trigger Mode  : N/A
            m = p1.match(line)
            if m:
                parsed_dict['wbfft_trigger_mode'] = m.groupdict()['wbfft_trigger_mode']
                continue

            # Enable UTSC         : False
            m = p2.match(line)
            if m:
                if m.groupdict()['enable_utsc'] == 'True':
                    parsed_dict['enable_utsc'] = True
                else:
                    parsed_dict['enable_utsc'] = False
                continue

            # Samples Num         : 0
            m = p3.match(line)
            if m:
                parsed_dict['samples_num'] = int(m.groupdict()['samples_num'])
                continue

            # Low Bin SesID       : 00001000
            m = p4.match(line)
            if m:
                parsed_dict['low_bin_session_id'] = m.groupdict()['low_bin_session_id'].strip()
                continue

            # PNM Dest IP         : 0.0.0.0
            m = p5.match(line)
            if m:
                parsed_dict['pnm_dest_ip'] = m.groupdict()['pnm_dest_ip'].strip()
                continue

            # PNM Dest Mac        : 0000.0000.0000
            m = p6.match(line)
            if m:
                parsed_dict['pnm_dest_mac'] = m.groupdict()['pnm_dest_mac'].strip()
                continue

        return parsed_dict
