"""starOS implementation of show_ims-auth_sessions_summary.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowImsSchema(MetaParser):
    """Schema for show ims-auth sessions summary"""

    schema = {
        'ims': {
            'total': str,
            'authorizing': str,
            'pending': str,
            'issued': str,
            'done': str,
            'reauthorizing': str,
            'abort': str,
            'release': str,
            'state': str,
            'reconnecting': str,
            'reconnect': str,
            'update': str,
            'revoke': str,
            'preservation': str,
            'preservation_done': str,
            'reactivation': str,
            'fallback': str
        }     
    }


class ShowIms(ShowImsSchema):
    """Parser for show ims-auth sessions summary"""

    cli_command = 'show ims-auth sessions summary'

    """
   Total IMS Auth sessions: 3

Session State:
Authorizing:                   0             Auth Pending:                  0

Auth Issued:                   0             Auth Done:                     3

Reauthorizing:                 0             Abort Issued:                  0

Pending Release:               0             Last State:                    0

Reconnecting:                  0             Reconnect Pending:             0

Pending Update:                0             Revoke Issued:                 0

Preservation Issued:           0             Preservation Done:             0

Reactivation Issued:           0             Local Fallback:                0

    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ims_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'Total\sIMS\sAuth\ssessions:\s(?P<total_IMS>\d+)')
        p1 = re.compile(r'Authorizing:\s+(?P<auth>\d+)\s+Auth\sPending:\s+(?P<auth_pending>\d+)')
        p2 = re.compile(r'Auth\sIssued:\s+(?P<auth_issued>\d+)\s+Auth\sDone:\s+(?P<auth_done>\d+)')
        p3 = re.compile(r'Reauthorizing:\s+(?P<reauth>\d+)\s+Abort\sIssued:\s+(?P<abort_issued>\d+)')
        p4 = re.compile(r'Pending\sRelease:\s+(?P<pending_release>\d+)\s+Last\sState:\s+(?P<last_state>\d+)')
        p5 = re.compile(r'Reconnecting:\s+(?P<reconnecting>\d+)\s+Reconnect\sPending:\s+(?P<reconnect_pending>\d+)')
        p6 = re.compile(r'Pending\sUpdate:\s+(?P<pending_update>\d+)\s+Revoke\sIssued:\s+(?P<revoke_issued>\d+)')
        p7 = re.compile(r'Preservation\sIssued:\s+(?P<preserv_issued>\d+)\s+Preservation\sDone:\s+(?P<preserv_done>\d+)')
        p8 = re.compile(r'Reactivation\sIssued:\s+(?P<react_issued>\d+)\s+Local\sFallback:\s+(?P<local_fallback>\d+)')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                total = m.groupdict()['total_IMS']
                result_dict['total'] = total
                
            m = p1.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                authorizing = m.groupdict()['auth']
                result_dict['authorizing'] = authorizing
                pending = m.groupdict()['auth_pending']
                result_dict['pending'] = pending

            m = p2.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                issued = m.groupdict()['auth_issued']
                result_dict['issued'] = issued
                done = m.groupdict()['auth_done']
                result_dict['done'] = done
            
            m = p3.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                reauthorizing = m.groupdict()['reauth']
                result_dict['reauthorizing'] = reauthorizing
                abort = m.groupdict()['abort_issued']
                result_dict['abort'] = abort
            
            m = p4.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                release = m.groupdict()['pending_release']
                result_dict['release'] = release
                state = m.groupdict()['last_state']
                result_dict['state'] = state
            
            m = p5.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                reconnecting = m.groupdict()['reconnecting']
                result_dict['reconnecting'] = reconnecting
                reconnect = m.groupdict()['reconnect_pending']
                result_dict['reconnect'] = reconnect
            
            m = p6.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                update = m.groupdict()['pending_update']
                result_dict['update'] = update
                revoke = m.groupdict()['revoke_issued']
                result_dict['revoke'] = revoke
            
            m = p7.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                preservation = m.groupdict()['preserv_issued']
                result_dict['preservation'] = preservation
                preservation_done = m.groupdict()['preserv_done']
                result_dict['preservation_done'] = preservation_done

            m = p8.match(line)
            if m:
                if 'ims' not in ims_dict:
                    result_dict = ims_dict.setdefault('ims',{})
                reactivation = m.groupdict()['react_issued']
                result_dict['reactivation'] = reactivation
                fallback = m.groupdict()['local_fallback']
                result_dict['fallback'] = fallback
                continue

        return ims_dict