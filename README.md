# OPC_Project09

This project's aim is to develop a web app' using the Django framework.


# Introduction

This project is composed of:
* A registration + login page
* A user than can : 
    * create object and modify items using forms and model.forms
    * delete an object
    * follow other users
    * complete other users objects


# Requirements

* Python3 at https://www.python.org/downloads
* Pipenv, if not already pre-installed with the python distribution
* ... and that's it !


# Installation

## 1. Acquire the codebase
Using the git console, the git app or straight from the source ! 

### With Git console
Navigate to desired location and use:
```
git clone https://github.com/Dhyakia/OPC_Project09.git
```

### With Git Desktop
With the desktop app, simply click on the "Code" (green button) at the top of this page and then "Open with GitHub Desktop".

Clone the file to desired location and you're done !

### With manual download
Click on the "Code" (green button) at the top of this page and then "Download Zip"

Un-zip the file into the desired location and you're done !

## 2. Setting up a virtual environnement
For a better user experience, it is recommanded to use a virtual environnement.

1. With the console, navigate to the folder of installation.

2. Next, to create the environnement, enter this command:
    
    Windows: ```python venv -m venv ```

    MacOs/Linux: ```python -m venv venv ```

3. Now, all that's left if to activate it:

    Windows: ```venv/scripts/activate```

    MacOs/Linux: ```venv/bin/activate```

If everything is done correctly, you should now see the "venv" tag at the start of the line of the console.

## 3. Install the dependencies

Using the console, navigate to the project folder and enter:
```
pip install -r requirements.txt
```

# Usage

## Starting the server
Activate the virtual environnement.


Using the console, navigate inside the LITReview folder, and enter:

```
python manage.py runserver
```

## Browsing the content
You can now navigate the page, just like a website, but only localy !

The starting url is the login page, at : http://127.0.0.1:8000/login/

# Futur viewing

This is the ninth out of thirteen python project with OpenClassRoom