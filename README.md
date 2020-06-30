# Creating REST-API Through Django

Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.

## Installation

Use the virtual environment (anaconda) to install django.

```bash
conda create --name_env django=2.0
```
Created a directory (django_project) under which first django project is made

```python
django-admin startproject postmann # name of project
django-admin startapp api # name of application 1
django-admin startapp signup_page # name of application 2
```
Postgres Database setup for creating and storing user data
```python
pip install psycopg2-binary # command for installing postgres database
```

## Abstract

In this 'postmann' project, we made APIs for User Signin/signup in food Webpage. For this we created two applications, " signup_page " which is responsible for performing POST operations i.e. create and storing user input data in database. And " api " application responsible for performing GET operation i.e. Getting stored data from database for validating returning user signin. 

## Steps For User
-> Runserver click on url.   
-> Home page will open, click on 'login' in Navbar of this page.  
-> In login page, Create an Account on clicking signup button.  
-> Enter your Credentials as asked. Follow the password creating rules.  
-> After account creation Go back to login page and try to signin with 
   same credentials used for signup.



## Requirement.txt
certifi==2020.4.5.1  
chardet==3.0.4.  
Django==2.1.5.  
djangorestframework==3.11.0.  
idna==2.9.   
psycopg2-binary==2.8.5.  
pytz==2020.1.   
requests==2.24.0.  
urllib3==1.25.9

