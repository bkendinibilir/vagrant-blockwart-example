# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"

Vagrant.require_plugin "vagrant-blockwart"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "precise32"
  config.vm.hostname = "node1"
  config.vm.provision :blockwart do |bw|
    bw.node_name = "node1"
  end

  # config.vm.network :forwarded_port, guest: 80, host: 8080
  # config.vm.network :private_network, ip: "192.168.33.10"
  # config.vm.network :public_network
  # config.ssh.forward_agent = true

  # config.vm.synced_folder "../data", "/vagrant_data"

  # config.vm.provider :virtualbox do |vb|
  #   vb.gui = true
  #   vb.customize ["modifyvm", :id, "--memory", "1024"]
  # end
end
