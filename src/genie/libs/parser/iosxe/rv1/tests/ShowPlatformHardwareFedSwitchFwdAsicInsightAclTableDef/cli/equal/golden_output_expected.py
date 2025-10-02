expected_output = {
  'acl_entries': {
    583: {
      'acl_oid': 583,
      'acl_key_profile_oid': 511,
      'acl_match_key_fields': [
        'IPV4_SIP',
        'IPV4_DIP',
        'TOS',
        'PROTOCOL',
        'IPV4_FLAGS'
      ],
      'acl_commands': [
        'DROP',
        'FORCE_TRAP_WITH_EVENT',
        'COUNTER',
        'DO_MIRROR',
        'MIRROR_CMD'
      ],
      'acl_cmd_profile_oid': 581
    }
  }
}
