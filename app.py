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
        return send_msg_to_clients(form.name._value())

    elif request.method == 'GET':
        return render_template('forms/send.html', form=form)


def send_msg_to_clients(msg):
    twitter = Twitter(
        auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

    file = open("/Users/ashansa/softwares/github/socialPlatform/accounts.txt", "r")
    i = 0
    for acc_id in file:
        status_msg = "@" + acc_id + " " + msg
        results = twitter.statuses.update(status=status_msg)
        i += 1
    # return "Message sent to " + str(i) + " users"
        form = SendMsgForm(request.form)
        form.result.data = ("<p>Message sent to " + str(i) + " users</p>")
    return render_template('forms/send.html', form=form)


if __name__ == "__main__":
    app.run()