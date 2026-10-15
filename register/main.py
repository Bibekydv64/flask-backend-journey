from flask import Flask,redirect,request,flash,render_template




app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
        if request.method == 'POST':
            pass

        flash('invalid! try again sir')
        return render_template('index.html') 
