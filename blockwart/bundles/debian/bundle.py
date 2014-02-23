pkg_apt = {
    "debconf-utils": {},
    "unzip": {},
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

files = {
    "/etc/hosts": {
        "source": "hosts",
        "mode": "0644",
    }
}