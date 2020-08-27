import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================================
# Schema for:
#  * 'show ap dot11 dual-band summary'
# ====================================
class ShowApDot11DualBandSummarySchema(MetaParser):
    """Schema for show ap dot11 dual-band summary."""

    schema = {
        "ap_dot11_dual-band_summary": {
            int: {
                "ap_name": str,
                "ap_mac_address": str,
                "slot_id": int,
                "admin_state": str,
                "oper_state": str,
                "width": int,
                "tx_pwr": str,
                "mode": str,
                "subband": str,
                "channel": str
            }
        }
    }


# ====================================
# Parser for:
#  * 'show ap dot11 dual-band summary'
# ====================================
class ShowApDot11DualBandSummary(ShowApDot11DualBandSummarySchema):
    """Parser for show ap dot11 dual-band summary"""

    cli_command = 'show ap dot11 dual-band summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        show_ap_dot11_dual_band_summary_dict = {}

        # AP Name                           Mac Address     Slot  Admin State   Oper State     Width  Txpwr           Mode    Subband    channel
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
        # aa-test-4800                 64d8.14ec.1120  0     Enabled       Down           20     *1/8 (23 dBm)   Local   All        (6)*
        # aa-test-4800                 64d8.14ec.1120  2     Enabled       Down           20     N/A             Monitor All        N/A

        remove_lines = ()

        # Remove unwanted lines from raw text
        def filter_lines(raw_output, remove_lines):
            # Remove empty lines
            clean_lines = list(filter(None, raw_output.splitlines()))
            rendered_lines = []
            for clean_line in clean_lines:
                clean_line_strip = clean_line.strip()
                # Remove lines unwanted lines from list of "remove_lines"
                if not clean_line_strip.startswith(remove_lines):
                    rendered_lines.append(clean_line_strip)
            return rendered_lines

        out = filter_lines(raw_output=out, remove_lines=remove_lines)

        # AP Name                           Mac Address     Slot  Admin State   Oper State     Width  Txpwr           Mode    Subband    channel
        ap_info_headers_capture = re.compile(
            r"^AP\s+Name\s+Mac\s+Address\s+Slot\s+Admin\s+State\s+Oper\s+State\s+Width\s+Txpwr\s+Mode\s+Subband\s+channel$")
        # ---------------------------------------------------------------------------------------------------------------------------------------------------------
        delimiter_capture = re.compile(
            r"^---------------------------------------------------------------------------------------------------------------------------------------------------------$")
        # aa-test-4800                 64d8.14ec.1120  0     Enabled       Down           20     *1/8 (23 dBm)   Local   All        (6)*
        ap_info_capture = re.compile(
            r"^(?P<ap_name>\S+)\s+(?P<ap_mac_address>\S+)\s+(?P<slot_id>\d+)\s+(?P<admin_state>(Enabled|Disabled))\s+(?P<oper_state>\S+)\s+(?P<width>\d+)\s+(?P<tx_pwr>(N\/A|\*.*m\)))\s+(?P<mode>\S+)\s+(?P<subband>\S+)\s+(?P<channel>\S+)$")

        ap_index = 0

        for line in out:
            # AP Name                           Mac Address     Slot  Admin State   Oper State     Width  Txpwr           Mode    Subband    channel
            if ap_info_headers_capture.match(line):
                ap_info_headers_capture_match = ap_info_headers_capture.match(line)
                groups = ap_info_headers_capture_match.groupdict()
                if not show_ap_dot11_dual_band_summary_dict.get('ap_dot11_dual-band_summary', {}):
                    show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'] = {}
                continue
            # ---------------------------------------------------------------------------------------------------------------------------------------------------------
            elif delimiter_capture.match(line):
                delimiter_capture_match = delimiter_capture.match(line)
                groups = delimiter_capture_match.groupdict()
                continue
            # aa-test-4800                 64d8.14ec.1120  0     Enabled       Down           20     *1/8 (23 dBm)   Local   All        (6)*
            elif ap_info_capture.match(line):
                ap_index = ap_index + 1
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index] = {}
                ap_info_capture_match = ap_info_capture.match(line)
                groups = ap_info_capture_match.groupdict()
                ap_name = groups['ap_name']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update(
                    {'ap_name': ap_name})
                ap_mac_address = groups['ap_mac_address']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update(
                    {'ap_mac_address': ap_mac_address})
                slot_id = int(groups['slot_id'])
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update(
                    {'slot_id': slot_id})
                admin_state = groups['admin_state']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update(
                    {'admin_state': admin_state})
                oper_state = groups['oper_state']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update(
                    {'oper_state': oper_state})
                width = int(groups['width'])
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update({'width': width})
                tx_pwr = groups['tx_pwr']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update({'tx_pwr': tx_pwr})
                mode = groups['mode']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update({'mode': mode})
                subband = groups['subband']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update(
                    {'subband': subband})
                channel = groups['channel']
                show_ap_dot11_dual_band_summary_dict['ap_dot11_dual-band_summary'][ap_index].update(
                    {'channel': channel})
                continue

        return show_ap_dot11_dual_band_summary_dict
