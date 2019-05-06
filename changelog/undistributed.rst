* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                   INTERFACE
--------------------------------------------------------------------------------
* IOSXE
	   * Added interface value under convert_intf_name method of common file

--------------------------------------------------------------------------------
                                BGP
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowBgpAllNeighbors for more varied neighbor capabilities
		    * vrf default value handled
	  * Updated ShowIpBgpNeighbors to support different Address familiy
* IOSXR
    * Updated ShowBgpAllAll for more variations of parameters
    * Updated ShowBgpAllNeighbors for more varied neighbor capabilities

--------------------------------------------------------------------------------
                                  POLICY-MAP
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowPolicyMapInterface to support more policy action type
    
--------------------------------------------------------------------------------
                                   PLATFORM
--------------------------------------------------------------------------------
* IOSXE
    * Updated ShowPlatform to support optional output

--------------------------------------------------------------------------------
                                   RIP
--------------------------------------------------------------------------------
* IOSXR
    * Updated ShowRipInterface for more varied interface name and status

