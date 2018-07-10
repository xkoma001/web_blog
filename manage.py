#! /user/bin/env python

from flask_script import Manager, Server
from app import create_app

app = create_app('development')
manage = Manager(app)
manage.add_command('runserver', Server(host=app.config['HOST'], port=app.config['PORT']))

if __name__ == '__main__':
    manage.run()
