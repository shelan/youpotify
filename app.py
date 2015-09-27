# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
from twitter import *

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

config = {}
execfile("oauth.py", config)



@app.route('/send', methods=['GET', 'POST'])
def send():
    form = SendMsgForm(request.form)
    if request.method == 'POST':
        return sendMsgToClients(form.name._value())

    elif request.method == 'GET':
        return render_template('forms/send.html', form=form)


def sendMsgToClients(msg):
    twitter = Twitter(
        auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

    for i in range(1):
        results = twitter.statuses.update(status=msg)
        form = SendMsgForm(request.form)
    return render_template('forms/send.html', form=form)


if __name__ == "__main__":
    app.run()