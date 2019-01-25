| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.16        |


* Fix for parser `show ip arp` under NXOS.


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.15        |


* Mandatory pump version number to avoid conflict with pypi


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.14        |


* Added parsers.json file required for the new Genie search index.


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.13        |


* Parsers are now made indexable by show command
  *  Updated all parsers to parse custom "output"
  *  Took out cmd to outside of parser and named to "cli_command" and "xml_command" for cli and xml parsers

--------------------------------------------------------------------------------
                                NTP
--------------------------------------------------------------------------------
* IOSXR
    * Add ShowNtpAssociations for 'show ntp associations'
    * Add ShowNtpStatus for 'show ntp status'


| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   | 3.1.12        |

--------------------------------------------------------------------------------
                                ARP
--------------------------------------------------------------------------------

* NXOS
    * Add ShowIpArpDetailVrfAll for 'show ip arp detail vrf all'
    * Add ShowIpArpSummaryVrfAll for 'show ip arp summary vrf all'
    * Add ShowIpArpstatisticsVrfAll for 'show ip arp statistics vrf all'

* IOSXE
    * Add ShowArp for
    	* 'show arp <WORD>'
    	* 'show arp vrf <vrf>' 
    	* 'show arp vrf <vrf> <WORD>'
    * Add ShowIpArpSummary for 'show ip arp summary'
    * Add ShowIpTraffic for 'show ip traffic'

* IOSXR
    * Add ShowArpDetail for
    	* 'show arp detail'
    	* 'show arp vrf <WORD> detail'
    * Add ShowArpTrafficDetail for 'show arp traffic detail'

* IOS
    * Add ShowIpArp for
        * 'show ip arp <WORD>'
        * 'show ip arp vrf <vrf>' 
        * 'show ip arp vrf <vrf> <WORD>'
    * Add ShowIpArpSummary for 'show ip arp summary'
    * Add ShowIpTraffic for 'show ip traffic'

--------------------------------------------------------------------------------
                                NTP
--------------------------------------------------------------------------------

* IOS
  * Updated parsers:
     * ShowNtpAssociations
* IOSXE
  * Updated parsers:
     * ShowNtpAssociations
* JUNOS
  * Updated parsers:
     * ShowNtpAssociations

--------------------------------------------------------------------------------
                                Interface
--------------------------------------------------------------------------------

* IOSXR
  * Updated parsers:
    * ShowInterfacesDetail

--------------------------------------------------------------------------------
                                PIM
--------------------------------------------------------------------------------

* NXOS
  * Updated parsers:
    * ShowIpv6PimNeighbor - bugfix

--------------------------------------------------------------------------------
                                HSRP
--------------------------------------------------------------------------------

* NXOS
  * Updated parsers:
    * ShowHsrpAll - bugfix

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------

* NXOS
  * Updated parsers:
    * ShowBgpL2vpnEvpnNeighbors - bugfix