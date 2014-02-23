pkg_apt = {
    "debconf-utils": {
        "installed": True,
    },
}

actions = {
    'update_apt': {
        'command': "apt-get update",
    },
}

svc_upstart = {
    "portmap": {
        "running": False,
    },
    "rpcbind-boot": {
        "running": False,
    },
}