test = {
    'name' : '2.3',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> data.num_rows == 84826
                True
                """
            },  {
                'code' : r"""
                >>> meanExpMin = min(data.column('meanExp'))
                >>> lower = stats.where('statistic', 'mean').column('meanExp')[0] - 2 * stats.where('statistic', 'std').column('meanExp')[0]
                >>> actualMin = stats.where('statistic', 'min').column('meanExp')[0]
                >>> actualMin < lower < meanExpMin
                True
                """
            }]
        }]
}