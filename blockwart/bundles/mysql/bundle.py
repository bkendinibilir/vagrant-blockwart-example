pkg_apt = {
    "mysql-server-5.5": {
        "installed": True,
        'depends': [
            'debconf_selection:mysql-server/root_password',
            'debconf_selection:mysql-server/root_password_again',
        ],
    },
}

actions = {
	"restart_mysql": {
		'command': "service mysql restart",
		'timing': 'triggered',
	}, 
}

files = {
	"/etc/mysql/conf.d/mysqld_bind.cnf": {
		"mode": "0644",
        "owner": "root",
        "group": "root",
        "source": "mysqld_bind.cnf",
        "triggers": [
        	"restart_mysql",
        ]
	},
}

debconf_selections = {
	"mysql-server/root_password": {
		"pkg_name": "mysql-server-5.5",
		"value": "password root",
		"unless": "dpkg -l|grep -E '^ii\s+mysql-server-5.5'",
	},
	"mysql-server/root_password_again": {
		"pkg_name": "mysql-server-5.5",
		"value": "password root",
		"unless": "dpkg -l|grep -E '^ii\s+mysql-server-5.5'",
	},
}
