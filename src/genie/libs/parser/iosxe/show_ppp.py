"""show_PPP.py
IOSXE parsers for the following show commands:
    * 'show ppp statistics'
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Optional

# import parser utils
from genie.libs.parser.utils.common import Common

class ShowPppStatisticsSchema(MetaParser):
    ''' Schema for:
            show ppp statistics
    '''
    schema = {
        Optional('ppp_handles_allocated'): {
            'type': int,
            'total_allocated': int,
            'since_cleared': int,
        },
        Optional('ppp_handles_freed'): {
            'type': int,
            'total_freed': int,
            'since_cleared': int,
        },
        Optional('ppp_encap_intf'): {
            'type': int,
            'total_intf': int,
            'since_cleared': int,
        },
        Optional('ppp_links_lcp_stage'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('ppp_links_unauth_stage'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('ppp_links_auth_stage'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('ppp_links_forward_stage'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('ppp_links_loc_term_stage'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('successful_lcp_neg'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('auth_stage'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('ipcp_sessions'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('chap_auth_attemps'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('chap_auth_failures'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('pap_auth_attempts'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('pap_auth_success'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('pap_auth_failures'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('total_sessions'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('non_mlp_sessions'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('total_links'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('non_mlp_links'): {
            'type': int,
            'peak': int,
            'current': int,
        },
        Optional('missed_keepalives'): {
            'type': int,
            'total': int,
            'since_cleared': int,
        },
        Optional('rec_lcp_term_frm_peer'): {
            'type': int,
            'total': int,
            'since_cleared': int,
        },
        Optional('lower_layer_disc'): {
            'type': int,
            'total': int,
            'since_cleared': int,
        },
        Optional('user_cleared'): {
            'type': int,
            'total': int,
            'since_cleared': int,
        },
    }

class ShowPppStatistics(ShowPppStatisticsSchema):
    ''' Parser for:
            show ppp statictics
    '''
    cli_command = 'show ppp statistics'

    def cli(self, output=None):
        cmd = self.cli_command

        if output is None:
            output = self.device.execute(cmd)

        res_dict = {}

        # 14   PPP Handles Allocated                       4          4         
        p1 = re.compile(r'^(?P<type>\d+)\s+PPP Handles Allocated\s+'
                r'(?P<total_allocated>\d+)\s+(?P<since_cleared>\d+)$')

        # 15   PPP Handles Freed                           1          1         
        p2 = re.compile(r'^(?P<type>\d+)\s+PPP Handles Freed\s+'
                r'(?P<total_freed>\d+)\s+(?P<since_cleared>\d+)$')

        # 19   PPP Encapped Interfaces                     4          4   
        p3 = re.compile(r'^(?P<type>\d+)\s+PPP Encapped Interfaces\s+'
                r'(?P<total_intf>\d+)\s+(?P<since_cleared>\d+)$')

        # 1    Links at LCP Stage                          1          0         
        p4 = re.compile(r'^(?P<type>\d+)\s+Links at LCP Stage\s+'
                        r'(?P<peak>\d+)\s+(?P<current>\d+)$')

        # 2    Links at Unauthenticated Name Stage         1          0         
        p5 = re.compile(r'^(?P<type>\d+)\s+Links at Unauthenticated Name Stage\s+'
                        r'(?P<peak>\d+)\s+(?P<current>\d+)$')

        # 3    Links at Authenticated Name Stage           1          0         
        p6 = re.compile(r'^(?P<type>\d+)\s+Links at Authenticated Name Stage\s+'
                        r'(?P<peak>\d+)\s+(?P<current>\d+)$')

        # 6    Links at Forwarded Stage                    1          0         
        p7 = re.compile(r'^(?P<type>\d+)\s+Links at Forwarded Stage\s+'
                        r'(?P<peak>\d+)\s+(?P<current>\d+)$')

        # 7    Links at Local Termination Stage            1          1         
        p8 = re.compile(r'^(?P<type>\d+)\s+Links at Local Termination Stage\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 20   Successful LCP neogtiations                 66         66        
        p9 = re.compile(r'^(?P<type>\d+)\s+Successful LCP neogtiations\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 22   Entered Authentication Stage                66         66        
        p10 = re.compile(r'(?P<type>\d+)\s+Entered Authentication Stage\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 28   IPCP UP Sessions                            1          1         
        p11 = re.compile(r'(?P<type>\d+)\s+IPCP UP Sessions\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 48   CHAP authentication attempts                22         22        
        p12 = re.compile(r'^(?P<type>\d+)\s+CHAP authentication attempts\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 50   CHAP authentication failures                22         22        
        p13 = re.compile(r'^(?P<type>\d+)\s+CHAP authentication failures\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 51   PAP authentication attempts                 44         44        
        p14 = re.compile(r'^(?P<type>\d+)\s+PAP authentication attempts\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 52   PAP authentication successes                25         25        
        p15 = re.compile(r'^(?P<type>\d+)\s+PAP authentication successes\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 53   PAP authentication failures                 3          3         
        p16 = re.compile(r'^(?P<type>\d+)\s+PAP authentication failures\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 95   Total Sessions                              1          1         
        p17 = re.compile(r'^(?P<type>\d+)\s+Total Sessions\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 96   Non-MLP Sessions                            1          1         
        p18 = re.compile(r'^(?P<type>\d+)\s+Non-MLP Sessions\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 98   Total Links                                 2          1
        p19 = re.compile(r'^(?P<type>\d+)\s+Total Links\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 99   Non-MLP Links                               2          1
        p20 = re.compile(r'^(?P<type>\d+)\s+Non-MLP Links\s+'
                        r'(?P<peak>\d+) +(?P<current>\d+)$')

        # 11   Missed too many keepalives                  1          1         
        p21 = re.compile(r'^(?P<type>\d+)\s+Missed too many keepalives\s+'
                        r'(?P<total>\d+) +(?P<since_cleared>\d+)$')

        # 17   Received LCP TERMREQ from peer              16         16
        p22 = re.compile(r'^(?P<type>\d+)\s+Received LCP TERMREQ from peer\s+'
                        r'(?P<total>\d+) +(?P<since_cleared>\d+)$')

        # 29   Lower Layer disconnected                    14         14
        p23 = re.compile(r'^(?P<type>\d+)\s+Lower Layer disconnected\s+'
                        r'(?P<total>\d+) +(?P<since_cleared>\d+)$')

        # 61   User cleared from exec prompt               4          4
        p24 = re.compile(r'^(?P<type>\d+)\s+User cleared from exec prompt\s+'
                        r'(?P<total>\d+) +(?P<since_cleared>\d+)$')

        for line in output.splitlines():
            line = line.strip()

            # 14   PPP Handles Allocated                       4          4        
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                alloc_dict = res_dict.setdefault('ppp_handles_allocated', {})
                alloc_dict.update({
                    'type' : int(groups['type']),
                    'total_allocated' : int(groups['total_allocated']),
                    'since_cleared' : int(groups['since_cleared'])
                })
                continue

            # 15   PPP Handles Freed                           1          1        
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                freed_dict = res_dict.setdefault('ppp_handles_freed', {})
                freed_dict.update({
                    'type' : int(groups['type']),
                    'total_freed' : int(groups['total_freed']),
                    'since_cleared' : int(groups['since_cleared'])
                })
                continue

            # 19   PPP Encapped Interfaces                     4          4  
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                encap_dict = res_dict.setdefault('ppp_encap_intf', {})
                encap_dict.update({
                    'type' : int(groups['type']),
                    'total_intf' : int(groups['total_intf']),
                    'since_cleared' : int(groups['since_cleared'])
                })
                continue

            # 1    Links at LCP Stage                          1          0
            m = p4.match(line)
            if m:
                groups = m.groupdict()
                lcp_dict = res_dict.setdefault('ppp_links_lcp_stage', {})
                lcp_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue
 
            # 2    Links at Unauthenticated Name Stage         1          0
            m = p5.match(line)
            if m:
                groups = m.groupdict()
                unauth_dict = res_dict.setdefault('ppp_links_unauth_stage', {})
                unauth_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 3    Links at Authenticated Name Stage           1          0
            m = p6.match(line)
            if m:
                groups = m.groupdict()
                auth_dict = res_dict.setdefault('ppp_links_auth_stage', {})
                auth_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 6    Links at Forwarded Stage                    1          0     
            m = p7.match(line)
            if m:
                groups = m.groupdict()
                forward_dict = res_dict.setdefault('ppp_links_forward_stage', {})
                forward_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 7    Links at Local Termination Stage            1          1  
            m = p8.match(line)
            if m:
                groups = m.groupdict()
                auth_dict = res_dict.setdefault('ppp_links_loc_term_stage', {})
                auth_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 20   Successful LCP neogtiations                 66         66  
            m = p9.match(line)
            if m:
                groups = m.groupdict()
                lcp_neg_dict = res_dict.setdefault('successful_lcp_neg', {})
                lcp_neg_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 22   Entered Authentication Stage                66         66   
            m = p10.match(line)
            if m:
                groups = m.groupdict()
                auth_stage_dict = res_dict.setdefault('auth_stage', {})
                auth_stage_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 28   IPCP UP Sessions                            1          1 
            m = p11.match(line)
            if m:
                groups = m.groupdict()
                ipcp_dict = res_dict.setdefault('ipcp_sessions', {})
                ipcp_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 48   CHAP authentication attempts                22         22   
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                chap_auth_dict = res_dict.setdefault('chap_auth_attemps', {})
                chap_auth_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 50   CHAP authentication failures                22         22        
            m = p13.match(line)
            if m:
                groups = m.groupdict()
                auth_fail_dict = res_dict.setdefault('chap_auth_failures', {})
                auth_fail_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 51   PAP authentication attempts                 44         44 
            m = p14.match(line)
            if m:
                groups = m.groupdict()
                ppp_auth_attempt_dict = res_dict.setdefault('pap_auth_attempts', {})
                ppp_auth_attempt_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 52   PAP authentication successes                25         25
            m = p15.match(line)
            if m:
                groups = m.groupdict()
                ppp_auth_dict = res_dict.setdefault('pap_auth_success', {})
                ppp_auth_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 53   PAP authentication failures                 3          3
            m = p16.match(line)
            if m:
                groups = m.groupdict()
                ppp_auth_failure_dict = res_dict.setdefault('pap_auth_failures', {})
                ppp_auth_failure_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 95   Total Sessions                              1          1
            m = p17.match(line)
            if m:
                groups = m.groupdict()
                total_sessions_dict = res_dict.setdefault('total_sessions', {})
                total_sessions_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 96   Non-MLP Sessions                            1          1
            m = p18.match(line)
            if m:
                groups = m.groupdict()
                non_mlp_dict = res_dict.setdefault('non_mlp_sessions', {})
                non_mlp_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 98   Total Links                                 2          1
            m = p19.match(line)
            if m:
                groups = m.groupdict()
                #total_links = groups['total_links']
                total_links_dict = res_dict.setdefault('total_links', {})
                total_links_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 99   Non-MLP Links                               2          1
            m = p20.match(line)
            if m:
                groups = m.groupdict()
                non_mlp_links_dict = res_dict.setdefault('non_mlp_links', {})
                non_mlp_links_dict.update({
                    'type' : int(groups['type']),
                    'peak' : int(groups['peak']),
                    'current' : int(groups['current'])
                })
                continue

            # 11   Missed too many keepalives                  1          1
            m = p21.match(line)
            if m:
                groups = m.groupdict()
                missed_dict = res_dict.setdefault('missed_keepalives', {})
                missed_dict.update({
                    'type' : int(groups['type']),
                    'total' : int(groups['total']),
                    'since_cleared' : int(groups['since_cleared'])
                })
                continue

            # 17   Received LCP TERMREQ from peer              16         16
            m = p22.match(line)
            if m:
                groups = m.groupdict()
                lcp_term_dict = res_dict.setdefault('rec_lcp_term_frm_peer', {})
                lcp_term_dict.update({
                    'type' : int(groups['type']),
                    'total' : int(groups['total']),
                    'since_cleared' : int(groups['since_cleared'])
                })
                continue

            # 29   Lower Layer disconnected                    14         14
            m = p23.match(line)
            if m:
                groups = m.groupdict()
                low_dict = res_dict.setdefault('lower_layer_disc', {})
                low_dict.update({
                    'type' : int(groups['type']),
                    'total' : int(groups['total']),
                    'since_cleared' : int(groups['since_cleared'])
                })
                continue

            # 61   User cleared from exec prompt               4          4
            m = p24.match(line)
            if m:
                groups = m.groupdict()
                user_dict = res_dict.setdefault('user_cleared', {})
                user_dict.update({
                    'type' : int(groups['type']),
                    'total' : int(groups['total']),
                    'since_cleared' : int(groups['since_cleared'])
                })
                continue

        return res_dict



