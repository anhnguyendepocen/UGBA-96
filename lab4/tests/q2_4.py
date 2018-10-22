test = {
  'name': 'Question 2.4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> noncontacted_age_matches.num_rows == 360
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> noncontacted_age_matches.num_columns == 8
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> noncontacted_age_matches.column(5).item(2) == 43
          True
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
