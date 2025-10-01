import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Optional
from genie.metaparser.util.schemaengine import Schema, ListOf, Any

class ShowVoiceCallSummarySchema(MetaParser):
    '''Schema for show voice call summary'''
    schema = {
        'ports': {
            Any(): {
                'codec': str,
                'vad': str,
                'vtsp_state': str,
                'vpm_state': str,
            }
        }
    
    }

class ShowVoiceCallSummary(ShowVoiceCallSummarySchema):
    '''Parser for show voice call summary'''
    cli_command = 'show voice call summary'

    def cli(self, output=None, **kwargs):
        if output is None:
            out = self.device.execute(self.cli_command.format(**kwargs))

        if output is not None:

            out = output
        
        # Init return dictionary

        parsed = {}

        # port: 1/0/0:23.1, codec: "G729", vad: "OFF", vtsp_state: "DOWN", vpm_state: "UP"
        p0 = re.compile(r'^(?P<port>[\d/]+(?::\d+\.\d+|(?:\.\d+){0,2})?)\s+(?P<codec>\S+)\s+(?P<vad>\S+)\s+(?P<vtsp_state>\S+)(?:\s+(?P<vpm_state>\S+))?$')
        for line in out.splitlines():
            line = line.strip()
            # port: 1/0/0:23.1, codec: "G729", vad: "OFF", vtsp_state: "DOWN", vpm_state: "UP"
            m0 = p0.match(line)
            if m0:
                group = m0.groupdict()
                ports_dict = parsed.setdefault('ports', {})
                ports_dict[group['port']] = {
                    'codec': group['codec'].strip(),
                    'vad': group['vad'].strip(),
                    'vtsp_state': group['vtsp_state'].strip(),  
                    'vpm_state': group['vpm_state'].strip() if group['vpm_state'] else ' ',
                }
         

        return parsed

class ShowVoiceDspSchema(MetaParser):
    """Schema for show voice dsp"""
    schema = {
        'flex_voice_cards': {
            Any(): {
                # Changed to ListOf dictionaries to capture multiple DSP entries
                Optional('dsp_voice_channels'): ListOf(
                    {
                        'dsp_type': str,
                        'dsp_num': str,
                        'ch': str,
                        'codec': str,
                        'dspware_version': str,
                        'curr_state': str,
                        'boot_state': str,
                        'rst': str,
                        'ai': str,
                        'voiceport': str,
                        'ts': str,
                        'abort': str,
                        'pack_count': str,
                    }
                ),
                # Changed to ListOf dictionaries to capture multiple DSP entries
                Optional('dsp_signaling_channels'): ListOf(
                    {
                        'dsp_type': str,
                        'dsp_num': str,
                        'ch': str,
                        'codec': str,
                        'dspware_version': str,
                        'curr_state': str,
                        'boot_state': str,
                        'rst': str,
                        'ai': str,
                        'voiceport': str,
                        'ts': str,
                        'abort': str,
                        'pack_count': str,
                    }
                )
            }
        }
    }


class ShowVoiceDsp(ShowVoiceDspSchema):
    """Parser for show voice dsp"""

    cli_command = 'show voice dsp'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing
        # ------------------------------- FLEX VOICE CARD 1/0 -------------------------------------
        p0 = re.compile(r'^-+\s+FLEX VOICE CARD\s+(?P<card_id>\d+/\d+)\s+-+$')
        # *DSP VOICE CHANNELS*
        p1 = re.compile(r'^\*DSP VOICE CHANNELS\*')
        # *DSP SIGNALING CHANNELS*
        p2 = re.compile(r'^\*DSP SIGNALING CHANNELS\*')
        # DM8147 001 01 {flex}        64.3.1 alloc idle      0  0 1/0/0     00    0          5/0
        p3 = re.compile(
            r'^(?P<dsp_type>\S+)\s+(?P<dsp_num>\d+)\s+(?P<ch>\d+)\s+(?P<codec>\S+)\s+'
            r'(?P<dspware_version>\S+)\s+(?P<curr_state>\S+)\s+(?P<boot_state>\S+)\s+'
            r'(?P<rst>\d+)\s+(?P<ai>\d+)\s+(?P<voiceport>\S+)\s+(?P<ts>\d+)\s+'
            r'(?P<abort>\d+)\s+(?P<pack_count>\S+)'
        )

        current_card = None
        current_section = None

        for line in output.splitlines():
            line = line.strip()

            # ------------------------------- FLEX VOICE CARD 1/0 -------------------------------------
            match = p0.match(line)
            if match:
                current_card = match.group('card_id')
                # Initialize the card entry, but do not pre-initialize dsp_voice_channels/dsp_signaling_channels
                parsed_dict.setdefault('flex_voice_cards', {}).setdefault(current_card, {})
                current_section = None # Reset section when a new card is found
                continue

            # *DSP VOICE CHANNELS*
            if p1.match(line):
                current_section = 'dsp_voice_channels'
                continue

            # *DSP SIGNALING CHANNELS*
            if p2.match(line):
                current_section = 'dsp_signaling_channels'
                continue

            # DM8147 001 01 {flex}        64.3.1 alloc idle      0  0 1/0/0     00    0          5/0
            match = p3.match(line)
            # Populate the appropriate section with DSP entry data
            if match and current_card and current_section:
                card_data = parsed_dict['flex_voice_cards'][current_card]
                # Use setdefault to ensure the list for the current_section exists
                section_list = card_data.setdefault(current_section, [])
                # Append the matched data as a new dictionary to the list
                section_list.append(match.groupdict())
        return parsed_dict
