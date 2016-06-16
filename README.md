# Docker Image w/ a Scalable Flask App Directory (+NGINX & uWSGI)

Attempting to provide a base for multi-file Flask micro-services, w/ a working server setup and easy dependency management in Docker.

Goals:
* Create a base for microservice Flask apps. The db portion is commented out assuming the app is an API-first app.
* Use Docker as alternative to virtualenv, with added benefit of easy deployment. Assuming that each microservice has it's own Docker instance that can be spun up/down without touching source on other services.
* Server tutorials tend to stop at the most basic one-page Flask app, but my apps usually get complex enough to need the app factory + blueprints Flask app.

Using tiangolo's uwsgi-nginx-flask-docker setup, with customization starting at the ini file.

## Instructions (Mac)
###### First-time:
1. [Install Docker Engine] (https://docs.docker.com/engine/installation/)
2. Create a default Docker virtual machine:
   ```
$ docker-machine create --driver virtualbox default
   ```
3. Clone repo, rename... Here we'll call it 'my_service'
   ```
$ cd /path/to/my_service
   ```

###### Normal procedure:
1. Start the virtual machine:
   ```
   $ docker-machine start default
   ```
   
2. Start the daemon, so you can use the 'docker' command inside the VM:
  ```
   $ eval $(docker-machine env default)
  ```
  * You'll need to redo this when opening new/extra terminal windows.
   
3. Build the image (or rebuild):

  * You'll need to do this the first time, AND any time you update the files.
   ```
   $ docker build -t folder_name_in_docker_dir/image_name .
   ```
   For example, I built an image named 'my_service_image' in a folder called 'my_services':
   ```
   $ docker build -t my_services/my_service_image .
   ```
   (Don't forget the period at the end!)
   
   This process will read the directions in the file named 'Dockerfile'
   
   It'll take a bit of time, and when it's finished, you can check for the image:
   ```
   $ docker images
   ```
   
4. Run the image:
   ```
   $ docker run --rm -p 80:80 my_services/my_service_image
   ```
   This starts a server running the flask app inside the container.
   
   
   Now, to check that the app is running:
5. Check the virtual machine's IP address:
   ```
   $ docker-machine ip default
   ```
   The output will be similar to: 192.168.99.100
   
6. Go to that address in your browser and you should see "Docker Flask app successfully Set Up"
  * This is what's returned in app/main/views.py index() function
  * 192.168.99.100/template returns a test of the template_test()
   
7. Ctrl + C shuts down the server, and removes the container.


###### Notes:
* To investigate the image without running the server:
  
  * Bash shell:
     ```
     $ docker run --rm -it my_services/my_service_image bash
     ```
     Then `$ ls`, `$ cd ..` etc to navigate around and investigate the Linux directories.
   
     `$ exit` to close the container
     
  * Python shell:
     ```
     $ docker run --rm -it my_services/my_service_image python
     ```
     `>>> exit()` to close.
     
* Install additional python modules you need:
  1. Edit requirements.txt. Remove my placeholder modules if they're not needed.
   
  2. In the Dockerfile, uncomment the relevant requirements.txt lines so the modules are installed at runtime.
   ```
   # ADD requirements.txt /tmp/requirements.txt

   # RUN pip install -r /tmp/requirements.txt
   ```
   * Remember you have to rebuild the image after changes (Step 3 above)
   
* Note that the images are pretty stripped down, you'll have to uncomment the vim line to install vim, and add other installs for needed software as needs advance.
   
* You can alter the port when running the server:
   ```
   $ docker run --rm -p 8000:80 my_services/my_service_image
   ```
  * now in your browser the site url can be accessed at that port: 192.168.99.100:8000 for example


## What's missing?
* Instructions for connecting to a db... At least a convenient export for db address.
* Actual deployment considerations
