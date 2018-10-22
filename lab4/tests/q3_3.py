test = {
  'name': 'Question 3.3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> noncontacted_full_matches.num_rows == 360
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> noncontacted_full_matches.num_columns == 8
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> noncontacted_full_matches.column(5).item(2) == 43
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> noncontacted_full_matches.column(4).item(1) == 0
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
