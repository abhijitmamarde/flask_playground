from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("home.html")


@app.route('/invalid_user')
@app.route('/invalid_user/<username>')
def invalid_user(username=None):
    return render_template("invalid_user.html", username=username)


@app.route('/invalid_password')
def invalid_password():
    return render_template("invalid_password.html")


@app.route('/login', methods = ['POST'])
def on_login():
    print("on_login:")
    print(request.form)

    username = request.form['name']
    password = request.form['password']
    
    if username !='admin':
        return redirect(url_for('invalid_user', username=username))
    if password != 'secret':
        return redirect(url_for('invalid_password'))

    return redirect(url_for('dashboard'))


@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")

if __name__ == '__main__':
    app.run()
