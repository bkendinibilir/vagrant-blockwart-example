pkg_apt = {
    "debconf-utils": {},
    "unzip": {},
}

actions = {
    'update_apt': {
        'command': "apt-get update",
        'unless': "stat /var/lib/apt/lists | grep Modify | grep \"$(date +%Y-%m-%d)\"",
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