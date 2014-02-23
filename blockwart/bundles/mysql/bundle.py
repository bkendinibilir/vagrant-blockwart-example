pkg_apt = {
    "mysql-server-5.5": {
        "installed": True,
        'depends': [
            'debconf_selection:mysql-server/root_password',
            'debconf_selection:mysql-server/root_password_again',
        ],
    },
}

debconf_selections = {
	"mysql-server/root_password": {
		"pkg_name": "mysql-server-5.5",
		"value": "password root",
	},
	"mysql-server/root_password_again": {
		"pkg_name": "mysql-server-5.5",
		"value": "password root",
	}
}