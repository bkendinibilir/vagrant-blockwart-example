# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.require_plugin "vagrant-blockwart"
Vagrant.require_plugin "vagrant-hostsupdater"

VM_NAME = 'devel'
VM_HOST = 'devel.vm'
VM_IP = '192.168.33.10'

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.define VM_NAME do |node|
    node.vm.network :private_network, ip: VM_IP
    node.vm.hostname = VM_NAME
    node.hostsupdater.aliases = %w(VM_HOST shopware.VM_HOST)
    node.vm.provision :blockwart do |bw|
      bw.node_name = VM_NAME
      bw.node_host = VM_HOST
      bw.interactive = false
    end
  end
end
