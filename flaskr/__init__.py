#!/usr/bin/python3
import os

from flask import Flask

def create_app(test_config=True):
	# create and configure the app
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY = 'dev',
		DATABASE=os.path.join(app.instance_path, 'flask.sqlite')
	)
	if test_config is None:
		app.config.from_pyfile('config.py')
	else:
		# load the test config if passed in
		app.config.from_mapping(test_config)
	
	try:
		os.makedirs(app.instance_path)
	except OSError:
		pass

	def hello():
		return 'Hello, World!'
	
	return app
