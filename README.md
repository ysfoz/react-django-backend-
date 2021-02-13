# Django-React-Project-Backend

## Link-Heroku
<p>🔥<a href='https://blog-backend-ysf.herokuapp.com'>blog-backend-ysf.herokuapp.com<a/></p>




## Getting Started

Setup project environment with [virtualenv](https://virtualenv.pypa.io) and [pip](https://pip.pypa.io).

```bash
$ virtualenv project-env
$ source project-env/bin/activate
$ pip install -r https://github.com/ysfoz/react-django-backend-/blob/main/requirements.txt


$ cd projectname/
$ cp settings_custom.py.edit settings_custom.py
$ python manage.py migrate
$ python manage.py runserver
```

## Features

* Basic Django scaffolding (commands, templatetags, statics, media files, etc).
* Split settings in two files. `settings_custom.py` for specific environment settings (localhost, production, etc). `projectname/settings.py` for core settings.
* Simple logging setup ready for production envs.

## Contributing

I love contributions, so please feel free to fix bugs, improve things, provide documentation. Just send a pull request.