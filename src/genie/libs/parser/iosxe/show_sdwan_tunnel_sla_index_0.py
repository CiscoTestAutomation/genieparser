"""
Author: Andrasi Gergo
Contact: gandrasi.work@gmail.com
"""
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

# ========================================================
# Schema for "show sdwan tunnel sla index 0"
# ========================================================

class ShowSdwanTunnelSlaIndex0Schema(MetaParser):
    schema = {
        "lines": {
            Any(): {
                "color": str,
                "loss": str,
                "latency": str,
                "jitter": str,
                "slaclass": str
            }            
        }
    }

class ShowSdwanTunnelSlaIndex0(ShowSdwanTunnelSlaIndex0Schema):
    """
    Parser for show sdwan tunnel sla index 0 on ios-xe sdwan devices.
    parser class - implements detail parsing mechanisms for cli output.
    """
    cli_command = "show sdwan tunnel sla index 0"
    """
    tunnel sla-class 0
     sla-name    __all_tunnels__
     sla-loss    0
     sla-latency 0
     sla-jitter  0
                                        SRC    DST    REMOTE       T LOCAL   T REMOTE  MEAN  MEAN     MEAN    SLA CLASS
    PROTO  SRC IP        DST IP          PORT   PORT   SYSTEM IP    COLOR     COLOR     LOSS  LATENCY  JITTER  INDEX      SLA CLASS NAME
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    ipsec  10.91.243.31  10.91.254.211   12346  12346  10.91.252.6  private1  private1  0     29       1       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  10.91.243.31  10.91.254.212   12346  12346  10.91.252.7  private1  private1  0     29       0       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  10.91.243.31  10.91.254.227   12346  12346  10.91.252.8  private1  private1  0     23       0       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  10.91.243.31  10.91.254.228   12346  12346  10.91.252.9  private1  private1  0     23       1       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.55.14.29     12386  12406  10.91.252.6  3g        3g        0     35       5       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.55.14.31     12386  12346  10.91.252.7  3g        3g        0     35       5       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.228.123.61   12386  12366  10.91.252.8  3g        3g        0     37       6       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.1.2   10.228.123.63   12386  12346  10.91.252.9  3g        3g        0     36       6       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.2.2   10.55.14.28     12406  12406  10.91.252.6  lte       lte       0     36       7       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.2.2   10.55.14.30     12406  12366  10.91.252.7  lte       lte       0     36       8       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    ipsec  192.168.2.2   10.228.123.60   12406  12366  10.91.252.8  lte       lte       100   0        0       0          __all_tunnels__
    ipsec  192.168.2.2   10.228.123.62   12406  12366  10.91.252.9  lte       lte       0     37       7       0,1,2,3,4  __all_tunnels__, Bulk-Data, Scavenger, Transactional-Data, Voice
    """

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        sla_dict = {}

        result_dict = {}

        p0 = re.compile(r"^(?P<proto>\w+)\s+(?P<srcip>\d+\.\d+\.\d+\.\d+)\s+(?P<destip>\d+\.\d+\.\d+\.\d+)\s+(?P<srcport>\d+)\s+(?P<destport>\d+)\s+(?P<remip>\d+\.\d+\.\d+\.\d+)\s+(?P<localcolor>\w+)\s+(?P<remotecolor>\w+)\s+(?P<loss>\d+)\s+(?P<latency>\d+)\s+(?P<jitter>\d+)\s+(?P<slaclass>\S+)\s+(?P<slaclassname>.*)\s+")

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if "lines" not in sla_dict:
                    result_dict = sla_dict.setdefault("lines",{})
                destip = m.groupdict()["destip"]
                color = m.groupdict()["localcolor"]
                loss = m.groupdict()["loss"]
                latency = m.groupdict()["latency"]
                jitter = m.groupdict()["jitter"]
                slaclass = m.groupdict()["slaclass"]
                result_dict[destip] = {}
                result_dict[destip]["color"] = color
                result_dict[destip]["loss"] = loss
                result_dict[destip]["latency"] = latency
                result_dict[destip]["jitter"] = jitter
                result_dict[destip]["slaclass"] = slaclass
                continue
        return sla_dict