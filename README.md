# Demo script
This demo script is intended to walk people new to Docker through running a
container from Docker Hub, creating then running their own image, and finally
using Docker Compose to automate the running of multiple containers.

## Setup
1. Make sure that you have installed VirtualBox and Vagrant, then clone this
   repository using Git.
2. Open a terminal, `cd` to your cloned repository, then run `vagrant up` to
   start the virtual machine.
3. Wait a bit while the provisioner runs. It's installing Docker and some other
   things.
4. Run `vagrant ssh` to open an SSH session to the virtual machine.

## Running an image
1. Start by running `docker run alpine`. You'll see Docker pulling in the image
   and it will then launch your container.
2. It ran - but it just kicked you straight out.
3. `docker run -it alpine` and have a look around. The `-i` and `-t` switches
   open an interactive session and allocate a TTY, allowing you to have a proper
   console session inside of the container.
4. Press CTRL+D to exit the container terminal and return to the virtual
   machine.

## Building an image
1. First of all, `cd /vagrant` as that's where the Dockerfile is.
2. To build the container image, run `docker build .` - note the last dot:
   that's the build context which in this case is the current directory.
3. Docker will now build the container, doing what is defined in the Dockerfile.
4. Once it's built, `docker image list` reveals our image, but it's only
   referred to by hash.
5. Rebuild the image, but this time add a tag - run `docker build --tag
   webapp .`.
6. Notice that the build was much quicker - almost instant. This is because
   Docker is able to determine that nothing has changed and simply rebuilds the
   image using a cache.
7. Run `docker image list` again to show the image with a more usable name.

## Running the webapp
1. With the image built, it can be run by executing `docker run
   --name=webapp-container webapp`.
2. Running that command will result in an attached session - you'll be able to
   see the container's `stdout` stream.
3. The server says it's listening! Browse to http://localhost:5000 to try and
   load the page.
4. It's likely that will result in a connection reset error. This is correct, as
   no ports are being forwarded to the container - the Docker daemon has no idea
   where to route this traffic.
5. Press CTRL+C to kill the container, then run `docker run
   --name=webapp-container -p5000 webapp`.
6. Try browsing to http://localhost:5000 again - you should see a web page now.
7. Kill the container and start it again. Notice how the ID has changed.

## Docker compose
1. Make sure that any other containers are killed - run `docker ps -a` to list
   containers and `docker rm -f $CONTAINER_NAME` to remove them.
2. Run `docker-compose up -d --scale webapp=4`.
3. Browse to http://localhost and refresh. Nginx is load balancing your requests
   across four containers.
