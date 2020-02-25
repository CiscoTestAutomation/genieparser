| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |     20.2      |

--------------------------------------------------------------------------------
                                New
--------------------------------------------------------------------------------
* IOS
    * Added ShowInterfaceStatus for:
        * show interface status
* IOSXE
    * Added ShowInterfaceStatus for:
        * show interface status
    * Added ShowProcessesMemorySorted for:
        * show processes memory sorted
    * Added ShowPlatformSoftwareMemoryBacktrace for:
        * show platform software memory {process} switch active {slot} alloc backtrace
    * Added ShowPlatformSoftwareMemoryCallsite for:
        * show platform software memory {process} switch active {slot} alloc callsite brief
    * Added ShowProcessesMemoryPlatformSorted for:
        * show processes memory platform sorted
* IOSXR
    * Added ShowSsh for:
        * show ssh session details
    * Added ShowSshHistory for:
        * show ssh history
* LINUX
    * Added Ps for:
        * ps -ef
        * ps -ef | grep {grep}

--------------------------------------------------------------------------------
                                Fix
--------------------------------------------------------------------------------

* IOSXE
    * Updated ShowIpCefInternal
        * Update schema and regex to support more various output
    * Updated ShowVlan
        * Modified if-condition to support various output.
    * Updated ShowEthernetServiceInstanceDetail
        * Modified regex to support outputs
    * Updated ShowVrfDetail:
        * Modified regex to support customer output
    * Updated ShowIpIgmpInterface:
        * Modified schema to support more various output
    * Updated ShowIpPimInterfaceDetail:
        * Modified schema to support more varied output
    * Updated ShowAccessLists:
        * Modified regex to parse more outputs
    * Updated ShowVersion:
        * Modified schema to support more varied output
    * Updated ShowLldpEntry:
        * Added Optional keys to the schema
* IOSXR
    * Updated ShowRouteIpv4:
        * Modified regex to support more various output
    * Updated ShowVersion:
        * To support output from Cisco 8000 series