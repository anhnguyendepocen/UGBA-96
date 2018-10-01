test = {
  'name': 'Question 4_2',
  'points': 1,
  'suites': [
    {
       'cases': [
        {
          'code': r"""
          >>> treatment_perform.column(1)[50]
          -0.3151487786892126
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> control_perform.column(1)[50]
          -0.30619993683238095
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
