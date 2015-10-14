# ----------------------------------------------------------------------------#
# Imports
# ----------------------------------------------------------------------------#

from flask import Flask, render_template, request, flash, url_for
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from werkzeug.utils import secure_filename, redirect
from MusicBuilder import MusicBuilder
from forms import *
from twitter import *

# ----------------------------------------------------------------------------#
# App Config.
# ----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

music_albums = MusicBuilder(
    access_key=app.config.get('ACCESS_KEY'),
    access_secret=app.config.get('ACCESS_SECRET'),
    consumer_key=app.config.get('CONSUMER_KEY'),
    consumer_secret=app.config.get('CONSUMER_SECRET'))


@app.route('/')
def home():
    form = SendMsgForm(request.form)
    return render_template('forms/send.html', form=form)


@app.route('/send', methods=['GET', 'POST'])
def send():
    form = SendMsgForm(request.form)
    try:
        albums = music_albums.get_music(username=form.name.data)
        return render_template('forms/send.html', albums=albums, form=form, )

    except Exception, ex:
        flash(str("No user found ... Enter a valid Twitter handle"), "alert-danger")
        return render_template('forms/send.html', form=form, )


@app.errorhandler(500)
def internal_error(error):
    # db_session.rollback()
    return render_template('errors/500.html'), 500


@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)