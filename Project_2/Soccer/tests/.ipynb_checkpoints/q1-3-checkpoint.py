test = {
    'name' : '1.3',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> weight = variables.where('variable name', 'weight')
                >>> weight.column('classification')[0]
                'quantitative'
                """
            }, {
                'code' : r"""
                >>> refNum = variables.where('variable name', 'refNum')
                >>> refNum.column('classification')[0]
                'categorical'
                """
            }]
        }]
}