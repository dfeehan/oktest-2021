test = {   'name': 'childmort_2015',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> childmort_2015.num_rows == '
                                               '201\n'
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.isclose(childmort_2015.where('country', "
                                               "are.equal_to('Denmark'))['childmort_m'][0],0.00429676)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> '
                                               "np.isclose(childmort_2015.where('country', "
                                               "are.equal_to('Denmark'))['childmort_f'][0],0.0038797999999999888)\n"
                                               'True',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
