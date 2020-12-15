<h1 align="center">
    Minor Project 1 (Chatbot API)
</h1>

<p align="center">

<img alt="Expo" src="https://img.shields.io/badge/Python-3.8.6-blue">

<img alt="Expo" src="https://img.shields.io/badge/Django-3.1.2-blue">

<img alt="GitHub" src="https://img.shields.io/github/license/Sanket-Valani/bvm-minor-project-1-chatbot-api?label=License">

</p>

This app is JSON api server for the chatbot in [android app](https://github.com/Sanket-Valani/bvm-minor-project-1-android-app/)

### Installation:

I don't know how exactly to copy a django project but just create a new django project and copy paste all the things from this repo to that folder and append these lines to settings.py
```
import os

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'resources/'),
)
```

### Running App:

Connect your phone and laptop/pc to a common wifi network and then run
```sh
$ python manage.py runserver 192.168.43.111:8000 
```
If your wifi broadcast ip is not 192.168.43.111 then check it and change it accordingly.
