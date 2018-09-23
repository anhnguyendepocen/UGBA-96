test = {
  'name': 'Question 2_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> ca_mobility_public.num_rows
          12
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> ca_mobility_private.column('count mean')[0]
          463.8125
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
