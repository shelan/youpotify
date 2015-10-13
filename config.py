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


CONSUMER_KEY = 'c3WfzWemjUm2K0DCEsnheR8O0'
CONSUMER_SECRET = 'EI1Zl1SPpb8SrnNH4XqKfBX7dw4LjlmFydgm6SPNr6ILLI5SaT'
ACCESS_KEY = '1665548742-2L48xwqnH6Rsp1AMINZCpFAwNT64tMH0LebqQtX'
ACCESS_SECRET = 'ty5aU1BZqjIQaHO3HjvEpqTWZK0KabvhbJw444zHpppLk'