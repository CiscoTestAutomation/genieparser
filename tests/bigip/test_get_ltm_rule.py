# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# BigIP get_ltm_rule
from genie.libs.parser.bigip.get_ltm_rule import LtmRule

# ==================================
# Unit test for parsing BigIP URL '/mgmt/tm/ltm/rule'
# ==================================


class FakeResponse(object):
    def json(self):
        return {
            "kind": "tm:ltm:rule:rulecollectionstate",
            "selfLink": "https://localhost/mgmt/tm/ltm/rule?ver=14.1.2.1",
            "items": [
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "SNAT-10-197-225.tcl",
                    "partition": "Common",
                    "fullPath": "/Common/SNAT-10-197-225.tcl",
                    "generation": 607,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-10-197-225.tcl?ver=14.1.2.1",
                    "apiAnonymous": 'when CLIENT_ACCEPTED { snat 10.197.225.[getfield [IP::client_addr] "." 4] }',
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "SNAT-39",
                    "partition": "Common",
                    "fullPath": "/Common/SNAT-39",
                    "generation": 972,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-39?ver=14.1.2.1",
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_APM_ExchangeSupport_OA_BasicAuth",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_APM_ExchangeSupport_OA_BasicAuth",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_OA_BasicAuth?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    # Global variables\n    # static::POLICY_RESULT_CACHE_AUTHFAILED\n    #     Administrator can set this into 1, when there is a necessity to cache failed policy result.\n    #     This may be needed to avoid account locked caused by the Active Sync device when it uses wrong passwords.\n    #     One possible scenario, is that when the user changes the password in Active Directory, but missed to changed in their devices.\n    # Responses\n    # On denied result\n    #     Administrator can customize the responses to the device depends on more complex conditions when necessary.\n    #     In those cases, please use ACCESS::respond command.\n    #     The following is the syntax of ACCESS::respond\n    #     ACCESS::respond <status code> [ content <body> ] [ <Additional Header> <Additional Header value>* ]\n    #     e.g. ACCESS::respond 401 content "Error: Denied" WWW-Authenticate "basic realm=\\"f5.com\\"" Connection close\n    when RULE_INIT {\n        # Please set the following global variables for customized responses.\n        set static::actsync_401_http_body "<html><title>Authentication Failured</title><body>Error: Authentication Failure</body></html>"\n        set static::actsync_503_http_body "<html><title>Service is not available</title><body>Error: Service is not available</body></html>"\n        set static::ACCESS_LOG_PREFIX                 "01490000:7:"\n\n        # Second Virtual Server name for 401 NTLM responder\n        set static::ACCESS_SECOND_VIRTUAL_NAME        "_ACCESS_401_NTLM_responder_HTTPS"\n\n        set static::POLICY_INPROGRESS                 "policy_inprogress"\n        set static::POLICY_AUTHFAILED                 "policy_authfailed"\n        # The request with huge content length can not be used for starting ACCESS session.\n        # This kind of request will be put on hold, and this iRule will try to use another\n        # request to start the session. The following value is used for Outlook Anywhere.\n        set static::OA_MAGIC_CONTENT_LEN              1073741824\n\n        # Similar with OutlookAnywhere case, ACCESS can not use the request which is\n        # larger then following size. This becomes an issue with application that using\n        # Exchange Web Service as its main protocol such as Mac OS X applications\n        # (e.g. Mail app, Microsoft Entourage, etc)\n        # This kind of request will be put on hold, and this iRule will try to use another\n        # request to start the session.\n        set static::FIRST_BIG_POST_CONTENT_LEN        640000\n\n        # Set it into 1 if the backend EWS handler accepts HTTP Basic Authentication.\n        set static::EWS_BKEND_BASIC_AUTH              0\n        # The following variable controls the polling mechanism.\n        set static::POLICY_RESULT_POLL_INTERVAL       250\n        set static::POLICY_RESULT_POLL_MAXRETRYCYCLE  600\n\n        # Set this global variable to 1 for caching authentication failure\n        # Useful for avoiding account locked out.\n        set static::POLICY_RESULT_CACHE_AUTHFAILED    0\n\n        # set this global variable to set alternative timeout for particular session\n        set static::POLICY_ALT_INACTIVITY_TIMEOUT     120\n\n        set static::ACCESS_USERKEY_TBLNAME            "_access_userkey"\n\n\n        set static::ACCESS_DEL_COOKIE_HDR_VAL         "MRHSession=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; path=/"\n\n        log -noname accesscontrol.local1.debug "01490000:7: EWS_BKEND_BASIC_AUTH = $static::EWS_BKEND_BASIC_AUTH"\n    }\n    when ACCESS_ACL_ALLOWED {\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX [HTTP::method] [HTTP::uri] [HTTP::header Content-Length]"\n\n        # MSFT Exchange\'s EWS request handler always requesting NTLM even the connection has been\n        # already authenticated if there is a HTTP Basic Auth in the request.\n        if { [ info exists f_exchange_web_service ] && $f_exchange_web_service  == 1 }  {\n            if { $static::EWS_BKEND_BASIC_AUTH == 0 } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Removing HTTP Basic Authorization header"\n                HTTP::header remove Authorization\n            }\n        }\n    }\n\n    when HTTP_REQUEST {\n        set http_path                       [ string tolower [HTTP::path] ]\n        set f_clientless_mode               0\n        set f_alt_inactivity_timeout        0\n        set f_rpc_over_http                 0\n        set f_exchange_web_service          0\n        set f_auto_discover                 0\n        set f_activesync                    0\n        set f_offline_address_book          0\n        set f_availability_service          0\n\n        #  Here put appropriate pool when necessary.\n        switch -glob $http_path {\n        "/rpc/rpcproxy.dll" {\n            # Supports for RPC over HTTP. (Outlook Anywhere)\n            set f_rpc_over_http 1\n        }\n        "/autodiscover/autodiscover.xml" {\n            # Supports for Auto Discover protocol.\n            set f_auto_discover 1\n            # This request does not require long inactivity timeout.\n            # Don\'t use this for now\n            set f_alt_inactivity_timeout 0\n        }\n        "/microsoft-server-activesync" {\n            # Supports for ActiveSync\n            set f_activesync 1\n        }\n        "/oab/*" {\n            # Supports for Offline Address Book\n            set f_offline_address_book 1\n            # Don\'t use this for now\n            set f_alt_inactivity_timeout 0\n        }\n        "/ews/*" {\n            # Support for Exchange Web Service\n            # Outlook\'s Availability Service borrows this protocol.\n            set f_exchange_web_service 1\n        }\n        "/as/*" {\n            # Support for Availability Service.\n            # do nothing for now. (Untested)\n            set f_availability_service 1\n        }\n        default {\n            return\n        }\n        }\n\n        set f_reqside_set_sess_id           0\n        set http_method                     [HTTP::method]\n        set http_hdr_host                   [HTTP::host]\n        set http_hdr_uagent                 [HTTP::header User-Agent]\n        set http_uri                        [HTTP::uri]\n        set http_content_len                [HTTP::header Content-Length]\n        set MRHSession_cookie               [HTTP::cookie value MRHSession]\n        set auth_info_b64enc                ""\n\n        if { ! [ info exists src_ip ] } {\n            set src_ip                            [IP::remote_addr]\n        }\n        if { ! [ info exists PROFILE_POLICY_TIMEOUT ] } {\n            set PROFILE_POLICY_TIMEOUT            [PROFILE::access access_policy_timeout]\n        }\n        if { ! [ info exists PROFILE_MAX_SESS_TIMEOUT ] } {\n            set PROFILE_MAX_SESS_TIMEOUT          [PROFILE::access max_session_timeout]\n        }\n        if { ! [ info exists PROFILE_RESTRICT_SINGLE_IP ] } {\n            set PROFILE_RESTRICT_SINGLE_IP        1\n        }\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX method: $http_method"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Src IP: $src_ip"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX User-Agent: $http_hdr_uagent"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP uri: $http_uri"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP len: $http_content_len"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Restrict-to-single-client-ip: $PROFILE_RESTRICT_SINGLE_IP"\n\n        # First, do we have valid MRHSession cookie.\n        if { $MRHSession_cookie != "" } {\n            if { [ACCESS::session exists -state_allow -sid $MRHSession_cookie] } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *VALID* MRHSession cookie: $MRHSession_cookie"\n            } else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *INVALID* MRHSession cookie: $MRHSession_cookie"\n                set MRHSession_cookie ""\n                HTTP::cookie remove MRHSession\n            }\n        }\n\n        set http_hdr_auth [HTTP::header Authorization]\n        if { [ string match -nocase {basic *} $http_hdr_auth ] != 1 } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Not basic authentication. Ignore received auth header"\n            set http_hdr_auth ""\n        }\n\n        if { $http_hdr_auth == "" } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX No/Empty Auth header"\n            # clean up the cookie\n            if { $MRHSession_cookie == "" } {\n                HTTP::respond 401 content  $static::actsync_401_http_body WWW-Authenticate "Basic realm=\\"[HTTP::header Host]\\"" Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL Connection Close\n                return\n            }\n            # Do nothing if we have a valid MRHSession cookie.\n        }\n\n        set f_release_request           0\n        # Optimization for clients which support cookie\n        if { $MRHSession_cookie != "" } {\n            # Default profile access setting is false\n            if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n                set f_release_request 1\n            }\n            elseif { [ IP::addr $src_ip equals [ ACCESS::session data get -sid $MRHSession_cookie "session.user.clientip" ] ] } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP matched"\n                set f_release_request 1\n            }\n            else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP does not matched"\n                set MRHSession_cookie ""\n                HTTP::cookie remove MRHSession\n            }\n        }\n\n        if { $f_release_request == 0 } {\n            set apm_username [string tolower [HTTP::username]]\n            set apm_password [HTTP::password]\n            if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n                binary scan [md5 "$apm_password"] H* user_hash\n            }\n            else {\n                binary scan [md5 "$apm_password$src_ip"] H* user_hash\n            }\n            set user_key    "$apm_username.$user_hash"\n            unset user_hash\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP Hdr Auth: $http_hdr_auth"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX apm_username: $apm_username"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX user_key = $user_key"\n            set apm_cookie_list             [ ACCESS::user getsid $user_key ]\n            if { [ llength $apm_cookie_list ] != 0 } {\n                set apm_cookie [ ACCESS::user getkey [ lindex $apm_cookie_list 0 ] ]\n                if { $apm_cookie != "" } {\n                    HTTP::cookie insert name MRHSession value $apm_cookie\n                    set f_release_request 1\n                }\n            }\n        }\n\n        if { $http_content_len ==  $static::OA_MAGIC_CONTENT_LEN } {\n            set f_oa_magic_content_len 1\n        }\n\n        set f_sleep_here 0\n        set retry 1\n\n        while { $f_release_request == 0 && $retry <=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } {\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Trying #$retry for $http_method $http_uri $http_content_len"\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Reading $user_key from table $static::ACCESS_USERKEY_TBLNAME"\n\n            set apm_cookie [table lookup -subtable  $static::ACCESS_USERKEY_TBLNAME -notouch $user_key]\n            if { $apm_cookie != "" } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Verifying table cookie = $apm_cookie"\n\n                # Accessing SessionDB is not that cheap. Here we are trying to check known value.\n                if { $apm_cookie == "policy_authfailed" || $apm_cookie == "policy_inprogress"} {\n                    # Do nothing\n                } elseif  { ! [ ACCESS::session exists $apm_cookie ] } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX table cookie = $apm_cookie is out-of-sync"\n                    # Table value is out of sync. Ignores it.\n                    set apm_cookie ""\n                }\n            }\n\n            switch $apm_cookie {\n            "" {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX NO APM Cookie found"\n\n                if { [ info exists f_oa_magic_content_len ] && $f_oa_magic_content_len == 1 } {\n                    # Outlook Anywhere request comes in pair. The one with 1G payload is not usable\n                    # for creating new session since 1G content-length is intended for client to upload\n                    # the data when needed.\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Start to wait $static::POLICY_RESULT_POLL_INTERVAL ms for request with magic content-len"\n                    set f_sleep_here 1\n                } elseif { [ info exists f_exchange_web_service ] && $f_exchange_web_service == 1 && $http_content_len > $static::FIRST_BIG_POST_CONTENT_LEN } {\n                    # Here we are getting large EWS request, which can\'t be used for starting new session\n                    # in clientless-mode. Have it here waiting for next smaller one.\n                    # We are holding the request here in HTTP filter, and HTTP filter automatically\n                    # clamping down the TCP window when necessary.\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Start to wait $static::POLICY_RESULT_POLL_INTERVAL ms for big EWS request"\n                    set f_sleep_here 1\n                } else {\n                   set apm_cookie               "policy_inprogress"\n                   set f_reqside_set_sess_id    1\n                   set f_release_request        1\n                }\n            }\n            "policy_authfailed" {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Found $user_key with AUTH_FAILED"\n                HTTP::respond 401 content  $static::actsync_401_http_body\n                set f_release_request 1\n            }\n            "policy_inprogress" {\n                if { [ info exists f_activesync ] && ($f_activesync == 1) } {\n                    # For ActiveSync requests, aggressively starts new session.\n                    set f_reqside_set_sess_id    1\n                    set f_release_request        1\n                } else {\n                    set f_sleep_here 1\n                }\n            }\n            default {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Using MRHSession = $apm_cookie"\n                HTTP::header insert Cookie "MRHSession=$apm_cookie"\n                set f_release_request 1\n            }\n            }\n\n            if { $f_reqside_set_sess_id == 1 } {\n                set f_reqside_set_sess_id 0\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Setting $user_key=$apm_cookie $PROFILE_POLICY_TIMEOUT $PROFILE_POLICY_TIMEOUT"\n                set f_clientless_mode 1\n                HTTP::cookie remove MRHSession\n                HTTP::header insert "clientless-mode" 1\n                HTTP::header insert "username" $apm_username\n                HTTP::header insert "password" $apm_password\n                table set -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key $apm_cookie $PROFILE_POLICY_TIMEOUT $PROFILE_POLICY_TIMEOUT\n            }\n\n            if { $f_sleep_here == 1 } {\n                set f_sleep_here 0\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Waiting  $static::POLICY_RESULT_POLL_INTERVAL ms for $http_method $http_uri"\n                after  $static::POLICY_RESULT_POLL_INTERVAL\n            }\n\n            incr retry\n        }\n\n        if { ($f_release_request == 0) && ($retry >=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE) } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Policy did not finish in [expr { $static::POLICY_RESULT_POLL_MAXRETRYCYCLE * $static::POLICY_RESULT_POLL_INTERVAL } ] ms. Close connection for $http_method $http_uri"\n\n            table delete -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key\n            ACCESS::disable\n            TCP::close\n            return\n        }\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Releasing request $http_method $http_uri"\n    }\n\n    when ACCESS_SESSION_STARTED {\n        if { [ info exists user_key ] } {\n\n            ACCESS::session data set "session.user.uuid" $user_key\n            ACCESS::session data set "session.user.microsoft-exchange-client" 1\n\n            if { [ info exists f_activesync ] && $f_activesync == 1 } {\n                ACCESS::session data set "session.user.microsoft-activesync" 1\n            }\n            elseif { [ info exists f_auto_discover ] && $f_auto_discover == 1 } {\n                ACCESS::session data set "session.user.microsoft-autodiscover" 1\n            }\n            elseif { [ info exists f_availability_service ] && $f_availability_service == 1 } {\n                ACCESS::session data set "session.user.microsoft-availabilityservice" 1\n            }\n            elseif { [ info exists f_rpc_over_http ] && $f_rpc_over_http == 1 } {\n                ACCESS::session data set "session.user.microsoft-rpcoverhttp" 1\n            }\n            elseif { [ info exists f_offline_address_book ] && $f_offline_address_book == 1 } {\n                ACCESS::session data set "session.user.microsoft-offlineaddressbook" 1\n            }\n            elseif { [ info exists f_exchange_web_service ] && $f_exchange_web_service == 1 } {\n                ACCESS::session data set "session.user.microsoft-exchangewebservice" 1\n            }\n        }\n        if { [ info exists f_alt_inactivity_timeout ] && $f_alt_inactivity_timeout == 1 } {\n            ACCESS::session data set "session.inactivity_timeout"  $static::POLICY_ALT_INACTIVITY_TIMEOUT\n        }\n    }\n\n    when ACCESS_POLICY_COMPLETED {\n        if { ! [ info exists user_key ] } {\n            return\n        }\n\n        set user_key_value ""\n        set f_delete_session 0\n        set policy_result [ACCESS::policy result]\n        set sid [ ACCESS::session sid ]\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX ACCESS_POLICY_COMPLETED: policy_result = \\"$policy_result\\" user_key = \\"$user_key\\" sid = \\"$sid\\""\n\n        set inactivity_timeout [ACCESS::session data get "session.inactivity_timeout"]\n        set max_sess_timeout [ACCESS::session data get "session.max_session_timeout"]\n        if { $max_sess_timeout == "" } {\n             set max_sess_timeout $PROFILE_MAX_SESS_TIMEOUT\n        }\n\n        switch $policy_result {\n        "allow" {\n            # We depends on this table record self-cleanup capability in order to\n            # indirectly sync with session DB.\n            set user_key_value $sid\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Result: Allow: $user_key => $sid $inactivity_timeout $max_sess_timeout"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX user_key_value = $user_key_value"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX sid = $sid"\n        }\n        "deny" {\n            # When necessary the admin here can check appropriate session variable\n            # and decide what response more appropriate then this default response.\n            ACCESS::respond 401 content  $static::actsync_401_http_body Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL Connection Close\n            if {  $static::POLICY_RESULT_CACHE_AUTHFAILED == 1 } {\n                set user_key_value  $static::POLICY_AUTHFAILED\n            } else {\n                set f_delete_session  1\n            }\n        }\n        default {\n            ACCESS::respond 503 content  $static::actsync_503_http_body Connection Close\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Got unsupported policy result for $user_key ($sid)"\n            set f_delete_session  1\n        }\n        }\n        if { $user_key_value != "" } {\n           log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Setting $user_key => $user_key_value $inactivity_timeout $max_sess_timeout in table $static::ACCESS_USERKEY_TBLNAME"\n\n           table set -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key $user_key_value $inactivity_timeout $max_sess_timeout\n        } else {\n           log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Deleting $user_key in table $static::ACCESS_USERKEY_TBLNAME"\n\n           table delete -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key\n        }\n\n        if { $f_delete_session == 1 } {\n           ACCESS::session remove\n           set f_delete_session 0\n           log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Removing the session for $user_key."\n        }\n    }\ndefinition-signature B1IR2MLC4VSVVTAxgOlbnmxBXZrz7g/jBySWM+WsjwfY8sVY/+/Ss7wZpem7Aotnw3BZdtj14KQPUeSPb1WiMAKc3GxZ0NeWzg/YjbfiJ8ebLTGun9QozSqorwv93+L9UU2Rn1T/hS8kx2peJdCFBm0FVkvVTHrGV88gZhwc77dSZzWm4ynA01qwjYn2WGDztLUpn5Cdx3XSS25sNBINe4QHeJ+7uT8DKl/psLHNT7kk7vJ3Z3uAJJIKCx434KaYTDu0OmNrLk1Rt1R+Ha3Nd+ifGdRYIZrZfYNtr0YIXErzvVlUwrvcF/OHtiLbpgVzerliIOY9VwXBngOGli444Q==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_APM_ExchangeSupport_OA_NtlmAuth",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_APM_ExchangeSupport_OA_NtlmAuth",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_OA_NtlmAuth?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when RULE_INIT {\n        set static::POLICY_INPROGRESS                 "policy_inprogress"\n        set static::POLICY_FAILED                     "policy_failed"\n        set static::POLICY_SUCCEED                    "policy_succeed"\n        set static::POLICY_DONE_WAIT_SEC              5\n\n        set static::FIRST_BIG_POST_CONTENT_LEN        640000\n        set static::POLICY_RESULT_POLL_INTERVAL       100\n        set static::POLICY_RESULT_POLL_MAXRETRYCYCLE  100\n        set static::ACCESS_USERKEY_TBLNAME            "_access_userkey"\n        set static::ACCESS_LOG_PREFIX                 "01490000:7:"\n\n        set static::USE_NTLM_AUTH                     0\n        set static::USE_BASIC_AUTH                    1\n        set static::USE_NTLM_BASIC_AUTH               2\n\n        set static::URL_DEFAULT                       0\n        set static::URL_RPC_OVER_HTTP                 1\n        set static::URL_AUTODISCOVER                  2\n        set static::URL_ACTIVE_SYNC                   3\n        set static::URL_OFFLINEADDRESSBOOK            4\n        set static::URL_EXCHANGEWEBSERVICE            5\n\n        set static::RECVD_AUTH_NONE                   0\n        set static::RECVD_AUTH_NTLM                   1\n        set static::RECVD_AUTH_BASIC                  2\n\n        set static::ACCESS_DEL_COOKIE_HDR_VAL         "MRHSession=deleted; \\\n                                                       expires=Thu, 01-Jan-1970 00:00:01 GMT;\\\n                                                       path=/"\n\n    }\n\n    when HTTP_REQUEST {\n        set http_path                       [string tolower [HTTP::path]]\n        set url_path                        $static::URL_DEFAULT\n        set use_auth                        $static::USE_NTLM_AUTH\n        set f_disable_sso                   0\n\n        switch -glob $http_path {\n        "/rpc/rpcproxy.dll" {\n            set url_path                    $static::URL_RPC_OVER_HTTP\n        }\n        "/autodiscover/autodiscover.xml" {\n            set url_path                    $static::URL_ACTIVE_SYNC\n            # Need to support both NTLM and Basic authentication for this URL\n            set use_auth                    $static::USE_NTLM_BASIC_AUTH\n        }\n        "/microsoft-server-activesync*" {\n            set url_path                    $static::URL_ACTIVE_SYNC\n            # Use only Basic authentication for this URL\n            set use_auth                    $static::USE_BASIC_AUTH\n            set f_disable_sso               1\n        }\n        "/oab*" {\n            set url_path                    $static::URL_OFFLINEADDRESSBOOK\n        }\n        "/ews*" {\n            set url_path                    $static::URL_EXCHANGEWEBSERVICE\n        }\n        default {\n            ECA::disable\n            return\n        }\n        }\n\n        if { ! [ info exists f_ntlm_auth_succeed ] } {\n            set f_ntlm_auth_succeed         0\n        }\n        if { ! [ info exists sid_cache ] } {\n            set sid_cache                         ""\n        }\n        if { ! [ info exists PROFILE_POLICY_TIMEOUT ] } { \n            set PROFILE_POLICY_TIMEOUT            [PROFILE::access access_policy_timeout]\n        }\n        if { ! [ info exists PROFILE_MAX_SESS_TIMEOUT ] } {\n            set PROFILE_MAX_SESS_TIMEOUT          [PROFILE::access max_session_timeout]\n        }\n        if { ! [ info exists src_ip ] } {\n            set src_ip                            [IP::remote_addr]\n        }\n        if { ! [ info exists PROFILE_RESTRICT_SINGLE_IP ] } {\n            set PROFILE_RESTRICT_SINGLE_IP        1\n        }\n\n        set http_method                     [HTTP::method]\n        set http_hdr_host                   [HTTP::host]\n        set http_hdr_uagent                 [HTTP::header User-Agent]\n        set http_uri                        [HTTP::uri]\n        set http_content_len                [HTTP::header Content-Length]\n        set MRHSession_cookie               [HTTP::cookie value MRHSession]\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX method:      $http_method"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Src IP:      $src_ip"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX User-Agent:  $http_hdr_uagent"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP uri:    $http_uri"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP len:    $http_content_len"\n\n        if { ! [ info exists ECA_METADATA_ARG ] } {\n            # Generating argument for ECA::metadata\n            # The NTLM configuration name is derived from assigned virtual name with the algorithm as follows:\n            # <virtual-fullpath> ::= <folder-path>"/"<virtual-basename> as "/" is the last "/" char.\n            # <config-fullpath>  ::= <folder-path>"/" "exch_ntlm" "_" <virtual-basename>\n            # e.g.  Let us say the virtual name is "/prod/exch/vs1", The folder path is "/prod/exch/",\n            #       then object name will be "/prod/exch/exch_ntlm_vs1".\n            set vs_name [virtual name]\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX virtual:     $vs_name"\n            set slash_index [ string last / $vs_name ]\n            if { $slash_index == -1 } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Error: the virtual name does not contain folder information"\n                ACCESS::disable\n                TCP::close\n                return\n            }\n            set ECA_METADATA_ARG    "select_ntlm:"\n            append ECA_METADATA_ARG [ string range $vs_name 0 $slash_index ]\n            append ECA_METADATA_ARG "exch_ntlm_"\n            append ECA_METADATA_ARG [ string range $vs_name [ expr { $slash_index + 1 } ] end ]\n            unset slash_index\n            unset vs_name\n        }\n\n        if { $use_auth == $static::USE_NTLM_AUTH } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Enable ECA: $ECA_METADATA_ARG"\n            ECA::enable\n            ECA::select $ECA_METADATA_ARG\n            return\n        } else {\n            set recvd_auth                      $static::RECVD_AUTH_NONE\n            set http_hdr_auth                   [HTTP::header Authorization]\n            set auth_data                       [split $http_hdr_auth " "]\n            if { $http_hdr_auth != "" } {\n                if { [ llength $auth_data ] == 2 } {\n                    set auth_scheme [ lindex $auth_data 0]\n                    if { [string equal -nocase $auth_scheme "ntlm" ] == 1 } {\n                        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Recv\'d HTTP NTLM Authentication"\n                        set recvd_auth          $static::RECVD_AUTH_NTLM\n                    } elseif { [ string equal -nocase [ lindex $auth_data 0] "basic" ] == 1 } {\n                        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Recv\'d HTTP Basic Authentication"\n                        set recvd_auth          $static::RECVD_AUTH_BASIC\n                        set user                [string tolower [HTTP::username]]\n                        set password            [HTTP::password]\n                    }\n                }\n            }\n            if { $use_auth == $static::USE_BASIC_AUTH } {\n                if { $recvd_auth == $static::RECVD_AUTH_BASIC } {\n                    # Defer the process until later\n                } else {\n                    HTTP::respond 401 -version 1.1 noserver WWW-Authenticate "Basic realm=\\"$http_hdr_host\\"" \\\n                                Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL Connection Close\n                    return\n                }\n            } elseif { $use_auth == $static::USE_NTLM_BASIC_AUTH } {\n                if { ($recvd_auth == $static::RECVD_AUTH_NTLM) || ($f_ntlm_auth_succeed == 1) } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Enable ECA: $ECA_METADATA_ARG"\n                    ECA::enable\n                    ECA::select $ECA_METADATA_ARG\n                    return\n                } elseif { $recvd_auth == $static::RECVD_AUTH_BASIC } {\n                    # Defer the process until later\n                } else {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Request Authorization: NTLM + Basic"\n                    HTTP::respond 401 -version 1.1 noserver WWW-Authenticate "Basic realm=\\"$http_hdr_host\\"" \\\n                                WWW-Authenticate "NTLM" Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL Connection Close\n                    return\n                }\n            }\n\n            # Disable NTLM auth\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Disable ECA"\n            ECA::disable\n            # Disable KCD sso\n            set f_disable_sso               1\n\n            if { $MRHSession_cookie != "" } {\n                if { [ACCESS::session exists -state_allow -sid $MRHSession_cookie] } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *VALID* MRHSession cookie: $MRHSession_cookie"\n                    # Default profile access setting is false\n                    if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n                        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Release the request"\n                        return\n                    }\n                    elseif { [ IP::addr $src_ip equals [ ACCESS::session data get -sid $MRHSession_cookie "session.user.clientip" ] ] } {\n                        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP matched. Release the request"\n                        return\n                    }\n                    else {\n                        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP does not matched"\n                    }\n                }\n                else {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *INVALID* MRHSession cookie: $MRHSession_cookie"\n                }\n\n                set MRHSession_cookie ""\n                HTTP::cookie remove MRHSession\n            }\n\n            set user_key                {}\n            if { $PROFILE_RESTRICT_SINGLE_IP == 1 } {\n                append user_key                    $src_ip\n            }\n            append user_key                 $password\n            binary scan [md5 $user_key ] H* user_key\n            set user_key                    "$user.$user_key"\n\n            set apm_cookie_list             [ ACCESS::user getsid $user_key ]\n            if { [ llength $apm_cookie_list ] != 0 } {\n                set MRHSession_cookie [ ACCESS::user getkey [ lindex $apm_cookie_list 0 ] ]\n                if { $MRHSession_cookie != "" } {\n                    HTTP::cookie remove MRHSession \n                    HTTP::cookie insert name MRHSession value $MRHSession_cookie\n                    return\n                }\n            }\n\n            HTTP::cookie remove MRHSession\n            HTTP::header insert "clientless-mode"       1\n            HTTP::header insert "username"              $user\n            HTTP::header insert "password"              $password\n            return\n        }\n    }\n\n    when ECA_REQUEST_ALLOWED {\n        set f_ntlm_auth_succeed                 1\n\n        if { $MRHSession_cookie == "" } {\n            # Retrieve from SID cache\n            set MRHSession_cookie   $sid_cache\n            HTTP::cookie insert name MRHSession value $sid_cache\n        }\n\n        if { $MRHSession_cookie != "" } {\n            # Destroy session ID cache. This client should not need session ID cache \n            if { ($sid_cache != "") && ($sid_cache != $MRHSession_cookie) } {\n                set sid_cache   ""\n            }\n            if { [ ACCESS::session exists -state_allow $MRHSession_cookie ] } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *VALID* MRHSession cookie: $MRHSession_cookie"\n                # Default profile access setting is false\n                if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Release the request"\n                    return\n                }\n                elseif { [ IP::addr $src_ip equals [ ACCESS::session data get -sid $MRHSession_cookie "session.user.clientip" ] ] } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP matched. Release the request"\n                    return\n                }\n                else {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP does not matched"\n                }\n            } else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *INVALID* MRHSession cookie: $MRHSession_cookie"\n            }\n        }\n\n        set MRHSession  ""\n        set sid_cache   ""\n        HTTP::cookie remove MRHSession\n\n        # Build user_key\n        set    user_key                 {}\n        append user_key                 [string tolower [ECA::username]] "@" [ string tolower [ECA::domainname] ]\n        if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n            append user_key             ":" $src_ip\n        }\n        append user_key                 ":" [ECA::client_machine_name]\n\n        set apm_cookie_list             [ ACCESS::user getsid $user_key ]\n        if { [ llength $apm_cookie_list ] != 0 } {\n            set MRHSession_cookie [ ACCESS::user getkey [ lindex $apm_cookie_list 0 ] ]\n            if { $MRHSession_cookie != "" } {\n                set sid_cache           $MRHSession_cookie\n                HTTP::cookie insert name MRHSession value $MRHSession_cookie\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX APM Cookie found: $sid_cache"\n                return\n            }\n        }\n        unset apm_cookie_list\n\n        set try                         1\n        set start_policy_str            $src_ip\n        append start_policy_str         [TCP::client_port]\n\n        while { $try <=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } {\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX NO APM Cookie found"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Trying #$try for $http_method $http_uri $http_content_len"\n\n            if { $http_content_len > $static::FIRST_BIG_POST_CONTENT_LEN } {\n                # Wait at below\n            } else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX EXEC: table set -notouch -subtable  $static::ACCESS_USERKEY_TBLNAME -excl $user_key $start_policy_str $PROFILE_POLICY_TIMEOUT $PROFILE_MAX_SESS_TIMEOUT"\n                set policy_status [table set -notouch -subtable  $static::ACCESS_USERKEY_TBLNAME -excl $user_key $start_policy_str $PROFILE_POLICY_TIMEOUT $PROFILE_MAX_SESS_TIMEOUT]\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX DONE: table set -notouch -subtable  $static::ACCESS_USERKEY_TBLNAME -excl $user_key $start_policy_str $PROFILE_POLICY_TIMEOUT $PROFILE_MAX_SESS_TIMEOUT"\n                if { $policy_status == $start_policy_str } {\n                    # ACCESS Policy has not started. Start one\n                    HTTP::header insert "clientless-mode"    1\n                    break\n                } elseif { $policy_status == $static::POLICY_SUCCEED } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX table is out-of-sync retry"\n                    table delete -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key\n                    continue\n                } elseif { $policy_status == $static::POLICY_FAILED } {\n                    ACCESS::disable\n                    TCP::close\n                    return\n                }\n                # Wait at below\n            }\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Waiting  $static::POLICY_RESULT_POLL_INTERVAL ms for $http_method $http_uri"\n            # Touch the entry table\n            table lookup -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key\n            after  $static::POLICY_RESULT_POLL_INTERVAL\n\n            set apm_cookie_list             [ ACCESS::user getsid $user_key ]\n            if { [ llength $apm_cookie_list ] != 0 } {\n                set MRHSession_cookie [ ACCESS::user getkey [ lindex $apm_cookie_list 0 ] ]\n                if { $MRHSession_cookie != "" } {\n                    set sid_cache           $MRHSession_cookie\n                    HTTP::cookie insert name MRHSession value $MRHSession_cookie\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX APM Cookie found: $sid_cache"\n                    return\n                }\n            }\n\n            incr try\n        }\n\n        if { $try >  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Policy did not finish in [ expr { $static::POLICY_RESULT_POLL_MAXRETRYCYCLE * $static::POLICY_RESULT_POLL_INTERVAL } ] ms. Close connection for $http_method $http_uri"\n            table delete -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key\n            ACCESS::disable\n            TCP::close\n            return\n        }\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Releasing request $http_method $http_uri"\n\n        unset try\n        unset start_policy_str\n    }\n\n    when ECA_REQUEST_DENIED {\n        set f_ntlm_auth_succeed                 0\n    }\n\n    when HTTP_RESPONSE_RELEASE {\n        if { ! [info exists user_key] } {\n            return\n        }\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP response: status:           [HTTP::status]"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP response: Server:           [HTTP::header Server]"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP response: Content-Length:   [HTTP::header Content-Length]"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP response: WWW-Authenticate: [HTTP::header WWW-Authenticate]"\n    }\n\n    when ACCESS_SESSION_STARTED {\n        if { [ info exists user_key ] } {\n            ACCESS::session data set "session.user.uuid" $user_key\n            ACCESS::session data set "session.user.microsoft-exchange-client" 1\n        }\n    }\n\n    when ACCESS_ACL_ALLOWED {\n        if { [ info exists f_disable_sso ] && $f_disable_sso == 1 } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Disable WEBSSO"\n            WEBSSO::disable\n        }\n    }\n\n    when ACCESS_POLICY_COMPLETED {\n        if { ! [ info exists user_key ] } {\n            return\n        }\n\n        set user_key_value ""\n        set f_delete_session 0\n        set policy_result [ACCESS::policy result]\n        set sid [ ACCESS::session sid ]\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX ACCESS_POLICY_COMPLETED: policy_result = \\"$policy_result\\" user_key = \\"$user_key\\" sid = \\"$sid\\""\n\n        switch $policy_result {\n        "allow" {\n            set user_key_value          $sid\n            set sid_cache               $user_key_value\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Result: Allow: $user_key"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX sid = $sid"\n\n        }\n        "deny" {\n            ACCESS::respond 401 content  $static::actsync_401_http_body Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL Connection Close\n            set f_delete_session  1\n        }\n        default {\n            ACCESS::respond 503 content  $static::actsync_503_http_body Connection Close\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Got unsupported policy result for $user_key ($sid)"\n            set f_delete_session  1\n        }\n        }\n\n        if { $f_ntlm_auth_succeed == 1 } {\n            if { $user_key_value != "" } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Setting $user_key => $static::POLICY_SUCCEED"\n                table set -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key $static::POLICY_SUCCEED\n            } else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Setting $user_key => $static::POLICY_FAILED  $static::POLICY_DONE_WAIT_SEC $static::POLICY_DONE_WAIT_SEC_in table $static::ACCESS_USERKEY_TBLNAME"\n                table set -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key $static::POLICY_FAILED  $static::POLICY_DONE_WAIT_SEC $static::POLICY_DONE_WAIT_SEC\n            }\n        }\n\n        if { $f_delete_session == 1 } {\n            ACCESS::session remove\n            set f_delete_session 0\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Removing the session for $user_key."\n        }\n    }\ndefinition-signature X6dt8EqJFS+8GoWtne8ePfboJR+q5TILymdnfjtylTpC5BikvDFsa3VI6x0V/MP0lJDJrjotJPN2GTogthp48mnmZ2yg+zLskYONNC+vv5yQKc7SLmQf2Eoe8C2CJ8crBUOmfi0f+kjj1GboTVcxNAJ+tpPwb+KKTpnic7WPHo8F/LO5Ou0T5tsls8AmIE/dU0pSKhgit1h5gA+pfKoeA66fhRDcwrSAJ9d/odE55+s/LxJxZqG0PzOVE7HHdbeDiRdRYyBMJQ54Ri/tJuhWQJF/4BYi6V7ScWZQ+fyvFAgb3rRl9xgCqQK3gKQpwLRK11s6+L+PPEQx863YHOEobA==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_APM_ExchangeSupport_helper",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_APM_ExchangeSupport_helper",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_helper?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    # The purpose of this iRule is for help the main virtual for the timing of the HTTP request retry\n    # during the SSO process for OutlookAnywhere protocol request which has a Content-Length value of 1GB.\n\n    when HTTP_REQUEST {\n        #  Waiting for the first chunk of data.\n        HTTP::collect 1\n    }\n\n    when HTTP_REQUEST_DATA {\n        # Respond 401 and close the connection once we received the data.\n        HTTP::respond 401 WWW-Authenticate NTLM Connection close\n    }\ndefinition-signature qJiKrxH5xpBJr4VoBOszXDm+lvsjXtXlGXxiExuAyMkGwnIml1ED3xohHaNWu4/2/AAwX44zX2g3sr1cFx6yQeWIZVrkllxTSSqDqB9BYiLSO1kIn15vzpnj+bqzNTkvcl9fdu6yBT3Bz5X3EfCNLByKa059NQU2l/1StKK0e/KA0cCSAOzB4sh+BVI2VPPgL2R3XqoOrdgHHEE1PnBwC9WRk5Y5XFdaowpd2rfDoYBZM2C+MIxeryxMYLinXHfHbGaug4go8VX67eskI6XxWbm2fjXTBjTjMyxt7OpA6dc6S8IA3FJawUasvexJvHrdPyul2BMGRDqa+p6ZhOLzNw==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_APM_ExchangeSupport_main",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_APM_ExchangeSupport_main",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_main?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    # Global variables\n    # static::POLICY_RESULT_CACHE_AUTHFAILED\n    #     Administrator can set this into 1, when there is a necessity to cache failed policy result.\n    #     This may be needed to avoid account locked caused by the Active Sync device when it uses wrong passwords.\n    #     One possible scenario, is that when the user changes the password in Active Directory, but missed to changed in their devices.\n    # Responses\n    # On denied result\n    #     Administrator can customize the responses to the device depends on more complex conditions when necessary.\n    #     In those cases, please use ACCESS::respond command.\n    #     The following is the syntax of ACCESS::respond\n    #     ACCESS::respond <status code> [ content <body> ] [ <Additional Header> <Additional Header value>* ]\n    #     e.g. ACCESS::respond 401 content "Error: Denied" WWW-Authenticate "basic realm=\\"f5.com\\"" Connection close\n    when RULE_INIT {\n        # Please set the following global variables for customized responses.\n        set static::actsync_401_http_body "<html><title>Authentication Failured</title><body>Error: Authentication Failure</body></html>"\n        set static::actsync_503_http_body "<html><title>Service is not available</title><body>Error: Service is not available</body></html>"\n        set static::ACCESS_LOG_PREFIX                 "01490000:7:"\n\n        # Second Virtual Server name for 401 NTLM responder\n        set static::ACCESS_SECOND_VIRTUAL_NAME        "_ACCESS_401_NTLM_responder_HTTPS"\n\n        set static::POLICY_INPROGRESS                 "policy_inprogress"\n        set static::POLICY_AUTHFAILED                 "policy_authfailed"\n        # The request with huge content length can not be used for starting ACCESS session.\n        # This kind of request will be put on hold, and this iRule will try to use another\n        # request to start the session. The following value is used for Outlook Anywhere.\n        set static::OA_MAGIC_CONTENT_LEN              1073741824\n\n        # Similar with OutlookAnywhere case, ACCESS can not use the request which is\n        # larger then following size. This becomes an issue with application that using\n        # Exchange Web Service as its main protocol such as Mac OS X applications\n        # (e.g. Mail app, Microsoft Entourage, etc)\n        # This kind of request will be put on hold, and this iRule will try to use another\n        # request to start the session.\n        set static::FIRST_BIG_POST_CONTENT_LEN        640000\n\n        # Set it into 1 if the backend EWS handler accepts HTTP Basic Authentication.\n        set static::EWS_BKEND_BASIC_AUTH              0\n        # Set it into 1 if the backend RPC-over-HTTP handler accepts HTTP Basic Authentication.\n        set static::RPC_OVER_HTTP_BKEND_BASIC_AUTH    0\n        # The following variable controls the polling mechanism.\n        set static::POLICY_RESULT_POLL_INTERVAL       250\n        set static::POLICY_RESULT_POLL_MAXRETRYCYCLE  600\n\n        # Set this global variable to 1 for caching authentication failure\n        # Useful for avoiding account locked out.\n        set static::POLICY_RESULT_CACHE_AUTHFAILED    0\n\n        # set this global variable to set alternative timeout for particular session\n        set static::POLICY_ALT_INACTIVITY_TIMEOUT     120\n\n        set static::ACCESS_USERKEY_TBLNAME            "_access_userkey"\n\n\n        set static::ACCESS_DEL_COOKIE_HDR_VAL         "MRHSession=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; path=/"\n\n        log -noname accesscontrol.local1.debug "01490000:7: RPC_OVER_HTTP_BKEND_BASIC_AUTH = $static::RPC_OVER_HTTP_BKEND_BASIC_AUTH"\n        log -noname accesscontrol.local1.debug "01490000:7: EWS_BKEND_BASIC_AUTH = $static::EWS_BKEND_BASIC_AUTH"\n    }\n    when ACCESS_ACL_ALLOWED {\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX [HTTP::method] [HTTP::uri] [HTTP::header Content-Length]"\n\n        if { [ info exists f_rpc_over_http ] && $f_rpc_over_http == 1 }  {\n            if { $static::RPC_OVER_HTTP_BKEND_BASIC_AUTH == 0 } {\n                if { [ info exists f_oa_magic_content_len ] && $f_oa_magic_content_len == 1 } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Use this virtual $static::ACCESS_SECOND_VIRTUAL_NAME just once. Will be reset back after disconnection."\n                    use virtual $static::ACCESS_SECOND_VIRTUAL_NAME\n                }\n               log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Remove HTTP Auth header"\n               HTTP::header remove Authorization\n            }\n        }\n        # MSFT Exchange\'s EWS request handler always requesting NTLM even the connection has been\n        # already authenticated if there is a HTTP Basic Auth in the request.\n        if { [ info exists f_exchange_web_service ] && $f_exchange_web_service  == 1 }  {\n            if { $static::EWS_BKEND_BASIC_AUTH == 0 } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Removing HTTP Basic Authorization header"\n                HTTP::header remove Authorization\n            }\n        }\n    }\n\n    when HTTP_REQUEST {\n        set http_path                       [ string tolower [HTTP::path] ]\n        set f_clientless_mode               0\n        set f_alt_inactivity_timeout        0\n        set f_rpc_over_http                 0\n        set f_exchange_web_service          0\n        set f_auto_discover                 0\n        set f_activesync                    0\n        set f_offline_address_book          0\n        set f_availability_service          0\n\n        #  Here put appropriate pool when necessary.\n        switch -glob $http_path {\n        "/rpc/rpcproxy.dll" {\n            # Supports for RPC over HTTP. (Outlook Anywhere)\n            set f_rpc_over_http 1\n        }\n        "/autodiscover/autodiscover.xml" {\n            # Supports for Auto Discover protocol.\n            set f_auto_discover 1\n            # This request does not require long inactivity timeout.\n            # Don\'t use this for now\n            set f_alt_inactivity_timeout 0\n        }\n        "/microsoft-server-activesync" {\n            # Supports for ActiveSync\n            set f_activesync 1\n        }\n        "/oab/*" {\n            # Supports for Offline Address Book\n            set f_offline_address_book 1\n        }\n        "/ews/*" {\n            # Support for Exchange Web Service\n            # Outlook\'s Availability Service borrows this protocol.\n            set f_exchange_web_service 1\n        }\n        "/as/*" {\n            # Support for Availability Service.\n            # do nothing for now. (Untested)\n            set f_availability_service 1\n        }\n        default {\n            return\n        }\n        }\n\n        set f_reqside_set_sess_id           0\n        set http_method                     [HTTP::method]\n        set http_hdr_host                   [HTTP::host]\n        set http_hdr_uagent                 [HTTP::header User-Agent]\n        set src_ip                          [IP::remote_addr]\n        set http_uri                        [HTTP::uri]\n        set http_content_len                [HTTP::header Content-Length]\n        set MRHSession_cookie               [HTTP::cookie value MRHSession]\n        set auth_info_b64enc                ""\n\n        if { ! [ info exists PROFILE_POLICY_TIMEOUT ] } {\n            set PROFILE_POLICY_TIMEOUT            [PROFILE::access access_policy_timeout]\n        }\n        if { ! [ info exists PROFILE_MAX_SESS_TIMEOUT ] } {\n            set PROFILE_MAX_SESS_TIMEOUT          [PROFILE::access max_session_timeout]\n        }\n        if { ! [ info exists PROFILE_RESTRICT_SINGLE_IP ] } {\n            set PROFILE_RESTRICT_SINGLE_IP        1\n        }\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX method: $http_method"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Src IP: $src_ip"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX User-Agent: $http_hdr_uagent"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP uri: $http_uri"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP len: $http_content_len"\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Restrict-to-single-client-ip: $PROFILE_RESTRICT_SINGLE_IP"\n\n        # First, do we have valid MRHSession cookie.\n        if { $MRHSession_cookie != "" } {\n            if { [ACCESS::session exists -state_allow -sid $MRHSession_cookie] } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *VALID* MRHSession cookie: $MRHSession_cookie"\n            } else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *INVALID* MRHSession cookie: $MRHSession_cookie"\n                set MRHSession_cookie ""\n                HTTP::cookie remove MRHSession\n            }\n        }\n\n        set http_hdr_auth [HTTP::header Authorization]\n        if { [ string match -nocase {basic *} $http_hdr_auth ] != 1 } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Not basic authentication. Ignore received auth header"\n            set http_hdr_auth ""\n        }\n\n        if { $http_hdr_auth == "" } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX No/Empty Auth header"\n            # clean up the cookie\n            if { $MRHSession_cookie == "" } {\n                HTTP::respond 401 content  $static::actsync_401_http_body WWW-Authenticate "Basic realm=\\"[HTTP::header Host]\\"" Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL Connection close\n                return\n            }\n            # Do nothing if we have a valid MRHSession cookie.\n        }\n\n        set f_release_request           0\n        # Optimization for clients which support cookie\n        if { $MRHSession_cookie != "" } {\n            # Default profile access setting is false\n            if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n                set f_release_request 1\n            }\n            elseif { [ IP::addr $src_ip equals [ ACCESS::session data get -sid $MRHSession_cookie "session.user.clientip" ] ] } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP matched"\n                set f_release_request 1\n            }\n            else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP does not matched"\n                set MRHSession_cookie ""\n                HTTP::cookie remove MRHSession\n            }\n        }\n\n        if { $f_release_request == 0 } {\n            set apm_username [ string tolower [HTTP::username]]\n            set apm_password [HTTP::password]\n            if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n                binary scan [md5 "$apm_password"] H* user_hash\n            } else {\n                binary scan [md5 "$apm_password$src_ip"] H* user_hash\n            }\n\n            set user_key    {}\n            append user_key $apm_username "." $user_hash\n            unset user_hash\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP Hdr Auth: $http_hdr_auth"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX apm_username: $apm_username"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX user_key = $user_key"\n            set apm_cookie_list             [ ACCESS::user getsid $user_key ]\n            if { [ llength $apm_cookie_list ] != 0 } {\n                set apm_cookie [ ACCESS::user getkey [ lindex $apm_cookie_list 0 ] ]\n                if { $apm_cookie != "" } {\n                    HTTP::cookie insert name MRHSession value $apm_cookie\n                    set f_release_request 1\n                }\n            }\n        }\n\n        if { $http_content_len ==  $static::OA_MAGIC_CONTENT_LEN } {\n            set f_oa_magic_content_len 1\n        }\n\n        set f_sleep_here 0\n        set retry 1\n\n        while { $f_release_request == 0 && $retry <=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } {\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Trying #$retry for $http_method $http_uri $http_content_len"\n\n            # This is also going to touch the table entry timer.\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Reading $user_key from table $static::ACCESS_USERKEY_TBLNAME"\n\n            set apm_cookie [table lookup -subtable  $static::ACCESS_USERKEY_TBLNAME -notouch $user_key]\n            if { $apm_cookie != "" } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Verifying table cookie = $apm_cookie"\n\n                # Accessing SessionDB is not that cheap. Here we are trying to check known value.\n                if { $apm_cookie == "policy_authfailed" || $apm_cookie == "policy_inprogress"} {\n                    # Do nothing\n                } elseif  { ! [ ACCESS::session exists $apm_cookie ] } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX table cookie = $apm_cookie is out-of-sync"\n                    # Table value is out of sync. Ignores it.\n                    set apm_cookie ""\n                }\n            }\n\n            switch $apm_cookie {\n            "" {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX NO APM Cookie found"\n\n                if { [ info exists f_oa_magic_content_len ] && $f_oa_magic_content_len == 1 } {\n                    # Outlook Anywhere request comes in pair. The one with 1G payload is not usable\n                    # for creating new session since 1G content-length is intended for client to upload\n                    # the data when needed.\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Start to wait $static::POLICY_RESULT_POLL_INTERVAL ms for request with magic content-len"\n                    set f_sleep_here 1\n                } elseif { [ info exists f_exchange_web_service ] && $f_exchange_web_service == 1 && $http_content_len > $static::FIRST_BIG_POST_CONTENT_LEN } {\n                    # Here we are getting large EWS request, which can\'t be used for starting new session\n                    # in clientless-mode. Have it here waiting for next smaller one.\n                    # We are holding the request here in HTTP filter, and HTTP filter automatically\n                    # clamping down the TCP window when necessary.\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Start to wait $static::POLICY_RESULT_POLL_INTERVAL ms for big EWS request"\n                    set f_sleep_here 1\n                } else {\n                   set apm_cookie               "policy_inprogress"\n                   set f_reqside_set_sess_id    1\n                   set f_release_request        1\n                }\n            }\n            "policy_authfailed" {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Found $user_key with AUTH_FAILED"\n                HTTP::respond 401 content  $static::actsync_401_http_body\n                set f_release_request 1\n            }\n            "policy_inprogress" {\n                if { [ info exists f_activesync ] && ($f_activesync == 1) } {\n                    # For ActiveSync requests, aggressively starts new session.\n                    set f_reqside_set_sess_id    1\n                    set f_release_request        1\n                } else {\n                    set f_sleep_here 1\n                }\n            }\n            default {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Using MRHSession = $apm_cookie"\n                HTTP::header insert Cookie "MRHSession=$apm_cookie"\n                set f_release_request 1\n            }\n            }\n\n            if { $f_reqside_set_sess_id == 1 } {\n                set f_reqside_set_sess_id 0\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Setting $user_key=$apm_cookie $PROFILE_POLICY_TIMEOUT $PROFILE_MAX_SESS_TIMEOUT"\n                set f_clientless_mode 1\n                HTTP::cookie remove MRHSession\n                HTTP::header insert "clientless-mode" 1\n                HTTP::header insert "username" $apm_username\n                HTTP::header insert "password" $apm_password\n                table set -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key $apm_cookie $PROFILE_POLICY_TIMEOUT $PROFILE_MAX_SESS_TIMEOUT\n            }\n\n            if { $f_sleep_here == 1 } {\n                set f_sleep_here 0\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Waiting  $static::POLICY_RESULT_POLL_INTERVAL ms for $http_method $http_uri"\n                after  $static::POLICY_RESULT_POLL_INTERVAL\n            }\n\n            incr retry\n        }\n\n        if { $f_release_request == 0 && $retry >=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Policy did not finish in [expr { $static::POLICY_RESULT_POLL_MAXRETRYCYCLE * $static::POLICY_RESULT_POLL_INTERVAL } ] ms. Close connection for $http_method $http_uri"\n\n            table delete -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key\n            ACCESS::disable\n            TCP::close\n            return\n        }\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Releasing request $http_method $http_uri"\n    }\n\n    when ACCESS_SESSION_STARTED {\n        if { [ info exists user_key ] } {\n            ACCESS::session data set "session.user.uuid" $user_key\n            ACCESS::session data set "session.user.microsoft-exchange-client" 1\n\n            if { [ info exists f_activesync ] && $f_activesync == 1 } {\n                ACCESS::session data set "session.user.microsoft-activesync" 1\n            }\n            elseif { [ info exists f_auto_discover ] && $f_auto_discover == 1 } {\n                ACCESS::session data set "session.user.microsoft-autodiscover" 1\n            }\n            elseif { [ info exists f_availability_service ] && $f_availability_service == 1 } {\n                ACCESS::session data set "session.user.microsoft-availabilityservice" 1\n            }\n            elseif { [ info exists f_rpc_over_http ] && $f_rpc_over_http == 1 } {\n                ACCESS::session data set "session.user.microsoft-rpcoverhttp" 1\n            }\n            elseif { [ info exists f_offline_address_book ] && $f_offline_address_book == 1 } {\n                ACCESS::session data set "session.user.microsoft-offlineaddressbook" 1\n            }\n            elseif { [ info exists f_exchange_web_service ] && $f_exchange_web_service == 1 } {\n                ACCESS::session data set "session.user.microsoft-exchangewebservice" 1\n            }\n        }\n        if { [ info exists f_alt_inactivity_timeout ] && $f_alt_inactivity_timeout == 1 } {\n            ACCESS::session data set "session.inactivity_timeout"  $static::POLICY_ALT_INACTIVITY_TIMEOUT\n        }\n    }\n\n    when HTTP_RESPONSE {\n        if { [ info exists f_auto_discover ] && $f_auto_discover == 1 } {\n            set content_len [ HTTP::header Content-Length ]\n            if {  $content_len > 0 } {\n                HTTP::collect $content_len\n            }\n        }\n    }\n    when HTTP_RESPONSE_DATA {\n        if { [ info exists f_auto_discover ] && $f_auto_discover == 1 } {\n            if { [ regsub -line {<AuthPackage>Ntlm</AuthPackage>} [ HTTP::payload ] {<AuthPackage>Basic</AuthPackage>} payload ] != 0 } {\n                HTTP::payload replace 0 $content_len $payload\n            }\n        }\n    }\n    when ACCESS_POLICY_COMPLETED {\n        if { ! [ info exists user_key ] } {\n            return\n        }\n\n        set user_key_value ""\n        set f_delete_session 0\n        set policy_result [ACCESS::policy result]\n        set sid [ ACCESS::session sid ]\n\n        log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX ACCESS_POLICY_COMPLETED: policy_result = \\"$policy_result\\" user_key = \\"$user_key\\" sid = \\"$sid\\""\n\n        set inactivity_timeout [ACCESS::session data get "session.inactivity_timeout"]\n        set max_sess_timeout [ACCESS::session data get "session.max_session_timeout"]\n        if { $max_sess_timeout == "" } {\n             set max_sess_timeout $PROFILE_MAX_SESS_TIMEOUT\n        }\n\n        switch $policy_result {\n        "allow" {\n            # We depends on this table record self-cleanup capability in order to\n            # indirectly sync with session DB.\n            set user_key_value $sid\n\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Result: Allow: $user_key => $sid $inactivity_timeout $max_sess_timeout"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX user_key_value = $user_key_value"\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX sid = $sid"\n        }\n        "deny" {\n            # When necessary the admin here can check appropriate session variable\n            # and decide what response more appropriate then this default response.\n            ACCESS::respond 401 content  $static::actsync_401_http_body Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL Connection close\n            if {  $static::POLICY_RESULT_CACHE_AUTHFAILED == 1 } {\n                set user_key_value  $static::POLICY_AUTHFAILED\n            } else {\n                set f_delete_session  1\n            }\n        }\n        default {\n            ACCESS::respond 503 content  $static::actsync_503_http_body Connection close\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Got unsupported policy result for $user_key ($sid)"\n            set f_delete_session  1\n        }\n        }\n        if { $user_key_value != "" } {\n           log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Setting $user_key => $user_key_value $inactivity_timeout $max_sess_timeout in table $static::ACCESS_USERKEY_TBLNAME"\n\n           table set -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key $user_key_value $inactivity_timeout $max_sess_timeout\n        } else {\n           log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Deleting $user_key in table $static::ACCESS_USERKEY_TBLNAME"\n\n           table delete -subtable  $static::ACCESS_USERKEY_TBLNAME $user_key\n        }\n\n        if { $f_delete_session == 1 } {\n           ACCESS::session remove\n           set f_delete_session 0\n           log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Removing the session for $user_key."\n        }\n    }\ndefinition-signature ITBkr3SVPYk5UZu6F9TDEQuWGp64htd0HDsL3WNUHQqaVbu0m1tox3dTyf9X8y1MSr2KIbUfOIovCbiSXqnWRTAnSMqESm2gwlMBNCBOxTsh3AD83JE2N08jZjnC/jjnl4HRsq71uBbyHLZiL+mp1wXDtxUBUOfh7G/NUs9BajAVgQM7Vx9/Ogs+zX6ag08CXOjWwgPL5hRezZJwZEp1AXM8YrSbyT456P6axwWsB015wqJXvwpRKWcQ7sHEvkbbd928Q3koLevE6ecByjezjphomokwmi813aA7WCNbG6Tl+3YznsYAgxn2Skv0Gq7pMfoj9QFt/a39RXGyHOhRcQ==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_APM_MS_Office_OFBA_Support",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_APM_MS_Office_OFBA_Support",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_MS_Office_OFBA_Support?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012, 2016-2017.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n# Supporting MS-OFBA protocol for native office applications.\n# sys_APM_MS_Office_OFBA_DG - iRule data group to customize ofba user agent strings and\n#                     few other parameters.\n#\n# sys_APM_MS_Office_OFBA_DG::useragent - useragent strings are mandatory, \n#       these strings are used to detect OFBA clients. All user agent strings should start\n#       with useragent name, for e.g: useragent1, useragent2.. etc.\n#\n# sys_APM_MS_Office_OFBA_DG::ie_sp_session_sharing_enabled - Parameter to specify whether to enable or\n#       disable IE session sharing using persistent cookie named "MRHSOffice".\n#       Default is disabled (0), value can be 0 or 1\n#     \n# sys_APM_MS_Office_OFBA_DG::ie_sp_session_sharing_inactivity_timeout - inactivity timeout value \n#       for the persistent cookie value "MRHSOffice"\n#       everytime, the SharePoint site refreshes or gets any response from\n#       SharePoint Server.  Value can be any positive value given in seconds.\n#       Default value as 60 secs\n#\n# sys_APM_MS_Office_OFBA_DG::ofba_auth_dialog_size - OFBA dialog browser\n#       resolution size given as widthxheight, default 800x600\n#\n# static::MS_OFBA_ENABLED_CLIENT_TYPE - "ms-ofba-compliant" session variable\n#       value that can be used in Access policy Logon agent branch, to add the required authentication\n#       for MS OFBA compliant applications.\n#\n    proc write_log {level message} {\n\n        ACCESS::log $level "\\[MSOFBA\\] $message"\n#       Logs printing for 12.x or older releases\n#       log -noname accesscontrol.local1.$level "01490000: \\[MSOFBA\\] $message"\n    }\n\n    proc is_ofba_passthrough_uri {uri} {\n        for { set i 0 } { $i < [llength $static::MS_OFBA_PASSTHROUGH_URI_LIST] } { incr i } {\n            if { $uri == [lindex $static::MS_OFBA_PASSTHROUGH_URI_LIST $i] } {\n                return 1;\n            }\n        }\n        return 0\n    }\n\n    when RULE_INIT {\n        set static::MS_OFBA_ENABLED_CLIENT_TYPE "ms-ofba-compliant"\n        set static::MS_OFBA_AUTH_REQ_URI "/ms-ofba-req-auth"\n        set static::MS_OFBA_AUTH_RETURN_URI "/ms-ofba-auth-success"\n        set static::MS_OFBA_AUTH_DIALOG_SZ "800x600"\n        set static::MS_OFBA_AUTH_SUCCESS_BODY "<html><head><title>User Authenticated</title></head><body><b>Successful OFBA authentication</b></body></html>"\n        set static::MS_OFBA_IRULE_DG "sys_APM_MS_Office_OFBA_DG"\n        set static::MULTI_DOMAIN_AUTH_RESP_URI "/f5networks-sso-resp"\n        set static::MS_OFBA_PASSTHROUGH_URI_LIST {$static::MULTI_DOMAIN_AUTH_RESP_URI "/my.status.eps" "/my.report.eps"}\n# sp_persistent_ck: would help to share the session from sharepoint site to\n# office applications, if enabled.\n        set static::SP_PERSISTENT_CK "MRHSOffice"\n        set static::SP_PERSISTENT_CK_TIMEOUT 60\n        set static::MS_OFBA_AUTH_TYPE_COOKIE "Auth-Type"\n        set static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE "ms-ofba"\n    }\n\n    when CLIENT_ACCEPTED {\n        if { ![info exists ofba_user_agent_list] } {\n# check for config change from datagroup\n# since this iRule is read-only, dg config change is done in CLIENT_ACCEPTED rather than in RULE_INIT\n            set ofba_user_agent_list [class search -value -all $static::MS_OFBA_IRULE_DG starts_with useragent]\n            set f_sp_persistent_ck [class search -value $static::MS_OFBA_IRULE_DG equals ie_sp_session_sharing_enabled]\n            set sp_persistent_ck_timeout [class search -value $static::MS_OFBA_IRULE_DG equals ie_sp_session_sharing_inactivity_timeout]\n            set ofba_auth_dialog_sz [class search -value $static::MS_OFBA_IRULE_DG equals ofba_auth_dialog_size]\n        }\n    }\n\n    when HTTP_REQUEST {\n# client detection, for ofba client\n        set ms_sp_client_type "none"\n        set http_path [string tolower [HTTP::path]]\n        set http_user_agent [string tolower [HTTP::header "User-Agent"]]\n        set session_id [HTTP::cookie value "MRHSession"]\n        set f_allow_session 0\n        set ms_ofba_auth_cookie ""\n\n        if {[HTTP::header exists "X-FORMS_BASED_AUTH_ACCEPTED"] &&\n            (([HTTP::header "X-FORMS_BASED_AUTH_ACCEPTED"] equals "t") ||\n             ([HTTP::header "X-FORMS_BASED_AUTH_ACCEPTED"] equals "f"))} {\n                set ms_sp_client_type "ms-ofba"\n            } elseif { $http_path == $static::MS_OFBA_AUTH_REQ_URI } {\n                set ms_sp_client_type "ms-ofba"\n            } else {\n                if {(!($http_user_agent contains "frontpage") && [string match -nocase {*mozilla*} $http_user_agent]) ||\n                    [string match -nocase {*opera*} $http_user_agent]} {\n                        set ms_sp_client_type "browser"\n                        set ms_ofba_auth_cookie [HTTP::cookie value $static::MS_OFBA_AUTH_TYPE_COOKIE]\n                        if { $ms_ofba_auth_cookie == $static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE } {\n                            # ofba authentication is still in progress, there may be a case where initial\n                            # access denied and user is retrying the session without closing the ofba\n                            # initiated browser\n                            set ms_sp_client_type "ms-ofba"\n                            call write_log debug "Detecting the client type as ms-ofba based auth type cookie"\n                        }\n                    } else {\n                        foreach ofba_user_agent $ofba_user_agent_list {\n                            set ofba_user_agent [string trim $ofba_user_agent]\n                            if { $ofba_user_agent != "" && [string match -nocase *$ofba_user_agent* $http_user_agent] } {\n                                set ms_sp_client_type "ms-ofba"\n                                    break\n                            }\n                        }\n                    }\n            }\n\n        if { $ms_sp_client_type == "ms-ofba" } {\n            call write_log debug "Client-type: (ms-ofba-compliant), http path: ($http_path), user agent: ($http_user_agent)"\n        }\n\n        if { $ms_sp_client_type != "ms-ofba" } {\n            return\n        } elseif { $session_id != "" } {\n            if { [ACCESS::session exists -state_allow $session_id] } {\n                set f_allow_session 1\n                return\n            }\n        } elseif { $f_sp_persistent_ck == "1" && [HTTP::cookie exists $static::SP_PERSISTENT_CK] } {\n            set sp_persistent_ck_value [HTTP::cookie value $static::SP_PERSISTENT_CK]\n            if { $sp_persistent_ck_value != "" && [ACCESS::session exists -state_allow $sp_persistent_ck_value] } {\n                if {not ([catch {HTTP::cookie insert name "MRHSession" value $sp_persistent_ck_value}]) } {\n                    call write_log debug "Restored persistent cookie for sid: ($sp_persistent_ck_value)"\n                    set f_allow_session 1\n                    return\n                } else {\n                    call write_log error "Restoring persistent cookie failed for sid: ($sp_persistent_ck_value)"\n                    unset sp_persistent_ck_value\n                }\n            } else {\n                unset sp_persistent_ck_value\n            }\n        }\n\n        if { !($f_allow_session) && $http_path != $static::MS_OFBA_AUTH_REQ_URI } {\n            if { $ms_ofba_auth_cookie == $static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE } {\n                if { ![call is_ofba_passthrough_uri $http_path]  } {\n                    call write_log debug "Redirecting for MS OFBA, based on auth type"\n                    HTTP::respond 302 -version 1.1 -noserver Location $static::MS_OFBA_AUTH_REQ_URI\n                }\n            } else {\n                call write_log debug "Responding 403 for MS OFBA initiation"\n                if {$ofba_auth_dialog_sz == ""} {\n                    set ofba_auth_dialog_sz $static::MS_OFBA_AUTH_DIALOG_SZ\n                }\n                HTTP::respond 403 -version "1.1" noserver \\\n                    "X-FORMS_BASED_AUTH_REQUIRED" "https://[HTTP::host]$static::MS_OFBA_AUTH_REQ_URI" \\\n                    "X-FORMS_BASED_AUTH_RETURN_URL" "https://[HTTP::host]$static::MS_OFBA_AUTH_RETURN_URI" \\\n                    "X-FORMS_BASED_AUTH_DIALOG_SIZE" $ofba_auth_dialog_sz \\\n                    "Set-Cookie" "MRHSession=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;secure" \\\n                    "Set-Cookie" "LastMRH_Session=deleted; expires=Thu, 01 Jan 1970 00:00:00 GMT;path=/;secure" \\\n                    "Set-Cookie" "$static::MS_OFBA_AUTH_TYPE_COOKIE=$static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE;path=/;secure;HttpOnly" \\\n                    "Connection" "Close"\n            }\n        }\n    }\n\n    when HTTP_RESPONSE {\n        if { $f_sp_persistent_ck == "1" && ([info exists ms_sp_client_type] && $ms_sp_client_type == "browser") && $session_id != ""} {\n            if {$sp_persistent_ck_timeout == ""} {\n                set sp_persistent_ck_timeout $static::SP_PERSISTENT_CK_TIMEOUT\n            }\n            call write_log debug "Set-Cookie for SharePoint persistent cookie: ($static::SP_PERSISTENT_CK) for sid: ($session_id), having timeout: ($sp_persistent_ck_timeout)"\n\n            HTTP::cookie remove $static::SP_PERSISTENT_CK\n            HTTP::cookie insert name $static::SP_PERSISTENT_CK value $session_id path "/"\n            HTTP::cookie expires $static::SP_PERSISTENT_CK $sp_persistent_ck_timeout relative\n            HTTP::cookie secure $static::SP_PERSISTENT_CK enable\n            HTTP::cookie httponly $static::SP_PERSISTENT_CK enable\n\n        } elseif { [info exists sp_persistent_ck_value] && $sp_persistent_ck_value ne "" } {\n            call write_log debug "Restoring Cookie for MRHSession from persistent cookie: ($sp_persistent_ck_value)"\n\n            HTTP::cookie insert name MRHSession value $sp_persistent_ck_value path "/"\n            HTTP::cookie secure MRHSession enable\n            unset sp_persistent_ck_value\n        }\n    }\n\n    when ACCESS_SESSION_STARTED {\n        if { ![info exists ms_sp_client_type] || $ms_sp_client_type != "ms-ofba"} {\n            return\n        }\n        ACCESS::session data set session.client.type $static::MS_OFBA_ENABLED_CLIENT_TYPE\n    }\n\n    when ACCESS_ACL_ALLOWED {\n        switch -glob -- [string tolower [HTTP::path]] $static::MS_OFBA_AUTH_REQ_URI {\n            ACCESS::respond 302 noserver Location "https://[HTTP::host]$static::MS_OFBA_AUTH_RETURN_URI"\n        } $static::MS_OFBA_AUTH_RETURN_URI {\n            ACCESS::respond 200 content $static::MS_OFBA_AUTH_SUCCESS_BODY noserver \\\n                "Set-Cookie" "$static::MS_OFBA_AUTH_TYPE_COOKIE=deleted;expires=Thu, 01 Jan 1970 00:00:00 GMT;;path=/;secure;HttpOnly"\n        } "*/signout.aspx" {\n            ACCESS::respond 302 noserver Location "/vdesk/hangup.php3"\n                return\n        } "/_layouts/accessdenied.aspx" {\n            if {[string tolower [URI::query [HTTP::uri] loginasanotheruser]] equals "true" } {\n                ACCESS::session remove\n                ACCESS::respond 302 noserver Location "/"\n                return\n            }\n        } default {\n        }\n    }\ndefinition-signature e637kI9h5Ix7GFOay3azJpy0f7omhsLIP4EQQgdAxYzNVqFFpHpDlig4J/vuG/QbYUg5i0VDCnKNeL6FGQhMtIT6BNW9ucPGv46CKuS4UHxffnFGETafdGXnQg9j3RZGakjHZAwJmaQ0jLaXVG0tGo7e2P7lS6SC192xI8VqAkihMQCS7DaWDWuqYUeULk4YIPb8nGyw+3ZKCPTkOCqxWS4v2zMEhtCA7A9AzJAH2kg8o6HiEjEEt+PI6BclKOxyONdGkskEFBjqp1GZAlfRkcHbeFvgvXMa9ODZSzFHtT6rV+YsqmGfd4KHk5azrTCfhitvfU2miAD4M2/rHD1y/Q==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_APM_Office365_SAML_BasicAuth",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_APM_Office365_SAML_BasicAuth",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_Office365_SAML_BasicAuth?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when RULE_INIT {\n        set static::ACCESS_LOG_ECP_PREFIX       "014d0002:7: ECP client"\n    }\n    when HTTP_REQUEST {\n        set http_path            [string tolower [HTTP::path]]\n        set http_hdr_auth        [HTTP::header Authorization]\n        set http_hdr_client_app  [HTTP::header X-MS-Client-Application]\n        set http_hdr_client_ip   [HTTP::header X-MS-Forwarded-Client-IP]\n        set MRHSession_cookie    [HTTP::cookie value MRHSession]\n\n        if { ($http_path == "/saml/idp/profile/redirectorpost/sso") &&\n             ($http_hdr_client_app != "") &&\n             ($http_hdr_client_app contains "Microsoft.Exchange") } {\n            HTTP::uri "/saml/idp/profile/ecp/sso"\n        } elseif { ($http_path != "/saml/idp/profile/ecp/sso")  } {\n            return\n        }\n        set f_saml_ecp_request 1\n        unset http_path\n\n        # If MRHSession cookie from client is present, skip further processing.\n        if { $MRHSession_cookie != "" } {\n            if { [ACCESS::session exists -state_allow -sid $MRHSession_cookie] } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_ECP_PREFIX HTTP *VALID* MRHSession cookie: $MRHSession_cookie"\n            } else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_ECP_PREFIX HTTP *INVALID* MRHSession cookie: $MRHSession_cookie"\n            }\n            return\n        }\n\n        if { ($http_hdr_client_app != "") &&\n            ($http_hdr_client_app contains "Microsoft.Exchange") &&\n            ($http_hdr_client_ip != "") } {\n\t    set src_ip $http_hdr_client_ip\n\t}\n        unset http_hdr_client_app\n        unset http_hdr_client_ip\n\n        if { ! [ info exists src_ip ] } {\n            set src_ip          [IP::remote_addr]\n        }\n\n        # Only allow HTTP Basic Authentication.\n        if { ($http_hdr_auth == "") || ([ string match -nocase {basic *} $http_hdr_auth ] != 1 ) } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_ECP_PREFIX ECP request does not contain HTTP Basic Authorization header."\n            unset http_hdr_auth\n            return\n        }\n\n        set apm_username        [ string tolower [HTTP::username] ]\n        set apm_password        [HTTP::password]\n\n        binary scan [md5 "$apm_password$src_ip"] H* user_hash\n        set user_key {}\n        append user_key $apm_username "." $user_hash\n        unset user_hash\n\n        set apm_cookie_list             [ ACCESS::user getsid $user_key ]\n        if { [ llength $apm_cookie_list ] != 0 } {\n            set apm_cookie [ ACCESS::user getkey [ lindex $apm_cookie_list 0 ] ]\n            if { $apm_cookie != "" } {\n                HTTP::cookie insert name MRHSession value $apm_cookie\n            }\n        }\n\n        HTTP::header insert "clientless-mode" 1\n        HTTP::header insert "username" $apm_username\n        HTTP::header insert "password" $apm_password\n        unset apm_username\n        unset apm_password\n        unset http_hdr_auth\n    }\n\n    when ACCESS_SESSION_STARTED {\n        if { [ info exists f_saml_ecp_request ] && $f_saml_ecp_request == 1 } {\n            if { [ info exists user_key ] } {\n                ACCESS::session data set "session.user.uuid" $user_key\n            }\n            if { [ info exists  src_ip ] } {\n                ACCESS::session data set "session.user.clientip" $src_ip\n            }\n        }\n    }\n\n    when HTTP_RESPONSE {\n        if { [ info exists f_saml_ecp_request ] && $f_saml_ecp_request == 1 } {\n            unset f_saml_ecp_request\n            unset apm_cookie\n        }\n    }\ndefinition-signature lbhM9rFH3R+uo+pp4DWotUdvGbvFhCBhe5aZKgpRZdl5k39X50MrrIhz2UkjY1VV2JORwPaSpdyN6mVY0cJccFdLjGgaNCtNuMoT2grlOE7F9Zw73imFGbu8UiqmZT0ZLcNXCglZplp08o9O9xn7UNJ5E/gYWrjCI2QaebwGu1NMSLK+/WjGHNKr28xN2Cwo0rk9hg+6fC9YxzlGVoRlxPuYRelygqD0bAQKTux4tuTQPF/4CDNpttyVX72ULJpZUINwW1UeCZoosB1O4XubT9PaqEl53ioom8LcGZEn5vKOH+TlvKXjPi5kV1ci2d+fjCf7ZoOW6EVyEEc2aL2cWw==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_APM_activesync",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_APM_activesync",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_activesync?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when RULE_INIT {\n        set static::actsync_401_http_body   "<html><title>Authentication Failed</title><body>Error: Authentication Failure</body></html>"\n        set static::actsync_503_http_body   "<html><title>Service is not available</title><body>Error: Service is not available</body></html>"\n        set static::ACCESS_LOG_PREFIX       "01490000:7:"\n    }\n    when HTTP_REQUEST {\n        set http_path                       [string tolower [HTTP::path]]\n        set f_clientless_mode               0\n\n        if { $http_path == "/microsoft-server-activesync" } {\n        }\n        elseif { $http_path == "/autodiscover/autodiscover.xml" } {\n            set f_auto_discover 1\n        }\n        else return\n\n        if { ! [ info exists src_ip ] } {\n            set src_ip                            [IP::remote_addr]\n        }\n        if { ! [ info exists PROFILE_RESTRICT_SINGLE_IP ] } {\n            set PROFILE_RESTRICT_SINGLE_IP  \t  1\n        }\n        # Only allow HTTP Basic Authentication.\n        set auth_info_b64enc                ""\n        set http_hdr_auth                   [HTTP::header Authorization]\n        regexp -nocase {Basic (.*)} $http_hdr_auth match auth_info_b64enc\n        if { $auth_info_b64enc == "" } {\n            set http_hdr_auth ""\n        }\n\n        if { $http_hdr_auth == "" } {\n            log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX Empty/invalid HTTP Basic Authorization header"\n            HTTP::respond 401 content $static::actsync_401_http_body Connection close\n            return\n        }\n\n        set MRHSession_cookie               [HTTP::cookie value MRHSession]\n        # Do we have valid MRHSession cookie.\n        if { $MRHSession_cookie != "" } {\n            if { [ACCESS::session exists -state_allow -sid $MRHSession_cookie] } {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *VALID* MRHSession cookie: $MRHSession_cookie"\n                # Default profile access setting is false\n                if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n                    return\n                }\n                elseif { [ IP::addr $src_ip equals [ ACCESS::session data get -sid $MRHSession_cookie "session.user.clientip" ] ] } {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP matched"\n                    return\n                }\n                else {\n                    log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX source IP does not matched"\n                }\n            }\n            else {\n                log -noname accesscontrol.local1.debug "$static::ACCESS_LOG_PREFIX HTTP *INVALID* MRHSession cookie: $MRHSession_cookie"\n            }\n            set MRHSession_cookie ""\n            HTTP::cookie remove MRHSession\n        }\n\n        set apm_username                    [ string tolower [HTTP::username] ]\n        set apm_password                    [HTTP::password]\n\n        if { $PROFILE_RESTRICT_SINGLE_IP == 0 } {\n            binary scan [md5 "$apm_password$"] H* user_hash\n        } else {\n            binary scan [md5 "$apm_password$src_ip"] H* user_hash\n        }\n        set user_key {}\n        append user_key $apm_username "." $user_hash\n        unset user_hash\n\n        set f_insert_clientless_mode    0\n        set apm_cookie_list             [ ACCESS::user getsid $user_key ]\n        if { [ llength $apm_cookie_list ] != 0 } {\n            set apm_cookie [ ACCESS::user getkey [ lindex $apm_cookie_list 0 ] ]\n            if { $apm_cookie != "" } {\n                HTTP::cookie insert name MRHSession value $apm_cookie\n            } else {\n                set f_insert_clientless_mode 1\n            }\n        } else {\n            set f_insert_clientless_mode 1\n        }\n\n        if { $f_insert_clientless_mode == 1 } {\n            HTTP::header insert "clientless-mode" 1\n            HTTP::header insert "username" $apm_username\n            HTTP::header insert "password" $apm_password\n        }\n        unset f_insert_clientless_mode\n    }\n    when ACCESS_SESSION_STARTED {\n        if { [ info exists user_key ] } {\n            ACCESS::session data set "session.user.uuid" $user_key\n            ACCESS::session data set "session.user.microsoft-exchange-client" 1\n            ACCESS::session data set "session.user.activesync" 1\n            if { [ info exists f_auto_discover ] && $f_auto_discover == 1 } {\n                set f_auto_discover 0\n                ACCESS::session data set "session.user.microsoft-autodiscover" 1\n            }\n        }\n    }\n    when ACCESS_POLICY_COMPLETED {\n        if { ! [ info exists user_key ] } {\n            return\n        }\n\n        set policy_result [ACCESS::policy result]\n        switch $policy_result {\n        "allow" {\n        }\n        "deny" {\n            ACCESS::respond 401 content $static::actsync_401_http_body Connection close\n            ACCESS::session remove\n        }\n        default {\n            ACCESS::respond 503 content $static::actsync_503_http_body Connection close\n            ACCESS::session remove\n        }\n        }\n\n        unset user_key\n    }\ndefinition-signature d3ZoP7HHzJwjxIV+zgaF0J7nh0d0e3rlE5srbLvvZXOW9mSQ4VzalGLunwQMl6rths50p6zwETao3banbrWCnI+HEBKtDy61/wFJJ3UJ6RHWPSFSFQhcJMOY4WIdSRuu0VwTlMn6vte42xe2UmTWeB7tSs/STKoOQrDy0U7c34AAG9gSRaikPJz/hi/McWRIxX4LtS+gecwXX1KXM3lB7dz1kvOYOid9h1tsmUtftpB/neqmReMch3gaWrL7ZYcEECCcHEhyW6B7hqT91r5a9VG4nlq8oQ5MLa07zwVT5HV2id5lgIfhpPSzXUJbe3SJ7wN5TThtaWhBgDIHp+CYJA==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_auth_krbdelegate",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_auth_krbdelegate",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_krbdelegate?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when HTTP_REQUEST {\n        set thecert ""\n        set ckname F5KRBAUTH\n        set ckpass abc123\n        set authprofiles [PROFILE::list auth]\n        # Search the auth profiles for the krbdelegate(7) and grab cookie info\n        foreach profname $authprofiles {\n            if { [PROFILE::auth $profname type] == 7 } {\n                set tmpckname [PROFILE::auth $profname cookie_name]\n                set tmpckpass [PROFILE::auth $profname cookie_key]\n                if {[PROFILE::auth $profname cookie_name] != "" } {\n                    set ckname $tmpckname\n                    set ckpass $tmpckpass\n                    break\n                }\n            }\n        }\n        set seecookie 0\n        set insertcookie 0\n        # check for the cookie\n        if {not [info exists tmm_auth_http_sids(krbdelegate)]} {\n            set tmm_auth_sid [AUTH::start pam default_krbdelegate]\n            set tmm_auth_http_sids(krbdelegate) $tmm_auth_sid\n            AUTH::subscribe $tmm_auth_sid\n        } else {\n            set tmm_auth_sid $tmm_auth_http_sids(krbdelegate)\n        }\n        if { [PROFILE::exists clientssl] } {\n            set certcmd "SSL::cert 0"\n            set thecert [ eval $certcmd ]\n        }\n        if { $thecert == "" } {\n            # if no cert, assume old kerb delegation\n            # if there is no Authorization header and no cookie, get one.\n            if { ([HTTP::header Authorization] == "") and\n                  (not [HTTP::cookie exists $ckname])} {\n                HTTP::respond 401 WWW-Authenticate Negotiate\n                return\n            }\n        }\n        if {[HTTP::cookie exists $ckname]} {\n            set ckval [HTTP::cookie decrypt $ckname $ckpass]\n            AUTH::username_credential $tmm_auth_sid "cookie"\n            AUTH::password_credential $tmm_auth_sid $ckval\n            set seecookie 1\n        } else {\n            if { $thecert == "" } {\n                # Kerberos Delegation - set username\n                # Strip off the Negotiate before the base64d goodness\n                AUTH::username_credential $tmm_auth_sid [lindex [HTTP::header Authorization] 1]\n            }\n            else {\n                # Protocol Transition - set ttm_auth_sid\n                AUTH::username_credential $tmm_auth_sid "krpprottran"\n                AUTH::cert_credential $tmm_auth_sid $thecert\n            }\n            AUTH::password_credential $tmm_auth_sid "xxxx"\n        }\n        AUTH::authenticate $tmm_auth_sid\n\n        if {not [info exists tmm_auth_http_collect_count]} {\n            HTTP::collect\n            set tmm_auth_http_successes 0\n            set tmm_auth_http_collect_count 1\n        } else {\n            incr tmm_auth_http_collect_count\n        }\n    }\n    when AUTH_RESULT {\n        if {not [info exists tmm_auth_http_sids(krbdelegate)] or \\\n            ($tmm_auth_http_sids(krbdelegate) != [AUTH::last_event_session_id]) or \\\n            (not [info exists tmm_auth_http_collect_count])} {\n            return\n        }\n        if {[AUTH::status] == 0} {\n            incr tmm_auth_http_successes\n        }\n        # If multiple auth sessions are pending and\n        # one failure results in termination and this is a failure\n        # or enough successes have now occurred\n        if {([array size tmm_auth_http_sids] > 1) and \\\n            ((not [info exists tmm_auth_http_sufficient_successes] or \\\n             ($tmm_auth_http_successes >= $tmm_auth_http_sufficient_successes)))} {\n            # Abort the other auth sessions\n            foreach {type sid} [array get tmm_auth_http_sids] {\n                unset tmm_auth_http_sids($type)\n                if {($type ne "krbdelegate") and ($sid != -1)} {\n                    AUTH::abort $sid\n                    incr tmm_auth_http_collect_count -1\n               }\n            }\n        }\n        # If this is the last outstanding auth then either\n        # release or respond to this session\n        incr tmm_auth_http_collect_count -1\n        if {$tmm_auth_http_collect_count == 0} {\n            unset tmm_auth_http_collect_count\n            if { [AUTH::status] == 0 } {\n                array set pamout [AUTH::response_data]\n                HTTP::header replace Authorization "Negotiate $pamout(krbdelegate:attr:SPNEGO)"\n                if {$seecookie == 0} {\n                    set insertcookie $pamout(krbdelegate:attr:KRB5CCNAME)\n                }\n                HTTP::release\n            } else {\n                HTTP::respond 401 WWW-Authenticate Negotiate "Set-Cookie" "$ckname= ; expires=Wed Dec 31 16:00:00 1969"\n            }\n        }\n    }\n    # When the response goes out, if we need to insert a cookie, do it.\n    when HTTP_RESPONSE {\n        if {$insertcookie != 0} {\n            HTTP::cookie insert name $ckname value $insertcookie\n            HTTP::cookie encrypt $ckname $ckpass\n        }\n    }\ndefinition-signature KlDm5lT1k17/I3injIvybDZ6HIJC8qpdPgwUlPQ42tufrR7ZVVFvtDlDEdN4/QPtex/u1oEA6mij+N8mMc/FSy3B+jRogi7HyI/2glxNh8St/+odNp3ho6gWvTpNAS8XBIdixxCxpJYahIw5h9flJ+gZywLabCSMQAlFYoXqdpjZp5oZ/kN7/J94joR0okCRxI7fHgVLNcbXKWg+Kcuw0TJkyNWWJh1J6DeRURPzol+yo8GmCMdDia9MF68Kho8b5LWQuZIwt727OThDz0BBhAuG6oEn06GiPmPSxczJrei/k5Zd1SsJe0xpWvlLKP4vps/W8TcMhY3xwY70RP1cfQ==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_auth_ldap",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_auth_ldap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ldap?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when HTTP_REQUEST {\n        if {not [info exists tmm_auth_http_sids(ldap)]} {\n            set tmm_auth_sid [AUTH::start pam default_ldap]\n            set tmm_auth_http_sids(ldap) $tmm_auth_sid\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_sid\n            }\n        } else {\n            set tmm_auth_sid $tmm_auth_http_sids(ldap)\n        }\n        AUTH::username_credential $tmm_auth_sid [HTTP::username]\n        AUTH::password_credential $tmm_auth_sid [HTTP::password]\n        AUTH::authenticate $tmm_auth_sid\n\n        if {not [info exists tmm_auth_http_collect_count]} {\n            HTTP::collect\n            set tmm_auth_http_successes 0\n            set tmm_auth_http_collect_count 1\n        } else {\n            incr tmm_auth_http_collect_count\n        }\n    }\n    when AUTH_RESULT {\n        if {not [info exists tmm_auth_http_sids(ldap)] or \\\n           ($tmm_auth_http_sids(ldap) != [AUTH::last_event_session_id]) or \\\n           (not [info exists tmm_auth_http_collect_count])} {\n            return\n        }\n        if {[AUTH::status] == 0} {\n            incr tmm_auth_http_successes\n        }\n        # If multiple auth sessions are pending and\n        # one failure results in termination and this is a failure\n        # or enough successes have now occurred\n        if {([array size tmm_auth_http_sids] > 1) and \\\n            ((not [info exists tmm_auth_http_sufficient_successes] or \\\n             ($tmm_auth_http_successes >= $tmm_auth_http_sufficient_successes)))} {\n            # Abort the other auth sessions\n            foreach {type sid} [array get tmm_auth_http_sids] {\n                unset tmm_auth_http_sids($type)\n                if {($type ne "ldap") and ($sid != -1)} {\n                    AUTH::abort $sid\n                    incr tmm_auth_http_collect_count -1\n                }\n            }\n        }\n\n        # If this is the last outstanding auth then either\n        # release or respond to this session\n        incr tmm_auth_http_collect_count -1\n        if {$tmm_auth_http_collect_count == 0} {\n            unset tmm_auth_http_collect_count\n            if {[AUTH::status] == 0} {\n                HTTP::release\n            } else {\n                HTTP::respond 401\n            }\n        }\n    }\ndefinition-signature kzFhXHp72R2BTE+vwS9DBG2dlHsnGdWPsFSEx18DMcXyOypZi34rS+un6RpZeQ0Yib9GjXmEmIqLYQVCS9JTmcnjE0AEztcIot24B1NBVOHHAUfA7LJko7hqB9L0STfRTSbjaV13+kVDJMWYj1qcxGX7bIjzxXtPwPaDHWooxADCxmLlt9siSSYYnJqTJLcSutAJd16k+Y6lUKrcXoCl+0YIKm1CF+RUyWFsCNZxcmaOIyUqUnrLgpBinYyxb2T0MN9K/A9mXT6L+gscqHT+kAXxDJESOO1FHHvq4ld2dfK+Z6eWALvR0NGaCmYN2SEnfyZ3dfvb0ZdfWcyTqysEOw==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_auth_radius",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_auth_radius",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_radius?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when HTTP_REQUEST {\n        if {not [info exists tmm_auth_http_sids(radius)]} {\n            set tmm_auth_sid [AUTH::start pam default_radius]\n            set tmm_auth_http_sids(radius) $tmm_auth_sid\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_sid\n            }\n        } else {\n            set tmm_auth_sid $tmm_auth_http_sids(radius)\n        }\n        AUTH::username_credential $tmm_auth_sid [HTTP::username]\n        AUTH::password_credential $tmm_auth_sid [HTTP::password]\n        AUTH::authenticate $tmm_auth_sid\n\n        if {not [info exists tmm_auth_http_collect_count]} {\n            HTTP::collect\n            set tmm_auth_http_successes 0\n            set tmm_auth_http_collect_count 1\n        } else {\n            incr tmm_auth_http_collect_count\n        }\n    }\n    when AUTH_RESULT {\n        if {not [info exists tmm_auth_http_sids(radius)] or \\\n            ($tmm_auth_http_sids(radius) != [AUTH::last_event_session_id]) or \\\n            (not [info exists tmm_auth_http_collect_count])} {\n            return\n        }\n        if {[AUTH::status] == 0} {\n            incr tmm_auth_http_successes\n        }\n        # If multiple auth sessions are pending and\n        # one failure results in termination and this is a failure\n        # or enough successes have now occurred\n        if {([array size tmm_auth_http_sids] > 1) and \\\n            ((not [info exists tmm_auth_http_sufficient_successes] or \\\n             ($tmm_auth_http_successes >= $tmm_auth_http_sufficient_successes)))} {\n            # Abort the other auth sessions\n            foreach {type sid} [array get tmm_auth_http_sids] {\n                unset tmm_auth_http_sids($type)\n                if {($type ne "radius") and ($sid != -1)} {\n                    AUTH::abort $sid\n                    incr tmm_auth_http_collect_count -1\n                }\n            }\n        }\n        # If this is the last outstanding auth then either\n        # release or respond to this session\n        incr tmm_auth_http_collect_count -1\n        if {$tmm_auth_http_collect_count == 0} {\n            unset tmm_auth_http_collect_count\n            if { [AUTH::status] == 0 } {\n                HTTP::release\n            } else {\n                HTTP::respond 401\n            }\n        }\n    }\ndefinition-signature k3ZS7fMZZN+W3HDVg2i2FWS28Mv/l0JDnym3rEGY/JOn/L71DpzEEpTvyO+wU2Oecu7XfnBpkRG5mTTGGBMOOPKXoNFdRYbXprB+DRJhG2vOcR4KnxEsKyGuOM8MxNVb9Bg6jufGsqql/vEEGJJH43RjUqYIOiMNotKbghiC3BUBQfMN6XZlP3tgXTMM1wLSxei840hKMxpCa+CKWvQcnFHKzmwD3uN1S18Dx6yzGUFLSY+OFPHsctywMPQwzrZV7slOBgRGZMQbxqQAejddagQimzGzCKb0cDqdU2X4Vu6uqx1G3Lv1cihvMFDM7pLnfi2JskZ0nxNBBZ8rOcCVPw==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_auth_ssl_cc_ldap",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_auth_ssl_cc_ldap",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_cc_ldap?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when CLIENT_ACCEPTED {\n        set tmm_auth_ssl_cc_ldap_sid 0\n        set tmm_auth_ssl_cc_ldap_done 0\n    }\n    when CLIENTSSL_CLIENTCERT {\n        if {[SSL::cert count] == 0} {\n            return\n        }\n        set tmm_auth_ssl_cc_ldap_done 0\n        if {$tmm_auth_ssl_cc_ldap_sid == 0} {\n            set tmm_auth_ssl_cc_ldap_sid [AUTH::start pam default_ssl_cc_ldap]\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_ssl_cc_ldap_sid\n            }\n        }\n        AUTH::cert_credential $tmm_auth_ssl_cc_ldap_sid [SSL::cert 0]\n        AUTH::authenticate $tmm_auth_ssl_cc_ldap_sid\n        SSL::handshake hold\n    }\n    when CLIENTSSL_HANDSHAKE {\n        set tmm_auth_ssl_cc_ldap_done 1\n    }\n    when AUTH_RESULT {\n        if {[info exists tmm_auth_ssl_cc_ldap_sid] and \\\n            ($tmm_auth_ssl_cc_ldap_sid == [AUTH::last_event_session_id])} {\n            set tmm_auth_status [AUTH::status]\n            if {$tmm_auth_status == 0} {\n                set tmm_auth_ssl_cc_ldap_done 1\n                SSL::handshake resume\n            } elseif {$tmm_auth_status != -1 || $tmm_auth_ssl_cc_ldap_done == 0} {\n                reject\n            }\n        }\n    }\ndefinition-signature Ls7LEbcMGMMAy6eJsdaAn7tu3l2ROMB2XWCeLRc6GfBOiSF+EvVbQcSrl5MqklVcnQF9c4fzz+ffOPFyA9RkbicoFO2F/nr2B7NOFcuNNx3e9f/043A62ODBb6d18/IKO3hnEVwnRRBkB9SRPKc6tsHrReewPEB8TdA1eNb5JcautKEa3pbxLR76k60FS8k5wyPJ7W58gKT1tnR2n5EgM5K3wQSiCXKCONknyS2MKB6iEkk3uXSbQP0lzFCxPAPyR2JQ/ZNniC3jYghSr+M5i3KaMKjSjdsTt6fYpDxLH9Iikk5ZrtJGTJeP7P8cNQallzP7JJsB5aqui/SbFA0SFQ==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_auth_ssl_crldp",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_auth_ssl_crldp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_crldp?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when CLIENT_ACCEPTED {\n        set tmm_auth_ssl_crldp_sid 0\n        set tmm_auth_ssl_crldp_done 0\n    }\n    when CLIENTSSL_CLIENTCERT {\n        if {[SSL::cert count] == 0} {\n            return\n        }\n        set tmm_auth_ssl_crldp_done 0\n        if {$tmm_auth_ssl_crldp_sid == 0} {\n            set tmm_auth_ssl_crldp_sid [AUTH::start pam default_ssl_crldp]\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_ssl_crldp_sid\n            }\n        }\n        AUTH::cert_credential $tmm_auth_ssl_crldp_sid [SSL::cert 0]\n        AUTH::cert_issuer_credential $tmm_auth_ssl_crldp_sid [SSL::cert issuer 0]\n        AUTH::authenticate $tmm_auth_ssl_crldp_sid\n        SSL::handshake hold\n    }\n    when CLIENTSSL_HANDSHAKE {\n        set tmm_auth_ssl_crldp_done 1\n    }\n    when AUTH_RESULT {\n        if {[info exists tmm_auth_ssl_crldp_sid] and \\\n            ($tmm_auth_ssl_crldp_sid == [AUTH::last_event_session_id])} {\n            set tmm_auth_status [AUTH::status]\n            if {$tmm_auth_status == 0} {\n                set tmm_auth_ssl_crldp_done 1\n                SSL::handshake resume\n            } elseif {$tmm_auth_status != -1 || $tmm_auth_ssl_crldp_done == 0} {\n                reject\n            }\n        }\n    }\ndefinition-signature mVtMWHPruxGXVKW3hAZn3uBJkGNB8SmyzvR6u2OrQ+U71Ms+vAVuNSzCBJ05qJ7qfouOwtUYMtB1QMSjEdnLe2Z259y4gfnrEZEDpEZX8Co1rTEoP3grsw0heuITOPIX6R+MXrqfcmbaKRGGq2wJcNPLJXY/VsdYQBPDmaPrn/ZPRbmXSdRnpGFz4yN99tOw4OE5wvkp4CRg/zfSfQeFkzLrSeApGSWWAVMT09LW6aZmOWuC2bzr7Gpc7vtJtFuka8U7jSXAMJNOzqE55qhIvA3Y7UkIYemyXD0NCXmkUEWsPsuIzmZH6k6W8cXdhHtk+YEDvJDhKNO7h/C0qKPlaA==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_auth_ssl_ocsp",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_auth_ssl_ocsp",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_ocsp?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when CLIENT_ACCEPTED {\n        set tmm_auth_ssl_ocsp_sid 0\n        set tmm_auth_ssl_ocsp_done 0\n    }\n    when CLIENTSSL_CLIENTCERT {\n        if {[SSL::cert count] == 0} {\n            return\n        }\n        set tmm_auth_ssl_ocsp_done 0\n        if {$tmm_auth_ssl_ocsp_sid == 0} {\n            set tmm_auth_ssl_ocsp_sid [AUTH::start pam default_ssl_ocsp]\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_ssl_ocsp_sid\n            }\n        }\n        AUTH::cert_credential $tmm_auth_ssl_ocsp_sid [SSL::cert 0]\n        AUTH::cert_issuer_credential $tmm_auth_ssl_ocsp_sid [SSL::cert issuer 0]\n        AUTH::authenticate $tmm_auth_ssl_ocsp_sid\n        SSL::handshake hold\n    }\n    when CLIENTSSL_HANDSHAKE {\n        set tmm_auth_ssl_ocsp_done 1\n    }\n    when AUTH_RESULT {\n        if {[info exists tmm_auth_ssl_ocsp_sid] and \\\n            ($tmm_auth_ssl_ocsp_sid == [AUTH::last_event_session_id])} {\n            set tmm_auth_status [AUTH::status]\n            if {$tmm_auth_status == 0} {\n                set tmm_auth_ssl_ocsp_done 1\n                SSL::handshake resume\n            } elseif {$tmm_auth_status != -1 || $tmm_auth_ssl_ocsp_done == 0} {\n                reject\n            }\n        }\n    }\ndefinition-signature UAbD8tfmCrHiqB/uh1XzQfJvsgT+StbJ+Zq37qc+ODGStnFwDjXroPuPGPAycPBveiky0CU9/gR24Y8zfhMzbHK2lm/WvUq7cdrVIX2ZAvIVof9PpmfWli1c9iPe8EEau0yrOD7pZeyMpYM2hIlG1L9YmhBSJGwGV2UzmKmFdLsBWuGfcfBW7ZXQTjKz0UhT4YWUbpF0ws9QNJln8zsiCPlChF2OAJk35ZxGoZmKGA/xL2fJVbsI3vz3HAbAadKx0AiXqk6aTwtQny18mu0nVsPbO5t/KwqH6C3rc/qoVgqG6FsvVen2OvNYDBnq4gm+A5Mf1abey7+edQT6KJ9ztA==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_auth_tacacs",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_auth_tacacs",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_tacacs?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when HTTP_REQUEST {\n        if {not [info exists tmm_auth_http_sids(tacacs)]} {\n            set tmm_auth_sid [AUTH::start pam default_tacacs]\n            set tmm_auth_http_sids(tacacs) $tmm_auth_sid\n            if {[info exists tmm_auth_subscription]} {\n                AUTH::subscribe $tmm_auth_sid\n            }\n        } else {\n            set tmm_auth_sid $tmm_auth_http_sids(tacacs)\n        }\n        AUTH::username_credential $tmm_auth_sid [HTTP::username]\n        AUTH::password_credential $tmm_auth_sid [HTTP::password]\n        AUTH::authenticate $tmm_auth_sid\n\n        if {not [info exists tmm_auth_http_collect_count]} {\n            HTTP::collect\n            set tmm_auth_http_successes 0\n            set tmm_auth_http_collect_count 1\n        } else {\n            incr tmm_auth_http_collect_count\n        }\n    }\n    when AUTH_RESULT {\n        if {not [info exists tmm_auth_http_sids(tacacs)] or \\\n            ($tmm_auth_http_sids(tacacs) != [AUTH::last_event_session_id]) or \\\n            (not [info exists tmm_auth_http_collect_count])} {\n            return\n        }\n        if {[AUTH::status] == 0} {\n            incr tmm_auth_http_successes\n        }\n        # If multiple auth sessions are pending and\n        # one failure results in termination and this is a failure\n        # or enough successes have now occurred\n        if {([array size tmm_auth_http_sids] > 1) and \\\n            ((not [info exists tmm_auth_http_sufficient_successes] or \\\n             ($tmm_auth_http_successes >= $tmm_auth_http_sufficient_successes)))} {\n            # Abort the other auth sessions\n            foreach {type sid} [array get tmm_auth_http_sids] {\n                unset tmm_auth_http_sids($type)\n                if {($type ne "tacacs") and ($sid != -1)} {\n                    AUTH::abort $sid\n                    incr tmm_auth_http_collect_count -1\n                }\n            }\n        }\n        # If this is the last outstanding auth then either\n        # release or respond to this session\n        incr tmm_auth_http_collect_count -1\n        if {$tmm_auth_http_collect_count == 0} {\n            unset tmm_auth_http_collect_count\n            if { [AUTH::status] == 0 } {\n                HTTP::release\n            } else {\n                HTTP::respond 401\n            }\n        }\n    }\ndefinition-signature qR6ynw882+5gcwiV6eymN/CZAoF+G4aRd2Xfr+4KWfXAD27876SoHuTyuTKxKxcG5oGXOPppqH/vtbtnBiI+UW6CLEHne3+RPx9EaSxX4ElCg/1ap69j3xPmh2IVSTCrR/93vu9Bnt6DEkNbXelWze5C0jVwMogQdsiVpmn7+YfkSmyyEeAvx8aHkvhK8KL0Pp8AiqrvyDWcBVAtXtioS0YC3S8pxRbpWHuVzA9e4SXNIpCk8vigk7gOmQthC+xerw0/8PEmOfT4G2LNr7TG4M1kQFkLR1foz4EwODEODHjyiyNTWZsCH4sPWJM6xJXS+NbL4k+0lWNPyhnyAGbnpw==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "_sys_https_redirect",
                    "partition": "Common",
                    "fullPath": "/Common/_sys_https_redirect",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_https_redirect?ver=14.1.2.1",
                    "apiAnonymous": 'nodelete nowrite \n# Copyright 2003-2006, 2012-2013, 2016.  F5 Networks, Inc.  See End User License Agreement ("EULA")\n# for license terms. Notwithstanding anything to the contrary in the EULA,\n# Licensee may copy and modify this software product for its internal business\n# purposes. Further, Licensee may upload, publish and distribute the modified\n# version of the software product on devcentral.f5.com.\n#\n    when HTTP_REQUEST {\n       HTTP::redirect https://[getfield [HTTP::host] ":" 1][HTTP::uri]\n    }\ndefinition-signature WsYy2M6xMqvosIKIEH/FSsvhtWMe6xKOA6i7f09Hbp6tJviSRXSan9xiuI8AUXXeWwB4wU/ZVfd8OXR92fOjZY1GFyea9NoY64nZMZ3+/Yy5XuiqA1bBUNIpZNmv2/zYOhDBsO0Wg27evtJrkgU/3K0cBMIgaAM5gDjlmd1KPSPmpXgcMzNpbSuNAgw8uy5FKlFEjjSNmTzTvKy83QcFFoigAixOsq0ds9Qt2gPvQ+u/4qibvTo/mxf5LF1rDc1cWoVxwspGbC5VMt1DKjG5hRo0PAr2ES9bUyQst+30CoSULDgl3hWt9Q4S5OCKbwTHRZmglvZ12s8+Qolr56cVtQ==',
                    "apiRawValues": {
                        "verificationStatus": "signature-verified"
                    },
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "http-redirect-https.tcl",
                    "partition": "Common",
                    "fullPath": "/Common/http-redirect-https.tcl",
                    "generation": 874,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~http-redirect-https.tcl?ver=14.1.2.1",
                    "apiAnonymous": 'when HTTP_REQUEST { \n    HTTP::redirect "https://[HTTP::host][HTTP::uri]" \n}',
                },
                {
                    "kind": "tm:ltm:rule:rulestate",
                    "name": "terraform_irule",
                    "partition": "Common",
                    "fullPath": "/Common/terraform_irule",
                    "generation": 1,
                    "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~terraform_irule?ver=14.1.2.1",
                    "apiAnonymous": 'when HTTP_REQUEST {\n\n  if { [string tolower [HTTP::header value Upgrade]] equals "websocket" } {\n    HTTP::disable\n#    ASM::disable\n    log local0. "[IP::client_addr] - Connection upgraded to websocket protocol. Disabling ASM-checks and HTTP protocol. Traffic is treated as L4 TCP stream."\n  } else {\n    HTTP::enable\n#    ASM::enable\n    log local0. "[IP::client_addr] - Regular HTTP request. ASM-checks and HTTP protocol enabled. Traffic is deep-inspected at L7."\n  }\n}',
                },
            ],
        }


class test_get_ltm_rule(unittest.TestCase):

    maxDiff = None

    empty_output = {"get.return_value": {}}

    golden_parsed_output = {
        "items": [
            {
                "apiAnonymous": "when CLIENT_ACCEPTED { snat 10.197.225.[getfield "
                '[IP::client_addr] "." 4] }',
                "fullPath": "/Common/SNAT-10-197-225.tcl",
                "generation": 607,
                "kind": "tm:ltm:rule:rulestate",
                "name": "SNAT-10-197-225.tcl",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-10-197-225.tcl?ver=14.1.2.1",
            },
            {
                "fullPath": "/Common/SNAT-39",
                "generation": 972,
                "kind": "tm:ltm:rule:rulestate",
                "name": "SNAT-39",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~SNAT-39?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    # Global variables\n"
                "    # static::POLICY_RESULT_CACHE_AUTHFAILED\n"
                "    #     Administrator can set this into 1, when "
                "there is a necessity to cache failed policy "
                "result.\n"
                "    #     This may be needed to avoid account "
                "locked caused by the Active Sync device when it "
                "uses wrong passwords.\n"
                "    #     One possible scenario, is that when the "
                "user changes the password in Active Directory, "
                "but missed to changed in their devices.\n"
                "    # Responses\n"
                "    # On denied result\n"
                "    #     Administrator can customize the "
                "responses to the device depends on more complex "
                "conditions when necessary.\n"
                "    #     In those cases, please use "
                "ACCESS::respond command.\n"
                "    #     The following is the syntax of "
                "ACCESS::respond\n"
                "    #     ACCESS::respond <status code> [ content "
                "<body> ] [ <Additional Header> <Additional Header "
                "value>* ]\n"
                "    #     e.g. ACCESS::respond 401 content "
                '"Error: Denied" WWW-Authenticate "basic '
                'realm=\\"f5.com\\"" Connection close\n'
                "    when RULE_INIT {\n"
                "        # Please set the following global "
                "variables for customized responses.\n"
                "        set static::actsync_401_http_body "
                '"<html><title>Authentication '
                "Failured</title><body>Error: Authentication "
                'Failure</body></html>"\n'
                "        set static::actsync_503_http_body "
                '"<html><title>Service is not '
                "available</title><body>Error: Service is not "
                'available</body></html>"\n'
                "        set "
                "static::ACCESS_LOG_PREFIX                 "
                '"01490000:7:"\n'
                "\n"
                "        # Second Virtual Server name for 401 NTLM "
                "responder\n"
                "        set "
                "static::ACCESS_SECOND_VIRTUAL_NAME        "
                '"_ACCESS_401_NTLM_responder_HTTPS"\n'
                "\n"
                "        set "
                "static::POLICY_INPROGRESS                 "
                '"policy_inprogress"\n'
                "        set "
                "static::POLICY_AUTHFAILED                 "
                '"policy_authfailed"\n'
                "        # The request with huge content length "
                "can not be used for starting ACCESS session.\n"
                "        # This kind of request will be put on "
                "hold, and this iRule will try to use another\n"
                "        # request to start the session. The "
                "following value is used for Outlook Anywhere.\n"
                "        set "
                "static::OA_MAGIC_CONTENT_LEN              "
                "1073741824\n"
                "\n"
                "        # Similar with OutlookAnywhere case, "
                "ACCESS can not use the request which is\n"
                "        # larger then following size. This "
                "becomes an issue with application that using\n"
                "        # Exchange Web Service as its main "
                "protocol such as Mac OS X applications\n"
                "        # (e.g. Mail app, Microsoft Entourage, "
                "etc)\n"
                "        # This kind of request will be put on "
                "hold, and this iRule will try to use another\n"
                "        # request to start the session.\n"
                "        set "
                "static::FIRST_BIG_POST_CONTENT_LEN        640000\n"
                "\n"
                "        # Set it into 1 if the backend EWS "
                "handler accepts HTTP Basic Authentication.\n"
                "        set "
                "static::EWS_BKEND_BASIC_AUTH              0\n"
                "        # The following variable controls the "
                "polling mechanism.\n"
                "        set "
                "static::POLICY_RESULT_POLL_INTERVAL       250\n"
                "        set "
                "static::POLICY_RESULT_POLL_MAXRETRYCYCLE  600\n"
                "\n"
                "        # Set this global variable to 1 for "
                "caching authentication failure\n"
                "        # Useful for avoiding account locked "
                "out.\n"
                "        set "
                "static::POLICY_RESULT_CACHE_AUTHFAILED    0\n"
                "\n"
                "        # set this global variable to set "
                "alternative timeout for particular session\n"
                "        set "
                "static::POLICY_ALT_INACTIVITY_TIMEOUT     120\n"
                "\n"
                "        set "
                "static::ACCESS_USERKEY_TBLNAME            "
                '"_access_userkey"\n'
                "\n"
                "\n"
                "        set "
                "static::ACCESS_DEL_COOKIE_HDR_VAL         "
                '"MRHSession=deleted; expires=Thu, 01-Jan-1970 '
                '00:00:01 GMT; path=/"\n'
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"01490000:7: EWS_BKEND_BASIC_AUTH = '
                '$static::EWS_BKEND_BASIC_AUTH"\n'
                "    }\n"
                "    when ACCESS_ACL_ALLOWED {\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX [HTTP::method] '
                '[HTTP::uri] [HTTP::header Content-Length]"\n'
                "\n"
                "        # MSFT Exchange's EWS request handler "
                "always requesting NTLM even the connection has "
                "been\n"
                "        # already authenticated if there is a "
                "HTTP Basic Auth in the request.\n"
                "        if { [ info exists f_exchange_web_service "
                "] && $f_exchange_web_service  == 1 }  {\n"
                "            if { $static::EWS_BKEND_BASIC_AUTH == "
                "0 } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Removing HTTP Basic '
                'Authorization header"\n'
                "                HTTP::header remove "
                "Authorization\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when HTTP_REQUEST {\n"
                "        set http_path                       [ "
                "string tolower [HTTP::path] ]\n"
                "        set f_clientless_mode               0\n"
                "        set f_alt_inactivity_timeout        0\n"
                "        set f_rpc_over_http                 0\n"
                "        set f_exchange_web_service          0\n"
                "        set f_auto_discover                 0\n"
                "        set f_activesync                    0\n"
                "        set f_offline_address_book          0\n"
                "        set f_availability_service          0\n"
                "\n"
                "        #  Here put appropriate pool when "
                "necessary.\n"
                "        switch -glob $http_path {\n"
                '        "/rpc/rpcproxy.dll" {\n'
                "            # Supports for RPC over HTTP. "
                "(Outlook Anywhere)\n"
                "            set f_rpc_over_http 1\n"
                "        }\n"
                '        "/autodiscover/autodiscover.xml" {\n'
                "            # Supports for Auto Discover "
                "protocol.\n"
                "            set f_auto_discover 1\n"
                "            # This request does not require long "
                "inactivity timeout.\n"
                "            # Don't use this for now\n"
                "            set f_alt_inactivity_timeout 0\n"
                "        }\n"
                '        "/microsoft-server-activesync" {\n'
                "            # Supports for ActiveSync\n"
                "            set f_activesync 1\n"
                "        }\n"
                '        "/oab/*" {\n'
                "            # Supports for Offline Address Book\n"
                "            set f_offline_address_book 1\n"
                "            # Don't use this for now\n"
                "            set f_alt_inactivity_timeout 0\n"
                "        }\n"
                '        "/ews/*" {\n'
                "            # Support for Exchange Web Service\n"
                "            # Outlook's Availability Service "
                "borrows this protocol.\n"
                "            set f_exchange_web_service 1\n"
                "        }\n"
                '        "/as/*" {\n'
                "            # Support for Availability Service.\n"
                "            # do nothing for now. (Untested)\n"
                "            set f_availability_service 1\n"
                "        }\n"
                "        default {\n"
                "            return\n"
                "        }\n"
                "        }\n"
                "\n"
                "        set f_reqside_set_sess_id           0\n"
                "        set http_method                     "
                "[HTTP::method]\n"
                "        set http_hdr_host                   "
                "[HTTP::host]\n"
                "        set http_hdr_uagent                 "
                "[HTTP::header User-Agent]\n"
                "        set http_uri                        "
                "[HTTP::uri]\n"
                "        set http_content_len                "
                "[HTTP::header Content-Length]\n"
                "        set MRHSession_cookie               "
                "[HTTP::cookie value MRHSession]\n"
                '        set auth_info_b64enc                ""\n'
                "\n"
                "        if { ! [ info exists src_ip ] } {\n"
                "            set src_ip                            "
                "[IP::remote_addr]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_POLICY_TIMEOUT ] } {\n"
                "            set PROFILE_POLICY_TIMEOUT            "
                "[PROFILE::access access_policy_timeout]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_MAX_SESS_TIMEOUT ] } {\n"
                "            set PROFILE_MAX_SESS_TIMEOUT          "
                "[PROFILE::access max_session_timeout]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_RESTRICT_SINGLE_IP ] } {\n"
                "            set PROFILE_RESTRICT_SINGLE_IP        "
                "1\n"
                "        }\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX method: '
                '$http_method"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Src IP: $src_ip"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX User-Agent: '
                '$http_hdr_uagent"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP uri: $http_uri"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP len: '
                '$http_content_len"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX '
                "Restrict-to-single-client-ip: "
                '$PROFILE_RESTRICT_SINGLE_IP"\n'
                "\n"
                "        # First, do we have valid MRHSession "
                "cookie.\n"
                '        if { $MRHSession_cookie != "" } {\n'
                "            if { [ACCESS::session exists "
                "-state_allow -sid $MRHSession_cookie] } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *VALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "            } else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *INVALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                '                set MRHSession_cookie ""\n'
                "                HTTP::cookie remove MRHSession\n"
                "            }\n"
                "        }\n"
                "\n"
                "        set http_hdr_auth [HTTP::header "
                "Authorization]\n"
                "        if { [ string match -nocase {basic *} "
                "$http_hdr_auth ] != 1 } {\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Not basic '
                'authentication. Ignore received auth header"\n'
                '            set http_hdr_auth ""\n'
                "        }\n"
                "\n"
                '        if { $http_hdr_auth == "" } {\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX No/Empty Auth '
                'header"\n'
                "            # clean up the cookie\n"
                '            if { $MRHSession_cookie == "" } {\n'
                "                HTTP::respond 401 content  "
                "$static::actsync_401_http_body WWW-Authenticate "
                '"Basic realm=\\"[HTTP::header Host]\\"" '
                "Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL "
                "Connection Close\n"
                "                return\n"
                "            }\n"
                "            # Do nothing if we have a valid "
                "MRHSession cookie.\n"
                "        }\n"
                "\n"
                "        set f_release_request           0\n"
                "        # Optimization for clients which support "
                "cookie\n"
                '        if { $MRHSession_cookie != "" } {\n'
                "            # Default profile access setting is "
                "false\n"
                "            if { $PROFILE_RESTRICT_SINGLE_IP == 0 "
                "} {\n"
                "                set f_release_request 1\n"
                "            }\n"
                "            elseif { [ IP::addr $src_ip equals [ "
                "ACCESS::session data get -sid $MRHSession_cookie "
                '"session.user.clientip" ] ] } {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP matched"\n'
                "                set f_release_request 1\n"
                "            }\n"
                "            else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP does not '
                'matched"\n'
                '                set MRHSession_cookie ""\n'
                "                HTTP::cookie remove MRHSession\n"
                "            }\n"
                "        }\n"
                "\n"
                "        if { $f_release_request == 0 } {\n"
                "            set apm_username [string tolower "
                "[HTTP::username]]\n"
                "            set apm_password [HTTP::password]\n"
                "            if { $PROFILE_RESTRICT_SINGLE_IP == 0 "
                "} {\n"
                '                binary scan [md5 "$apm_password"] '
                "H* user_hash\n"
                "            }\n"
                "            else {\n"
                "                binary scan [md5 "
                '"$apm_password$src_ip"] H* user_hash\n'
                "            }\n"
                "            set user_key    "
                '"$apm_username.$user_hash"\n'
                "            unset user_hash\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP Hdr Auth: '
                '$http_hdr_auth"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX apm_username: '
                '$apm_username"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX user_key = '
                '$user_key"\n'
                "            set apm_cookie_list             [ "
                "ACCESS::user getsid $user_key ]\n"
                "            if { [ llength $apm_cookie_list ] != "
                "0 } {\n"
                "                set apm_cookie [ ACCESS::user "
                "getkey [ lindex $apm_cookie_list 0 ] ]\n"
                '                if { $apm_cookie != "" } {\n'
                "                    HTTP::cookie insert name "
                "MRHSession value $apm_cookie\n"
                "                    set f_release_request 1\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "\n"
                "        if { $http_content_len ==  "
                "$static::OA_MAGIC_CONTENT_LEN } {\n"
                "            set f_oa_magic_content_len 1\n"
                "        }\n"
                "\n"
                "        set f_sleep_here 0\n"
                "        set retry 1\n"
                "\n"
                "        while { $f_release_request == 0 && $retry "
                "<=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } "
                "{\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Trying #$retry for '
                '$http_method $http_uri $http_content_len"\n'
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Reading $user_key '
                'from table $static::ACCESS_USERKEY_TBLNAME"\n'
                "\n"
                "            set apm_cookie [table lookup "
                "-subtable  $static::ACCESS_USERKEY_TBLNAME "
                "-notouch $user_key]\n"
                '            if { $apm_cookie != "" } {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Verifying table '
                'cookie = $apm_cookie"\n'
                "\n"
                "                # Accessing SessionDB is not that "
                "cheap. Here we are trying to check known value.\n"
                "                if { $apm_cookie == "
                '"policy_authfailed" || $apm_cookie == '
                '"policy_inprogress"} {\n'
                "                    # Do nothing\n"
                "                } elseif  { ! [ ACCESS::session "
                "exists $apm_cookie ] } {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX table cookie = '
                '$apm_cookie is out-of-sync"\n'
                "                    # Table value is out of sync. "
                "Ignores it.\n"
                '                    set apm_cookie ""\n'
                "                }\n"
                "            }\n"
                "\n"
                "            switch $apm_cookie {\n"
                '            "" {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX NO APM Cookie found"\n'
                "\n"
                "                if { [ info exists "
                "f_oa_magic_content_len ] && "
                "$f_oa_magic_content_len == 1 } {\n"
                "                    # Outlook Anywhere request "
                "comes in pair. The one with 1G payload is not "
                "usable\n"
                "                    # for creating new session "
                "since 1G content-length is intended for client to "
                "upload\n"
                "                    # the data when needed.\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Start to wait '
                "$static::POLICY_RESULT_POLL_INTERVAL ms for "
                'request with magic content-len"\n'
                "                    set f_sleep_here 1\n"
                "                } elseif { [ info exists "
                "f_exchange_web_service ] && "
                "$f_exchange_web_service == 1 && $http_content_len "
                "> $static::FIRST_BIG_POST_CONTENT_LEN } {\n"
                "                    # Here we are getting large "
                "EWS request, which can't be used for starting new "
                "session\n"
                "                    # in clientless-mode. Have it "
                "here waiting for next smaller one.\n"
                "                    # We are holding the request "
                "here in HTTP filter, and HTTP filter "
                "automatically\n"
                "                    # clamping down the TCP "
                "window when necessary.\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Start to wait '
                "$static::POLICY_RESULT_POLL_INTERVAL ms for big "
                'EWS request"\n'
                "                    set f_sleep_here 1\n"
                "                } else {\n"
                "                   set apm_cookie               "
                '"policy_inprogress"\n'
                "                   set f_reqside_set_sess_id    "
                "1\n"
                "                   set f_release_request        "
                "1\n"
                "                }\n"
                "            }\n"
                '            "policy_authfailed" {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Found $user_key with '
                'AUTH_FAILED"\n'
                "                HTTP::respond 401 content  "
                "$static::actsync_401_http_body\n"
                "                set f_release_request 1\n"
                "            }\n"
                '            "policy_inprogress" {\n'
                "                if { [ info exists f_activesync ] "
                "&& ($f_activesync == 1) } {\n"
                "                    # For ActiveSync requests, "
                "aggressively starts new session.\n"
                "                    set f_reqside_set_sess_id    "
                "1\n"
                "                    set f_release_request        "
                "1\n"
                "                } else {\n"
                "                    set f_sleep_here 1\n"
                "                }\n"
                "            }\n"
                "            default {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Using MRHSession = '
                '$apm_cookie"\n'
                "                HTTP::header insert Cookie "
                '"MRHSession=$apm_cookie"\n'
                "                set f_release_request 1\n"
                "            }\n"
                "            }\n"
                "\n"
                "            if { $f_reqside_set_sess_id == 1 } {\n"
                "                set f_reqside_set_sess_id 0\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Setting '
                "$user_key=$apm_cookie $PROFILE_POLICY_TIMEOUT "
                '$PROFILE_POLICY_TIMEOUT"\n'
                "                set f_clientless_mode 1\n"
                "                HTTP::cookie remove MRHSession\n"
                "                HTTP::header insert "
                '"clientless-mode" 1\n'
                '                HTTP::header insert "username" '
                "$apm_username\n"
                '                HTTP::header insert "password" '
                "$apm_password\n"
                "                table set -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key "
                "$apm_cookie $PROFILE_POLICY_TIMEOUT "
                "$PROFILE_POLICY_TIMEOUT\n"
                "            }\n"
                "\n"
                "            if { $f_sleep_here == 1 } {\n"
                "                set f_sleep_here 0\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Waiting  '
                "$static::POLICY_RESULT_POLL_INTERVAL ms for "
                '$http_method $http_uri"\n'
                "                after  "
                "$static::POLICY_RESULT_POLL_INTERVAL\n"
                "            }\n"
                "\n"
                "            incr retry\n"
                "        }\n"
                "\n"
                "        if { ($f_release_request == 0) && ($retry "
                ">=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE) } "
                "{\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Policy did not finish '
                "in [expr { "
                "$static::POLICY_RESULT_POLL_MAXRETRYCYCLE * "
                "$static::POLICY_RESULT_POLL_INTERVAL } ] ms. "
                'Close connection for $http_method $http_uri"\n'
                "\n"
                "            table delete -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key\n"
                "            ACCESS::disable\n"
                "            TCP::close\n"
                "            return\n"
                "        }\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Releasing request '
                '$http_method $http_uri"\n'
                "    }\n"
                "\n"
                "    when ACCESS_SESSION_STARTED {\n"
                "        if { [ info exists user_key ] } {\n"
                "\n"
                "            ACCESS::session data set "
                '"session.user.uuid" $user_key\n'
                "            ACCESS::session data set "
                '"session.user.microsoft-exchange-client" 1\n'
                "\n"
                "            if { [ info exists f_activesync ] && "
                "$f_activesync == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-activesync" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_auto_discover ] && $f_auto_discover == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-autodiscover" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_availability_service ] && "
                "$f_availability_service == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-availabilityservice" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_rpc_over_http ] && $f_rpc_over_http == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-rpcoverhttp" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_offline_address_book ] && "
                "$f_offline_address_book == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-offlineaddressbook" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_exchange_web_service ] && "
                "$f_exchange_web_service == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-exchangewebservice" 1\n'
                "            }\n"
                "        }\n"
                "        if { [ info exists "
                "f_alt_inactivity_timeout ] && "
                "$f_alt_inactivity_timeout == 1 } {\n"
                "            ACCESS::session data set "
                '"session.inactivity_timeout"  '
                "$static::POLICY_ALT_INACTIVITY_TIMEOUT\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when ACCESS_POLICY_COMPLETED {\n"
                "        if { ! [ info exists user_key ] } {\n"
                "            return\n"
                "        }\n"
                "\n"
                '        set user_key_value ""\n'
                "        set f_delete_session 0\n"
                "        set policy_result [ACCESS::policy "
                "result]\n"
                "        set sid [ ACCESS::session sid ]\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX '
                "ACCESS_POLICY_COMPLETED: policy_result = "
                '\\"$policy_result\\" user_key = \\"$user_key\\" '
                'sid = \\"$sid\\""\n'
                "\n"
                "        set inactivity_timeout [ACCESS::session "
                'data get "session.inactivity_timeout"]\n'
                "        set max_sess_timeout [ACCESS::session "
                'data get "session.max_session_timeout"]\n'
                '        if { $max_sess_timeout == "" } {\n'
                "             set max_sess_timeout "
                "$PROFILE_MAX_SESS_TIMEOUT\n"
                "        }\n"
                "\n"
                "        switch $policy_result {\n"
                '        "allow" {\n'
                "            # We depends on this table record "
                "self-cleanup capability in order to\n"
                "            # indirectly sync with session DB.\n"
                "            set user_key_value $sid\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Result: Allow: '
                "$user_key => $sid $inactivity_timeout "
                '$max_sess_timeout"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX user_key_value = '
                '$user_key_value"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX sid = $sid"\n'
                "        }\n"
                '        "deny" {\n'
                "            # When necessary the admin here can "
                "check appropriate session variable\n"
                "            # and decide what response more "
                "appropriate then this default response.\n"
                "            ACCESS::respond 401 content  "
                "$static::actsync_401_http_body Set-Cookie "
                "$static::ACCESS_DEL_COOKIE_HDR_VAL Connection "
                "Close\n"
                "            if {  "
                "$static::POLICY_RESULT_CACHE_AUTHFAILED == 1 } {\n"
                "                set user_key_value  "
                "$static::POLICY_AUTHFAILED\n"
                "            } else {\n"
                "                set f_delete_session  1\n"
                "            }\n"
                "        }\n"
                "        default {\n"
                "            ACCESS::respond 503 content  "
                "$static::actsync_503_http_body Connection Close\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Got unsupported '
                'policy result for $user_key ($sid)"\n'
                "            set f_delete_session  1\n"
                "        }\n"
                "        }\n"
                '        if { $user_key_value != "" } {\n'
                "           log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Setting $user_key => '
                "$user_key_value $inactivity_timeout "
                "$max_sess_timeout in table "
                '$static::ACCESS_USERKEY_TBLNAME"\n'
                "\n"
                "           table set -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key "
                "$user_key_value $inactivity_timeout "
                "$max_sess_timeout\n"
                "        } else {\n"
                "           log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Deleting $user_key in '
                'table $static::ACCESS_USERKEY_TBLNAME"\n'
                "\n"
                "           table delete -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key\n"
                "        }\n"
                "\n"
                "        if { $f_delete_session == 1 } {\n"
                "           ACCESS::session remove\n"
                "           set f_delete_session 0\n"
                "           log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Removing the session '
                'for $user_key."\n'
                "        }\n"
                "    }\n"
                "definition-signature "
                "B1IR2MLC4VSVVTAxgOlbnmxBXZrz7g/jBySWM+WsjwfY8sVY/+/Ss7wZpem7Aotnw3BZdtj14KQPUeSPb1WiMAKc3GxZ0NeWzg/YjbfiJ8ebLTGun9QozSqorwv93+L9UU2Rn1T/hS8kx2peJdCFBm0FVkvVTHrGV88gZhwc77dSZzWm4ynA01qwjYn2WGDztLUpn5Cdx3XSS25sNBINe4QHeJ+7uT8DKl/psLHNT7kk7vJ3Z3uAJJIKCx434KaYTDu0OmNrLk1Rt1R+Ha3Nd+ifGdRYIZrZfYNtr0YIXErzvVlUwrvcF/OHtiLbpgVzerliIOY9VwXBngOGli444Q==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_APM_ExchangeSupport_OA_BasicAuth",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_APM_ExchangeSupport_OA_BasicAuth",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_OA_BasicAuth?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when RULE_INIT {\n"
                "        set "
                "static::POLICY_INPROGRESS                 "
                '"policy_inprogress"\n'
                "        set "
                "static::POLICY_FAILED                     "
                '"policy_failed"\n'
                "        set "
                "static::POLICY_SUCCEED                    "
                '"policy_succeed"\n'
                "        set "
                "static::POLICY_DONE_WAIT_SEC              5\n"
                "\n"
                "        set "
                "static::FIRST_BIG_POST_CONTENT_LEN        640000\n"
                "        set "
                "static::POLICY_RESULT_POLL_INTERVAL       100\n"
                "        set "
                "static::POLICY_RESULT_POLL_MAXRETRYCYCLE  100\n"
                "        set "
                "static::ACCESS_USERKEY_TBLNAME            "
                '"_access_userkey"\n'
                "        set "
                "static::ACCESS_LOG_PREFIX                 "
                '"01490000:7:"\n'
                "\n"
                "        set "
                "static::USE_NTLM_AUTH                     0\n"
                "        set "
                "static::USE_BASIC_AUTH                    1\n"
                "        set "
                "static::USE_NTLM_BASIC_AUTH               2\n"
                "\n"
                "        set "
                "static::URL_DEFAULT                       0\n"
                "        set "
                "static::URL_RPC_OVER_HTTP                 1\n"
                "        set "
                "static::URL_AUTODISCOVER                  2\n"
                "        set "
                "static::URL_ACTIVE_SYNC                   3\n"
                "        set "
                "static::URL_OFFLINEADDRESSBOOK            4\n"
                "        set "
                "static::URL_EXCHANGEWEBSERVICE            5\n"
                "\n"
                "        set "
                "static::RECVD_AUTH_NONE                   0\n"
                "        set "
                "static::RECVD_AUTH_NTLM                   1\n"
                "        set "
                "static::RECVD_AUTH_BASIC                  2\n"
                "\n"
                "        set "
                "static::ACCESS_DEL_COOKIE_HDR_VAL         "
                '"MRHSession=deleted; \\\n'
                "                                                       "
                "expires=Thu, 01-Jan-1970 00:00:01 GMT;\\\n"
                "                                                       "
                'path=/"\n'
                "\n"
                "    }\n"
                "\n"
                "    when HTTP_REQUEST {\n"
                "        set http_path                       "
                "[string tolower [HTTP::path]]\n"
                "        set url_path                        "
                "$static::URL_DEFAULT\n"
                "        set use_auth                        "
                "$static::USE_NTLM_AUTH\n"
                "        set f_disable_sso                   0\n"
                "\n"
                "        switch -glob $http_path {\n"
                '        "/rpc/rpcproxy.dll" {\n'
                "            set url_path                    "
                "$static::URL_RPC_OVER_HTTP\n"
                "        }\n"
                '        "/autodiscover/autodiscover.xml" {\n'
                "            set url_path                    "
                "$static::URL_ACTIVE_SYNC\n"
                "            # Need to support both NTLM and Basic "
                "authentication for this URL\n"
                "            set use_auth                    "
                "$static::USE_NTLM_BASIC_AUTH\n"
                "        }\n"
                '        "/microsoft-server-activesync*" {\n'
                "            set url_path                    "
                "$static::URL_ACTIVE_SYNC\n"
                "            # Use only Basic authentication for "
                "this URL\n"
                "            set use_auth                    "
                "$static::USE_BASIC_AUTH\n"
                "            set f_disable_sso               1\n"
                "        }\n"
                '        "/oab*" {\n'
                "            set url_path                    "
                "$static::URL_OFFLINEADDRESSBOOK\n"
                "        }\n"
                '        "/ews*" {\n'
                "            set url_path                    "
                "$static::URL_EXCHANGEWEBSERVICE\n"
                "        }\n"
                "        default {\n"
                "            ECA::disable\n"
                "            return\n"
                "        }\n"
                "        }\n"
                "\n"
                "        if { ! [ info exists f_ntlm_auth_succeed "
                "] } {\n"
                "            set f_ntlm_auth_succeed         0\n"
                "        }\n"
                "        if { ! [ info exists sid_cache ] } {\n"
                "            set sid_cache                         "
                '""\n'
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_POLICY_TIMEOUT ] } { \n"
                "            set PROFILE_POLICY_TIMEOUT            "
                "[PROFILE::access access_policy_timeout]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_MAX_SESS_TIMEOUT ] } {\n"
                "            set PROFILE_MAX_SESS_TIMEOUT          "
                "[PROFILE::access max_session_timeout]\n"
                "        }\n"
                "        if { ! [ info exists src_ip ] } {\n"
                "            set src_ip                            "
                "[IP::remote_addr]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_RESTRICT_SINGLE_IP ] } {\n"
                "            set PROFILE_RESTRICT_SINGLE_IP        "
                "1\n"
                "        }\n"
                "\n"
                "        set http_method                     "
                "[HTTP::method]\n"
                "        set http_hdr_host                   "
                "[HTTP::host]\n"
                "        set http_hdr_uagent                 "
                "[HTTP::header User-Agent]\n"
                "        set http_uri                        "
                "[HTTP::uri]\n"
                "        set http_content_len                "
                "[HTTP::header Content-Length]\n"
                "        set MRHSession_cookie               "
                "[HTTP::cookie value MRHSession]\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX method:      '
                '$http_method"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Src IP:      '
                '$src_ip"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX User-Agent:  '
                '$http_hdr_uagent"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP uri:    '
                '$http_uri"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP len:    '
                '$http_content_len"\n'
                "\n"
                "        if { ! [ info exists ECA_METADATA_ARG ] } "
                "{\n"
                "            # Generating argument for "
                "ECA::metadata\n"
                "            # The NTLM configuration name is "
                "derived from assigned virtual name with the "
                "algorithm as follows:\n"
                "            # <virtual-fullpath> ::= "
                '<folder-path>"/"<virtual-basename> as "/" is the '
                'last "/" char.\n'
                "            # <config-fullpath>  ::= "
                '<folder-path>"/" "exch_ntlm" "_" '
                "<virtual-basename>\n"
                "            # e.g.  Let us say the virtual name "
                'is "/prod/exch/vs1", The folder path is '
                '"/prod/exch/",\n'
                "            #       then object name will be "
                '"/prod/exch/exch_ntlm_vs1".\n'
                "            set vs_name [virtual name]\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX virtual:     '
                '$vs_name"\n'
                "            set slash_index [ string last / "
                "$vs_name ]\n"
                "            if { $slash_index == -1 } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Error: the virtual '
                'name does not contain folder information"\n'
                "                ACCESS::disable\n"
                "                TCP::close\n"
                "                return\n"
                "            }\n"
                "            set ECA_METADATA_ARG    "
                '"select_ntlm:"\n'
                "            append ECA_METADATA_ARG [ string "
                "range $vs_name 0 $slash_index ]\n"
                '            append ECA_METADATA_ARG "exch_ntlm_"\n'
                "            append ECA_METADATA_ARG [ string "
                "range $vs_name [ expr { $slash_index + 1 } ] end "
                "]\n"
                "            unset slash_index\n"
                "            unset vs_name\n"
                "        }\n"
                "\n"
                "        if { $use_auth == $static::USE_NTLM_AUTH "
                "} {\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Enable ECA: '
                '$ECA_METADATA_ARG"\n'
                "            ECA::enable\n"
                "            ECA::select $ECA_METADATA_ARG\n"
                "            return\n"
                "        } else {\n"
                "            set recvd_auth                      "
                "$static::RECVD_AUTH_NONE\n"
                "            set http_hdr_auth                   "
                "[HTTP::header Authorization]\n"
                "            set auth_data                       "
                '[split $http_hdr_auth " "]\n'
                '            if { $http_hdr_auth != "" } {\n'
                "                if { [ llength $auth_data ] == 2 "
                "} {\n"
                "                    set auth_scheme [ lindex "
                "$auth_data 0]\n"
                "                    if { [string equal -nocase "
                '$auth_scheme "ntlm" ] == 1 } {\n'
                "                        log -noname "
                "accesscontrol.local1.debug "
                "\"$static::ACCESS_LOG_PREFIX Recv'd HTTP NTLM "
                'Authentication"\n'
                "                        set recvd_auth          "
                "$static::RECVD_AUTH_NTLM\n"
                "                    } elseif { [ string equal "
                '-nocase [ lindex $auth_data 0] "basic" ] == 1 } '
                "{\n"
                "                        log -noname "
                "accesscontrol.local1.debug "
                "\"$static::ACCESS_LOG_PREFIX Recv'd HTTP Basic "
                'Authentication"\n'
                "                        set recvd_auth          "
                "$static::RECVD_AUTH_BASIC\n"
                "                        set user                "
                "[string tolower [HTTP::username]]\n"
                "                        set password            "
                "[HTTP::password]\n"
                "                    }\n"
                "                }\n"
                "            }\n"
                "            if { $use_auth == "
                "$static::USE_BASIC_AUTH } {\n"
                "                if { $recvd_auth == "
                "$static::RECVD_AUTH_BASIC } {\n"
                "                    # Defer the process until "
                "later\n"
                "                } else {\n"
                "                    HTTP::respond 401 -version "
                '1.1 noserver WWW-Authenticate "Basic '
                'realm=\\"$http_hdr_host\\"" \\\n'
                "                                Set-Cookie "
                "$static::ACCESS_DEL_COOKIE_HDR_VAL Connection "
                "Close\n"
                "                    return\n"
                "                }\n"
                "            } elseif { $use_auth == "
                "$static::USE_NTLM_BASIC_AUTH } {\n"
                "                if { ($recvd_auth == "
                "$static::RECVD_AUTH_NTLM) || "
                "($f_ntlm_auth_succeed == 1) } {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Enable ECA: '
                '$ECA_METADATA_ARG"\n'
                "                    ECA::enable\n"
                "                    ECA::select "
                "$ECA_METADATA_ARG\n"
                "                    return\n"
                "                } elseif { $recvd_auth == "
                "$static::RECVD_AUTH_BASIC } {\n"
                "                    # Defer the process until "
                "later\n"
                "                } else {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Request '
                'Authorization: NTLM + Basic"\n'
                "                    HTTP::respond 401 -version "
                '1.1 noserver WWW-Authenticate "Basic '
                'realm=\\"$http_hdr_host\\"" \\\n'
                "                                WWW-Authenticate "
                '"NTLM" Set-Cookie '
                "$static::ACCESS_DEL_COOKIE_HDR_VAL Connection "
                "Close\n"
                "                    return\n"
                "                }\n"
                "            }\n"
                "\n"
                "            # Disable NTLM auth\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Disable ECA"\n'
                "            ECA::disable\n"
                "            # Disable KCD sso\n"
                "            set f_disable_sso               1\n"
                "\n"
                '            if { $MRHSession_cookie != "" } {\n'
                "                if { [ACCESS::session exists "
                "-state_allow -sid $MRHSession_cookie] } {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *VALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "                    # Default profile access "
                "setting is false\n"
                "                    if { "
                "$PROFILE_RESTRICT_SINGLE_IP == 0 } {\n"
                "                        log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Release the request"\n'
                "                        return\n"
                "                    }\n"
                "                    elseif { [ IP::addr $src_ip "
                "equals [ ACCESS::session data get -sid "
                '$MRHSession_cookie "session.user.clientip" ] ] } '
                "{\n"
                "                        log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP matched. '
                'Release the request"\n'
                "                        return\n"
                "                    }\n"
                "                    else {\n"
                "                        log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP does not '
                'matched"\n'
                "                    }\n"
                "                }\n"
                "                else {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *INVALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "                }\n"
                "\n"
                '                set MRHSession_cookie ""\n'
                "                HTTP::cookie remove MRHSession\n"
                "            }\n"
                "\n"
                "            set user_key                {}\n"
                "            if { $PROFILE_RESTRICT_SINGLE_IP == 1 "
                "} {\n"
                "                append "
                "user_key                    $src_ip\n"
                "            }\n"
                "            append user_key                 "
                "$password\n"
                "            binary scan [md5 $user_key ] H* "
                "user_key\n"
                "            set user_key                    "
                '"$user.$user_key"\n'
                "\n"
                "            set apm_cookie_list             [ "
                "ACCESS::user getsid $user_key ]\n"
                "            if { [ llength $apm_cookie_list ] != "
                "0 } {\n"
                "                set MRHSession_cookie [ "
                "ACCESS::user getkey [ lindex $apm_cookie_list 0 ] "
                "]\n"
                '                if { $MRHSession_cookie != "" } '
                "{\n"
                "                    HTTP::cookie remove "
                "MRHSession \n"
                "                    HTTP::cookie insert name "
                "MRHSession value $MRHSession_cookie\n"
                "                    return\n"
                "                }\n"
                "            }\n"
                "\n"
                "            HTTP::cookie remove MRHSession\n"
                "            HTTP::header insert "
                '"clientless-mode"       1\n'
                "            HTTP::header insert "
                '"username"              $user\n'
                "            HTTP::header insert "
                '"password"              $password\n'
                "            return\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when ECA_REQUEST_ALLOWED {\n"
                "        set f_ntlm_auth_succeed                 "
                "1\n"
                "\n"
                '        if { $MRHSession_cookie == "" } {\n'
                "            # Retrieve from SID cache\n"
                "            set MRHSession_cookie   $sid_cache\n"
                "            HTTP::cookie insert name MRHSession "
                "value $sid_cache\n"
                "        }\n"
                "\n"
                '        if { $MRHSession_cookie != "" } {\n'
                "            # Destroy session ID cache. This "
                "client should not need session ID cache \n"
                '            if { ($sid_cache != "") && '
                "($sid_cache != $MRHSession_cookie) } {\n"
                '                set sid_cache   ""\n'
                "            }\n"
                "            if { [ ACCESS::session exists "
                "-state_allow $MRHSession_cookie ] } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *VALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "                # Default profile access setting "
                "is false\n"
                "                if { $PROFILE_RESTRICT_SINGLE_IP "
                "== 0 } {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Release the request"\n'
                "                    return\n"
                "                }\n"
                "                elseif { [ IP::addr $src_ip "
                "equals [ ACCESS::session data get -sid "
                '$MRHSession_cookie "session.user.clientip" ] ] } '
                "{\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP matched. '
                'Release the request"\n'
                "                    return\n"
                "                }\n"
                "                else {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP does not '
                'matched"\n'
                "                }\n"
                "            } else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *INVALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "            }\n"
                "        }\n"
                "\n"
                '        set MRHSession  ""\n'
                '        set sid_cache   ""\n'
                "        HTTP::cookie remove MRHSession\n"
                "\n"
                "        # Build user_key\n"
                "        set    user_key                 {}\n"
                "        append user_key                 [string "
                'tolower [ECA::username]] "@" [ string tolower '
                "[ECA::domainname] ]\n"
                "        if { $PROFILE_RESTRICT_SINGLE_IP == 0 } "
                "{\n"
                '            append user_key             ":" '
                "$src_ip\n"
                "        }\n"
                '        append user_key                 ":" '
                "[ECA::client_machine_name]\n"
                "\n"
                "        set apm_cookie_list             [ "
                "ACCESS::user getsid $user_key ]\n"
                "        if { [ llength $apm_cookie_list ] != 0 } "
                "{\n"
                "            set MRHSession_cookie [ ACCESS::user "
                "getkey [ lindex $apm_cookie_list 0 ] ]\n"
                '            if { $MRHSession_cookie != "" } {\n'
                "                set sid_cache           "
                "$MRHSession_cookie\n"
                "                HTTP::cookie insert name "
                "MRHSession value $MRHSession_cookie\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX APM Cookie found: '
                '$sid_cache"\n'
                "                return\n"
                "            }\n"
                "        }\n"
                "        unset apm_cookie_list\n"
                "\n"
                "        set try                         1\n"
                "        set start_policy_str            $src_ip\n"
                "        append start_policy_str         "
                "[TCP::client_port]\n"
                "\n"
                "        while { $try <=  "
                "$static::POLICY_RESULT_POLL_MAXRETRYCYCLE } {\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX NO APM Cookie found"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Trying #$try for '
                '$http_method $http_uri $http_content_len"\n'
                "\n"
                "            if { $http_content_len > "
                "$static::FIRST_BIG_POST_CONTENT_LEN } {\n"
                "                # Wait at below\n"
                "            } else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX EXEC: table set '
                "-notouch -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME -excl $user_key "
                "$start_policy_str $PROFILE_POLICY_TIMEOUT "
                '$PROFILE_MAX_SESS_TIMEOUT"\n'
                "                set policy_status [table set "
                "-notouch -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME -excl $user_key "
                "$start_policy_str $PROFILE_POLICY_TIMEOUT "
                "$PROFILE_MAX_SESS_TIMEOUT]\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX DONE: table set '
                "-notouch -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME -excl $user_key "
                "$start_policy_str $PROFILE_POLICY_TIMEOUT "
                '$PROFILE_MAX_SESS_TIMEOUT"\n'
                "                if { $policy_status == "
                "$start_policy_str } {\n"
                "                    # ACCESS Policy has not "
                "started. Start one\n"
                "                    HTTP::header insert "
                '"clientless-mode"    1\n'
                "                    break\n"
                "                } elseif { $policy_status == "
                "$static::POLICY_SUCCEED } {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX table is out-of-sync '
                'retry"\n'
                "                    table delete -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key\n"
                "                    continue\n"
                "                } elseif { $policy_status == "
                "$static::POLICY_FAILED } {\n"
                "                    ACCESS::disable\n"
                "                    TCP::close\n"
                "                    return\n"
                "                }\n"
                "                # Wait at below\n"
                "            }\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Waiting  '
                "$static::POLICY_RESULT_POLL_INTERVAL ms for "
                '$http_method $http_uri"\n'
                "            # Touch the entry table\n"
                "            table lookup -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key\n"
                "            after  "
                "$static::POLICY_RESULT_POLL_INTERVAL\n"
                "\n"
                "            set apm_cookie_list             [ "
                "ACCESS::user getsid $user_key ]\n"
                "            if { [ llength $apm_cookie_list ] != "
                "0 } {\n"
                "                set MRHSession_cookie [ "
                "ACCESS::user getkey [ lindex $apm_cookie_list 0 ] "
                "]\n"
                '                if { $MRHSession_cookie != "" } '
                "{\n"
                "                    set sid_cache           "
                "$MRHSession_cookie\n"
                "                    HTTP::cookie insert name "
                "MRHSession value $MRHSession_cookie\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX APM Cookie found: '
                '$sid_cache"\n'
                "                    return\n"
                "                }\n"
                "            }\n"
                "\n"
                "            incr try\n"
                "        }\n"
                "\n"
                "        if { $try >  "
                "$static::POLICY_RESULT_POLL_MAXRETRYCYCLE } {\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Policy did not finish '
                "in [ expr { "
                "$static::POLICY_RESULT_POLL_MAXRETRYCYCLE * "
                "$static::POLICY_RESULT_POLL_INTERVAL } ] ms. "
                'Close connection for $http_method $http_uri"\n'
                "            table delete -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key\n"
                "            ACCESS::disable\n"
                "            TCP::close\n"
                "            return\n"
                "        }\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Releasing request '
                '$http_method $http_uri"\n'
                "\n"
                "        unset try\n"
                "        unset start_policy_str\n"
                "    }\n"
                "\n"
                "    when ECA_REQUEST_DENIED {\n"
                "        set f_ntlm_auth_succeed                 "
                "0\n"
                "    }\n"
                "\n"
                "    when HTTP_RESPONSE_RELEASE {\n"
                "        if { ! [info exists user_key] } {\n"
                "            return\n"
                "        }\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP response: '
                'status:           [HTTP::status]"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP response: '
                'Server:           [HTTP::header Server]"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP response: '
                'Content-Length:   [HTTP::header Content-Length]"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP response: '
                "WWW-Authenticate: [HTTP::header "
                'WWW-Authenticate]"\n'
                "    }\n"
                "\n"
                "    when ACCESS_SESSION_STARTED {\n"
                "        if { [ info exists user_key ] } {\n"
                "            ACCESS::session data set "
                '"session.user.uuid" $user_key\n'
                "            ACCESS::session data set "
                '"session.user.microsoft-exchange-client" 1\n'
                "        }\n"
                "    }\n"
                "\n"
                "    when ACCESS_ACL_ALLOWED {\n"
                "        if { [ info exists f_disable_sso ] && "
                "$f_disable_sso == 1 } {\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Disable WEBSSO"\n'
                "            WEBSSO::disable\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when ACCESS_POLICY_COMPLETED {\n"
                "        if { ! [ info exists user_key ] } {\n"
                "            return\n"
                "        }\n"
                "\n"
                '        set user_key_value ""\n'
                "        set f_delete_session 0\n"
                "        set policy_result [ACCESS::policy "
                "result]\n"
                "        set sid [ ACCESS::session sid ]\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX '
                "ACCESS_POLICY_COMPLETED: policy_result = "
                '\\"$policy_result\\" user_key = \\"$user_key\\" '
                'sid = \\"$sid\\""\n'
                "\n"
                "        switch $policy_result {\n"
                '        "allow" {\n'
                "            set user_key_value          $sid\n"
                "            set sid_cache               "
                "$user_key_value\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Result: Allow: '
                '$user_key"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX sid = $sid"\n'
                "\n"
                "        }\n"
                '        "deny" {\n'
                "            ACCESS::respond 401 content  "
                "$static::actsync_401_http_body Set-Cookie "
                "$static::ACCESS_DEL_COOKIE_HDR_VAL Connection "
                "Close\n"
                "            set f_delete_session  1\n"
                "        }\n"
                "        default {\n"
                "            ACCESS::respond 503 content  "
                "$static::actsync_503_http_body Connection Close\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Got unsupported '
                'policy result for $user_key ($sid)"\n'
                "            set f_delete_session  1\n"
                "        }\n"
                "        }\n"
                "\n"
                "        if { $f_ntlm_auth_succeed == 1 } {\n"
                '            if { $user_key_value != "" } {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Setting $user_key => '
                '$static::POLICY_SUCCEED"\n'
                "                table set -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key "
                "$static::POLICY_SUCCEED\n"
                "            } else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Setting $user_key => '
                "$static::POLICY_FAILED  "
                "$static::POLICY_DONE_WAIT_SEC "
                "$static::POLICY_DONE_WAIT_SEC_in table "
                '$static::ACCESS_USERKEY_TBLNAME"\n'
                "                table set -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key "
                "$static::POLICY_FAILED  "
                "$static::POLICY_DONE_WAIT_SEC "
                "$static::POLICY_DONE_WAIT_SEC\n"
                "            }\n"
                "        }\n"
                "\n"
                "        if { $f_delete_session == 1 } {\n"
                "            ACCESS::session remove\n"
                "            set f_delete_session 0\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Removing the session '
                'for $user_key."\n'
                "        }\n"
                "    }\n"
                "definition-signature "
                "X6dt8EqJFS+8GoWtne8ePfboJR+q5TILymdnfjtylTpC5BikvDFsa3VI6x0V/MP0lJDJrjotJPN2GTogthp48mnmZ2yg+zLskYONNC+vv5yQKc7SLmQf2Eoe8C2CJ8crBUOmfi0f+kjj1GboTVcxNAJ+tpPwb+KKTpnic7WPHo8F/LO5Ou0T5tsls8AmIE/dU0pSKhgit1h5gA+pfKoeA66fhRDcwrSAJ9d/odE55+s/LxJxZqG0PzOVE7HHdbeDiRdRYyBMJQ54Ri/tJuhWQJF/4BYi6V7ScWZQ+fyvFAgb3rRl9xgCqQK3gKQpwLRK11s6+L+PPEQx863YHOEobA==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_APM_ExchangeSupport_OA_NtlmAuth",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_APM_ExchangeSupport_OA_NtlmAuth",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_OA_NtlmAuth?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    # The purpose of this iRule is for help the "
                "main virtual for the timing of the HTTP request "
                "retry\n"
                "    # during the SSO process for OutlookAnywhere "
                "protocol request which has a Content-Length value "
                "of 1GB.\n"
                "\n"
                "    when HTTP_REQUEST {\n"
                "        #  Waiting for the first chunk of data.\n"
                "        HTTP::collect 1\n"
                "    }\n"
                "\n"
                "    when HTTP_REQUEST_DATA {\n"
                "        # Respond 401 and close the connection "
                "once we received the data.\n"
                "        HTTP::respond 401 WWW-Authenticate NTLM "
                "Connection close\n"
                "    }\n"
                "definition-signature "
                "qJiKrxH5xpBJr4VoBOszXDm+lvsjXtXlGXxiExuAyMkGwnIml1ED3xohHaNWu4/2/AAwX44zX2g3sr1cFx6yQeWIZVrkllxTSSqDqB9BYiLSO1kIn15vzpnj+bqzNTkvcl9fdu6yBT3Bz5X3EfCNLByKa059NQU2l/1StKK0e/KA0cCSAOzB4sh+BVI2VPPgL2R3XqoOrdgHHEE1PnBwC9WRk5Y5XFdaowpd2rfDoYBZM2C+MIxeryxMYLinXHfHbGaug4go8VX67eskI6XxWbm2fjXTBjTjMyxt7OpA6dc6S8IA3FJawUasvexJvHrdPyul2BMGRDqa+p6ZhOLzNw==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_APM_ExchangeSupport_helper",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_APM_ExchangeSupport_helper",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_helper?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    # Global variables\n"
                "    # static::POLICY_RESULT_CACHE_AUTHFAILED\n"
                "    #     Administrator can set this into 1, when "
                "there is a necessity to cache failed policy "
                "result.\n"
                "    #     This may be needed to avoid account "
                "locked caused by the Active Sync device when it "
                "uses wrong passwords.\n"
                "    #     One possible scenario, is that when the "
                "user changes the password in Active Directory, "
                "but missed to changed in their devices.\n"
                "    # Responses\n"
                "    # On denied result\n"
                "    #     Administrator can customize the "
                "responses to the device depends on more complex "
                "conditions when necessary.\n"
                "    #     In those cases, please use "
                "ACCESS::respond command.\n"
                "    #     The following is the syntax of "
                "ACCESS::respond\n"
                "    #     ACCESS::respond <status code> [ content "
                "<body> ] [ <Additional Header> <Additional Header "
                "value>* ]\n"
                "    #     e.g. ACCESS::respond 401 content "
                '"Error: Denied" WWW-Authenticate "basic '
                'realm=\\"f5.com\\"" Connection close\n'
                "    when RULE_INIT {\n"
                "        # Please set the following global "
                "variables for customized responses.\n"
                "        set static::actsync_401_http_body "
                '"<html><title>Authentication '
                "Failured</title><body>Error: Authentication "
                'Failure</body></html>"\n'
                "        set static::actsync_503_http_body "
                '"<html><title>Service is not '
                "available</title><body>Error: Service is not "
                'available</body></html>"\n'
                "        set "
                "static::ACCESS_LOG_PREFIX                 "
                '"01490000:7:"\n'
                "\n"
                "        # Second Virtual Server name for 401 NTLM "
                "responder\n"
                "        set "
                "static::ACCESS_SECOND_VIRTUAL_NAME        "
                '"_ACCESS_401_NTLM_responder_HTTPS"\n'
                "\n"
                "        set "
                "static::POLICY_INPROGRESS                 "
                '"policy_inprogress"\n'
                "        set "
                "static::POLICY_AUTHFAILED                 "
                '"policy_authfailed"\n'
                "        # The request with huge content length "
                "can not be used for starting ACCESS session.\n"
                "        # This kind of request will be put on "
                "hold, and this iRule will try to use another\n"
                "        # request to start the session. The "
                "following value is used for Outlook Anywhere.\n"
                "        set "
                "static::OA_MAGIC_CONTENT_LEN              "
                "1073741824\n"
                "\n"
                "        # Similar with OutlookAnywhere case, "
                "ACCESS can not use the request which is\n"
                "        # larger then following size. This "
                "becomes an issue with application that using\n"
                "        # Exchange Web Service as its main "
                "protocol such as Mac OS X applications\n"
                "        # (e.g. Mail app, Microsoft Entourage, "
                "etc)\n"
                "        # This kind of request will be put on "
                "hold, and this iRule will try to use another\n"
                "        # request to start the session.\n"
                "        set "
                "static::FIRST_BIG_POST_CONTENT_LEN        640000\n"
                "\n"
                "        # Set it into 1 if the backend EWS "
                "handler accepts HTTP Basic Authentication.\n"
                "        set "
                "static::EWS_BKEND_BASIC_AUTH              0\n"
                "        # Set it into 1 if the backend "
                "RPC-over-HTTP handler accepts HTTP Basic "
                "Authentication.\n"
                "        set "
                "static::RPC_OVER_HTTP_BKEND_BASIC_AUTH    0\n"
                "        # The following variable controls the "
                "polling mechanism.\n"
                "        set "
                "static::POLICY_RESULT_POLL_INTERVAL       250\n"
                "        set "
                "static::POLICY_RESULT_POLL_MAXRETRYCYCLE  600\n"
                "\n"
                "        # Set this global variable to 1 for "
                "caching authentication failure\n"
                "        # Useful for avoiding account locked "
                "out.\n"
                "        set "
                "static::POLICY_RESULT_CACHE_AUTHFAILED    0\n"
                "\n"
                "        # set this global variable to set "
                "alternative timeout for particular session\n"
                "        set "
                "static::POLICY_ALT_INACTIVITY_TIMEOUT     120\n"
                "\n"
                "        set "
                "static::ACCESS_USERKEY_TBLNAME            "
                '"_access_userkey"\n'
                "\n"
                "\n"
                "        set "
                "static::ACCESS_DEL_COOKIE_HDR_VAL         "
                '"MRHSession=deleted; expires=Thu, 01-Jan-1970 '
                '00:00:01 GMT; path=/"\n'
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"01490000:7: RPC_OVER_HTTP_BKEND_BASIC_AUTH = '
                '$static::RPC_OVER_HTTP_BKEND_BASIC_AUTH"\n'
                "        log -noname accesscontrol.local1.debug "
                '"01490000:7: EWS_BKEND_BASIC_AUTH = '
                '$static::EWS_BKEND_BASIC_AUTH"\n'
                "    }\n"
                "    when ACCESS_ACL_ALLOWED {\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX [HTTP::method] '
                '[HTTP::uri] [HTTP::header Content-Length]"\n'
                "\n"
                "        if { [ info exists f_rpc_over_http ] && "
                "$f_rpc_over_http == 1 }  {\n"
                "            if { "
                "$static::RPC_OVER_HTTP_BKEND_BASIC_AUTH == 0 } {\n"
                "                if { [ info exists "
                "f_oa_magic_content_len ] && "
                "$f_oa_magic_content_len == 1 } {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Use this virtual '
                "$static::ACCESS_SECOND_VIRTUAL_NAME just once. "
                'Will be reset back after disconnection."\n'
                "                    use virtual "
                "$static::ACCESS_SECOND_VIRTUAL_NAME\n"
                "                }\n"
                "               log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Remove HTTP Auth '
                'header"\n'
                "               HTTP::header remove Authorization\n"
                "            }\n"
                "        }\n"
                "        # MSFT Exchange's EWS request handler "
                "always requesting NTLM even the connection has "
                "been\n"
                "        # already authenticated if there is a "
                "HTTP Basic Auth in the request.\n"
                "        if { [ info exists f_exchange_web_service "
                "] && $f_exchange_web_service  == 1 }  {\n"
                "            if { $static::EWS_BKEND_BASIC_AUTH == "
                "0 } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Removing HTTP Basic '
                'Authorization header"\n'
                "                HTTP::header remove "
                "Authorization\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when HTTP_REQUEST {\n"
                "        set http_path                       [ "
                "string tolower [HTTP::path] ]\n"
                "        set f_clientless_mode               0\n"
                "        set f_alt_inactivity_timeout        0\n"
                "        set f_rpc_over_http                 0\n"
                "        set f_exchange_web_service          0\n"
                "        set f_auto_discover                 0\n"
                "        set f_activesync                    0\n"
                "        set f_offline_address_book          0\n"
                "        set f_availability_service          0\n"
                "\n"
                "        #  Here put appropriate pool when "
                "necessary.\n"
                "        switch -glob $http_path {\n"
                '        "/rpc/rpcproxy.dll" {\n'
                "            # Supports for RPC over HTTP. "
                "(Outlook Anywhere)\n"
                "            set f_rpc_over_http 1\n"
                "        }\n"
                '        "/autodiscover/autodiscover.xml" {\n'
                "            # Supports for Auto Discover "
                "protocol.\n"
                "            set f_auto_discover 1\n"
                "            # This request does not require long "
                "inactivity timeout.\n"
                "            # Don't use this for now\n"
                "            set f_alt_inactivity_timeout 0\n"
                "        }\n"
                '        "/microsoft-server-activesync" {\n'
                "            # Supports for ActiveSync\n"
                "            set f_activesync 1\n"
                "        }\n"
                '        "/oab/*" {\n'
                "            # Supports for Offline Address Book\n"
                "            set f_offline_address_book 1\n"
                "        }\n"
                '        "/ews/*" {\n'
                "            # Support for Exchange Web Service\n"
                "            # Outlook's Availability Service "
                "borrows this protocol.\n"
                "            set f_exchange_web_service 1\n"
                "        }\n"
                '        "/as/*" {\n'
                "            # Support for Availability Service.\n"
                "            # do nothing for now. (Untested)\n"
                "            set f_availability_service 1\n"
                "        }\n"
                "        default {\n"
                "            return\n"
                "        }\n"
                "        }\n"
                "\n"
                "        set f_reqside_set_sess_id           0\n"
                "        set http_method                     "
                "[HTTP::method]\n"
                "        set http_hdr_host                   "
                "[HTTP::host]\n"
                "        set http_hdr_uagent                 "
                "[HTTP::header User-Agent]\n"
                "        set src_ip                          "
                "[IP::remote_addr]\n"
                "        set http_uri                        "
                "[HTTP::uri]\n"
                "        set http_content_len                "
                "[HTTP::header Content-Length]\n"
                "        set MRHSession_cookie               "
                "[HTTP::cookie value MRHSession]\n"
                '        set auth_info_b64enc                ""\n'
                "\n"
                "        if { ! [ info exists "
                "PROFILE_POLICY_TIMEOUT ] } {\n"
                "            set PROFILE_POLICY_TIMEOUT            "
                "[PROFILE::access access_policy_timeout]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_MAX_SESS_TIMEOUT ] } {\n"
                "            set PROFILE_MAX_SESS_TIMEOUT          "
                "[PROFILE::access max_session_timeout]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_RESTRICT_SINGLE_IP ] } {\n"
                "            set PROFILE_RESTRICT_SINGLE_IP        "
                "1\n"
                "        }\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX method: '
                '$http_method"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Src IP: $src_ip"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX User-Agent: '
                '$http_hdr_uagent"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP uri: $http_uri"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP len: '
                '$http_content_len"\n'
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX '
                "Restrict-to-single-client-ip: "
                '$PROFILE_RESTRICT_SINGLE_IP"\n'
                "\n"
                "        # First, do we have valid MRHSession "
                "cookie.\n"
                '        if { $MRHSession_cookie != "" } {\n'
                "            if { [ACCESS::session exists "
                "-state_allow -sid $MRHSession_cookie] } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *VALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "            } else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *INVALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                '                set MRHSession_cookie ""\n'
                "                HTTP::cookie remove MRHSession\n"
                "            }\n"
                "        }\n"
                "\n"
                "        set http_hdr_auth [HTTP::header "
                "Authorization]\n"
                "        if { [ string match -nocase {basic *} "
                "$http_hdr_auth ] != 1 } {\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Not basic '
                'authentication. Ignore received auth header"\n'
                '            set http_hdr_auth ""\n'
                "        }\n"
                "\n"
                '        if { $http_hdr_auth == "" } {\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX No/Empty Auth '
                'header"\n'
                "            # clean up the cookie\n"
                '            if { $MRHSession_cookie == "" } {\n'
                "                HTTP::respond 401 content  "
                "$static::actsync_401_http_body WWW-Authenticate "
                '"Basic realm=\\"[HTTP::header Host]\\"" '
                "Set-Cookie $static::ACCESS_DEL_COOKIE_HDR_VAL "
                "Connection close\n"
                "                return\n"
                "            }\n"
                "            # Do nothing if we have a valid "
                "MRHSession cookie.\n"
                "        }\n"
                "\n"
                "        set f_release_request           0\n"
                "        # Optimization for clients which support "
                "cookie\n"
                '        if { $MRHSession_cookie != "" } {\n'
                "            # Default profile access setting is "
                "false\n"
                "            if { $PROFILE_RESTRICT_SINGLE_IP == 0 "
                "} {\n"
                "                set f_release_request 1\n"
                "            }\n"
                "            elseif { [ IP::addr $src_ip equals [ "
                "ACCESS::session data get -sid $MRHSession_cookie "
                '"session.user.clientip" ] ] } {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP matched"\n'
                "                set f_release_request 1\n"
                "            }\n"
                "            else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP does not '
                'matched"\n'
                '                set MRHSession_cookie ""\n'
                "                HTTP::cookie remove MRHSession\n"
                "            }\n"
                "        }\n"
                "\n"
                "        if { $f_release_request == 0 } {\n"
                "            set apm_username [ string tolower "
                "[HTTP::username]]\n"
                "            set apm_password [HTTP::password]\n"
                "            if { $PROFILE_RESTRICT_SINGLE_IP == 0 "
                "} {\n"
                '                binary scan [md5 "$apm_password"] '
                "H* user_hash\n"
                "            } else {\n"
                "                binary scan [md5 "
                '"$apm_password$src_ip"] H* user_hash\n'
                "            }\n"
                "\n"
                "            set user_key    {}\n"
                '            append user_key $apm_username "." '
                "$user_hash\n"
                "            unset user_hash\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP Hdr Auth: '
                '$http_hdr_auth"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX apm_username: '
                '$apm_username"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX user_key = '
                '$user_key"\n'
                "            set apm_cookie_list             [ "
                "ACCESS::user getsid $user_key ]\n"
                "            if { [ llength $apm_cookie_list ] != "
                "0 } {\n"
                "                set apm_cookie [ ACCESS::user "
                "getkey [ lindex $apm_cookie_list 0 ] ]\n"
                '                if { $apm_cookie != "" } {\n'
                "                    HTTP::cookie insert name "
                "MRHSession value $apm_cookie\n"
                "                    set f_release_request 1\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "\n"
                "        if { $http_content_len ==  "
                "$static::OA_MAGIC_CONTENT_LEN } {\n"
                "            set f_oa_magic_content_len 1\n"
                "        }\n"
                "\n"
                "        set f_sleep_here 0\n"
                "        set retry 1\n"
                "\n"
                "        while { $f_release_request == 0 && $retry "
                "<=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } "
                "{\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Trying #$retry for '
                '$http_method $http_uri $http_content_len"\n'
                "\n"
                "            # This is also going to touch the "
                "table entry timer.\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Reading $user_key '
                'from table $static::ACCESS_USERKEY_TBLNAME"\n'
                "\n"
                "            set apm_cookie [table lookup "
                "-subtable  $static::ACCESS_USERKEY_TBLNAME "
                "-notouch $user_key]\n"
                '            if { $apm_cookie != "" } {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Verifying table '
                'cookie = $apm_cookie"\n'
                "\n"
                "                # Accessing SessionDB is not that "
                "cheap. Here we are trying to check known value.\n"
                "                if { $apm_cookie == "
                '"policy_authfailed" || $apm_cookie == '
                '"policy_inprogress"} {\n'
                "                    # Do nothing\n"
                "                } elseif  { ! [ ACCESS::session "
                "exists $apm_cookie ] } {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX table cookie = '
                '$apm_cookie is out-of-sync"\n'
                "                    # Table value is out of sync. "
                "Ignores it.\n"
                '                    set apm_cookie ""\n'
                "                }\n"
                "            }\n"
                "\n"
                "            switch $apm_cookie {\n"
                '            "" {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX NO APM Cookie found"\n'
                "\n"
                "                if { [ info exists "
                "f_oa_magic_content_len ] && "
                "$f_oa_magic_content_len == 1 } {\n"
                "                    # Outlook Anywhere request "
                "comes in pair. The one with 1G payload is not "
                "usable\n"
                "                    # for creating new session "
                "since 1G content-length is intended for client to "
                "upload\n"
                "                    # the data when needed.\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Start to wait '
                "$static::POLICY_RESULT_POLL_INTERVAL ms for "
                'request with magic content-len"\n'
                "                    set f_sleep_here 1\n"
                "                } elseif { [ info exists "
                "f_exchange_web_service ] && "
                "$f_exchange_web_service == 1 && $http_content_len "
                "> $static::FIRST_BIG_POST_CONTENT_LEN } {\n"
                "                    # Here we are getting large "
                "EWS request, which can't be used for starting new "
                "session\n"
                "                    # in clientless-mode. Have it "
                "here waiting for next smaller one.\n"
                "                    # We are holding the request "
                "here in HTTP filter, and HTTP filter "
                "automatically\n"
                "                    # clamping down the TCP "
                "window when necessary.\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Start to wait '
                "$static::POLICY_RESULT_POLL_INTERVAL ms for big "
                'EWS request"\n'
                "                    set f_sleep_here 1\n"
                "                } else {\n"
                "                   set apm_cookie               "
                '"policy_inprogress"\n'
                "                   set f_reqside_set_sess_id    "
                "1\n"
                "                   set f_release_request        "
                "1\n"
                "                }\n"
                "            }\n"
                '            "policy_authfailed" {\n'
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Found $user_key with '
                'AUTH_FAILED"\n'
                "                HTTP::respond 401 content  "
                "$static::actsync_401_http_body\n"
                "                set f_release_request 1\n"
                "            }\n"
                '            "policy_inprogress" {\n'
                "                if { [ info exists f_activesync ] "
                "&& ($f_activesync == 1) } {\n"
                "                    # For ActiveSync requests, "
                "aggressively starts new session.\n"
                "                    set f_reqside_set_sess_id    "
                "1\n"
                "                    set f_release_request        "
                "1\n"
                "                } else {\n"
                "                    set f_sleep_here 1\n"
                "                }\n"
                "            }\n"
                "            default {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Using MRHSession = '
                '$apm_cookie"\n'
                "                HTTP::header insert Cookie "
                '"MRHSession=$apm_cookie"\n'
                "                set f_release_request 1\n"
                "            }\n"
                "            }\n"
                "\n"
                "            if { $f_reqside_set_sess_id == 1 } {\n"
                "                set f_reqside_set_sess_id 0\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Setting '
                "$user_key=$apm_cookie $PROFILE_POLICY_TIMEOUT "
                '$PROFILE_MAX_SESS_TIMEOUT"\n'
                "                set f_clientless_mode 1\n"
                "                HTTP::cookie remove MRHSession\n"
                "                HTTP::header insert "
                '"clientless-mode" 1\n'
                '                HTTP::header insert "username" '
                "$apm_username\n"
                '                HTTP::header insert "password" '
                "$apm_password\n"
                "                table set -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key "
                "$apm_cookie $PROFILE_POLICY_TIMEOUT "
                "$PROFILE_MAX_SESS_TIMEOUT\n"
                "            }\n"
                "\n"
                "            if { $f_sleep_here == 1 } {\n"
                "                set f_sleep_here 0\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Waiting  '
                "$static::POLICY_RESULT_POLL_INTERVAL ms for "
                '$http_method $http_uri"\n'
                "                after  "
                "$static::POLICY_RESULT_POLL_INTERVAL\n"
                "            }\n"
                "\n"
                "            incr retry\n"
                "        }\n"
                "\n"
                "        if { $f_release_request == 0 && $retry "
                ">=  $static::POLICY_RESULT_POLL_MAXRETRYCYCLE } "
                "{\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Policy did not finish '
                "in [expr { "
                "$static::POLICY_RESULT_POLL_MAXRETRYCYCLE * "
                "$static::POLICY_RESULT_POLL_INTERVAL } ] ms. "
                'Close connection for $http_method $http_uri"\n'
                "\n"
                "            table delete -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key\n"
                "            ACCESS::disable\n"
                "            TCP::close\n"
                "            return\n"
                "        }\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Releasing request '
                '$http_method $http_uri"\n'
                "    }\n"
                "\n"
                "    when ACCESS_SESSION_STARTED {\n"
                "        if { [ info exists user_key ] } {\n"
                "            ACCESS::session data set "
                '"session.user.uuid" $user_key\n'
                "            ACCESS::session data set "
                '"session.user.microsoft-exchange-client" 1\n'
                "\n"
                "            if { [ info exists f_activesync ] && "
                "$f_activesync == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-activesync" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_auto_discover ] && $f_auto_discover == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-autodiscover" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_availability_service ] && "
                "$f_availability_service == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-availabilityservice" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_rpc_over_http ] && $f_rpc_over_http == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-rpcoverhttp" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_offline_address_book ] && "
                "$f_offline_address_book == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-offlineaddressbook" 1\n'
                "            }\n"
                "            elseif { [ info exists "
                "f_exchange_web_service ] && "
                "$f_exchange_web_service == 1 } {\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-exchangewebservice" 1\n'
                "            }\n"
                "        }\n"
                "        if { [ info exists "
                "f_alt_inactivity_timeout ] && "
                "$f_alt_inactivity_timeout == 1 } {\n"
                "            ACCESS::session data set "
                '"session.inactivity_timeout"  '
                "$static::POLICY_ALT_INACTIVITY_TIMEOUT\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when HTTP_RESPONSE {\n"
                "        if { [ info exists f_auto_discover ] && "
                "$f_auto_discover == 1 } {\n"
                "            set content_len [ HTTP::header "
                "Content-Length ]\n"
                "            if {  $content_len > 0 } {\n"
                "                HTTP::collect $content_len\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "    when HTTP_RESPONSE_DATA {\n"
                "        if { [ info exists f_auto_discover ] && "
                "$f_auto_discover == 1 } {\n"
                "            if { [ regsub -line "
                "{<AuthPackage>Ntlm</AuthPackage>} [ HTTP::payload "
                "] {<AuthPackage>Basic</AuthPackage>} payload ] != "
                "0 } {\n"
                "                HTTP::payload replace 0 "
                "$content_len $payload\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "    when ACCESS_POLICY_COMPLETED {\n"
                "        if { ! [ info exists user_key ] } {\n"
                "            return\n"
                "        }\n"
                "\n"
                '        set user_key_value ""\n'
                "        set f_delete_session 0\n"
                "        set policy_result [ACCESS::policy "
                "result]\n"
                "        set sid [ ACCESS::session sid ]\n"
                "\n"
                "        log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX '
                "ACCESS_POLICY_COMPLETED: policy_result = "
                '\\"$policy_result\\" user_key = \\"$user_key\\" '
                'sid = \\"$sid\\""\n'
                "\n"
                "        set inactivity_timeout [ACCESS::session "
                'data get "session.inactivity_timeout"]\n'
                "        set max_sess_timeout [ACCESS::session "
                'data get "session.max_session_timeout"]\n'
                '        if { $max_sess_timeout == "" } {\n'
                "             set max_sess_timeout "
                "$PROFILE_MAX_SESS_TIMEOUT\n"
                "        }\n"
                "\n"
                "        switch $policy_result {\n"
                '        "allow" {\n'
                "            # We depends on this table record "
                "self-cleanup capability in order to\n"
                "            # indirectly sync with session DB.\n"
                "            set user_key_value $sid\n"
                "\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Result: Allow: '
                "$user_key => $sid $inactivity_timeout "
                '$max_sess_timeout"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX user_key_value = '
                '$user_key_value"\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX sid = $sid"\n'
                "        }\n"
                '        "deny" {\n'
                "            # When necessary the admin here can "
                "check appropriate session variable\n"
                "            # and decide what response more "
                "appropriate then this default response.\n"
                "            ACCESS::respond 401 content  "
                "$static::actsync_401_http_body Set-Cookie "
                "$static::ACCESS_DEL_COOKIE_HDR_VAL Connection "
                "close\n"
                "            if {  "
                "$static::POLICY_RESULT_CACHE_AUTHFAILED == 1 } {\n"
                "                set user_key_value  "
                "$static::POLICY_AUTHFAILED\n"
                "            } else {\n"
                "                set f_delete_session  1\n"
                "            }\n"
                "        }\n"
                "        default {\n"
                "            ACCESS::respond 503 content  "
                "$static::actsync_503_http_body Connection close\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Got unsupported '
                'policy result for $user_key ($sid)"\n'
                "            set f_delete_session  1\n"
                "        }\n"
                "        }\n"
                '        if { $user_key_value != "" } {\n'
                "           log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Setting $user_key => '
                "$user_key_value $inactivity_timeout "
                "$max_sess_timeout in table "
                '$static::ACCESS_USERKEY_TBLNAME"\n'
                "\n"
                "           table set -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key "
                "$user_key_value $inactivity_timeout "
                "$max_sess_timeout\n"
                "        } else {\n"
                "           log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Deleting $user_key in '
                'table $static::ACCESS_USERKEY_TBLNAME"\n'
                "\n"
                "           table delete -subtable  "
                "$static::ACCESS_USERKEY_TBLNAME $user_key\n"
                "        }\n"
                "\n"
                "        if { $f_delete_session == 1 } {\n"
                "           ACCESS::session remove\n"
                "           set f_delete_session 0\n"
                "           log -noname accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Removing the session '
                'for $user_key."\n'
                "        }\n"
                "    }\n"
                "definition-signature "
                "ITBkr3SVPYk5UZu6F9TDEQuWGp64htd0HDsL3WNUHQqaVbu0m1tox3dTyf9X8y1MSr2KIbUfOIovCbiSXqnWRTAnSMqESm2gwlMBNCBOxTsh3AD83JE2N08jZjnC/jjnl4HRsq71uBbyHLZiL+mp1wXDtxUBUOfh7G/NUs9BajAVgQM7Vx9/Ogs+zX6ag08CXOjWwgPL5hRezZJwZEp1AXM8YrSbyT456P6axwWsB015wqJXvwpRKWcQ7sHEvkbbd928Q3koLevE6ecByjezjphomokwmi813aA7WCNbG6Tl+3YznsYAgxn2Skv0Gq7pMfoj9QFt/a39RXGyHOhRcQ==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_APM_ExchangeSupport_main",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_APM_ExchangeSupport_main",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_ExchangeSupport_main?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012, 2016-2017.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "# Supporting MS-OFBA protocol for native office "
                "applications.\n"
                "# sys_APM_MS_Office_OFBA_DG - iRule data group to "
                "customize ofba user agent strings and\n"
                "#                     few other parameters.\n"
                "#\n"
                "# sys_APM_MS_Office_OFBA_DG::useragent - "
                "useragent strings are mandatory, \n"
                "#       these strings are used to detect OFBA "
                "clients. All user agent strings should start\n"
                "#       with useragent name, for e.g: useragent1, "
                "useragent2.. etc.\n"
                "#\n"
                "# "
                "sys_APM_MS_Office_OFBA_DG::ie_sp_session_sharing_enabled "
                "- Parameter to specify whether to enable or\n"
                "#       disable IE session sharing using "
                'persistent cookie named "MRHSOffice".\n'
                "#       Default is disabled (0), value can be 0 "
                "or 1\n"
                "#     \n"
                "# "
                "sys_APM_MS_Office_OFBA_DG::ie_sp_session_sharing_inactivity_timeout "
                "- inactivity timeout value \n"
                "#       for the persistent cookie value "
                '"MRHSOffice"\n'
                "#       everytime, the SharePoint site refreshes "
                "or gets any response from\n"
                "#       SharePoint Server.  Value can be any "
                "positive value given in seconds.\n"
                "#       Default value as 60 secs\n"
                "#\n"
                "# "
                "sys_APM_MS_Office_OFBA_DG::ofba_auth_dialog_size "
                "- OFBA dialog browser\n"
                "#       resolution size given as widthxheight, "
                "default 800x600\n"
                "#\n"
                "# static::MS_OFBA_ENABLED_CLIENT_TYPE - "
                '"ms-ofba-compliant" session variable\n'
                "#       value that can be used in Access policy "
                "Logon agent branch, to add the required "
                "authentication\n"
                "#       for MS OFBA compliant applications.\n"
                "#\n"
                "    proc write_log {level message} {\n"
                "\n"
                '        ACCESS::log $level "\\[MSOFBA\\] '
                '$message"\n'
                "#       Logs printing for 12.x or older releases\n"
                "#       log -noname accesscontrol.local1.$level "
                '"01490000: \\[MSOFBA\\] $message"\n'
                "    }\n"
                "\n"
                "    proc is_ofba_passthrough_uri {uri} {\n"
                "        for { set i 0 } { $i < [llength "
                "$static::MS_OFBA_PASSTHROUGH_URI_LIST] } { incr i "
                "} {\n"
                "            if { $uri == [lindex "
                "$static::MS_OFBA_PASSTHROUGH_URI_LIST $i] } {\n"
                "                return 1;\n"
                "            }\n"
                "        }\n"
                "        return 0\n"
                "    }\n"
                "\n"
                "    when RULE_INIT {\n"
                "        set static::MS_OFBA_ENABLED_CLIENT_TYPE "
                '"ms-ofba-compliant"\n'
                "        set static::MS_OFBA_AUTH_REQ_URI "
                '"/ms-ofba-req-auth"\n'
                "        set static::MS_OFBA_AUTH_RETURN_URI "
                '"/ms-ofba-auth-success"\n'
                "        set static::MS_OFBA_AUTH_DIALOG_SZ "
                '"800x600"\n'
                "        set static::MS_OFBA_AUTH_SUCCESS_BODY "
                '"<html><head><title>User '
                "Authenticated</title></head><body><b>Successful "
                'OFBA authentication</b></body></html>"\n'
                "        set static::MS_OFBA_IRULE_DG "
                '"sys_APM_MS_Office_OFBA_DG"\n'
                "        set static::MULTI_DOMAIN_AUTH_RESP_URI "
                '"/f5networks-sso-resp"\n'
                "        set static::MS_OFBA_PASSTHROUGH_URI_LIST "
                "{$static::MULTI_DOMAIN_AUTH_RESP_URI "
                '"/my.status.eps" "/my.report.eps"}\n'
                "# sp_persistent_ck: would help to share the "
                "session from sharepoint site to\n"
                "# office applications, if enabled.\n"
                "        set static::SP_PERSISTENT_CK "
                '"MRHSOffice"\n'
                "        set static::SP_PERSISTENT_CK_TIMEOUT 60\n"
                "        set static::MS_OFBA_AUTH_TYPE_COOKIE "
                '"Auth-Type"\n'
                "        set "
                'static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE "ms-ofba"\n'
                "    }\n"
                "\n"
                "    when CLIENT_ACCEPTED {\n"
                "        if { ![info exists ofba_user_agent_list] "
                "} {\n"
                "# check for config change from datagroup\n"
                "# since this iRule is read-only, dg config change "
                "is done in CLIENT_ACCEPTED rather than in "
                "RULE_INIT\n"
                "            set ofba_user_agent_list [class "
                "search -value -all $static::MS_OFBA_IRULE_DG "
                "starts_with useragent]\n"
                "            set f_sp_persistent_ck [class search "
                "-value $static::MS_OFBA_IRULE_DG equals "
                "ie_sp_session_sharing_enabled]\n"
                "            set sp_persistent_ck_timeout [class "
                "search -value $static::MS_OFBA_IRULE_DG equals "
                "ie_sp_session_sharing_inactivity_timeout]\n"
                "            set ofba_auth_dialog_sz [class search "
                "-value $static::MS_OFBA_IRULE_DG equals "
                "ofba_auth_dialog_size]\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when HTTP_REQUEST {\n"
                "# client detection, for ofba client\n"
                '        set ms_sp_client_type "none"\n'
                "        set http_path [string tolower "
                "[HTTP::path]]\n"
                "        set http_user_agent [string tolower "
                '[HTTP::header "User-Agent"]]\n'
                "        set session_id [HTTP::cookie value "
                '"MRHSession"]\n'
                "        set f_allow_session 0\n"
                '        set ms_ofba_auth_cookie ""\n'
                "\n"
                "        if {[HTTP::header exists "
                '"X-FORMS_BASED_AUTH_ACCEPTED"] &&\n'
                "            (([HTTP::header "
                '"X-FORMS_BASED_AUTH_ACCEPTED"] equals "t") ||\n'
                "             ([HTTP::header "
                '"X-FORMS_BASED_AUTH_ACCEPTED"] equals "f"))} {\n'
                '                set ms_sp_client_type "ms-ofba"\n'
                "            } elseif { $http_path == "
                "$static::MS_OFBA_AUTH_REQ_URI } {\n"
                '                set ms_sp_client_type "ms-ofba"\n'
                "            } else {\n"
                "                if {(!($http_user_agent contains "
                '"frontpage") && [string match -nocase {*mozilla*} '
                "$http_user_agent]) ||\n"
                "                    [string match -nocase "
                "{*opera*} $http_user_agent]} {\n"
                "                        set ms_sp_client_type "
                '"browser"\n'
                "                        set ms_ofba_auth_cookie "
                "[HTTP::cookie value "
                "$static::MS_OFBA_AUTH_TYPE_COOKIE]\n"
                "                        if { $ms_ofba_auth_cookie "
                "== $static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE } {\n"
                "                            # ofba authentication "
                "is still in progress, there may be a case where "
                "initial\n"
                "                            # access denied and "
                "user is retrying the session without closing the "
                "ofba\n"
                "                            # initiated browser\n"
                "                            set ms_sp_client_type "
                '"ms-ofba"\n'
                "                            call write_log debug "
                '"Detecting the client type as ms-ofba based auth '
                'type cookie"\n'
                "                        }\n"
                "                    } else {\n"
                "                        foreach ofba_user_agent "
                "$ofba_user_agent_list {\n"
                "                            set ofba_user_agent "
                "[string trim $ofba_user_agent]\n"
                "                            if { $ofba_user_agent "
                '!= "" && [string match -nocase *$ofba_user_agent* '
                "$http_user_agent] } {\n"
                "                                set "
                'ms_sp_client_type "ms-ofba"\n'
                "                                    break\n"
                "                            }\n"
                "                        }\n"
                "                    }\n"
                "            }\n"
                "\n"
                '        if { $ms_sp_client_type == "ms-ofba" } {\n'
                '            call write_log debug "Client-type: '
                "(ms-ofba-compliant), http path: ($http_path), "
                'user agent: ($http_user_agent)"\n'
                "        }\n"
                "\n"
                '        if { $ms_sp_client_type != "ms-ofba" } {\n'
                "            return\n"
                '        } elseif { $session_id != "" } {\n'
                "            if { [ACCESS::session exists "
                "-state_allow $session_id] } {\n"
                "                set f_allow_session 1\n"
                "                return\n"
                "            }\n"
                '        } elseif { $f_sp_persistent_ck == "1" && '
                "[HTTP::cookie exists $static::SP_PERSISTENT_CK] } "
                "{\n"
                "            set sp_persistent_ck_value "
                "[HTTP::cookie value $static::SP_PERSISTENT_CK]\n"
                '            if { $sp_persistent_ck_value != "" && '
                "[ACCESS::session exists -state_allow "
                "$sp_persistent_ck_value] } {\n"
                "                if {not ([catch {HTTP::cookie "
                'insert name "MRHSession" value '
                "$sp_persistent_ck_value}]) } {\n"
                "                    call write_log debug "
                '"Restored persistent cookie for sid: '
                '($sp_persistent_ck_value)"\n'
                "                    set f_allow_session 1\n"
                "                    return\n"
                "                } else {\n"
                "                    call write_log error "
                '"Restoring persistent cookie failed for sid: '
                '($sp_persistent_ck_value)"\n'
                "                    unset sp_persistent_ck_value\n"
                "                }\n"
                "            } else {\n"
                "                unset sp_persistent_ck_value\n"
                "            }\n"
                "        }\n"
                "\n"
                "        if { !($f_allow_session) && $http_path != "
                "$static::MS_OFBA_AUTH_REQ_URI } {\n"
                "            if { $ms_ofba_auth_cookie == "
                "$static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE } {\n"
                "                if { ![call "
                "is_ofba_passthrough_uri $http_path]  } {\n"
                "                    call write_log debug "
                '"Redirecting for MS OFBA, based on auth type"\n'
                "                    HTTP::respond 302 -version "
                "1.1 -noserver Location "
                "$static::MS_OFBA_AUTH_REQ_URI\n"
                "                }\n"
                "            } else {\n"
                '                call write_log debug "Responding '
                '403 for MS OFBA initiation"\n'
                '                if {$ofba_auth_dialog_sz == ""} '
                "{\n"
                "                    set ofba_auth_dialog_sz "
                "$static::MS_OFBA_AUTH_DIALOG_SZ\n"
                "                }\n"
                '                HTTP::respond 403 -version "1.1" '
                "noserver \\\n"
                '                    "X-FORMS_BASED_AUTH_REQUIRED" '
                '"https://[HTTP::host]$static::MS_OFBA_AUTH_REQ_URI" '
                "\\\n"
                "                    "
                '"X-FORMS_BASED_AUTH_RETURN_URL" '
                '"https://[HTTP::host]$static::MS_OFBA_AUTH_RETURN_URI" '
                "\\\n"
                "                    "
                '"X-FORMS_BASED_AUTH_DIALOG_SIZE" '
                "$ofba_auth_dialog_sz \\\n"
                '                    "Set-Cookie" '
                '"MRHSession=deleted; expires=Thu, 01 Jan 1970 '
                '00:00:00 GMT;path=/;secure" \\\n'
                '                    "Set-Cookie" '
                '"LastMRH_Session=deleted; expires=Thu, 01 Jan '
                '1970 00:00:00 GMT;path=/;secure" \\\n'
                '                    "Set-Cookie" '
                '"$static::MS_OFBA_AUTH_TYPE_COOKIE=$static::MS_OFBA_AUTH_TYPE_COOKIE_VALUE;path=/;secure;HttpOnly" '
                "\\\n"
                '                    "Connection" "Close"\n'
                "            }\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when HTTP_RESPONSE {\n"
                '        if { $f_sp_persistent_ck == "1" && ([info '
                "exists ms_sp_client_type] && $ms_sp_client_type "
                '== "browser") && $session_id != ""} {\n'
                '            if {$sp_persistent_ck_timeout == ""} '
                "{\n"
                "                set sp_persistent_ck_timeout "
                "$static::SP_PERSISTENT_CK_TIMEOUT\n"
                "            }\n"
                '            call write_log debug "Set-Cookie for '
                "SharePoint persistent cookie: "
                "($static::SP_PERSISTENT_CK) for sid: "
                "($session_id), having timeout: "
                '($sp_persistent_ck_timeout)"\n'
                "\n"
                "            HTTP::cookie remove "
                "$static::SP_PERSISTENT_CK\n"
                "            HTTP::cookie insert name "
                "$static::SP_PERSISTENT_CK value $session_id path "
                '"/"\n'
                "            HTTP::cookie expires "
                "$static::SP_PERSISTENT_CK "
                "$sp_persistent_ck_timeout relative\n"
                "            HTTP::cookie secure "
                "$static::SP_PERSISTENT_CK enable\n"
                "            HTTP::cookie httponly "
                "$static::SP_PERSISTENT_CK enable\n"
                "\n"
                "        } elseif { [info exists "
                "sp_persistent_ck_value] && "
                '$sp_persistent_ck_value ne "" } {\n'
                '            call write_log debug "Restoring '
                "Cookie for MRHSession from persistent cookie: "
                '($sp_persistent_ck_value)"\n'
                "\n"
                "            HTTP::cookie insert name MRHSession "
                'value $sp_persistent_ck_value path "/"\n'
                "            HTTP::cookie secure MRHSession "
                "enable\n"
                "            unset sp_persistent_ck_value\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when ACCESS_SESSION_STARTED {\n"
                "        if { ![info exists ms_sp_client_type] || "
                '$ms_sp_client_type != "ms-ofba"} {\n'
                "            return\n"
                "        }\n"
                "        ACCESS::session data set "
                "session.client.type "
                "$static::MS_OFBA_ENABLED_CLIENT_TYPE\n"
                "    }\n"
                "\n"
                "    when ACCESS_ACL_ALLOWED {\n"
                "        switch -glob -- [string tolower "
                "[HTTP::path]] $static::MS_OFBA_AUTH_REQ_URI {\n"
                "            ACCESS::respond 302 noserver Location "
                '"https://[HTTP::host]$static::MS_OFBA_AUTH_RETURN_URI"\n'
                "        } $static::MS_OFBA_AUTH_RETURN_URI {\n"
                "            ACCESS::respond 200 content "
                "$static::MS_OFBA_AUTH_SUCCESS_BODY noserver \\\n"
                '                "Set-Cookie" '
                '"$static::MS_OFBA_AUTH_TYPE_COOKIE=deleted;expires=Thu, '
                "01 Jan 1970 00:00:00 "
                'GMT;;path=/;secure;HttpOnly"\n'
                '        } "*/signout.aspx" {\n'
                "            ACCESS::respond 302 noserver Location "
                '"/vdesk/hangup.php3"\n'
                "                return\n"
                '        } "/_layouts/accessdenied.aspx" {\n'
                "            if {[string tolower [URI::query "
                '[HTTP::uri] loginasanotheruser]] equals "true" } '
                "{\n"
                "                ACCESS::session remove\n"
                "                ACCESS::respond 302 noserver "
                'Location "/"\n'
                "                return\n"
                "            }\n"
                "        } default {\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "e637kI9h5Ix7GFOay3azJpy0f7omhsLIP4EQQgdAxYzNVqFFpHpDlig4J/vuG/QbYUg5i0VDCnKNeL6FGQhMtIT6BNW9ucPGv46CKuS4UHxffnFGETafdGXnQg9j3RZGakjHZAwJmaQ0jLaXVG0tGo7e2P7lS6SC192xI8VqAkihMQCS7DaWDWuqYUeULk4YIPb8nGyw+3ZKCPTkOCqxWS4v2zMEhtCA7A9AzJAH2kg8o6HiEjEEt+PI6BclKOxyONdGkskEFBjqp1GZAlfRkcHbeFvgvXMa9ODZSzFHtT6rV+YsqmGfd4KHk5azrTCfhitvfU2miAD4M2/rHD1y/Q==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_APM_MS_Office_OFBA_Support",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_APM_MS_Office_OFBA_Support",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_MS_Office_OFBA_Support?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when RULE_INIT {\n"
                "        set static::ACCESS_LOG_ECP_PREFIX       "
                '"014d0002:7: ECP client"\n'
                "    }\n"
                "    when HTTP_REQUEST {\n"
                "        set http_path            [string tolower "
                "[HTTP::path]]\n"
                "        set http_hdr_auth        [HTTP::header "
                "Authorization]\n"
                "        set http_hdr_client_app  [HTTP::header "
                "X-MS-Client-Application]\n"
                "        set http_hdr_client_ip   [HTTP::header "
                "X-MS-Forwarded-Client-IP]\n"
                "        set MRHSession_cookie    [HTTP::cookie "
                "value MRHSession]\n"
                "\n"
                "        if { ($http_path == "
                '"/saml/idp/profile/redirectorpost/sso") &&\n'
                '             ($http_hdr_client_app != "") &&\n'
                "             ($http_hdr_client_app contains "
                '"Microsoft.Exchange") } {\n'
                "            HTTP::uri "
                '"/saml/idp/profile/ecp/sso"\n'
                "        } elseif { ($http_path != "
                '"/saml/idp/profile/ecp/sso")  } {\n'
                "            return\n"
                "        }\n"
                "        set f_saml_ecp_request 1\n"
                "        unset http_path\n"
                "\n"
                "        # If MRHSession cookie from client is "
                "present, skip further processing.\n"
                '        if { $MRHSession_cookie != "" } {\n'
                "            if { [ACCESS::session exists "
                "-state_allow -sid $MRHSession_cookie] } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_ECP_PREFIX HTTP *VALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "            } else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_ECP_PREFIX HTTP *INVALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "            }\n"
                "            return\n"
                "        }\n"
                "\n"
                '        if { ($http_hdr_client_app != "") &&\n'
                "            ($http_hdr_client_app contains "
                '"Microsoft.Exchange") &&\n'
                '            ($http_hdr_client_ip != "") } {\n'
                "\t    set src_ip $http_hdr_client_ip\n"
                "\t}\n"
                "        unset http_hdr_client_app\n"
                "        unset http_hdr_client_ip\n"
                "\n"
                "        if { ! [ info exists src_ip ] } {\n"
                "            set src_ip          "
                "[IP::remote_addr]\n"
                "        }\n"
                "\n"
                "        # Only allow HTTP Basic Authentication.\n"
                '        if { ($http_hdr_auth == "") || ([ string '
                "match -nocase {basic *} $http_hdr_auth ] != 1 ) } "
                "{\n"
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_ECP_PREFIX ECP request does '
                'not contain HTTP Basic Authorization header."\n'
                "            unset http_hdr_auth\n"
                "            return\n"
                "        }\n"
                "\n"
                "        set apm_username        [ string tolower "
                "[HTTP::username] ]\n"
                "        set apm_password        [HTTP::password]\n"
                "\n"
                '        binary scan [md5 "$apm_password$src_ip"] '
                "H* user_hash\n"
                "        set user_key {}\n"
                '        append user_key $apm_username "." '
                "$user_hash\n"
                "        unset user_hash\n"
                "\n"
                "        set apm_cookie_list             [ "
                "ACCESS::user getsid $user_key ]\n"
                "        if { [ llength $apm_cookie_list ] != 0 } "
                "{\n"
                "            set apm_cookie [ ACCESS::user getkey "
                "[ lindex $apm_cookie_list 0 ] ]\n"
                '            if { $apm_cookie != "" } {\n'
                "                HTTP::cookie insert name "
                "MRHSession value $apm_cookie\n"
                "            }\n"
                "        }\n"
                "\n"
                '        HTTP::header insert "clientless-mode" 1\n'
                '        HTTP::header insert "username" '
                "$apm_username\n"
                '        HTTP::header insert "password" '
                "$apm_password\n"
                "        unset apm_username\n"
                "        unset apm_password\n"
                "        unset http_hdr_auth\n"
                "    }\n"
                "\n"
                "    when ACCESS_SESSION_STARTED {\n"
                "        if { [ info exists f_saml_ecp_request ] "
                "&& $f_saml_ecp_request == 1 } {\n"
                "            if { [ info exists user_key ] } {\n"
                "                ACCESS::session data set "
                '"session.user.uuid" $user_key\n'
                "            }\n"
                "            if { [ info exists  src_ip ] } {\n"
                "                ACCESS::session data set "
                '"session.user.clientip" $src_ip\n'
                "            }\n"
                "        }\n"
                "    }\n"
                "\n"
                "    when HTTP_RESPONSE {\n"
                "        if { [ info exists f_saml_ecp_request ] "
                "&& $f_saml_ecp_request == 1 } {\n"
                "            unset f_saml_ecp_request\n"
                "            unset apm_cookie\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "lbhM9rFH3R+uo+pp4DWotUdvGbvFhCBhe5aZKgpRZdl5k39X50MrrIhz2UkjY1VV2JORwPaSpdyN6mVY0cJccFdLjGgaNCtNuMoT2grlOE7F9Zw73imFGbu8UiqmZT0ZLcNXCglZplp08o9O9xn7UNJ5E/gYWrjCI2QaebwGu1NMSLK+/WjGHNKr28xN2Cwo0rk9hg+6fC9YxzlGVoRlxPuYRelygqD0bAQKTux4tuTQPF/4CDNpttyVX72ULJpZUINwW1UeCZoosB1O4XubT9PaqEl53ioom8LcGZEn5vKOH+TlvKXjPi5kV1ci2d+fjCf7ZoOW6EVyEEc2aL2cWw==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_APM_Office365_SAML_BasicAuth",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_APM_Office365_SAML_BasicAuth",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_Office365_SAML_BasicAuth?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when RULE_INIT {\n"
                "        set static::actsync_401_http_body   "
                '"<html><title>Authentication '
                "Failed</title><body>Error: Authentication "
                'Failure</body></html>"\n'
                "        set static::actsync_503_http_body   "
                '"<html><title>Service is not '
                "available</title><body>Error: Service is not "
                'available</body></html>"\n'
                "        set static::ACCESS_LOG_PREFIX       "
                '"01490000:7:"\n'
                "    }\n"
                "    when HTTP_REQUEST {\n"
                "        set http_path                       "
                "[string tolower [HTTP::path]]\n"
                "        set f_clientless_mode               0\n"
                "\n"
                "        if { $http_path == "
                '"/microsoft-server-activesync" } {\n'
                "        }\n"
                "        elseif { $http_path == "
                '"/autodiscover/autodiscover.xml" } {\n'
                "            set f_auto_discover 1\n"
                "        }\n"
                "        else return\n"
                "\n"
                "        if { ! [ info exists src_ip ] } {\n"
                "            set src_ip                            "
                "[IP::remote_addr]\n"
                "        }\n"
                "        if { ! [ info exists "
                "PROFILE_RESTRICT_SINGLE_IP ] } {\n"
                "            set PROFILE_RESTRICT_SINGLE_IP  \t  "
                "1\n"
                "        }\n"
                "        # Only allow HTTP Basic Authentication.\n"
                '        set auth_info_b64enc                ""\n'
                "        set http_hdr_auth                   "
                "[HTTP::header Authorization]\n"
                "        regexp -nocase {Basic (.*)} "
                "$http_hdr_auth match auth_info_b64enc\n"
                '        if { $auth_info_b64enc == "" } {\n'
                '            set http_hdr_auth ""\n'
                "        }\n"
                "\n"
                '        if { $http_hdr_auth == "" } {\n'
                "            log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX Empty/invalid HTTP '
                'Basic Authorization header"\n'
                "            HTTP::respond 401 content "
                "$static::actsync_401_http_body Connection close\n"
                "            return\n"
                "        }\n"
                "\n"
                "        set MRHSession_cookie               "
                "[HTTP::cookie value MRHSession]\n"
                "        # Do we have valid MRHSession cookie.\n"
                '        if { $MRHSession_cookie != "" } {\n'
                "            if { [ACCESS::session exists "
                "-state_allow -sid $MRHSession_cookie] } {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *VALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "                # Default profile access setting "
                "is false\n"
                "                if { $PROFILE_RESTRICT_SINGLE_IP "
                "== 0 } {\n"
                "                    return\n"
                "                }\n"
                "                elseif { [ IP::addr $src_ip "
                "equals [ ACCESS::session data get -sid "
                '$MRHSession_cookie "session.user.clientip" ] ] } '
                "{\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP matched"\n'
                "                    return\n"
                "                }\n"
                "                else {\n"
                "                    log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX source IP does not '
                'matched"\n'
                "                }\n"
                "            }\n"
                "            else {\n"
                "                log -noname "
                "accesscontrol.local1.debug "
                '"$static::ACCESS_LOG_PREFIX HTTP *INVALID* '
                'MRHSession cookie: $MRHSession_cookie"\n'
                "            }\n"
                '            set MRHSession_cookie ""\n'
                "            HTTP::cookie remove MRHSession\n"
                "        }\n"
                "\n"
                "        set apm_username                    [ "
                "string tolower [HTTP::username] ]\n"
                "        set apm_password                    "
                "[HTTP::password]\n"
                "\n"
                "        if { $PROFILE_RESTRICT_SINGLE_IP == 0 } "
                "{\n"
                '            binary scan [md5 "$apm_password$"] H* '
                "user_hash\n"
                "        } else {\n"
                "            binary scan [md5 "
                '"$apm_password$src_ip"] H* user_hash\n'
                "        }\n"
                "        set user_key {}\n"
                '        append user_key $apm_username "." '
                "$user_hash\n"
                "        unset user_hash\n"
                "\n"
                "        set f_insert_clientless_mode    0\n"
                "        set apm_cookie_list             [ "
                "ACCESS::user getsid $user_key ]\n"
                "        if { [ llength $apm_cookie_list ] != 0 } "
                "{\n"
                "            set apm_cookie [ ACCESS::user getkey "
                "[ lindex $apm_cookie_list 0 ] ]\n"
                '            if { $apm_cookie != "" } {\n'
                "                HTTP::cookie insert name "
                "MRHSession value $apm_cookie\n"
                "            } else {\n"
                "                set f_insert_clientless_mode 1\n"
                "            }\n"
                "        } else {\n"
                "            set f_insert_clientless_mode 1\n"
                "        }\n"
                "\n"
                "        if { $f_insert_clientless_mode == 1 } {\n"
                '            HTTP::header insert "clientless-mode" '
                "1\n"
                '            HTTP::header insert "username" '
                "$apm_username\n"
                '            HTTP::header insert "password" '
                "$apm_password\n"
                "        }\n"
                "        unset f_insert_clientless_mode\n"
                "    }\n"
                "    when ACCESS_SESSION_STARTED {\n"
                "        if { [ info exists user_key ] } {\n"
                "            ACCESS::session data set "
                '"session.user.uuid" $user_key\n'
                "            ACCESS::session data set "
                '"session.user.microsoft-exchange-client" 1\n'
                "            ACCESS::session data set "
                '"session.user.activesync" 1\n'
                "            if { [ info exists f_auto_discover ] "
                "&& $f_auto_discover == 1 } {\n"
                "                set f_auto_discover 0\n"
                "                ACCESS::session data set "
                '"session.user.microsoft-autodiscover" 1\n'
                "            }\n"
                "        }\n"
                "    }\n"
                "    when ACCESS_POLICY_COMPLETED {\n"
                "        if { ! [ info exists user_key ] } {\n"
                "            return\n"
                "        }\n"
                "\n"
                "        set policy_result [ACCESS::policy "
                "result]\n"
                "        switch $policy_result {\n"
                '        "allow" {\n'
                "        }\n"
                '        "deny" {\n'
                "            ACCESS::respond 401 content "
                "$static::actsync_401_http_body Connection close\n"
                "            ACCESS::session remove\n"
                "        }\n"
                "        default {\n"
                "            ACCESS::respond 503 content "
                "$static::actsync_503_http_body Connection close\n"
                "            ACCESS::session remove\n"
                "        }\n"
                "        }\n"
                "\n"
                "        unset user_key\n"
                "    }\n"
                "definition-signature "
                "d3ZoP7HHzJwjxIV+zgaF0J7nh0d0e3rlE5srbLvvZXOW9mSQ4VzalGLunwQMl6rths50p6zwETao3banbrWCnI+HEBKtDy61/wFJJ3UJ6RHWPSFSFQhcJMOY4WIdSRuu0VwTlMn6vte42xe2UmTWeB7tSs/STKoOQrDy0U7c34AAG9gSRaikPJz/hi/McWRIxX4LtS+gecwXX1KXM3lB7dz1kvOYOid9h1tsmUtftpB/neqmReMch3gaWrL7ZYcEECCcHEhyW6B7hqT91r5a9VG4nlq8oQ5MLa07zwVT5HV2id5lgIfhpPSzXUJbe3SJ7wN5TThtaWhBgDIHp+CYJA==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_APM_activesync",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_APM_activesync",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_APM_activesync?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when HTTP_REQUEST {\n"
                '        set thecert ""\n'
                "        set ckname F5KRBAUTH\n"
                "        set ckpass abc123\n"
                "        set authprofiles [PROFILE::list auth]\n"
                "        # Search the auth profiles for the "
                "krbdelegate(7) and grab cookie info\n"
                "        foreach profname $authprofiles {\n"
                "            if { [PROFILE::auth $profname type] "
                "== 7 } {\n"
                "                set tmpckname [PROFILE::auth "
                "$profname cookie_name]\n"
                "                set tmpckpass [PROFILE::auth "
                "$profname cookie_key]\n"
                "                if {[PROFILE::auth $profname "
                'cookie_name] != "" } {\n'
                "                    set ckname $tmpckname\n"
                "                    set ckpass $tmpckpass\n"
                "                    break\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "        set seecookie 0\n"
                "        set insertcookie 0\n"
                "        # check for the cookie\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(krbdelegate)]} {\n"
                "            set tmm_auth_sid [AUTH::start pam "
                "default_krbdelegate]\n"
                "            set tmm_auth_http_sids(krbdelegate) "
                "$tmm_auth_sid\n"
                "            AUTH::subscribe $tmm_auth_sid\n"
                "        } else {\n"
                "            set tmm_auth_sid "
                "$tmm_auth_http_sids(krbdelegate)\n"
                "        }\n"
                "        if { [PROFILE::exists clientssl] } {\n"
                '            set certcmd "SSL::cert 0"\n'
                "            set thecert [ eval $certcmd ]\n"
                "        }\n"
                '        if { $thecert == "" } {\n'
                "            # if no cert, assume old kerb "
                "delegation\n"
                "            # if there is no Authorization header "
                "and no cookie, get one.\n"
                "            if { ([HTTP::header Authorization] == "
                '"") and\n'
                "                  (not [HTTP::cookie exists "
                "$ckname])} {\n"
                "                HTTP::respond 401 "
                "WWW-Authenticate Negotiate\n"
                "                return\n"
                "            }\n"
                "        }\n"
                "        if {[HTTP::cookie exists $ckname]} {\n"
                "            set ckval [HTTP::cookie decrypt "
                "$ckname $ckpass]\n"
                "            AUTH::username_credential "
                '$tmm_auth_sid "cookie"\n'
                "            AUTH::password_credential "
                "$tmm_auth_sid $ckval\n"
                "            set seecookie 1\n"
                "        } else {\n"
                '            if { $thecert == "" } {\n'
                "                # Kerberos Delegation - set "
                "username\n"
                "                # Strip off the Negotiate before "
                "the base64d goodness\n"
                "                AUTH::username_credential "
                "$tmm_auth_sid [lindex [HTTP::header "
                "Authorization] 1]\n"
                "            }\n"
                "            else {\n"
                "                # Protocol Transition - set "
                "ttm_auth_sid\n"
                "                AUTH::username_credential "
                '$tmm_auth_sid "krpprottran"\n'
                "                AUTH::cert_credential "
                "$tmm_auth_sid $thecert\n"
                "            }\n"
                "            AUTH::password_credential "
                '$tmm_auth_sid "xxxx"\n'
                "        }\n"
                "        AUTH::authenticate $tmm_auth_sid\n"
                "\n"
                "        if {not [info exists "
                "tmm_auth_http_collect_count]} {\n"
                "            HTTP::collect\n"
                "            set tmm_auth_http_successes 0\n"
                "            set tmm_auth_http_collect_count 1\n"
                "        } else {\n"
                "            incr tmm_auth_http_collect_count\n"
                "        }\n"
                "    }\n"
                "    when AUTH_RESULT {\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(krbdelegate)] or \\\n"
                "            ($tmm_auth_http_sids(krbdelegate) != "
                "[AUTH::last_event_session_id]) or \\\n"
                "            (not [info exists "
                "tmm_auth_http_collect_count])} {\n"
                "            return\n"
                "        }\n"
                "        if {[AUTH::status] == 0} {\n"
                "            incr tmm_auth_http_successes\n"
                "        }\n"
                "        # If multiple auth sessions are pending "
                "and\n"
                "        # one failure results in termination and "
                "this is a failure\n"
                "        # or enough successes have now occurred\n"
                "        if {([array size tmm_auth_http_sids] > 1) "
                "and \\\n"
                "            ((not [info exists "
                "tmm_auth_http_sufficient_successes] or \\\n"
                "             ($tmm_auth_http_successes >= "
                "$tmm_auth_http_sufficient_successes)))} {\n"
                "            # Abort the other auth sessions\n"
                "            foreach {type sid} [array get "
                "tmm_auth_http_sids] {\n"
                "                unset tmm_auth_http_sids($type)\n"
                '                if {($type ne "krbdelegate") and '
                "($sid != -1)} {\n"
                "                    AUTH::abort $sid\n"
                "                    incr "
                "tmm_auth_http_collect_count -1\n"
                "               }\n"
                "            }\n"
                "        }\n"
                "        # If this is the last outstanding auth "
                "then either\n"
                "        # release or respond to this session\n"
                "        incr tmm_auth_http_collect_count -1\n"
                "        if {$tmm_auth_http_collect_count == 0} {\n"
                "            unset tmm_auth_http_collect_count\n"
                "            if { [AUTH::status] == 0 } {\n"
                "                array set pamout "
                "[AUTH::response_data]\n"
                "                HTTP::header replace "
                'Authorization "Negotiate '
                '$pamout(krbdelegate:attr:SPNEGO)"\n'
                "                if {$seecookie == 0} {\n"
                "                    set insertcookie "
                "$pamout(krbdelegate:attr:KRB5CCNAME)\n"
                "                }\n"
                "                HTTP::release\n"
                "            } else {\n"
                "                HTTP::respond 401 "
                'WWW-Authenticate Negotiate "Set-Cookie" "$ckname= '
                '; expires=Wed Dec 31 16:00:00 1969"\n'
                "            }\n"
                "        }\n"
                "    }\n"
                "    # When the response goes out, if we need to "
                "insert a cookie, do it.\n"
                "    when HTTP_RESPONSE {\n"
                "        if {$insertcookie != 0} {\n"
                "            HTTP::cookie insert name $ckname "
                "value $insertcookie\n"
                "            HTTP::cookie encrypt $ckname $ckpass\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "KlDm5lT1k17/I3injIvybDZ6HIJC8qpdPgwUlPQ42tufrR7ZVVFvtDlDEdN4/QPtex/u1oEA6mij+N8mMc/FSy3B+jRogi7HyI/2glxNh8St/+odNp3ho6gWvTpNAS8XBIdixxCxpJYahIw5h9flJ+gZywLabCSMQAlFYoXqdpjZp5oZ/kN7/J94joR0okCRxI7fHgVLNcbXKWg+Kcuw0TJkyNWWJh1J6DeRURPzol+yo8GmCMdDia9MF68Kho8b5LWQuZIwt727OThDz0BBhAuG6oEn06GiPmPSxczJrei/k5Zd1SsJe0xpWvlLKP4vps/W8TcMhY3xwY70RP1cfQ==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_auth_krbdelegate",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_auth_krbdelegate",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_krbdelegate?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when HTTP_REQUEST {\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(ldap)]} {\n"
                "            set tmm_auth_sid [AUTH::start pam "
                "default_ldap]\n"
                "            set tmm_auth_http_sids(ldap) "
                "$tmm_auth_sid\n"
                "            if {[info exists "
                "tmm_auth_subscription]} {\n"
                "                AUTH::subscribe $tmm_auth_sid\n"
                "            }\n"
                "        } else {\n"
                "            set tmm_auth_sid "
                "$tmm_auth_http_sids(ldap)\n"
                "        }\n"
                "        AUTH::username_credential $tmm_auth_sid "
                "[HTTP::username]\n"
                "        AUTH::password_credential $tmm_auth_sid "
                "[HTTP::password]\n"
                "        AUTH::authenticate $tmm_auth_sid\n"
                "\n"
                "        if {not [info exists "
                "tmm_auth_http_collect_count]} {\n"
                "            HTTP::collect\n"
                "            set tmm_auth_http_successes 0\n"
                "            set tmm_auth_http_collect_count 1\n"
                "        } else {\n"
                "            incr tmm_auth_http_collect_count\n"
                "        }\n"
                "    }\n"
                "    when AUTH_RESULT {\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(ldap)] or \\\n"
                "           ($tmm_auth_http_sids(ldap) != "
                "[AUTH::last_event_session_id]) or \\\n"
                "           (not [info exists "
                "tmm_auth_http_collect_count])} {\n"
                "            return\n"
                "        }\n"
                "        if {[AUTH::status] == 0} {\n"
                "            incr tmm_auth_http_successes\n"
                "        }\n"
                "        # If multiple auth sessions are pending "
                "and\n"
                "        # one failure results in termination and "
                "this is a failure\n"
                "        # or enough successes have now occurred\n"
                "        if {([array size tmm_auth_http_sids] > 1) "
                "and \\\n"
                "            ((not [info exists "
                "tmm_auth_http_sufficient_successes] or \\\n"
                "             ($tmm_auth_http_successes >= "
                "$tmm_auth_http_sufficient_successes)))} {\n"
                "            # Abort the other auth sessions\n"
                "            foreach {type sid} [array get "
                "tmm_auth_http_sids] {\n"
                "                unset tmm_auth_http_sids($type)\n"
                '                if {($type ne "ldap") and ($sid '
                "!= -1)} {\n"
                "                    AUTH::abort $sid\n"
                "                    incr "
                "tmm_auth_http_collect_count -1\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "\n"
                "        # If this is the last outstanding auth "
                "then either\n"
                "        # release or respond to this session\n"
                "        incr tmm_auth_http_collect_count -1\n"
                "        if {$tmm_auth_http_collect_count == 0} {\n"
                "            unset tmm_auth_http_collect_count\n"
                "            if {[AUTH::status] == 0} {\n"
                "                HTTP::release\n"
                "            } else {\n"
                "                HTTP::respond 401\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "kzFhXHp72R2BTE+vwS9DBG2dlHsnGdWPsFSEx18DMcXyOypZi34rS+un6RpZeQ0Yib9GjXmEmIqLYQVCS9JTmcnjE0AEztcIot24B1NBVOHHAUfA7LJko7hqB9L0STfRTSbjaV13+kVDJMWYj1qcxGX7bIjzxXtPwPaDHWooxADCxmLlt9siSSYYnJqTJLcSutAJd16k+Y6lUKrcXoCl+0YIKm1CF+RUyWFsCNZxcmaOIyUqUnrLgpBinYyxb2T0MN9K/A9mXT6L+gscqHT+kAXxDJESOO1FHHvq4ld2dfK+Z6eWALvR0NGaCmYN2SEnfyZ3dfvb0ZdfWcyTqysEOw==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_auth_ldap",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_auth_ldap",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ldap?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when HTTP_REQUEST {\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(radius)]} {\n"
                "            set tmm_auth_sid [AUTH::start pam "
                "default_radius]\n"
                "            set tmm_auth_http_sids(radius) "
                "$tmm_auth_sid\n"
                "            if {[info exists "
                "tmm_auth_subscription]} {\n"
                "                AUTH::subscribe $tmm_auth_sid\n"
                "            }\n"
                "        } else {\n"
                "            set tmm_auth_sid "
                "$tmm_auth_http_sids(radius)\n"
                "        }\n"
                "        AUTH::username_credential $tmm_auth_sid "
                "[HTTP::username]\n"
                "        AUTH::password_credential $tmm_auth_sid "
                "[HTTP::password]\n"
                "        AUTH::authenticate $tmm_auth_sid\n"
                "\n"
                "        if {not [info exists "
                "tmm_auth_http_collect_count]} {\n"
                "            HTTP::collect\n"
                "            set tmm_auth_http_successes 0\n"
                "            set tmm_auth_http_collect_count 1\n"
                "        } else {\n"
                "            incr tmm_auth_http_collect_count\n"
                "        }\n"
                "    }\n"
                "    when AUTH_RESULT {\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(radius)] or \\\n"
                "            ($tmm_auth_http_sids(radius) != "
                "[AUTH::last_event_session_id]) or \\\n"
                "            (not [info exists "
                "tmm_auth_http_collect_count])} {\n"
                "            return\n"
                "        }\n"
                "        if {[AUTH::status] == 0} {\n"
                "            incr tmm_auth_http_successes\n"
                "        }\n"
                "        # If multiple auth sessions are pending "
                "and\n"
                "        # one failure results in termination and "
                "this is a failure\n"
                "        # or enough successes have now occurred\n"
                "        if {([array size tmm_auth_http_sids] > 1) "
                "and \\\n"
                "            ((not [info exists "
                "tmm_auth_http_sufficient_successes] or \\\n"
                "             ($tmm_auth_http_successes >= "
                "$tmm_auth_http_sufficient_successes)))} {\n"
                "            # Abort the other auth sessions\n"
                "            foreach {type sid} [array get "
                "tmm_auth_http_sids] {\n"
                "                unset tmm_auth_http_sids($type)\n"
                '                if {($type ne "radius") and ($sid '
                "!= -1)} {\n"
                "                    AUTH::abort $sid\n"
                "                    incr "
                "tmm_auth_http_collect_count -1\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "        # If this is the last outstanding auth "
                "then either\n"
                "        # release or respond to this session\n"
                "        incr tmm_auth_http_collect_count -1\n"
                "        if {$tmm_auth_http_collect_count == 0} {\n"
                "            unset tmm_auth_http_collect_count\n"
                "            if { [AUTH::status] == 0 } {\n"
                "                HTTP::release\n"
                "            } else {\n"
                "                HTTP::respond 401\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "k3ZS7fMZZN+W3HDVg2i2FWS28Mv/l0JDnym3rEGY/JOn/L71DpzEEpTvyO+wU2Oecu7XfnBpkRG5mTTGGBMOOPKXoNFdRYbXprB+DRJhG2vOcR4KnxEsKyGuOM8MxNVb9Bg6jufGsqql/vEEGJJH43RjUqYIOiMNotKbghiC3BUBQfMN6XZlP3tgXTMM1wLSxei840hKMxpCa+CKWvQcnFHKzmwD3uN1S18Dx6yzGUFLSY+OFPHsctywMPQwzrZV7slOBgRGZMQbxqQAejddagQimzGzCKb0cDqdU2X4Vu6uqx1G3Lv1cihvMFDM7pLnfi2JskZ0nxNBBZ8rOcCVPw==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_auth_radius",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_auth_radius",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_radius?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when CLIENT_ACCEPTED {\n"
                "        set tmm_auth_ssl_cc_ldap_sid 0\n"
                "        set tmm_auth_ssl_cc_ldap_done 0\n"
                "    }\n"
                "    when CLIENTSSL_CLIENTCERT {\n"
                "        if {[SSL::cert count] == 0} {\n"
                "            return\n"
                "        }\n"
                "        set tmm_auth_ssl_cc_ldap_done 0\n"
                "        if {$tmm_auth_ssl_cc_ldap_sid == 0} {\n"
                "            set tmm_auth_ssl_cc_ldap_sid "
                "[AUTH::start pam default_ssl_cc_ldap]\n"
                "            if {[info exists "
                "tmm_auth_subscription]} {\n"
                "                AUTH::subscribe "
                "$tmm_auth_ssl_cc_ldap_sid\n"
                "            }\n"
                "        }\n"
                "        AUTH::cert_credential "
                "$tmm_auth_ssl_cc_ldap_sid [SSL::cert 0]\n"
                "        AUTH::authenticate "
                "$tmm_auth_ssl_cc_ldap_sid\n"
                "        SSL::handshake hold\n"
                "    }\n"
                "    when CLIENTSSL_HANDSHAKE {\n"
                "        set tmm_auth_ssl_cc_ldap_done 1\n"
                "    }\n"
                "    when AUTH_RESULT {\n"
                "        if {[info exists "
                "tmm_auth_ssl_cc_ldap_sid] and \\\n"
                "            ($tmm_auth_ssl_cc_ldap_sid == "
                "[AUTH::last_event_session_id])} {\n"
                "            set tmm_auth_status [AUTH::status]\n"
                "            if {$tmm_auth_status == 0} {\n"
                "                set tmm_auth_ssl_cc_ldap_done 1\n"
                "                SSL::handshake resume\n"
                "            } elseif {$tmm_auth_status != -1 || "
                "$tmm_auth_ssl_cc_ldap_done == 0} {\n"
                "                reject\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "Ls7LEbcMGMMAy6eJsdaAn7tu3l2ROMB2XWCeLRc6GfBOiSF+EvVbQcSrl5MqklVcnQF9c4fzz+ffOPFyA9RkbicoFO2F/nr2B7NOFcuNNx3e9f/043A62ODBb6d18/IKO3hnEVwnRRBkB9SRPKc6tsHrReewPEB8TdA1eNb5JcautKEa3pbxLR76k60FS8k5wyPJ7W58gKT1tnR2n5EgM5K3wQSiCXKCONknyS2MKB6iEkk3uXSbQP0lzFCxPAPyR2JQ/ZNniC3jYghSr+M5i3KaMKjSjdsTt6fYpDxLH9Iikk5ZrtJGTJeP7P8cNQallzP7JJsB5aqui/SbFA0SFQ==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_auth_ssl_cc_ldap",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_auth_ssl_cc_ldap",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_cc_ldap?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when CLIENT_ACCEPTED {\n"
                "        set tmm_auth_ssl_crldp_sid 0\n"
                "        set tmm_auth_ssl_crldp_done 0\n"
                "    }\n"
                "    when CLIENTSSL_CLIENTCERT {\n"
                "        if {[SSL::cert count] == 0} {\n"
                "            return\n"
                "        }\n"
                "        set tmm_auth_ssl_crldp_done 0\n"
                "        if {$tmm_auth_ssl_crldp_sid == 0} {\n"
                "            set tmm_auth_ssl_crldp_sid "
                "[AUTH::start pam default_ssl_crldp]\n"
                "            if {[info exists "
                "tmm_auth_subscription]} {\n"
                "                AUTH::subscribe "
                "$tmm_auth_ssl_crldp_sid\n"
                "            }\n"
                "        }\n"
                "        AUTH::cert_credential "
                "$tmm_auth_ssl_crldp_sid [SSL::cert 0]\n"
                "        AUTH::cert_issuer_credential "
                "$tmm_auth_ssl_crldp_sid [SSL::cert issuer 0]\n"
                "        AUTH::authenticate "
                "$tmm_auth_ssl_crldp_sid\n"
                "        SSL::handshake hold\n"
                "    }\n"
                "    when CLIENTSSL_HANDSHAKE {\n"
                "        set tmm_auth_ssl_crldp_done 1\n"
                "    }\n"
                "    when AUTH_RESULT {\n"
                "        if {[info exists tmm_auth_ssl_crldp_sid] "
                "and \\\n"
                "            ($tmm_auth_ssl_crldp_sid == "
                "[AUTH::last_event_session_id])} {\n"
                "            set tmm_auth_status [AUTH::status]\n"
                "            if {$tmm_auth_status == 0} {\n"
                "                set tmm_auth_ssl_crldp_done 1\n"
                "                SSL::handshake resume\n"
                "            } elseif {$tmm_auth_status != -1 || "
                "$tmm_auth_ssl_crldp_done == 0} {\n"
                "                reject\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "mVtMWHPruxGXVKW3hAZn3uBJkGNB8SmyzvR6u2OrQ+U71Ms+vAVuNSzCBJ05qJ7qfouOwtUYMtB1QMSjEdnLe2Z259y4gfnrEZEDpEZX8Co1rTEoP3grsw0heuITOPIX6R+MXrqfcmbaKRGGq2wJcNPLJXY/VsdYQBPDmaPrn/ZPRbmXSdRnpGFz4yN99tOw4OE5wvkp4CRg/zfSfQeFkzLrSeApGSWWAVMT09LW6aZmOWuC2bzr7Gpc7vtJtFuka8U7jSXAMJNOzqE55qhIvA3Y7UkIYemyXD0NCXmkUEWsPsuIzmZH6k6W8cXdhHtk+YEDvJDhKNO7h/C0qKPlaA==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_auth_ssl_crldp",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_auth_ssl_crldp",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_crldp?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when CLIENT_ACCEPTED {\n"
                "        set tmm_auth_ssl_ocsp_sid 0\n"
                "        set tmm_auth_ssl_ocsp_done 0\n"
                "    }\n"
                "    when CLIENTSSL_CLIENTCERT {\n"
                "        if {[SSL::cert count] == 0} {\n"
                "            return\n"
                "        }\n"
                "        set tmm_auth_ssl_ocsp_done 0\n"
                "        if {$tmm_auth_ssl_ocsp_sid == 0} {\n"
                "            set tmm_auth_ssl_ocsp_sid "
                "[AUTH::start pam default_ssl_ocsp]\n"
                "            if {[info exists "
                "tmm_auth_subscription]} {\n"
                "                AUTH::subscribe "
                "$tmm_auth_ssl_ocsp_sid\n"
                "            }\n"
                "        }\n"
                "        AUTH::cert_credential "
                "$tmm_auth_ssl_ocsp_sid [SSL::cert 0]\n"
                "        AUTH::cert_issuer_credential "
                "$tmm_auth_ssl_ocsp_sid [SSL::cert issuer 0]\n"
                "        AUTH::authenticate "
                "$tmm_auth_ssl_ocsp_sid\n"
                "        SSL::handshake hold\n"
                "    }\n"
                "    when CLIENTSSL_HANDSHAKE {\n"
                "        set tmm_auth_ssl_ocsp_done 1\n"
                "    }\n"
                "    when AUTH_RESULT {\n"
                "        if {[info exists tmm_auth_ssl_ocsp_sid] "
                "and \\\n"
                "            ($tmm_auth_ssl_ocsp_sid == "
                "[AUTH::last_event_session_id])} {\n"
                "            set tmm_auth_status [AUTH::status]\n"
                "            if {$tmm_auth_status == 0} {\n"
                "                set tmm_auth_ssl_ocsp_done 1\n"
                "                SSL::handshake resume\n"
                "            } elseif {$tmm_auth_status != -1 || "
                "$tmm_auth_ssl_ocsp_done == 0} {\n"
                "                reject\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "UAbD8tfmCrHiqB/uh1XzQfJvsgT+StbJ+Zq37qc+ODGStnFwDjXroPuPGPAycPBveiky0CU9/gR24Y8zfhMzbHK2lm/WvUq7cdrVIX2ZAvIVof9PpmfWli1c9iPe8EEau0yrOD7pZeyMpYM2hIlG1L9YmhBSJGwGV2UzmKmFdLsBWuGfcfBW7ZXQTjKz0UhT4YWUbpF0ws9QNJln8zsiCPlChF2OAJk35ZxGoZmKGA/xL2fJVbsI3vz3HAbAadKx0AiXqk6aTwtQny18mu0nVsPbO5t/KwqH6C3rc/qoVgqG6FsvVen2OvNYDBnq4gm+A5Mf1abey7+edQT6KJ9ztA==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_auth_ssl_ocsp",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_auth_ssl_ocsp",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_ssl_ocsp?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when HTTP_REQUEST {\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(tacacs)]} {\n"
                "            set tmm_auth_sid [AUTH::start pam "
                "default_tacacs]\n"
                "            set tmm_auth_http_sids(tacacs) "
                "$tmm_auth_sid\n"
                "            if {[info exists "
                "tmm_auth_subscription]} {\n"
                "                AUTH::subscribe $tmm_auth_sid\n"
                "            }\n"
                "        } else {\n"
                "            set tmm_auth_sid "
                "$tmm_auth_http_sids(tacacs)\n"
                "        }\n"
                "        AUTH::username_credential $tmm_auth_sid "
                "[HTTP::username]\n"
                "        AUTH::password_credential $tmm_auth_sid "
                "[HTTP::password]\n"
                "        AUTH::authenticate $tmm_auth_sid\n"
                "\n"
                "        if {not [info exists "
                "tmm_auth_http_collect_count]} {\n"
                "            HTTP::collect\n"
                "            set tmm_auth_http_successes 0\n"
                "            set tmm_auth_http_collect_count 1\n"
                "        } else {\n"
                "            incr tmm_auth_http_collect_count\n"
                "        }\n"
                "    }\n"
                "    when AUTH_RESULT {\n"
                "        if {not [info exists "
                "tmm_auth_http_sids(tacacs)] or \\\n"
                "            ($tmm_auth_http_sids(tacacs) != "
                "[AUTH::last_event_session_id]) or \\\n"
                "            (not [info exists "
                "tmm_auth_http_collect_count])} {\n"
                "            return\n"
                "        }\n"
                "        if {[AUTH::status] == 0} {\n"
                "            incr tmm_auth_http_successes\n"
                "        }\n"
                "        # If multiple auth sessions are pending "
                "and\n"
                "        # one failure results in termination and "
                "this is a failure\n"
                "        # or enough successes have now occurred\n"
                "        if {([array size tmm_auth_http_sids] > 1) "
                "and \\\n"
                "            ((not [info exists "
                "tmm_auth_http_sufficient_successes] or \\\n"
                "             ($tmm_auth_http_successes >= "
                "$tmm_auth_http_sufficient_successes)))} {\n"
                "            # Abort the other auth sessions\n"
                "            foreach {type sid} [array get "
                "tmm_auth_http_sids] {\n"
                "                unset tmm_auth_http_sids($type)\n"
                '                if {($type ne "tacacs") and ($sid '
                "!= -1)} {\n"
                "                    AUTH::abort $sid\n"
                "                    incr "
                "tmm_auth_http_collect_count -1\n"
                "                }\n"
                "            }\n"
                "        }\n"
                "        # If this is the last outstanding auth "
                "then either\n"
                "        # release or respond to this session\n"
                "        incr tmm_auth_http_collect_count -1\n"
                "        if {$tmm_auth_http_collect_count == 0} {\n"
                "            unset tmm_auth_http_collect_count\n"
                "            if { [AUTH::status] == 0 } {\n"
                "                HTTP::release\n"
                "            } else {\n"
                "                HTTP::respond 401\n"
                "            }\n"
                "        }\n"
                "    }\n"
                "definition-signature "
                "qR6ynw882+5gcwiV6eymN/CZAoF+G4aRd2Xfr+4KWfXAD27876SoHuTyuTKxKxcG5oGXOPppqH/vtbtnBiI+UW6CLEHne3+RPx9EaSxX4ElCg/1ap69j3xPmh2IVSTCrR/93vu9Bnt6DEkNbXelWze5C0jVwMogQdsiVpmn7+YfkSmyyEeAvx8aHkvhK8KL0Pp8AiqrvyDWcBVAtXtioS0YC3S8pxRbpWHuVzA9e4SXNIpCk8vigk7gOmQthC+xerw0/8PEmOfT4G2LNr7TG4M1kQFkLR1foz4EwODEODHjyiyNTWZsCH4sPWJM6xJXS+NbL4k+0lWNPyhnyAGbnpw==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_auth_tacacs",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_auth_tacacs",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_auth_tacacs?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "nodelete nowrite \n"
                "# Copyright 2003-2006, 2012-2013, 2016.  F5 "
                "Networks, Inc.  See End User License Agreement "
                '("EULA")\n'
                "# for license terms. Notwithstanding anything to "
                "the contrary in the EULA,\n"
                "# Licensee may copy and modify this software "
                "product for its internal business\n"
                "# purposes. Further, Licensee may upload, publish "
                "and distribute the modified\n"
                "# version of the software product on "
                "devcentral.f5.com.\n"
                "#\n"
                "    when HTTP_REQUEST {\n"
                "       HTTP::redirect https://[getfield "
                '[HTTP::host] ":" 1][HTTP::uri]\n'
                "    }\n"
                "definition-signature "
                "WsYy2M6xMqvosIKIEH/FSsvhtWMe6xKOA6i7f09Hbp6tJviSRXSan9xiuI8AUXXeWwB4wU/ZVfd8OXR92fOjZY1GFyea9NoY64nZMZ3+/Yy5XuiqA1bBUNIpZNmv2/zYOhDBsO0Wg27evtJrkgU/3K0cBMIgaAM5gDjlmd1KPSPmpXgcMzNpbSuNAgw8uy5FKlFEjjSNmTzTvKy83QcFFoigAixOsq0ds9Qt2gPvQ+u/4qibvTo/mxf5LF1rDc1cWoVxwspGbC5VMt1DKjG5hRo0PAr2ES9bUyQst+30CoSULDgl3hWt9Q4S5OCKbwTHRZmglvZ12s8+Qolr56cVtQ==",
                "apiRawValues": {"verificationStatus": "signature-verified"},
                "fullPath": "/Common/_sys_https_redirect",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "_sys_https_redirect",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~_sys_https_redirect?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "when HTTP_REQUEST { \n"
                "    HTTP::redirect "
                '"https://[HTTP::host][HTTP::uri]" \n'
                "}",
                "fullPath": "/Common/http-redirect-https.tcl",
                "generation": 874,
                "kind": "tm:ltm:rule:rulestate",
                "name": "http-redirect-https.tcl",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~http-redirect-https.tcl?ver=14.1.2.1",
            },
            {
                "apiAnonymous": "when HTTP_REQUEST {\n"
                "\n"
                "  if { [string tolower [HTTP::header value "
                'Upgrade]] equals "websocket" } {\n'
                "    HTTP::disable\n"
                "#    ASM::disable\n"
                '    log local0. "[IP::client_addr] - Connection '
                "upgraded to websocket protocol. Disabling "
                "ASM-checks and HTTP protocol. Traffic is treated "
                'as L4 TCP stream."\n'
                "  } else {\n"
                "    HTTP::enable\n"
                "#    ASM::enable\n"
                '    log local0. "[IP::client_addr] - Regular HTTP '
                "request. ASM-checks and HTTP protocol enabled. "
                'Traffic is deep-inspected at L7."\n'
                "  }\n"
                "}",
                "fullPath": "/Common/terraform_irule",
                "generation": 1,
                "kind": "tm:ltm:rule:rulestate",
                "name": "terraform_irule",
                "partition": "Common",
                "selfLink": "https://localhost/mgmt/tm/ltm/rule/~Common~terraform_irule?ver=14.1.2.1",
            },
        ],
        "kind": "tm:ltm:rule:rulecollectionstate",
        "selfLink": "https://localhost/mgmt/tm/ltm/rule?ver=14.1.2.1",
    }

    golden_output = {"get.return_value": FakeResponse()}

    # def test_empty(self):
    #     self.device1 = Mock(**self.empty_output)
    #     obj = LtmRule(device=self.device1, alias='rest', via='rest', context='rest')
    #     with self.assertRaises(SchemaEmptyParserError):
    #         parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = LtmRule(
            device=self.device, alias="rest", via="rest", context="rest"
        )
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
