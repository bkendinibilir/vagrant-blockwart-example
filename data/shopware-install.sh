#!/bin/sh

cd /var/www/shopware.devel.vm/htdocs
wget http://releases.s3.shopware.com/install_4.2.1.zip
unzip -o install_4.2.1.zip 
rm install_4.2.1.zip 
rm -rf install/
chown -R www-data logs/ config.php cache/ files/ engine/ media/

echo "CREATE DATABASE IF NOT EXISTS shopware;" | mysql --defaults-file=/etc/mysql/debian.cnf
echo "GRANT ALL on shopware.* to shopware@localhost identified by \"shopware\";" | mysql --defaults-file=/etc/mysql/debian.cnf
zcat /vagrant/data/shopware-db-4.2.1.sql.gz | mysql --defaults-file=/etc/mysql/debian.cnf shopware

cat > config.php <<CONFIG
<?php return array (
  'db' =>
  array (
    'username' => 'shopware',
    'password' => 'shopware',
    'host' => 'localhost',
    'port' => '3306',
    'dbname' => 'shopware',
  ),
);
CONFIG

/etc/init.d/php5-fpm reload
