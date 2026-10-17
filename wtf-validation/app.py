from flask import Flask,render_template,redirect,url_for
from validation import registation


app = Flask(__name__)
app.secret_key = 'superkey'

@app.route('/',methods=['GET', 'POST'])
def home():
    form = registation()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        submit = form.submit.data
        print('bibek',name,email,password)
        return redirect(url_for('sucess'))

    return render_template('index.html')


@app.route('/sucess')
def sucess():
    return render_template('sucess.html')

app.run(debug=True)
