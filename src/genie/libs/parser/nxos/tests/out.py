# -*- coding: utf-8 -*-
import re
out = '''

    Dot1x Authenticator Port Statistics for Ethernet1/1
    --------------------------------------------
    RxStart = 0     RxLogoff = 0    RxResp = 0      RxRespID = 0
    RxInvalid = 0   RxLenErr = 0    RxTotal = 0

    TxReq = 0       TxReqID = 0     TxTotal = 3

    RxVersion = 0   LastRxSrcMAC = 00:00:00:ff:00:00
'''
dict = {}  # initialize empty dictionary

#re.compile => puts regex pattern as an Object to be used below
p1 = re.compile(r'((^[Dd]ot1x)\s+)?' +
                r'(([Aa]uthenticator)\s+)?' +
                r'(([Pp])ort\s+)?(([Ss]tatistics)\s+)?' +
                r'((for)\s+)?(?P<interface>(\w*)\d?(\/)(\d?))$\s*')

#
p2 = re.compile(r'(\w+) *\= *(\d)+ *')

p3 = re.compile(r'^([Rr]x[Vv]ersion) \= *(?P<rxversion>\d)' +
                r'   ([Ll]ast[Rr]x[Ss]rc[Mm][Aa][Cc]) \= (?P<lastrxsrcmac>\w+\:\w+\:\w+\:\w+\:\w+\:\w+)$')

# Add all lines into a list
for line in out.splitlines():
    line = line.strip()

    m = p1.match(line)  # returns a match object
    if m:
        # getting element at interface
        interface = m.groupdict()['interface']
        dict.setdefault("Interfaces", {}).setdefault(interface, {}).setdefault(
            'Interface', interface)  # initialize dict
        dict.setdefault("Interfaces", {}).setdefault(interface, {}).setdefault(
            'Statistics', {})  # add empty set for stats
        stats = dict.setdefault("Interfaces", {}).setdefault(interface, {}).setdefault(
            'Statistics', {})  # assign a var to location of stats

    m = p2.findall(line)  # Returns a list of all matching elements
    if m:
        for i in m:
            stats.update({i[0]: int(i[1])})  # add elements to 'Stats' set

    m = p3.match(line)  # last line
    if m:
        stats.update({'rxversion': int(m.groupdict()['rxversion'])})
        stats.update({'lastrxsrcmac': m.groupdict()['lastrxsrcmac']})
print(dict)
