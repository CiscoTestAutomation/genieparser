expected_output = {
    "rules": {
        1: {
            "match_mode":"mdt-subscription-mode",
            "command":"no update-policy",
            "action":"skip"
        },
        2: {
            "match_mode":"mdt-subscription-mode",
            "command":"no stream",
            "action":"skip"
        },
        3: {
            "match_mode":"mdt-subscription-mode",
            "command":"no filter",
            "action":"skip"
        },
        4: {
            "match_mode":"mdt-subscription-mode",
            "command":"no encoding",
            "action":"skip"
        },
        5: {
            "match_mode":"rogue-rule",
            "command":"no match",
            "action":"skip"
        },
        6: {
            "match_mode":"rogue-rule",
            "command":"no classify malicious",
            "action":"skip"
        },
        7: {
            "match_mode":"main-cpu",
            "command":"no main-cpu",
            "action":"post-apply"
        },
        8: {
            "match_mode":"flowmon",
            "command":"no record wireless",
            "action":"skip"
        },
        9: {
            "match_mode":"configure",
            "command":"no wireless country",
            "action":"skip"
        }
    }
}