# RytenLabWebsite

This website is developed for Ryten group lab at UCL Institute of Neurology, University College London. 
The site contains the research led by the group, group members/profiles, publications, collaborators and other resources developed within the lab at UCL.
The website is running from a virtual environment.

#Specification
1. django 1.10.8 - 2.0.2
2. python 2.7 - 3
3. db.sqlite3
4. postgres
5. vs code
6. vim
7. pip3
8. ubuntu server 16.04 or latest version

# Installation of packages
1. remove db.sqlite3 (if you wish to use postgresql)
2. install postgresql
3. install py-dev
4. install a virtualenv
3. now istall Django version
6. install psycopg2 (use with postgres)

# Database
1. configure django database settings
2. migrate database
3. create super user

# Development process
1. make a directory
2. create a virtual environment
3. start new django project
4. Start the website development
5. create templates
6. static files and so on

# Migrate to host server
1. create profile in the server
2. copy the project directory to the profile created in the server
3. configure the allow_host in the setting to allow the server IP address
4. make sure all settings are well configured and the python is accessing the correct path
6. make sure you install all the necessary packages in the server
5. make sure your virtualenv has django installed in it

