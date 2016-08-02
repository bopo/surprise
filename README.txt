python manage.py celery beat --loglevel=info
python manage.py celery worker --loglevel=info

deactivate
rmvirtualenv TAE
mkvirtualenv TAE
pip install -r requirements.txt
pip install gunicorn
gunicorn index:application


roles = {
	'type': 'rex',
	'rule': 'var pageData = .*?;',
	'path': '$.0.actionRule.0.url',
	'domain': 'http://share.laiwang.com/s/FYfXr?tm=f6aa84',
}