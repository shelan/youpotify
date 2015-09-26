from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField, StringField
from wtforms.validators import DataRequired, EqualTo, Length

class SendMsgForm(Form):
    name = StringField('msg', [DataRequired()])
    submit = SubmitField("Send")