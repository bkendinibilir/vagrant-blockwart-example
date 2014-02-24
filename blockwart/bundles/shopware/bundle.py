pkg_apt = {
    "apache2-mpm-worker": {
    	"installed": True,
        "triggers": [
        	"remove_index_html",
        	"remove_000-default",
        ],
    },
    "libapache2-mod-fastcgi": {},
    "php5": {},
    "php-apc": {
    	"installed": True,
    	"triggers": [
    		"activate_apc.php",
    	],
    },
    "php5-curl": {},
    "php5-gd": {},
    "php5-fpm" : {},
    "php5-mysql": {},
}

actions = {
	"remove_index_html": {
		"command": "rm -f /var/www/index.html",
		'timing': "triggered",
	},
	"remove_000-default": {
		"command": "rm -f /etc/apache2/sites-enabled/000-default",
		'timing': "triggered",
	},
	"apache2_graceful": {
		"command": "apache2ctl graceful",
		"timing": "triggered",
	},
	"php-fpm_restart": {
		"command": "/etc/init.d/php5-fpm restart",
		"timing": "triggered",
	},
	"activate_apc.php": {
		"command": "gunzip /usr/share/doc/php-apc/apc.php.gz -c > /var/www/default/apc.php",
		"timing": "triggered",
	},
	"install_shopware": {
		"command": "/vagrant/data/shopware-install.sh",
		"timing": "post",
		"unless": "test -d /var/www/shopware.devel.vm/htdocs/engine",
	}
}

files = {
	"/etc/apache2/sites-available/shopware.{}".format(node.hostname): {
		"source": "shopware-vhost",
		"mode": "0644",
		"depends": [
			"pkg_apt:apache2-mpm-worker",
		],
		"triggers": [
			"apache2_graceful",
		],
	},
	"/etc/apache2/conf.d/php5-fpm.conf": {
		"source": "php5-fpm.conf",
		"depends": [
			"pkg_apt:php5-fpm",
		],
		"triggers": [
			"apache2_graceful",
		],
	},
	"/etc/php5/conf.d/apc.ini": {
		"source": "apc.ini",
		"mode": "0644",
		"depends": [
			"pkg_apt:php-apc",
		],
		"triggers": [
			"php-fpm_restart",
		],
	},
	"/etc/php5/fpm/php.ini": {
		"source": "php.ini",
		"mode": "0644",
		"depends": [
			"pkg_apt:php5-fpm",
		],
		"triggers": [
			"php-fpm_restart",
		],
	},
}

# enable apache vhosts
symlinks = {
	"/etc/apache2/sites-enabled/shopware.{}".format(node.hostname): {
		"target": "/etc/apache2/sites-available/shopware.{}".format(node.hostname),
		"depends": [
			"file:/etc/apache2/sites-available/shopware.{}".format(node.hostname),
		],
	},
}

# enable apache modules
for a2mod in ['actions', 'fastcgi', 'alias']:
	for ftype in ['conf', 'load']:
		symlinks["/etc/apache2/mods-enabled/{}.{}".format(a2mod, ftype)] = {
			"target": "../mods-available/{}.{}".format(a2mod, ftype),
			"depends": [
				"pkg_apt:apache2-mpm-worker",
			],
			"triggers": [
				"apache2_graceful",
			],
		}
for a2mod in ['rewrite']:
	symlinks["/etc/apache2/mods-enabled/{}.load".format(a2mod)] = {
		"target": "../mods-available/{}.load".format(a2mod),
		"depends": [
			"pkg_apt:apache2-mpm-worker",
		],
		"triggers": [
			"apache2_graceful",
		],
	}

directories = {
	"/var/www/shopware.{}".format(node.hostname): {},
	"/var/www/shopware.{}/logs".format(node.hostname): {},
	"/var/www/shopware.{}/htdocs".format(node.hostname): {},
}