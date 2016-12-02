import os

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Secret key for session management. You can generate random strings here:
# http://clsc.net/tools-old/random-string-generator.php
SECRET_KEY = 'M0094QU0Ge3YMjUWK4b2WA1037lcLRJ2J8s179NG'

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')


CONSUMER_KEY = '<add your key>'
CONSUMER_SECRET = '<add your secrect>'
ACCESS_KEY = '<add your key>'
ACCESS_SECRET = '<add your secrect>'
