groups = {
    'debian': {
        'bundles': (
            'apt',
        ),
    },
    'shopware': {
        'bundles': (
            'apt', 'shopware', 'mysql'
        ),
        'members': (
            'node1',
        ),
        'subgroups': (
            'debian',
        ),
    },
    'all': {
        'member_patterns': (
            r".*",
        ),
    },
}
