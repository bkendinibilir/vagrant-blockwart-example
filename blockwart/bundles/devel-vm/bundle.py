files = {
	"/etc/apache2/sites-available/default": {
		"source": "default-vhost",
		"mode": "0644",
		"depends": [
			"pkg_apt:apache2-mpm-worker",
		],
		"triggers": [
			"apache2_graceful",
		],
	},
	"/var/www/default/phpinfo.php": {
		"source": "phpinfo.php",
	}
}

directories = {
	"/var/www/default": {}
}

symlinks = {
	"/etc/apache2/sites-enabled/default": {
		"target": "/etc/apache2/sites-available/default",
		"depends": [
			"pkg_apt:apache2-mpm-worker",
		],
	},
}

actions = {
	"apache2_graceful": {
		"command": "apache2ctl graceful",
		"timing": "triggered",
	},
	"activate_apc.php": {
		"command": "gunzip /usr/share/doc/php-apc/apc.php.gz -c > /var/www/default/apc.php",
		"depends": [
			"pkg_apt:php-apc",
			"dir:/var/www/default",
		],
		"timing": "triggered",
	}
}