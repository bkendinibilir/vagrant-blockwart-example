# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.require_plugin "vagrant-blockwart"
Vagrant.require_plugin "vagrant-hostmanager"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.define 'node1' do |node|
    node.vm.hostname = "node1"
    node.vm.network :private_network, ip: "192.168.33.10"
    node.hostmanager.aliases = %w(shopware.vm)
    node.vm.provision :blockwart do |bw|
      bw.node_name = "node1"
    end
  end

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  
end
