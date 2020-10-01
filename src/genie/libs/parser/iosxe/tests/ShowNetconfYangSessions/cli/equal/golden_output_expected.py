expected_output = {
  'datastores': {
    'C': {
      'lock': 'Global-lock',
      'name': 'candidate'
    },
    'R': {
      'lock': 'Global-lock',
      'name': 'running'
    },
    'S': {
      'lock': 'Global-lock',
      'name': 'startup'
    }
  },
  'session-count': 1,
  'sessions': [{
    'global-lock': 'None',
    'session-id': 24,
    'source-host': '5.28.35.35',
    'transport': 'netconf-ssh',
    'username': 'admin'
  }]
}