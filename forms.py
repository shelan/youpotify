from flask.ext.wtf.file import FileRequired, FileAllowed
from wtforms import validators
from flask_wtf import Form
from wtforms import SubmitField, StringField, FileField
from wtforms.validators import DataRequired

class SendMsgForm(Form):
    name = StringField('Enter your Twitter name  Eg: shelan', [DataRequired(),validators.Length(max=20)])
    result = StringField('result', [DataRequired()])
    submit = SubmitField("Send")

class UploadForm(Form):

    validators = [
        FileRequired(message='There was no file!')
    ]

    input_file = FileField('', validators=validators)
    submit = SubmitField(label="Upload")
