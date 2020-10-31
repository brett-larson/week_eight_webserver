from flask import Flask, render_template, redirect, url_for
from forms import PaymentForm


app = Flask(__name__)

app.config['SECRET_KEY'] = 'myKey'

@app.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')

@app.route('/payment', methods=['GET','POST'])
def payment():

    form = PaymentForm()

    if form.validate_on_submit():
        name = form.name.data

        form.name.data = ''

        return redirect(url_for('thankyou'))

    return render_template('payment.html', form=form)

if __name__ == '__main__':
    app.run(ssl_context='adhoc', debug=True, port=5000)