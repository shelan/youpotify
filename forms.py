from flask_wtf import Form
from wtforms import TextField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo, Length

class SendMsgForm(Form):
    name = TextField('msg', [DataRequired()])
    submit = SubmitField("Send")