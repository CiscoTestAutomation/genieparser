expected_output = {
     "dynamic_incompatibility_status": "No incompatible configurations",
     "incompatible_configuartion_list": {
         1: {
             "capability_requirement": "STRICT",
             "enable_Disable_command": "Please remove track delay in milliseconds from all objects",
             "capability": "CAP_FEATURE_OTM_TRACK_DELAY_MS_CONFIGURED",
             "description": "Objects with track delay in millliseconds detected",
             "service": "otm"
         },
         2: {
             "capability_requirement": "STRICT",
             "enable_Disable_command": "Please remove all extended community list commands using \"no ip extcommunity-list standard <com>\"",
             "capability": "CAP_FEATURE_RPM_EXTCOMM_LIST_WITH_SEQ",
             "description": "\"ip extcommunity-list standard/expanded <com> seq <seq> <action> [<community list>]\" is configured with sequence",
             "service": "rpm"
         },
         3: {
             "capability_requirement": "STRICT",
             "enable_Disable_command": "Please remove track list boolean/weight or remove the delay configs from them",
             "capability": "CAP_FEATURE_OTM_TRACK_DELAY_CONFIGURED_WITH_LIST",
             "description": "Track list boolean/weight with delay config found",
             "service": "otm"
         }
     }
}
