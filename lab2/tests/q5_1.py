test = {
  'name': 'Question 5_1',
  'points': 1,
  'suites': [
    {
       'cases': [
        {
          'code': r"""
          >>> experiment.num_rows == 249
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> experiment.num_columns
          11
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.mean(experiment.column(6))
          2.9751457807228916
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
