from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'dr1nkfr0mthefla$k'

@app.route('/')
def displaycounter():
    if 'visit' not in session:
        session['visit'] = 0
    else:
        session['visit'] = session['visit'] + 1
    return render_template('form.html', visit = session['visit'])

@app.route('/add', methods = ['POST'])
def add():
    session['visit'] = session['visit'] + 1
    return redirect('/')

@app.route('/reset', methods = ['POST'])
def reset():
    session.clear()
    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')







if __name__=="__main__":
    app.run(debug=True)