# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/xenial64"

  # Create a forwarded port mapping which allows access to a specific port
  # within the machine from a port on the host machine and only allow access
  # via 127.0.0.1 to disable public access
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  # Customize the amount of memory on the VM:
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "512"
  end

  # Provision the virtual machine with a normal shellscript. This will add
  # Docker's GPG key, add the repository, install Docker, and add the vagrant
  # user to the docker group.
  config.vm.provision "shell", inline: <<-SHELL
    echo "Adding Docker GPG key"
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

    echo "Adding Docker repository"
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

    echo "Installing Docker"
    apt-get update
    apt-cache policy docker-ce
    apt-get install -y docker-ce

    echo "Installing Docker Compose"
    curl -sL "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    chmod -v +x /usr/local/bin/docker-compose

    echo "Adding vagrant user to docker group"
    usermod -aG docker vagrant

    echo "Check that Docker is up"
    systemctl status docker
  SHELL

  # Finally, set a post-up message for further instructions
  config.vm.post_up_message = <<-POSTUP
    The Vagrant VM is now booted and accessible.

    To get a terminal, type `vagrant ssh`.

    Any files in #{File.expand_path File.dirname(__FILE__)} on your machine
    will be available in the VM under `/vagrant`.

    Have a look in there for a Dockerfile to build!
  POSTUP
end
