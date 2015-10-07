# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask, render_template, request, flash, url_for
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from werkzeug.utils import secure_filename, redirect
from forms import *
from twitter import *

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

config = {}
execfile("oauth.py", config)


@app.route('/')
def home():
    form = SendMsgForm(request.form)
    return render_template('forms/send.html', form=form)


@app.route('/send', methods=['GET', 'POST'])
def send():
    form = SendMsgForm(request.form)
    if request.method == 'POST':
        return send_msg_to_clients(form.name._value())

    elif request.method == 'GET':
        return render_template('forms/send.html', form=form)


@app.route('/configure', methods=('GET', 'POST'))
def configure():
    form = UploadForm()
    if request.method == 'POST':
        input_file = request.files['accounts']
        content = input_file.read();
        file = open("uploaded_accounts.txt", "w")
        file.write(content)
        flash("users uploaded",'alert-success')
        return redirect(url_for('send'))
        # Do stuff
    else:
        return render_template('forms/user.html', form=form)


def send_msg_to_clients(msg):
    try:
        twitter = Twitter(
            auth=OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

        # file = open("/Users/ashansa/softwares/github/socialPlatform/accounts.txt", "r")
        file = open("uploaded_accounts.txt", "r")
        ids = file.readlines();

        i = 0
        form = SendMsgForm(request.form)
        for acc_id in ids:
            status_msg = "@" + acc_id + " " + msg
            results = twitter.statuses.update(status=status_msg)
            i += 1
        # return "Message sent to " + str(i) + " users"
        # form.result.data = ("<p>Message sent to " + str(i) + " users</p>")
        flash("Message sent to " + str(i) + " users", "alert-info")
    except Exception, e:
        flash(str(e), "alert-danger")

    return render_template('forms/send.html', form=form)


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000)