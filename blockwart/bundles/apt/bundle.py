pkg_apt = {
    "debconf-utils": {
        "installed": True,  
    },
}

actions = {
    'update_apt': {
        'command': "apt-get update",
        'expected_return_code': 0,
        'timing': "pre",
    },
}