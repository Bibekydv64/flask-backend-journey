from flask import Flask,url_for,redirect,request,flash,render_template
import string


app = Flask(__name__)
app.secret_key = 'superkey'

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home', methods =['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if name in '':
            if len(name) > 5 and len(name) < 20:
                if email in '@' and email in string.digits:
                    if password in '':
                        if len(password) > 5 and len(password) < 20:
                            return render_template('sucess.html',name=name,email=email,password=password)
                        
                        flash('please fill chars:')
                        return render_template('index.html')

                flash('Space not require! pease remove space')
                return render_template('index.html')
        
            flash('@ and disit right require!')
            return render_template('index.html')
        
        flash('please fill chars:')
        return render_template('index.html')


app.run(debug=True)























































