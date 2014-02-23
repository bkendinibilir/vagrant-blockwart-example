groups = {
    'debian': {
        'bundles': (
            'apt',
        ),
    },
    'formmed-devel': {
        'bundles': (
            'shopware', 'mysql'
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
