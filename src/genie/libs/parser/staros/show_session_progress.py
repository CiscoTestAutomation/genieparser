"""starOS implementation of show_session_progress.py
Author: Luis Antonio Villalobos (luisvill)

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowSessionProgressSchema(MetaParser):
    """Schema for show session progress"""
    schema = {
        'session': {
            'In-progress_calls': str,
            'In-progress_active_calls': str,
            'In-progress_dormant_calls': str,
            'In-progress_alwayson_calls': str,
            'ARRIVED': str,
            'CSCF-CALL-ARRIVED': str,
            'CSCF-REGISTERING': str,
            'CSCF-REGISTERED': str,
            'LCP-NEG': str,
            'LCP-UP': str,
            'AUTHENTICATING': str,
            'BCMCS_SERVICE_AUTHENTICATING': str,
            'AUTHENTICATED': str,
            'PDG_AUTHORIZING': str,
            'PDG_AUTHORIZED': str,
            'IMS_AUTHORIZING': str,
            'IMS_AUTHORIZED': str,
            'MBMS_UE_AUTHORIZING': str,
            'MBMS_BEARER_AUTHORIZING': str,
            'DHCP_PENDING': str,
            'L2TP-LAC_CONNECTING': str,
            'MBMS_BEARER_CONNECTING': str,
            'CSCF-CALL-CONNECTING': str,
            'IPCP-UP': str,
            'NON-ANCHOR_CONNECTED': str,
            'AUTH-ONLY_CONNECTED': str,
            'SIMPLE-IPv4_CONNECTED': str,
            'SIMPLE-IPv6_CONNECTED': str,
            'SIMPLE-IPv4+IPv6_CONNECTED': str,
            'MOBILE-IPv4_CONNECTED': str,
            'MOBILE-IPv6_CONNECTED': str,
            'GTP_CONNECTING': str,
            'GTP_CONNECTED': str,
            'PROXY-MOBILE-IP_CONNECTING': str,
            'PROXY-MOBILE-IP_CONNECTED': str,
            'EPDG_RE-AUTHORIZING': str,
            'HA-IPSEC_CONNECTED': str,
            'L2TP-LAC_CONNECTED': str,
            'HNBGW_CONNECTED': str,
            'PDP-TYPE-PPP_CONNECTED': str,
            'IPSG_CONNECTED': str,
            'BCMCS_CONNECTED': str,
            'PCC_CONNECTED': str,
            'MBMS_UE_CONNECTED': str,
            'MBMS_BEARER_CONNECTED': str,
            'PAGING_CONNECTED': str,
            'PDN-TYPE-IPv4_CONNECTED': str,
            'PDN-TYPE-IPv6_CONNECTED': str,
            'PDN-TYPE-IPv4+IPv6_CONNECTED': str,
            'PDN-TYPE-Non-IP_CONNECTED': str,
            'CSCF-CALL-CONNECTED': str,
            'MME_ATTACHED': str,
            'HENBGW_CONNECTED': str,
            'CSCF-CALL-DISCONNECTING': str,
            'DISCONNECTING': str
        }
    }

class ShowSessionSchema(ShowSessionProgressSchema):
    """Parser for show session progress"""

    cli_command = 'show session progress'

    """
    [local]COR-VPC-1# show session progress 
Wednesday April 03 13:46:22 ART 2024
 2384060 In-progress calls
 2384060 In-progress active calls
       0 In-progress dormant calls
       0 In-progress always-on calls
      61 In-progress calls @ ARRIVED state
       0 In-progress calls @ CSCF-CALL-ARRIVED state 
       0 In-progress calls @ CSCF-REGISTERING state 
       0 In-progress calls @ CSCF-REGISTERED state 
       0 In-progress calls @ LCP-NEG state
       0 In-progress calls @ LCP-UP state
       0 In-progress calls @ AUTHENTICATING state
       0 In-progress calls @ BCMCS SERVICE AUTHENTICATING state
       0 In-progress calls @ AUTHENTICATED state
       0 In-progress calls @ PDG AUTHORIZING state
       0 In-progress calls @ PDG AUTHORIZED state
      29 In-progress calls @ IMS AUTHORIZING state
      15 In-progress calls @ IMS AUTHORIZED state
       0 In-progress calls @ MBMS UE AUTHORIZING state
       0 In-progress calls @ MBMS BEARER AUTHORIZING state
       0 In-progress calls @ DHCP PENDING state
       0 In-progress calls @ L2TP-LAC CONNECTING state
       0 In-progress calls @ MBMS BEARER CONNECTING state
       0 In-progress calls @ CSCF-CALL-CONNECTING state
       0 In-progress calls @ IPCP-UP state
       0 In-progress calls @ NON-ANCHOR CONNECTED state
       0 In-progress calls @ AUTH-ONLY CONNECTED state
       0 In-progress calls @ SIMPLE-IPv4 CONNECTED state
       0 In-progress calls @ SIMPLE-IPv6 CONNECTED state
       0 In-progress calls @ SIMPLE-IPv4+IPv6 CONNECTED state
       0 In-progress calls @ MOBILE-IPv4 CONNECTED state
       0 In-progress calls @ MOBILE-IPv6 CONNECTED state
       0 In-progress calls @ GTP CONNECTING state
       0 In-progress calls @ GTP CONNECTED state
       0 In-progress calls @ PROXY-MOBILE-IP CONNECTING state
       0 In-progress calls @ PROXY-MOBILE-IP CONNECTED state
       0 In-progress calls @ EPDG RE-AUTHORIZING state
       0 In-progress calls @ HA-IPSEC CONNECTED state
       0 In-progress calls @ L2TP-LAC CONNECTED state
       0 In-progress calls @ HNBGW CONNECTED state
       0 In-progress calls @ PDP-TYPE-PPP CONNECTED state
       0 In-progress calls @ IPSG CONNECTED state
       0 In-progress calls @ BCMCS CONNECTED state
       0 In-progress calls @ PCC CONNECTED state
       0 In-progress calls @ MBMS UE CONNECTED state
       0 In-progress calls @ MBMS BEARER CONNECTED state
       0 In-progress calls @ PAGING CONNECTED state
 1974827 In-progress calls @ PDN-TYPE-IPv4 CONNECTED state
  645499 In-progress calls @ PDN-TYPE-IPv6 CONNECTED state
       3 In-progress calls @ PDN-TYPE-IPv4+IPv6 CONNECTED state
       0 In-progress calls @ PDN-TYPE-Non-IP CONNECTED state
       0 In-progress calls @ CSCF-CALL-CONNECTED  state
       0 In-progress calls @ MME ATTACHED state
       0 In-progress calls @ HENBGW CONNECTED state
       0 In-progress calls @ CSCF-CALL-DISCONNECTING state
      43 In-progress calls @ DISCONNECTING state
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        # initial return dictionary
        session_dict = {}
        result_dict = {}

        # Define the regex pattern for matching the rows with values
        pattern1 = re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls$' , re.MULTILINE) 
        pattern2 = re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress active calls$' , re.MULTILINE)
        pattern3= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress dormant calls$' , re.MULTILINE)
        pattern4= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress always-on calls$' , re.MULTILINE)
        pattern5= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ ARRIVED state$' , re.MULTILINE)
        pattern6= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ CSCF-CALL-ARRIVED state' , re.MULTILINE)
        pattern7= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ CSCF-REGISTERING state' , re.MULTILINE)
        pattern8= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ CSCF-REGISTERED state' , re.MULTILINE)
        pattern9= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ LCP-NEG state' , re.MULTILINE)
        pattern10= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ LCP-UP state' , re.MULTILINE)
        pattern11= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ AUTHENTICATING state' , re.MULTILINE)
        pattern12= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ BCMCS SERVICE AUTHENTICATING state' , re.MULTILINE)
        pattern13= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ AUTHENTICATED state' , re.MULTILINE)
        pattern14= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PDG AUTHORIZING state' , re.MULTILINE)
        pattern15= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PDG AUTHORIZED state' , re.MULTILINE)
        pattern16= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ IMS AUTHORIZING state' , re.MULTILINE)
        pattern17= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ IMS AUTHORIZED state' , re.MULTILINE)
        pattern18= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MBMS UE AUTHORIZING state' , re.MULTILINE)
        pattern19= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MBMS BEARER AUTHORIZING state' , re.MULTILINE)
        pattern20= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ DHCP PENDING state' , re.MULTILINE)
        pattern21= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ L2TP-LAC CONNECTING state' , re.MULTILINE)
        pattern22= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MBMS BEARER CONNECTING state' , re.MULTILINE)
        pattern23= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ CSCF-CALL-CONNECTING state' , re.MULTILINE)
        pattern24= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ IPCP-UP state' , re.MULTILINE)
        pattern25= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ NON-ANCHOR CONNECTED state' , re.MULTILINE)
        pattern26= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ AUTH-ONLY CONNECTED state' , re.MULTILINE)
        pattern27= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ SIMPLE-IPv4 CONNECTED state' , re.MULTILINE)
        pattern28= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ SIMPLE-IPv6 CONNECTED state' , re.MULTILINE)
        pattern29= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ SIMPLE-IPv4\+IPv6 CONNECTED state' , re.MULTILINE)
        pattern30= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MOBILE-IPv4 CONNECTED state' , re.MULTILINE)
        pattern31= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MOBILE-IPv6 CONNECTED state' , re.MULTILINE)
        pattern32= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ GTP CONNECTING state' , re.MULTILINE)
        pattern33= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ GTP CONNECTED state' , re.MULTILINE)
        pattern34= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PROXY-MOBILE-IP CONNECTING state' , re.MULTILINE)
        pattern35= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PROXY-MOBILE-IP CONNECTED state' , re.MULTILINE)
        pattern36= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ EPDG RE-AUTHORIZING state' , re.MULTILINE)
        pattern37= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ HA-IPSEC CONNECTED state' , re.MULTILINE)
        pattern38= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ L2TP-LAC CONNECTED state' , re.MULTILINE)
        pattern39= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ HNBGW CONNECTED state' , re.MULTILINE)
        pattern40= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PDP-TYPE-PPP CONNECTED state' , re.MULTILINE)
        pattern41= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ IPSG CONNECTED state' , re.MULTILINE)
        pattern42= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ BCMCS CONNECTED state' , re.MULTILINE)
        pattern43= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PCC CONNECTED state' , re.MULTILINE)
        pattern44= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MBMS UE CONNECTED state' , re.MULTILINE)
        pattern45= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MBMS BEARER CONNECTED state' , re.MULTILINE)
        pattern46= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PAGING CONNECTED state' , re.MULTILINE)
        pattern47= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PDN-TYPE-IPv4 CONNECTED state' , re.MULTILINE)
        pattern48= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PDN-TYPE-IPv6 CONNECTED state' , re.MULTILINE)
        pattern49= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PDN-TYPE-IPv4\+IPv6 CONNECTED state' , re.MULTILINE)
        pattern50= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ PDN-TYPE-Non-IP CONNECTED state' , re.MULTILINE)
        pattern51= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ CSCF-CALL-CONNECTED  state' , re.MULTILINE)
        pattern52= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ MME ATTACHED state' , re.MULTILINE)
        pattern53= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ HENBGW CONNECTED state' , re.MULTILINE)
        pattern54= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ CSCF-CALL-DISCONNECTING state' , re.MULTILINE)
        pattern55= re.compile(r'^\s+(?P<Calls>\d+)\sIn-progress calls @ DISCONNECTING state' , re.MULTILINE)

        #For Loop to get all the values from output
        for match in out.splitlines(): #Split a string into a list where each line is a list item
            m= pattern1.match(match) #Matching values in pattern1 <re.Match object; span=(0, 26), match=' 2333036 In-progress calls'>
            if m:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
            
                #Defining a variable that contains the value of the regex
                call = m.groupdict()['Calls'].strip()
                result_dict['In-progress_calls']= call
                continue
            m1= pattern2.match(match) #Matching values in pattern2
            if m1:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m1.groupdict()['Calls'].strip()

                result_dict['In-progress_active_calls']= call
                continue
            m2= pattern3.match(match) #Matching values in pattern3
            if m2:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m2.groupdict()['Calls'].strip()

                result_dict['In-progress_dormant_calls']= call
                continue
            m3= pattern4.match(match) #Matching values in pattern4
            if m3:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m3.groupdict()['Calls'].strip()

                result_dict['In-progress_alwayson_calls']= call
                
                continue
            m4= pattern5.match(match) #Matching values in pattern5
            if m4:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m4.groupdict()['Calls'].strip()

                result_dict['ARRIVED']= call
                
                continue
            m5= pattern6.match(match) #Matching values in pattern6
            if m5:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m5.groupdict()['Calls'].strip()

                result_dict['CSCF-CALL-ARRIVED']= call
                
                continue
            m6= pattern7.match(match) #Matching values in pattern7
            if m6:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m6.groupdict()['Calls'].strip()

                result_dict['CSCF-REGISTERING']= call
                
                continue
            m7= pattern8.match(match) #Matching values in pattern8
            if m7:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m7.groupdict()['Calls'].strip()

                result_dict['CSCF-REGISTERED']= call
                
                continue
            m8= pattern9.match(match) #Matching values in pattern9
            if m8:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m8.groupdict()['Calls'].strip()

                result_dict['LCP-NEG']= call
                
                continue
            m9= pattern10.match(match) #Matching values in pattern10
            if m9:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m9.groupdict()['Calls'].strip()

                result_dict['LCP-UP']= call
                
                continue
            m10= pattern11.match(match) #Matching values in pattern11
            if m10:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m10.groupdict()['Calls'].strip()

                result_dict['AUTHENTICATING']= call
                
                continue
            m11= pattern12.match(match) #Matching values in pattern12
            if m11:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m11.groupdict()['Calls'].strip()

                result_dict['BCMCS_SERVICE_AUTHENTICATING']= call
                
                continue
            m12= pattern13.match(match) #Matching values in pattern13
            if m12:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m12.groupdict()['Calls'].strip()

                result_dict['AUTHENTICATED']= call
                
                continue
            m13= pattern14.match(match) #Matching values in pattern14
            if m13:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m13.groupdict()['Calls'].strip()

                result_dict['PDG_AUTHORIZING']= call
                
                continue
            m14= pattern15.match(match) #Matching values in pattern15
            if m14:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m14.groupdict()['Calls'].strip()

                result_dict['PDG_AUTHORIZED']= call
                
                continue
            m15= pattern16.match(match) #Matching values in pattern16
            if m15:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m15.groupdict()['Calls'].strip()

                result_dict['IMS_AUTHORIZING']= call
                
                continue
            m16= pattern17.match(match) #Matching values in pattern17
            if m16:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m16.groupdict()['Calls'].strip()

                result_dict['IMS_AUTHORIZED']= call
                
                continue
            m17= pattern18.match(match) #Matching values in pattern18
            if m17:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m17.groupdict()['Calls'].strip()

                result_dict['MBMS_UE_AUTHORIZING']= call
                
                continue
            m18= pattern19.match(match) #Matching values in pattern19
            if m18:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m18.groupdict()['Calls'].strip()

                result_dict['MBMS_BEARER_AUTHORIZING']= call
                
                continue
            m19= pattern20.match(match) #Matching values in pattern20
            if m19:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m19.groupdict()['Calls'].strip()

                result_dict['DHCP_PENDING']= call
                
                continue
            m20= pattern21.match(match) #Matching values in pattern21
            if m20:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m20.groupdict()['Calls'].strip()

                result_dict['L2TP-LAC_CONNECTING']= call
                
                continue
            m21= pattern22.match(match) #Matching values in pattern22
            if m21:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m21.groupdict()['Calls'].strip()

                result_dict['MBMS_BEARER_CONNECTING']= call
                
                continue
            m22= pattern23.match(match) #Matching values in pattern23
            if m22:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m22.groupdict()['Calls'].strip()

                result_dict['CSCF-CALL-CONNECTING']= call
                
                continue
            m23= pattern24.match(match) #Matching values in pattern24
            if m23:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m23.groupdict()['Calls'].strip()

                result_dict['IPCP-UP']= call
                
                continue
            m24= pattern25.match(match) #Matching values in pattern25
            if m24:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m24.groupdict()['Calls'].strip()

                result_dict['NON-ANCHOR_CONNECTED']= call
                
                continue
            m25= pattern26.match(match) #Matching values in pattern26
            if m25:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m25.groupdict()['Calls'].strip()

                result_dict['AUTH-ONLY_CONNECTED']= call
                
                continue
            m26= pattern27.match(match) #Matching values in pattern27
            if m26:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m26.groupdict()['Calls'].strip()

                result_dict['SIMPLE-IPv4_CONNECTED']= call
                
                continue
            m27= pattern28.match(match) #Matching values in pattern28
            if m27:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m27.groupdict()['Calls'].strip()

                result_dict['SIMPLE-IPv6_CONNECTED']= call
                
                continue
            m28= pattern29.match(match) #Matching values in pattern29
            if m28:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m28.groupdict()['Calls'].strip()

                result_dict['SIMPLE-IPv4+IPv6_CONNECTED']= call
                
                continue
            m29= pattern30.match(match) #Matching values in pattern30
            if m29:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m29.groupdict()['Calls'].strip()

                result_dict['MOBILE-IPv4_CONNECTED']= call
                
                continue
            m30= pattern31.match(match) #Matching values in pattern31
            if m30:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m30.groupdict()['Calls'].strip()

                result_dict['MOBILE-IPv6_CONNECTED']= call
                
                continue
            m31= pattern32.match(match) #Matching values in pattern32
            if m31:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m31.groupdict()['Calls'].strip()

                result_dict['GTP_CONNECTING']= call
                
                continue
            m32= pattern33.match(match) #Matching values in pattern33
            if m32:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m32.groupdict()['Calls'].strip()

                result_dict['GTP_CONNECTED']= call
                
                continue
            m33= pattern34.match(match) #Matching values in pattern34
            if m33:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m33.groupdict()['Calls'].strip()

                result_dict['PROXY-MOBILE-IP_CONNECTING']= call
                
                continue
            m34= pattern35.match(match) #Matching values in pattern35
            if m34:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m34.groupdict()['Calls'].strip()

                result_dict['PROXY-MOBILE-IP_CONNECTED']= call
                
                continue
            m35= pattern36.match(match) #Matching values in pattern36
            if m35:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m35.groupdict()['Calls'].strip()

                result_dict['EPDG_RE-AUTHORIZING']= call
                
                continue
            m36= pattern37.match(match) #Matching values in pattern37
            if m36:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m36.groupdict()['Calls'].strip()

                result_dict['HA-IPSEC_CONNECTED']= call
                
                continue
            m37= pattern38.match(match) #Matching values in pattern38
            if m37:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m37.groupdict()['Calls'].strip()

                result_dict['L2TP-LAC_CONNECTED']= call
                
                continue
            m38= pattern39.match(match) #Matching values in pattern39
            if m38:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m38.groupdict()['Calls'].strip()

                result_dict['HNBGW_CONNECTED']= call
                
                continue
            m39= pattern40.match(match) #Matching values in pattern40
            if m39:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m39.groupdict()['Calls'].strip()

                result_dict['PDP-TYPE-PPP_CONNECTED']= call
                
                continue
            m40= pattern41.match(match) #Matching values in pattern41
            if m40:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m40.groupdict()['Calls'].strip()

                result_dict['IPSG_CONNECTED']= call
                
                continue
            m41= pattern42.match(match) #Matching values in pattern42
            if m41:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m41.groupdict()['Calls'].strip()

                result_dict['BCMCS_CONNECTED']= call
                
                continue
            m42= pattern43.match(match) #Matching values in pattern43
            if m42:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m42.groupdict()['Calls'].strip()

                result_dict['PCC_CONNECTED']= call
                
                continue
            m43= pattern44.match(match) #Matching values in pattern44
            if m43:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m43.groupdict()['Calls'].strip()

                result_dict['MBMS_UE_CONNECTED']= call
                
                continue
            m44= pattern45.match(match) #Matching values in pattern45
            if m44:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m44.groupdict()['Calls'].strip()

                result_dict['MBMS_BEARER_CONNECTED']= call
                
                continue
            m45= pattern46.match(match) #Matching values in pattern46
            if m45:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m45.groupdict()['Calls'].strip()

                result_dict['PAGING_CONNECTED']= call
                
                continue
            m46= pattern47.match(match) #Matching values in pattern47
            if m46:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m46.groupdict()['Calls'].strip()

                result_dict['PDN-TYPE-IPv4_CONNECTED']= call
                
                continue
            m47= pattern48.match(match) #Matching values in pattern48
            if m47:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m47.groupdict()['Calls'].strip()

                result_dict['PDN-TYPE-IPv6_CONNECTED']= call
                
                continue
            m48= pattern49.match(match) #Matching values in pattern49
            if m48:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m48.groupdict()['Calls'].strip()

                result_dict['PDN-TYPE-IPv4+IPv6_CONNECTED']= call
                
                continue
            m49= pattern50.match(match) #Matching values in pattern50
            if m49:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m49.groupdict()['Calls'].strip()

                result_dict['PDN-TYPE-Non-IP_CONNECTED']= call
                
                continue
            m50= pattern51.match(match) #Matching values in pattern51
            if m50:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m50.groupdict()['Calls'].strip()

                result_dict['CSCF-CALL-CONNECTED']= call
                
                continue
            m51= pattern52.match(match) #Matching values in pattern52
            if m51:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m51.groupdict()['Calls'].strip()

                result_dict['MME_ATTACHED']= call
                
                continue
            m52= pattern53.match(match) #Matching values in pattern53
            if m52:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m52.groupdict()['Calls'].strip()

                result_dict['HENBGW_CONNECTED']= call
                
                continue
            m53= pattern54.match(match) #Matching values in pattern54
            if m53:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m53.groupdict()['Calls'].strip()

                result_dict['CSCF-CALL-DISCONNECTING']= call
                
                continue
            m54= pattern55.match(match) #Matching values in pattern55
            if m54:
                if 'session' not in session_dict:
                    result_dict = session_dict.setdefault('session',{})
                
                #Defining a variable that contains the value of the regex
                call = m54.groupdict()['Calls'].strip()

                result_dict['DISCONNECTING']= call
                continue
        return session_dict
