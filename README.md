# Backend Challenge

Designing and implementing an API REST with Python (Flask) to the [Snowman Backend Challenge](https://github.com/snowmanlabs/backend-challenge). 

### Software Requirements 

Miniconda (Windows only)  
VirtualEnv  
PostgreSQL  
Postman  

### Packages Requirements
flask  
flask_restful  
flask_jwt  
flask-sqlalchem  
uwsgi (production only)  
psycopg2 (production only)  


### Config Local Environment

#### Windows

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)
2. Install [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md)   
3. Install [Postman](https://www.getpostman.com/downloads/)   
4. Open Anaconda Prompt (Miniconda3)  
5. Install VirtualEnv `conda install virtualenv`  
6. Create a VirtualEnv `virtualenv -p python3 vm_python_dev`  
7. Activate VirtualEnv by running `activate.bat` inside the path `~/vm_python_dev/Scripts`  
8. Install the required packages inside VirtualEnv Dev environment running the dev requirements into git repository `pip3 install -r requirements/dev.txt` 
9. Run the app `python app.py`


#### Mac

1. Install Python3 
2. Install [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md)   
3. Install [Postman](https://www.getpostman.com/downloads/)   
4. Install VirtualEnv `brew install virtualenv`  
5. Create a VirtualEnv `virtualenv -p python3 vm_python_dev`
6. Activate VirtualEnv by running `source activate` inside the path `~/vm_python_dev/bin` 
7. Install the required packages inside VirtualEnv Dev environment running the dev requirements into git repository `pip3 install -r requirements/dev.txt`  
8. Run the app: `python app.py`


### Deploy Environment

1.  Connect to Git and create a new repo   
1.1. Clone the project repo in your machine `git clone git@github.com:ClaudioSiervi/backend-challenge-snowman.git`  
1.2. Change the remote repo URL `git remote set-url origin [new Git repo URL]`  

2. Connect to [Heroku](heroku.com) and create a new app  
2.1. Select 'Heroku Postgres' in the Add-ons field (Resource tab)  
2.2. Select the plan name: Hobby Dev - Free  
2.3. Select 'Connect to GitHub' in the deployment method (Deploy tab)  
2.4. Search by the [new Git repo name]  
2.6. Connect to the [new Git repo]  
2.7. Select deploy branch  