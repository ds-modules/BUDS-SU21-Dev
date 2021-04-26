test = {
    'name' : '1.2',
    'suites' : [{
            'cases' : [{
                'code' : r"""
                >>> data.num_columns == 19
                True
                """
            }, {
                'code' : r"""
                >>> [label in data.labels for label in cols_to_drop]
                [False, False, False, False, False, False, False, False, False]
                """
            }]
        }]
}