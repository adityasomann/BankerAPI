# BankerAPI

Rest-framework with JWT, Session handling and basic API call setup.  


1) Setting Up Virtual environment for python   
$ virtualenv -p python3 .env  
$ source .env/bin/activate  
$ pip install django  
$ deactivate  

2) Start a new django project  
$ django-admin.py startproject mysite  
$ ./manage.py migrate  
$ ./manage.py createsuperuser  
$ ./manage.py startapp myapp  

3) Run django with server  
$ ./manage.py runserver  

4) Django migration (Adding a new model and user requires data migration)  
$ ./manage.py makemigrations project_name  
$ ./manage.py migrate  

5) Install Project Dependencies  
pip install -r requirements.txt  



