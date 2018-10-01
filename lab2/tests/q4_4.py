test = {
  'name': 'Question 4_4',
  'points': 1,
  'suites': [
    {
       'cases': [
        {
          'code': r"""
          >>> treatment_quits.column(1)[13]
          0.06015037593984962
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> control_quits.column(1)[13]
          0.14754098360655737
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
