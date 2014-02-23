# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.require_plugin "vagrant-blockwart"
Vagrant.require_plugin "vagrant-hostsupdater"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.define 'devel' do |node|
    node.vm.network :private_network, ip: '192.168.33.10'
    node.vm.hostname = 'devel'
    node.hostsupdater.aliases = %w(devel.vm shopware.devel.vm)
    node.vm.provision :blockwart do |bw|
      bw.node_name = 'devel'
      bw.node_host = 'devel.vm'
    end
  end

end
