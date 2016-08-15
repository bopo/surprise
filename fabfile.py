# -*- coding: utf-8 -*-

import os
import time

from fabric.api import cd, env, local, run, task
from fabric.context_managers import prefix
from fabric.contrib import django, project
from fabric.contrib.console import prompt

HERE = os.path.abspath(os.path.dirname(__file__))

django.settings_module('config.settings.local')

env.roledefs = {
    'slave': ['root@101.200.136.70'],
    'master': ['root@114.55.86.150'],
    'vagrant': ['vagrant@127.0.0.1'],
}

env.fixtures = (
    'flatpages',
    'restful.goodscategory',
    'restful.preselectioncategory',
    'restful.total',
    'restful.goods',
    'restful.collect',
    'restful.prompt',
    'restful.banner',
    'restful.holiday',
    'restful.queryrule',
    'consumer.customuser',
)

env.excludes = (
    "*.pyc", "*.db", ".DS_Store", ".coverage", ".git", ".hg", ".tox", ".idea/",
    'assets/', 'database/backups', 'database/fixtures/', 'runtime/','node_modules')

env.remote_dir = '/home/apps/surprise'
env.local_dir = '.'
env.database = 'surprise'


@task
def urls():
    local('python manage.py show_urls')


@task
def runs(script=None):
    local('python manage.py runscript %s' % script)


@task
def test(task=''):
    local('''DJANGO_SETTINGS_MODULE=config.settings.tests python manage.py test %s''' % task)


@task
def static():
    with prefix('workon surprise'), cd(env.remote_dir):
        run('python manage.py collectstatic --dry-run -c --noinput')


@task
def rsync(static=None):
    clean()

    static and static()

    local_dir = os.getcwd() + os.sep
    return project.rsync_project(remote_dir=env.remote_dir, local_dir=local_dir, exclude=env.excludes, delete=True)


@task
def push(static=None):
    rsync(static)


@task
def migrate():
    with prefix('workon surprise'), cd(env.remote_dir):
        run('''DJANGO_SETTINGS_MODULE='config.settings.prod' python manage.py migrate''')


@task(alias='rr')
def restart():
    with prefix('workon surprise'), cd(env.remote_dir):
        run('/usr/bin/supervisorctl restart surprise')


@task
def stop():
    run('/usr/bin/supervisorctl stop surprise')


@task
def ur(static=None):
    stop()
    rsync(static)
    restart()


@task
def um(static=None):
    rsync(static)
    migrate()


@task
def uu(static=None):
    rsync(static)
    migrate()
    restart()


@task
def reload():
    run('/root/python/bin/supervisorctl reload')
    run('/root/python/bin/supervisorctl restart all')


@task
def prod(port=8000):
    local('''MODE=prod gunicorn --worker-class=gevent config.wsgi:application -b 0.0.0.0:%s &''' % port)


@task
def build():
    local('''python -m compileall .''')


@task
def clean(migrate=None):
    clean_temp()
    clean_static()
    migrate and clean_migrate()


@task
def clean_temp(migrate=None):
    local('find . -name "*.sql" | xargs rm -rf')
    local('find . -name "*.pyc" | xargs rm -rf')
    local('find . -name "*.bak" | xargs rm -rf')
    local('find . -name "*.log" | xargs rm -rf')
    local('find . -name ".DS_Store" | xargs rm -rf')


@task
def clean_static(migrate=None):
    local('rm -rf assets/static/*')


@task
def clean_migrate():
    local('find . -name "migrations" | xargs rm -rf')


@task
def distclean():
    clean_temp()
    clean_static()
    clean_migrate()


@task
def mm():
    local('python manage.py makemigrations')
    local('python manage.py migrate')


@task
def pack(time=None):
    local('tar zcfv ./release.tgz '
          '--exclude=.git '
          '--exclude=.tox '
          '--exclude=.svn '
          '--exclude=.idea '
          '--exclude=*.tgz '
          '--exclude=*.pyc '
          '--exclude=.vagrant '
          '--exclude=tests '
          '--exclude=storage '
          '--exclude=database '
          '--exclude=.DS_Store '
          '--exclude=.phpintel '
          '--exclude=.template '
          '--exclude=db.sqlite3 '
          '--exclude=Vagrantfile .')


@task
def setup():
    local('python manage.py migrate --settings config.settings.prod')


@task
def dumpdata(remote=None):
    num = 1

    for fixture in env.fixtures:
        if not remote:
            local('python manage.py dumpdata {} > database/fixtures/00{}_{}.json'.format(fixture, num, fixture))
        else:
            with prefix('workon surprise'), cd(env.remote_dir):
                run('python manage.py dumpdata {} > database/fixtures/00{}_{}.json'.format(fixture, num, fixture))

        num += 1


@task
def loaddata(remote=None):
    num = 1

    for fixture in env.fixtures:
        if not remote:
            local('python manage.py loaddata database/fixtures/00{}_{}.json'.format(num, fixture))
        else:
            with (prefix('workon surprise'), cd(env.remote_dir)):
                run(
                    'DJANGO_SETTINGS_MODULE=config.settings.prod python manage.py loaddata database/fixtures/00{}_{}.json'.format(
                        num, fixture))

        num += 1


@task
def restdb():
    local('dropdb {database}'.format(database=env.database))
    local('createdb {database} -O {database} -E UTF8 -e'.format(database=env.database))
    local('python manage.py migrate --noinput')
    # local('python manage.py loaddata database/fixtures/*.json')
    loaddata()


@task
def deploy():
    question = '你确实要这么做？'
    prompt(question, default=True)


@task
def backdb():
    backdir = 'database/backups/%s' % time.strftime('%Y%m%d%H', time.localtime())

    if not os.path.isdir(backdir):
        os.makedirs(backdir)

    for num, fixture in enumerate(env.fixtures):
        local('python manage.py dumpdata {} > {}/00{}_{}.json'.format(fixture, backdir, num, fixture))


@task
def syncdb(action='down'):
    if action == 'up':
        remote = False
        upload = True
    else:
        remote = True
        upload = False

    if remote:
        dumpdata(remote=remote)

    project.rsync_project(
        remote_dir=env.remote_dir + '/database/fixtures',
        local_dir='./database',
        exclude=env.excludes,
        upload=upload)

    # if action == 'up':
    #     with prefix('workon surprise'), cd(env.remote_dir):
    #         run('python manage.py loaddata database/fixtures/*.json')
    # else:
    # restdb()

@task
def dbmigrate():
    # backup data
    run('manage.py dumpdata --format=json > db.json')

    # rsync files.
    local('rsync -ave ssh rsync -ave ssh root@101.200.136.70:/home/apps/surprise /home/apps')
    
    # stop service
    local('/usr/bin/supervisorctl stop surprise')

    # migrate db
    local('dropdb {database}'.format(database=env.database))
    local('createdb {database} -O {database} -E UTF8 -e'.format(database=env.database))
    
    local('python manage.py migrate --noinput')
    local('python manage.py loaddata db.json')

    # start service
    local('/usr/bin/supervisorctl start surprise')

@task
def req():
    with prefix('workon surprise'), cd(env.remote_dir):
        run('pip install -r requirements/prod.txt')


@task
def check():
    local('python manage.py check')


@task
def init():
    setup()
    loaddata()
