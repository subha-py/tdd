from fabric.api import run
from fabric.context_managers import settings


def _get_manage_dot_py(host):
    return '~/sites/{host}/virtualenv/bin/python ~/sites/{host}/source/manage.py'.format(host=host)


def reset_database(host):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string='elspeth@{host}'.format(host=host)):
        run('{manage_dot_py} flush --noinput'.format(manage_dot_py=manage_dot_py))


def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py(host)
    with settings(host_string='elspeth@{host}'.format(host=host)):
        session_key = run('{manage_dot_py} create_session {email}'.format(manage_dot_py=manage_dot_py, email=email))
        return session_key.strip()


        # this file deletes the database and make one user logged in staging server
