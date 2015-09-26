#----------------------------------------------------------------------------#
# Imports
#----------------------------------------------------------------------------#

from flask import Flask, render_template, request
# from flask.ext.sqlalchemy import SQLAlchemy
import logging
from logging import Formatter, FileHandler
from forms import *
from twitter import *

#----------------------------------------------------------------------------#
# App Config.
#----------------------------------------------------------------------------#

app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
def home():
    return "hello"

@app.route('/sendMsg',methods=['GET', 'POST'])
def sendMsg():
    form = SendMsgForm(request.form)
    if request.method == 'POST':
        return sendMsgToClients(form.name._value())

    elif request.method == 'GET':
        return render_template('forms/sendMsg.html', form=form)


def sendMsgToClients(msg):
    CONSUMER_KEY = 'znwgG9GbkVHbu5xue5wFeS0N8'
    CONSUMER_SECRET = 'ogGSAYKjQ8UED7vPbqDryYQbjOXCRp73PYq3N14ASNZzovhgdp'
    ACCESS_KEY = '3769602317-zVv9DRo3rcMhgRJzk2ohCnW14aK92vOIFw4JNH2'
    ACCESS_SECRET = 'UBKw3SeippKb3qg3hWIiUSMiG3tqCkKfu8PTCW6Czlyl1'

    t = Twitter(
    auth=OAuth(ACCESS_KEY,ACCESS_SECRET,CONSUMER_KEY,CONSUMER_SECRET))

    for i in range(10):
        t.direct_messages.new(user="nithiniperera",text =msg +str(i))

    return "successfully sent the msg: " + msg

if __name__ == "__main__":
    app.run()