import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any

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
