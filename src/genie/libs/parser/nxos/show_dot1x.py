# -*- coding: utf-8 -*-
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


#Output given from sample output
output = '''

    Dot1x Authenticator Port Statistics for Ethernet1/1
    --------------------------------------------
    RxStart = 0     RxLogoff = 0    RxResp = 0      RxRespID = 0
    RxInvalid = 0   RxLenErr = 0    RxTotal = 0

    TxReq = 0       TxReqID = 0     TxTotal = 3

    RxVersion = 0   LastRxSrcMAC = 00:00:00:00:00:00
'''

# Function: Display all statistics on this interface.

#schema class


class ShowDot1xAllStatisticsSchema(MetaParser):
    # string here not needed
    ''' Schema for: 
            Show dot1x all statistics
    '''
# Got schema list from Genie (Dont need all the wrappers<>)
    schema = {
        'Interfaces': {
            Any(): {
                'Interface': str,
                'Statistics': {
                    'txreq': int,
                    'rxlogoff': int,
                    'rxtotal': int,
                    'txtotal': int,
                    'rxversion': int,
                    'lastrxsrcmac': str,
                    Optional('rxlenerr'): int,
                    Optional('txreq'): int,
                    Optional('txreqid'): int,
                    Optional('rxstart'): int,
                    Optional('rxlogoff'): int,
                    Optional('rxresp'): int,
                    Optional('rxrespid'): int,
                    Optional('txreqid'): int,
                    Optional('rxinvalid'): int,
                },
            }
        }
    }

#parser class
class ShowDot1xAllStatistics(ShowDot1xAllStatisticsSchema):
    "Parser for show dot1x all statistics"

    cli_command = 'show dot1x all statistics'

    def cli(self, output=None):  # CLI => command line interface
        if output is None:  # if no input as second arg
            out = self.device.execute(self.cli_command)
        else:
            out = output

        dict = {}  # initialize empty dictionary

        p1 = re.compile(r'((^[Dd]ot1x)\s+)?' +
                        '(([Aa]uthenticator)\s+)?' +
                        '(([Pp])ort\s+)?(([Ss]tatistics)\s+)?' +
                        '((for)\s+)?(?P<interface>(\w*)\d+(\/)(\d+))$\s*')



        p2 = re.compile(r'(\w+) *\= *(\d+)+ *')

        p3 = re.compile(r'^([Rr]x[Vv]ersion) \= *(?P<rxversion>\d+)' +
                        '   ([Ll]ast[Rr]x[Ss]rc[Mm][Aa][Cc]) = (?P<lastrxsrcmac>\w+:\w+:\w+:\w+:\w+:\w+)$')



        for line in out.splitlines():
            line = line.strip()

            #Dot1x Authenticator Port Statistics for Ethernet1/1
            m = p1.match(line)  # returns a match object
            if m:
                interface = m.groupdict()['interface']
                dict.setdefault("Interfaces", {}).setdefault(interface, {}).setdefault(
                    'Interface', interface)  # initialize dict
                dict.setdefault("Interfaces", {}).setdefault(interface, {}).setdefault(
                    'Statistics', {})  # add empty set for stats
                stats = dict.setdefault("Interfaces", {}).setdefault(interface, {}).setdefault(
                    'Statistics', {})  # assign a var to location of stats

            #RxStart = 0     RxLogoff = 0    RxResp = 0      RxRespID = 0
            #RxInvalid = 0   RxLenErr = 0    RxTotal = 0
            #TxReq = 0       TxReqID = 0     TxTotal = 3
            m = p2.findall(line)  # Returns a list of all matching elements
            if m:
                for i in m:
                    stats.update({i[0].lower(): int(i[1])})  # add elements to 'Stats' set

            #RxVersion = 0   LastRxSrcMAC = 00: 00: 00: 00: 00: 00
            m = p3.match(line)
            if m:
                stats.update({'rxversion': int(m.groupdict()['rxversion'])})
                stats.update({'lastrxsrcmac': m.groupdict()['lastrxsrcmac']})

        return dict
