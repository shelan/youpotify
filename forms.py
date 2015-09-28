from flask_wtf import Form
from wtforms import SubmitField, StringField
from wtforms.validators import DataRequired

class SendMsgForm(Form):
    name = StringField('Enter your Message', [DataRequired()])
    result = StringField('result', [DataRequired()])
    submit = SubmitField("Send")