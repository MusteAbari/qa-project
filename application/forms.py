from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, NumberRange

class CarForm(FlaskForm):
    reg = StringField('Car Number Plate', validators=[DataRequired()])
    make = StringField('Make of Car', validators=[DataRequired()])
    model = StringField('Model of Car', validators=[DataRequired()])
    mileage = StringField('Car Mileage', validators=[DataRequired()])
    colour = StringField('Car Colour', validators=[DataRequired()])
    age = IntegerField('Cars Age', validators=[NumberRange(min=2000, max=2021, message='Invalid length')])
    submit = SubmitField('Add Car')

class ReviewForm(FlaskForm):
    name = StringField('Name of Reviewer', validators=[DataRequired()])
    review = StringField('Your Car Review', validators=[DataRequired()])
    raiting = IntegerField('Raiting out of 10', validatorsvalidators=[NumberRange(min=1, max=10, message='Invalid length')])
    submit = SubmitField('Leave Review')

