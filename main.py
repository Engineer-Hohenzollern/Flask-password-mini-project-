from flask import (
    Flask,
    redirect,
    render_template,
    request,
    url_for
)

users = [(1, 'Name1', 'pass1'), (2, 'Name2', 'pass2'), (3, 'Name3', 'pas3')]
# users will be a list of DB table entries that would be extracted using cur.fetchall() and stored in users

app = Flask(__name__)
app.secret_key = 'Antz.Ai'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = [x for x in users if x[1] == username]
        if user[2] == password:
            return redirect(url_for('welcome'))

        return redirect(url_for('login'))

    return render_template('login.html')


@app.route('/welcome')
def profile():
    return render_template('welcome.html')
