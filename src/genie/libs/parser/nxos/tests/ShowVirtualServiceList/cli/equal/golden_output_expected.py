

expected_output = {
    'service': {
        "guestshell+": {
            'status': "activated",
            'package': "guestshell.ova",
        },
        "lxc4": {
            'status': "not installed",
        },
        "sc_sanity_03": {
            'status': "installed",
            'package': "ft_mv_no_onep.ova",
        },
        "lxc_upgrade": {
            'status': "activate failed",
            'package': "c63lxc_no_onep.ova",
        },
    },
}
