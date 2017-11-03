from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return """
    <h1>Hello world</h1>
    <form action="/login" method="POST">
    
    <p>Enter a name:<p>
    <p><input type="text" name="name"></p>

    <hr>

    <p>Enter a password:<p>
    <p><input type="password" name="password"></p>

    <p><input type="submit" name="Login"></p>

    </form>
    """


@app.route('/invalid_user/<username>')
def invalid_user(username=None):
    if username is None:
        return """
        <h1>INVALID USER!!!</h1>
        <hr>
        <p><a href="/">Go to HOME</a></p>
        """
    else:
        return """
        <h1>INVALID USER: %s</h1>

        <hr>
        <p><a href="/">Go to HOME</a></p>
        """ % (username)

@app.route('/invalid_password')
def invalid_password():
    return """
    <h1>INVALID PASSWORD!!!</h1>
    <hr>
    <p><a href="/">Go to HOME</a></p>
    """

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
    return """
    <h1>Welcome to ADMIN Dashboard!!!</h1>
    """

if __name__ == '__main__':
    app.run()
