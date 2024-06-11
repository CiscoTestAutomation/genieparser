"""starOS implementation of show_subscribers_summary.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowSubscribersSchema(MetaParser):
    """Schema for show subscribers summary"""

    schema = {
        'subscribers_summary': {
            Any(): {
                'NUM': str
            },
        }    
    }


class ShowSubscribers(ShowSubscribersSchema):
    """Parser for show subscribers summary"""

    cli_command = 'show subscribers summary'

    """
Total Subscribers:             8         
Active:                        8             Dormant:                       0         
LAPI Devices:                  0         
DCNR Devices:                  0         
pdsn-simple-ipv4:              0             pdsn-simple-ipv6:              0         
pdsn-mobile-ip:                0             ha-mobile-ipv6:                0         
hsgw-ipv6:                     0             hsgw-ipv4:                     0         
hsgw-ipv4-ipv6:                0             pgw-pmip-ipv6:                 0         
pgw-pmip-ipv4:                 0             pgw-pmip-ipv4-ipv6:            0         
pgw-gtp-ipv6:                  1             pgw-gtp-ipv4:                  7         
pgw-gtp-ipv4-ipv6:             0             sgw-gtp-ipv6:                  0         
sgw-gtp-ipv4:                  0             sgw-gtp-ipv4-ipv6:             0         
sgw-pmip-ipv6:                 0             sgw-pmip-ipv4:                 0         
sgw-pmip-ipv4-ipv6:            0             pgw-gtps2b-ipv4:               0         
pgw-gtps2b-ipv6:               0             pgw-gtps2b-ipv4-ipv6:          0         
pgw-gtps2a-ipv4:               0             pgw-gtps2a-ipv6:               0         
pgw-gtps2a-ipv4-ipv6:          0         
pgw-gtp-non-ip:                0             sgw-gtp-non-ip:                0         
mme:                           0             mme-embms:                     0         
henbgw-ue:                     0             henbgw-henb:                 0         
x2gw-enb:                      0         
ipsg-rad-snoop:                0             ipsg-rad-server:               0         
ha-mobile-ip:                  0             ggsn-pdp-type-ppp:             0         
ggsn-pdp-type-ipv4:            0             lns-l2tp:                      0         
ggsn-pdp-type-ipv6:            0             ggsn-pdp-type-ipv4v6:          0         
ggsn-mbms-ue-type-ipv4:        0         
pdif-simple-ipv4:              0         
pdif-simple-ipv6:              0             pdif-mobile-ip:                0         
wsg-simple-ipv4:               0             wsg-simple-ipv6:               0         
pdg-simple-ipv4:               0             ttg-ipv4:                      0         
pdg-simple-ipv6:               0             ttg-ipv6:                      0         
femto-ip:                      0             
epdg-pmip-ipv6:                0             epdg-pmip-ipv4:                0         
epdg-pmip-ipv4-ipv6:           0         
epdg-gtp-ipv6:                 0             epdg-gtp-ipv4:                 0         
epdg-gtp-ipv4-ipv6:            0         
sgsn:                          0             sgsn-pdp-type-ppp:             0         
sgsn-pdp-type-ipv4:            0             sgsn-pdp-type-ipv6:            0         
sgsn-pdp-type-ipv4-ipv6:       0             type not determined:           0         
sgsn-subs-type-gn:             0             sgsn-subs-type-s4:             0         
sgsn-pdp-type-gn:              0             sgsn-pdp-type-s4:              0         
cdma 1x rtt sessions:          0             cdma evdo sessions:            0         
cdma evdo rev-a sessions:      0             cdma 1x rtt active:            0         
cdma evdo active:              0             cdma evdo rev-a active:        0         
hnbgw:                         0             hnbgw-iu:                      0         
bng-simple-ipv4:               0         
pcc:                           0         
in bytes dropped:              999117        out bytes dropped:             10468     
in packet dropped:             11671         out packet dropped:            201       
in packet dropped zero mbr:    0             out packet dropped zero mbr:   0         
in bytes dropped ovrchrgPtn:   0             out bytes dropped ovrchrgPtn:  0         
in packet dropped ovrchrgPtn:  0             out packet dropped ovrchrgPtn: 0         
ipv4 ttl exceeded:             4             ipv4 bad hdr:                  0         
ipv4 bad length trim:          0         
ipv4 frag failure:             0             ipv4 frag sent:                0         
ipv4 in-acl dropped:           0             ipv4 out-acl dropped:          0         
ipv6 bad hdr:                  0             ipv6 bad length trim:          0         
ipv6 in-acl dropped:           0             ipv6 out-acl dropped:          0         
ipv4 in-css-down dropped:      0             ipv4 out-css-down dropped:     0         
ipv4 out xoff pkt dropped:     0             ipv6 out xoff pkt dropped:     0         
ipv4 xoff bytes dropped:       0             ipv6 xoff bytes dropped:       0         
ipv4 out no-flow dropped:      0         
ipv4 early pdu rcvd:           0             ipv4 icmp packets dropped:     0         
ipv6 iSubscriberst ehrpd-access drop:  0             ipv6 output ehrpd-access drop: 0         
dormancy count:                0             handoff count:                 16        
pdsn fwd dynamic flows:        0             pdsn rev dynamic flows:        0         
fwd static access-flows:       0             rev static access-flows:       0         
pdsn fwd packet filters:       0             pdsn rev packet filters:       0         
traffic flow templates:        0            
    
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        recovery_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        p0 = re.compile(r'(?P<total_subscribers>\bTotal\b.\bSubscribers\b.)\s+(?P<num>\d+)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'subscribers_summary' not in recovery_dict:
                    result_dict = recovery_dict.setdefault('subscribers_summary',{})
                total_subscribers = m.groupdict()['total_subscribers']
                num = m.groupdict()['num']
                result_dict[total_subscribers] = {}   
                result_dict[total_subscribers]['NUM'] = num 
                continue
        return recovery_dict