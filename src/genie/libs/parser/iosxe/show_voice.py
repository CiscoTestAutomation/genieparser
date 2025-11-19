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



class ShowVoiceDspASchema(MetaParser):
    """Schema for show voice dsp a"""
    schema = {
        'flex_voice_cards': {
            Any(): {  # Card identifier, e.g., '0/1', '0/2', etc.
                'dsp_active_voice_channels': {
                    Any(): {  # DSP identifier (voiceport)
                        'dspware_version': str,
                        'codec': str,
                        'dsp_type': str,
                        'vox_dsp_num': int,
                        'vox_ch': int,
                        'vox_ts': int,
                        'voiceport': str,
                        'slot': str,
                        'sig_dsp_num': int,
                        'sig_ch': int,
                        'sig_ts': int,
                        'rst': int,
                        'ai': int,
                        'abrt': int,
                        'tx_pack_count': int,
                        'rx_pack_count': int,
                    }
                }
            }
        }
    }

class ShowVoiceDspA(ShowVoiceDspASchema):
    """Parser for show voice dsp a"""

    cli_command = 'show voice dsp a'
    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)


        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing
        # ------------------------------- FLEX VOICE CARD 0/1 -------------------------------------
        p0 = re.compile(r'--+\s*FLEX VOICE CARD\s+(?P<card_id>\d+/\d+)\s*--+')

        # SP2700 62.3.4     g729r8    001 01 000 1/0/2     1/0   001 03 002   0  0    0       738/845
        p1 = re.compile(
            r'^(?P<dsp_type>\S+)\s+'
            r'(?P<dspware_version>\S+)\s+'
            r'(?P<codec>\S+)\s+'
            r'(?P<vox_dsp_num>\d+)\s+'
            r'(?P<vox_ch>\d+)\s+'
            r'(?P<vox_ts>\d+)\s+'
            r'(?P<voiceport>\S+)\s+'
            r'(?P<slot>\S+)\s+'
            r'(?P<sig_dsp_num>\d+)\s+'
            r'(?P<sig_ch>\d+)\s+'
            r'(?P<sig_ts>\d+)\s+'
            r'(?P<rst>\d+)\s+'
            r'(?P<ai>\d+)\s+'
            r'(?P<abrt>\d+)\s+'
            r'(?P<tx_pack_count>\d+)/(?P<rx_pack_count>\d+)$'
        )

        current_card = None
        for line in output.splitlines(): # This loop was missing or mis-indented in your snippet
            line = line.strip()
            if not line:
                continue


            # ------------------------------- FLEX VOICE CARD 0/1 -------------------------------------
            match = p0.match(line)
            if match :
                current_card = match.group('card_id')
                card_dict = parsed_dict.setdefault('flex_voice_cards', {}).setdefault(current_card, {})
                channel_dict = card_dict.setdefault('dsp_active_voice_channels', {})
                continue

            # SP2700 62.3.4     g729r8    001 01 000 1/0/2     1/0   001 03 002   0  0    0       738/845
            match = p1.match(line)
            if match :
                data = match.groupdict()
                identifier_dict = channel_dict.setdefault(data['voiceport'], {})
                
                for key, value in data.items():
                    identifier_dict[key] = int(value) if value.isnumeric() else value

        return parsed_dict

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

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue



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


class ShowVoiceDspGroupAllSchema(MetaParser):
    """Schema for show voice dsp group all"""
    schema = {
        'dsp_groups': {
            Any(): {  # slot e.g., '0/1', '0/2', etc.
                'slot_id': int,
                'dsps': {
                    Any(): {  # dsp number e.g., '1', '2'
                        'state': str,
                        'firmware': str,
                        'max_signal_voice_channel': str,
                        'max_credits': int,
                        'voice_credits': int,
                        'video_credits': int,
                        'num_of_sig_chnls_allocated': int,
                        'transcoding_channels_allocated': int,
                        'group': str,
                        'complexity': str,
                        'shared_credits': int,
                        'reserved_credits': int,
                        'signaling_channels_allocated': int,
                        'voice_channels_allocated': int,
                        'credits_used_rounded_up': int,
                        'slot': str,
                        'device_idx': int,
                        'dsp_type': str,
                    }
                }
            }
        }
    }


class ShowVoiceDspGroupAll(ShowVoiceDspGroupAllSchema):
    """Parser for show voice dsp group all"""

    cli_command = 'show voice dsp group all'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # Initialize the parsed dictionary
        parsed_dict = {}

        # Regular expressions for parsing
        # DSP groups on slot 0/1 slot id 1
        p1 = re.compile(r'^DSP\s+groups\s+on\s+slot\s+(?P<slot>\S+)\s+slot\s+id\s+(?P<slot_id>\d+)$')
        
        # dsp 1:
        p2 = re.compile(r'^dsp\s+(?P<dsp_num>\d+):$')
        
        # State: UP, firmware: 60.1.4
        p3 = re.compile(r'^\s*State:\s+(?P<state>\S+),\s+firmware:\s+(?P<firmware>\S+)$')
        
        # Max signal/voice channel: 8/8
        p4 = re.compile(r'^\s*Max\s+signal/voice\s+channel:\s+(?P<max_signal_voice_channel>\S+)$')
        
        # Max credits: 120, Voice credits: 120, Video credits: 0
        p5 = re.compile(r'^\s*Max\s+credits:\s+(?P<max_credits>\d+),\s+Voice\s+credits:\s+(?P<voice_credits>\d+),\s+Video\s+credits:\s+(?P<video_credits>\d+)$')
        
        # num_of_sig_chnls_allocated: 8
        p6 = re.compile(r'^\s*num_of_sig_chnls_allocated:\s+(?P<num_of_sig_chnls_allocated>\d+)$')
        
        # Transcoding channels allocated: 0
        p7 = re.compile(r'^\s*Transcoding\s+channels\s+allocated:\s+(?P<transcoding_channels_allocated>\d+)$')
        
        # Group: FLEX_GROUP_VOICE, complexity: FLEX
        p8 = re.compile(r'^\s*Group:\s+(?P<group>\S+),\s+complexity:\s+(?P<complexity>\S+)$')
        
        # Shared credits: 120, reserved credits: 0
        p9 = re.compile(r'^\s*Shared\s+credits:\s+(?P<shared_credits>\d+),\s+reserved\s+credits:\s+(?P<reserved_credits>\d+)$')
        
        # Signaling channels allocated: 8
        p10 = re.compile(r'^\s*Signaling\s+channels\s+allocated:\s+(?P<signaling_channels_allocated>\d+)$')
        
        # Voice channels allocated: 0
        p11 = re.compile(r'^\s*Voice\s+channels\s+allocated:\s+(?P<voice_channels_allocated>\d+)$')
        
        # Credits used (rounded-up): 0
        p12 = re.compile(r'^\s*Credits\s+used\s+\(rounded-up\):\s+(?P<credits_used_rounded_up>\d+)$')
        
        # Slot: 0/1
        p13 = re.compile(r'^\s*Slot:\s+(?P<slot>\S+)$')
        
        # Device idx: 0
        p14 = re.compile(r'^\s*Device\s+idx:\s+(?P<device_idx>\d+)$')
        
        # Dsp Type: DM8147
        p15 = re.compile(r'^\s*Dsp\s+Type:\s+(?P<dsp_type>\S+)$')

        current_slot = None
        current_dsp = None

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # DSP groups on slot 0/1 slot id 1
            m = p1.match(line)
            if m:
                current_slot = m.group('slot')
                slot_id = int(m.group('slot_id'))
                
                dsp_groups_dict = parsed_dict.setdefault('dsp_groups', {})
                slot_dict = dsp_groups_dict.setdefault(current_slot, {})
                slot_dict['slot_id'] = slot_id
                slot_dict.setdefault('dsps', {})
                continue

            # dsp 1:
            m = p2.match(line)
            if m and current_slot:
                current_dsp = m.group('dsp_num')
                parsed_dict['dsp_groups'][current_slot]['dsps'].setdefault(current_dsp, {})
                continue

            # State: UP, firmware: 60.1.4
            m = p3.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['state'] = m.group('state')
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['firmware'] = m.group('firmware')
                continue

            # Max signal/voice channel: 8/8
            m = p4.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['max_signal_voice_channel'] = m.group('max_signal_voice_channel')
                continue

            # Max credits: 120, Voice credits: 120, Video credits: 0
            m = p5.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['max_credits'] = int(m.group('max_credits'))
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['voice_credits'] = int(m.group('voice_credits'))
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['video_credits'] = int(m.group('video_credits'))
                continue

            # num_of_sig_chnls_allocated: 8
            m = p6.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['num_of_sig_chnls_allocated'] = int(m.group('num_of_sig_chnls_allocated'))
                continue

            # Transcoding channels allocated: 0
            m = p7.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['transcoding_channels_allocated'] = int(m.group('transcoding_channels_allocated'))
                continue

            # Group: FLEX_GROUP_VOICE, complexity: FLEX
            m = p8.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['group'] = m.group('group')
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['complexity'] = m.group('complexity')
                continue

            # Shared credits: 120, reserved credits: 0
            m = p9.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['shared_credits'] = int(m.group('shared_credits'))
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['reserved_credits'] = int(m.group('reserved_credits'))
                continue

            # Signaling channels allocated: 8
            m = p10.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['signaling_channels_allocated'] = int(m.group('signaling_channels_allocated'))
                continue

            # Voice channels allocated: 0
            m = p11.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['voice_channels_allocated'] = int(m.group('voice_channels_allocated'))
                continue

            # Credits used (rounded-up): 0
            m = p12.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['credits_used_rounded_up'] = int(m.group('credits_used_rounded_up'))
                continue

            # Slot: 0/1
            m = p13.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['slot'] = m.group('slot')
                continue

            # Device idx: 0
            m = p14.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['device_idx'] = int(m.group('device_idx'))
                continue

            # Dsp Type: DM8147
            m = p15.match(line)
            if m and current_slot and current_dsp:
                parsed_dict['dsp_groups'][current_slot]['dsps'][current_dsp]['dsp_type'] = m.group('dsp_type')
                continue

        return parsed_dict
