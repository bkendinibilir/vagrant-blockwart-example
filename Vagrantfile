# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.require_plugin "vagrant-blockwart"
Vagrant.require_plugin "vagrant-hostsupdater"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.define 'node1' do |node|
    node.vm.network :private_network, ip: '192.168.33.10'
    node.vm.hostname = 'node1'
    node.hostsupdater.aliases = %w(shopware.vm db.vm)
    node.vm.provision :blockwart do |bw|
      bw.node_name = 'node1'
      bw.node_host = 'node1.vm'
    end
  end

end
