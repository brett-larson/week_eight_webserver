from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import *

# Put this in its own "forms.py" file
class PaymentForm(FlaskForm):

    name = StringField("Name", validators=[DataRequired()])
    address = StringField("Address", validators=[DataRequired()])
    phone_number = StringField("Phone Number", validators=[DataRequired()])
    credit_card_number = StringField("Credit Card Number", validators=[DataRequired()])
    card_expiration_date = StringField("Expiration Date (MM/DD)", validators=[DataRequired()])
    submit = SubmitField("Submit")