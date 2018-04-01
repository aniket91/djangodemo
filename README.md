# djangodemo - A simple django based Web App project

------
Project Information
------
1. This project expects Django 2.0, which supports Python 3.4 and later.

------
Dependencies
------
1. sudo apt-get install python3.6
2. sudo apt-get install python3-pip
3. pip3 install django-health-check

------
Deployment steps
------
1. python3 manage.py migrate
2. python3 manage.py createsuperuser
3. python3 manage.py runserver 

-----
Run migrations
----
1. python3 manage.py makemigrations testapp
2. python3 manage.py sqlmigrate testapp 0001
3. python3 manage.py check
4. python3 manage.py migrate

----
URLs
----
1. http://localhost:8000/admin/
2. http://localhost:8000/test/
3. http://localhost:8000/health_check/

------
Related Links
------
1. http://opensourceforgeeks.blogspot.in/2018/01/writing-your-first-django-app-part-1.html