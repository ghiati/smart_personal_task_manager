from flask import Flask, render_template, request, redirect, url_for, session, flash
from website.models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_secret_key'

users = {}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('tasks'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash("Username already exists")
        else:
            users[username] = User(username, password)
            session['username'] = username
            return redirect(url_for('tasks'))
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = users.get(username)
    if user and user.check_password(password):
        session['username'] = username
        return redirect(url_for('tasks'))
    flash("Invalid username or password")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/tasks')
def tasks():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    # In a real application, you'd fetch tasks from a database
    # For this example, we'll use a dummy list
    user_tasks = ['Complete project', 'Buy groceries', 'Exercise']
    
    return render_template('tasks.html', tasks=user_tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    task = request.form['task']
    # Here you would typically add the task to a database
    # For this example, we'll just flash a message
    flash(f'Task added: {task}')
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    app.run(debug=True)