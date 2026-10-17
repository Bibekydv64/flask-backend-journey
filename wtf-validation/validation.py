from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,EmailField,SubmitField
from wtforms.validators import data_required,Email,length


class registation(FlaskForm):

    name = StringField('name', validators=[data_required()])
    email = StringField('email',validators=[data_required(),Email()])
    password = StringField('password',validators=[data_required(),length(min=4,max=20)])
    submit = SubmitField('register')




    

