from flask import Flask,render_template,request,url_for,flash


app = Flask(__name__)
app.secret_key = 'super-key'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/submit', methods = ['GET','POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        marks = request.form.get('marks')
        if name == str and int(marks) == int:
            if len(name) > 5 and marks > 100:
                if name == ' ' and marks > 0:
                    print("your name",name,"marks:",marks)
                    return render_template('student.html',name=name,marks=marks)
                flash('invalid! remove name space and marks put 0 se bada1')
                render_template('student.html')
            flash('invalid! remove name space and marks put 0 se bada2')
            return render_template('student.html')   
        flash('invalid! remove name space and marks put 0 se bada3')
        return render_template('student.html')


if __name__ == '__main__':
    app.run(debug=True)