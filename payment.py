from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)


class PaymentForm(FlaskForm):
    name = StringField("Name")
    submit = SubmitField('Submit')


@app.route('/payment', methods=['GET', 'POST'])
def payment():
    form = PaymentForm()

    if form.validate_on_submit():
        name = form.name.data


if __name__ == '__main__':
    app.run(debug=True)
