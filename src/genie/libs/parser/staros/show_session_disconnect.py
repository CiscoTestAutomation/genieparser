"""starOS implementation of show_show_session_disconnect-reasons_buckets.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Schema

class ShowSessionSchema(MetaParser):
    """Schema for show session disconnect-reasons buckets"""

    schema = {
        'show_session_disconnect-reasons_buckets': {
            Any(): {
                'NUM DISC': str,
                'PERCENTAGE': str,
                'NUM DISC2': str,
                'PERCENTAGE2': str,
                'NUM DISC3': str,
                'PERCENTAGE3': str,
                'NUM DISC4': str,
                'PERCENTAGE4': str
            },
        }    
    }


class ShowSession(ShowSessionSchema):
    """Parser for show session disconnect-reasons buckets"""

    cli_command = 'show session disconnect-reasons buckets'

    """
Disconnect Reason                                        Num Disc  Percentage    Num Disc  Percentage    Num Disc  Percentage    Num Disc  Percentage
-----------------------------------------------------  ----------  ----------  ----------  ----------  ----------  ----------  ----------  ----------
Admin-disconnect                                               72     0.14377          72     0.14377          72     0.14377          72     0.14377
Remote-disconnect                                           29173    58.25163       29173    58.25163       29172    58.25196       29172    58.25196
Local-disconnect                                                1     0.00200           1     0.00200           1     0.00200           1     0.00200
No-resource                                                     4     0.00799           4     0.00799           4     0.00799           4     0.00799
Pool-IP-address-not-valid                                       2     0.00399           2     0.00399           2     0.00399           2     0.00399
Idle-Inactivity-timeout                                      9141    18.25243        9141    18.25243        9140    18.25116        9140    18.25116
Absolute-timeout                                             4090     8.16677        4090     8.16677        4090     8.16710        4090     8.16710
Invalid-source-IP-address                                     314     0.62698         314     0.62698         314     0.62701         314     0.62701
lpool-ip-validation-failed                                     53     0.10583          53     0.10583          53     0.10583          53     0.10583
failed-update-handoff                                           5     0.00998           5     0.00998           5     0.00998           5     0.00998
failed-auth-with-charging-svc                                4961     9.90595        4961     9.90595        4961     9.90635        4961     9.90635
ims-authorization-failed                                       17     0.03395          17     0.03395          17     0.03395          17     0.03395
Gtp-context-replacement                                       164     0.32747         164     0.32747         164     0.32748         164     0.32748
ims-authorization-revoked                                       4     0.00799           4     0.00799           4     0.00799           4     0.00799
unknown-apn                                                    17     0.03395          17     0.03395          17     0.03395          17     0.03395
disconnect-from-policy-server                                1325     2.64571        1325     2.64571        1325     2.64582        1325     2.64582
gtpu-err-ind                                                   36     0.07188          36     0.07188          36     0.07189          36     0.07189
Sgw-context-replacement                                        19     0.03794          19     0.03794          19     0.03794          19     0.03794
ggsn-no-rsp-from-sgsn                                          19     0.03794          19     0.03794          19     0.03794          19     0.03794
4Gto3G-context-replacement                                     55     0.10982          55     0.10982          55     0.10983          55     0.10983
3Gto4G-context-replacement                                     35     0.06989          35     0.06989          35     0.06989          35     0.06989
srvcc-ps-to-cs-handover                                        74     0.14776          74     0.14776          74     0.14777          74     0.14777
disconnect-from-charging-server                               500     0.99838         500     0.99838         500     0.99842         500     0.99842            
    
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
        p0 = re.compile(r'(?P<disconnect_reason>^\w+.+[a-z])\s+(?P<numdisc>\d+)\s+(?P<percentage>\d+.\d+)\s+(?P<numdisc2>\d+)\s+(?P<percentage2>\d+.\d+)\s+(?P<numdisc3>\d+)\s+(?P<percentage3>\d+.\d+)\s+(?P<numdisc4>\d+)\s+(?P<percentage4>\d+.\d+)')
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'show_session_disconnect-reasons_buckets' not in recovery_dict:
                    result_dict = recovery_dict.setdefault('show_session_disconnect-reasons_buckets',{})
                disconnect_reason = m.groupdict()['disconnect_reason']
                num_disc = m.groupdict()['numdisc']
                percentage = m.groupdict()['percentage']
                num_disc2 = m.groupdict()['numdisc2']
                percentage2 = m.groupdict()['percentage2']
                num_disc3 = m.groupdict()['numdisc3']
                percentage3 = m.groupdict()['percentage3']
                num_disc4 = m.groupdict()['numdisc4']
                percentage4 = m.groupdict()['percentage4']
                result_dict[disconnect_reason] = {}
                result_dict[disconnect_reason]['NUM DISC'] = num_disc
                result_dict[disconnect_reason]['PERCENTAGE'] = percentage
                result_dict[disconnect_reason]['NUM DISC2'] = num_disc2
                result_dict[disconnect_reason]['PERCENTAGE2'] = percentage2
                result_dict[disconnect_reason]['NUM DISC3'] = num_disc3
                result_dict[disconnect_reason]['PERCENTAGE3'] = percentage3
                result_dict[disconnect_reason]['NUM DISC4'] = num_disc4
                result_dict[disconnect_reason]['PERCENTAGE4'] = percentage4           
                continue

        return recovery_dict