# Django Celery Rabbitmq Radis

## Setup

First, let's install RabbitMQ on Ubuntu by running the following command :

```sh
$ sudo apt-get install rabbitmq-server
```

Now that we have RabbitMQ installed, we need to enable it and start the service:

```sh
$ sudo systemctl enable rabbitmq-server
$ sudo systemctl start rabbitmq-server
$ sudo systemctl status rabbitmq-server
```

Then thing to do is to clone the repository:

```sh
$ git clone https://github.com/sarwarsikder/django_celery_rabbitmq_radis.git
$ cd django_celery_rabbitmq_radis
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```

Note the `(env)` in front of the prompt. This indicates that this terminal session operates in a virtual environment set
up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:

To run the worker process we can use the celery worker command with the -A flag:

```sh
(env)$ celery -A mysite worker -l info
```

Run The application by django command

```sh
(env)$ cd project
(env)$ python manage.py migrate
(env)$ python manage.py runserver
```

And navigate to the browser `http://127.0.0.1:8000/`
Send mail using Celery Queue Jobs `http://127.0.0.1:8000/send-email/`


