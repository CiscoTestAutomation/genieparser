* Please follow the template we introduced in NOVEMBER.md file.
* Every parser need to be added under the corresponding feature.

| Module                  | Version       |
| ------------------------|:-------------:|
| ``genie.libs.parser``   |               |

--------------------------------------------------------------------------------
                                platform
--------------------------------------------------------------------------------
* IOSXE
    * Added ShowRedundancyStates for:
        show redundancy states

--------------------------------------------------------------------------------
                                policy-map
--------------------------------------------------------------------------------
* IOSXE
    * Fix class ShowPolicyMapTypeSuperParser


* IOSXE
	* Added ShowEthernetServiceInstanceStats for:
		show ethernet service instance id {service_instance_id} interface {interface} stats
	* Added ShowEthernetServiceInstance for:
		show ethernet service instance
	* Added ShowEthernetServiceInstanceDetail for:
		show ethernet service instance id {service_instance_id} interface {interface} detail