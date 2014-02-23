# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

VM_NAME = "node1"
VM_IP = "192.168.33.10"

Vagrant.require_plugin "vagrant-blockwart"
Vagrant.require_plugin "vagrant-hostmanager"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.define VM_NAME do |node|
    node.vm.hostname = VM_NAME
    node.vm.network :private_network, ip: VM_IP
    node.hostmanager.aliases = %w(shopware.vm db.vm)
    node.vm.provision :blockwart do |bw|
      bw.node_name = VM_NAME
    end
  end

  config.hostmanager.enabled = true
  config.hostmanager.manage_host = true
  config.hostmanager.include_offline = true
  
end
