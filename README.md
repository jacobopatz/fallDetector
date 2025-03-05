# CS578-Project

## Prjoect Setup
### 1. Install anaconda for environment management
Anaconda will help us maintain environment dependencies across machines and easily port our environment to the raspberry pi. To install anaconda, if you don't already have it, [click here](https://www.anaconda.com/download) to download it from the anaconda website.
### 2. Clone github repository on your local machine
You can find the repository here https://github.com/Jacob-Opatz/CS578-Project. Once you are granted access, you can clone the repository a few ways. I prefer to use [GitHub Desktop](https://github.com/apps/desktop) but you may also open your terminal, navigate to the directory you wish to store the project in, and enter: 
```sh
git clone https://github.com/Jacob-Opatz/CS578-Project.git
```
### 3. Create conda environment 
Now, we can create the anaconda environment. In the base directory, i've included a file called `fallAppEnvironment.yaml`. This file includes all current dependencies of our project. To create the environment, navigate to the project root directory and enter the following: 

```sh
conda env create -f fallAppEnvironment.yaml
conda activate fallAppEnv
```
The `conda activate fallAppEnv` activates our environment as your current environment. You may need to activate this again at some point if you switch environments regularly.

### 4. Run the server
Nagivate to the `falldetectionapp` directory. There is another directory of the same name nested inside this one. For some reason, this is the standard setup of a django project. For the purposes of this project, you should only have to navigate within the terminal to the outer directory with this name, that is the directory that holds the `manage.py` script. Terminal actions for the project are ran through this script. To run the server after navigation to`/falldetectionapp`, enter: 

```sh
python manage.py runserver
```

### 5. Open the server in your browser
The above command will display something along the lines of `Starting development server at http://0.0.0.0:8000/`. You can go to your browser and enter the link given to view the webpage. Changes to any of the django files will be reflected in the browser immedietly after reload, no need to restart the server. 

#### Viewing the webpage on another local device
I've set up the project website to automatically be accessible by any device on your local network . The only thing is that the link will be different for these devices. You must find your machines IP address and replace the `0.0.0.0` portion of it with your IP address. Mine looks something like `http://192.168.0.12:8000` To find this enter: If you're interested, this is because 0.0.0.0 tells the server to accept connections from all network interfaces, including over LAN. To access over LAN on another device, you must specify the hosts IP address for the connection to be established. 
#### On mac
```sh
ipconfig getifaddr en0
```
#### On PC
```sh
ipconfig
```
and look for your IPv4 Address under your active network adapter.

### 6. Running client script
I've included an example client script located in `/client program/` called `message.py`. To simulate a http request (aka a request between our rasberry pi device and our server), navigate to this directory and enter: 
```sh
python message.py
```
type exit at anytime to exit the client program. 

## Project Overview
### Repository File Structure
Upon entering our project directory, you will see two main sub-directories: `/client program` and `/falldetectionapp`

#### `/client program`
Houses the python scripts to be run on our client, aka the raspberry pi. The code in this directory should be able to be run to simulate our client interaction with the server. For development this may be done on the same machine until we are able to port it over to the pi. 
#### `/falldetectionapp`
Houses all of our server side code, aka our django project. This code can be run to run the server that our client can interact with. 
### Django Project File Structure
Within the main `/falldetectionapp` directory, you will see many sub-directories. Each of these is a django app, a modular section of our program that each has it's own functionality. Each app includes the following esential files:
1. views.py- The main python logic for this app. All logical operations such as manipulation of our data-base and data processing happens here. Essentially, its the "brains" of our program. For pages that display information to the user, the view will also render the website. 
2. urls.py- This file defines the urls for the app, and maps each one to a view. For example, entering `http://0.0.0.0:8000/login` in your browser will trigger the login view to activate. 
3. models.py- The file that defines our database. A model can be though of as a python data structure. For example, we have a model for users that includes first_name, last_name, user_id, etc. 
4. templates- This is where our .html files go for displaying pages to the user. You render then using the  `views.py` if necessary. 
5. static- This is where our .css and .js files will live.

## Description Of Django Apps
Our project includes several apps, each represented by a sub-directory in the `/falldetectionapp` directory. Heres a description of what each app does:
### 1. falldetectionapp
This app is the top level for all subsequent apps. It holds all the information for our project to run. It contains the crucial `settings.py` file that defines many important details for our project. All other apps are included in this project because `falldetectionapp` links them together. For example, each apps url's are imported to this app so that they are accessible from our server.

### 2. API
This app handles all incoming data from our rasberry pi. It can recieve the data, do some processing, and then route the data to the necessery app. 

### 3.dashBoard
This app runs the visual dashboard that we will display to users after they login. It include information such as patient status.

### 4.Users
This app handles user information and authentication. It has important models such as `User` and `Patient`. These models link to our database so we can access user information through them.

### 5. Alerts 
This app handles all alerts to family members and emergency services. It will determine who to alert and what to say upon recipt of a fall detection from the API app. 




## Essential Django Commands

Django is a framework that allows us to build our project using python code and libraries. Once in the Django project directory,`falldetectionapp`, there are a few commands that will be useful in our development.
### Create Super User
Once you begin development, you'll most likely want to add yourself as a super user in order to access all of the admin features, to do this, follow the prompts after entering: 
```sh 
python manage.py createsuperuser
```

### Enter Python Shell
You may wish to view or modify certain model entries, and you can do so using the provided python shell. To start the shell, enter:
```sh
python manage.py shell
```
For example, if you wanted to view all users, in the shell type:

```python
from Users.models import User
entries = User.objects.all()
print(entries)
```

### Start server
```sh
python manage.py runserver
```
### Collect static
This command collects the .css, and .js files found in each app into a single statics folder for easier references. If you make a change in one of these files and you dont immedietly see it reflected in the browser after refreshing, it may be helpful to run:

```sh
python manage.py collectstatic
```

### migrate
Our database is setup using the django models, which allow us to interact with a SQLite database as if it were composed of python objects. After making changes to these models.py files, it is essential to migrate our database (which makes our SQLite database match our python objects). To do this, efter making changes enter: 
```sh
python manage.py makemigrations
```

Then, we must apply the migrations using:
```sh
python manage.py migrate
```








