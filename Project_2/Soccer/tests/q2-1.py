test = {
    'name' : '2.1',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> computed = list(stats.column('statistic'))
                >>> [stat in computed for stat in ['min', 'min', 'mean', 'std']]
                [True, True, True, True]
                """
            }, {
                'code' : r"""
                >>> stats.where('statistic', 'max').column('playerShort')[0]
                'zurutuza'
                """
            }, {
                'code' : r"""
                >>> actual = stats.where('statistic', 'max').column('meanIAT')[0]
                >>> np.isclose(actual, 0.573793)
                True
                """
            }]
        }]
}