# Backend Challenge - Snowman

#### Intro
Designing and implementing an API REST with Python.  
Clone the Git repo:  
`git clone git@github.com:ClaudioSiervi/backend-challenge-snowman.git`
 

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


### Config Dev Environment

#### Windows

1. Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)   
2. Install [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md)   
3. Install [Postman](https://www.getpostman.com/downloads/)   
4. Open Anaconda Prompt (Miniconda3)  
5. Install VirtualEnv `conda install virtualenv`  
6. Create a VirtualEnv `virtualenv vm_python_dev`  
7. Run the VirtualEnv created `~/vm_python_dev/Scripts/activate.bat`  
8. Install the required packages inside VirtualEnv Dev environment:`pip3 install -r requirements/dev.txt` 
9. Run the app: `python app.py`
10. If want shutdown the VirtualEnv server: `deactivate`


#### Mac/Linux

1. Install [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md)   
2. Install [Postman](https://www.getpostman.com/downloads/)   
3. Install VirtualEnv `apt-get install virtualenv`  
4. Open Anaconda Prompt (Miniconda3)  
5. Create a VirtualEnv `virtualenv vm_python_dev`  
6. Run the VirtualEnv  `source ~/vm_python/Scripts/activate`  
7. Install the required packages inside VirtualEnv Dev environment:`pip3 install -r requirements/dev.txt`  
8. Run the app: `python app.py`
9. If want shutdown the VirtualEnv server: `deactivate`  