* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

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

