import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Schema

class ShowSesDisReaSchema(MetaParser):
    """Schema for show session disconnect-reasons"""

    schema = {
        'dis_rea_table': {
            'TOTAL_DISCONNECTS': str,
            Any(): {
                'NUM_DISC': str,
                'PERCENTAGE': str,
            },
        }    
    }

class ShowSessionDiss(ShowSesDisReaSchema):
    """Parser for show session disconnect-reasons"""

    cli_command = 'show session disconnect-reasons'

    """
[local]COR-ASR5K-1# show session disconnect-reasons 
Monday January 29 14:48:31 ART 2024
Session Disconnect Statistics

Total Disconnects: 12345249830

Disconnect Reason                                        Num Disc  Percentage
-----------------------------------------------------  ----------  ----------
Admin-disconnect                                           898190     0.00728
Remote-disconnect                                     11802373713    95.60255
Local-disconnect                                          3653063     0.02959
Idle-Inactivity-timeout                                 414551522     3.35798
Session-setup-timeout                                      384617     0.00312
internal-error                                                  2     0.00000
path-failure                                               117515     0.00095
Gtp-unknown-pdp-addr-or-pdp-type                         28400654     0.23005
static-ip-validation-failed                                     5     0.00000
ggsn-aaa-auth-req-failed                                        2     0.00000
Long-duration-timeout                                    11185805     0.09061
failed-update-handoff                                     1212400     0.00982
call-internal-reject                                           29     0.00000
failed-auth-with-charging-svc                               11891     0.00010
ims-authorization-failed                                   779951     0.00632
Auth-failed                                              24576425     0.19908
Gtp-context-replacement                                   3179378     0.02575
ims-authorization-revoked                                    5270     0.00004
ims-auth-decision-invalid                                       1     0.00000
dt-ggsn-tun-reestablish-failed                            6064313     0.04912
No-response                                               3459270     0.02802
unknown-apn                                                     2     0.00000
gtpc-path-failure                                          343664     0.00278
gtpu-path-failure                                          923654     0.00748
disconnect-from-policy-server                               10969     0.00009
gtpu-err-ind                                              8389798     0.06796
apn-denied-no-subscription                                      3     0.00000
Sgw-context-replacement                                   3358732     0.02721
ggsn-no-rsp-from-sgsn                                    10433802     0.08452
invalid-qci                                                     1     0.00000
4Gto3G-context-replacement                                 615958     0.00499
3Gto4G-context-replacement                               10801712     0.08750
Local-fallback-timeout                                          1     0.00000
srvcc-ps-to-cs-handover                                         2     0.00000
pgw-transaction-timeout                                         1     0.00000
path-failure-s5                                            189532     0.00154
path-failure-s11                                           570060     0.00462
gtpu-path-failure-s5u                                       17299     0.00014
gtpu-path-failure-s1u                                        1561     0.00001
gtpu-err-ind-s5u                                            13387     0.00011
disconnect-from-charging-server                           8725676     0.07068
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        session_dict = {}   
        result_dict = {}

        # initial regexp pattern
        p0= re.compile(r'Total\s\Disconnects:(?P<total_disconnects_title>\s\d+)')
        p1 = re.compile(r'((?P<disconnect_reason>[\w\-*]+)\s+(?P<num_disc>\d+)\s+(?P<percentage>\d+\.\d{5}))')
    
        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'dis_rea_table' not in session_dict:
                    result_dict = session_dict.setdefault('dis_rea_table',{})
                total_dis = m.groupdict()['total_disconnects_title']
            
                result_dict['TOTAL_DISCONNECTS'] = total_dis

            m = p1.match(line)
            if m:
                if 'dis_rea_table' not in session_dict:
                    result_dict = session_dict.setdefault('dis_rea_table',{})
                disconnect = m.groupdict()['disconnect_reason']
                number_disconnected = m.groupdict()['num_disc']
                per = m.groupdict()['percentage'] 
                result_dict[disconnect] = {}
                result_dict[disconnect]['NUM_DISC'] = number_disconnected
                result_dict[disconnect]['PERCENTAGE'] = per

        return session_dict
