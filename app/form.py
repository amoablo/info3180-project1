from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileAllowed, FileRequired 
from wtforms.validators import DataRequired

class PropertyForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    bedRoom_number = StringField('No. of Bed Rooms', validators=[DataRequired()])
    bathRoom_number = StringField('No. of Bath Rooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    property_type = SelectField('Property Type', choices=[('House','House'),('Apartment','Apartment')],validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    image = FileField('Image', validators=[
        FileRequired(),
        FileAllowed(['jpg','png','jpeg'], 'Images only')
    ])