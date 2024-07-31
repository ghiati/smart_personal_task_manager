from flask import Flask, render_template, request, redirect, url_for, session, flash
from bson.objectid import ObjectId
import bcrypt
from website.database import get_users_collection, get_tasks_collection

app = Flask(__name__)
app.config['SECRET_KEY'] = 'My_secret_key'

# Get database collections
users_collection = get_users_collection()
tasks_collection = get_tasks_collection()

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
        
        existing_user = users_collection.find_one({'username': username})
        if existing_user:
            flash("Username already exists")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            users_collection.insert_one({'username': username, 'password': hashed_password})
            session['username'] = username
            return redirect(url_for('tasks'))
    return render_template('register.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    user = users_collection.find_one({'username': username})
    if user and bcrypt.checkpw(password.encode('utf-8'), user['password']):
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
    
    user_tasks = tasks_collection.find({'username': session['username']})
    return render_template('tasks.html', tasks=user_tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    if 'username' not in session:
        return redirect(url_for('home'))
    
    task = request.form['task']
    tasks_collection.insert_one({'username': session['username'], 'task': task})
    flash(f'Task added: {task}')
    return redirect(url_for('tasks'))

@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    if 'username' not in session:
        return redirect(url_for('home'))
    
    tasks_collection.delete_one({'_id': ObjectId(task_id), 'username': session['username']})
    flash('Task deleted')
    return redirect(url_for('tasks'))

if __name__ == '__main__':
    if users_collection and tasks_collection:
        app.run(debug=True)
    else:
        print("Error: Could not connect to the database. Application not started.")