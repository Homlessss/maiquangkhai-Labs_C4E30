from flask import Flask, render_template
import jinja2
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    users = {
        'Huy':{
                'name': 'Ngo Quoc Huy',
                'age': 20,
                'gender': 'male',
                'work' : 'Student'
                },
        'Tien':{
                'name': 'Tran Minh Tien',
                'age': 22,
                'gender': 'male',
                'work' : 'Student'
                },
        'Huyen':{
                'name': 'Le Thi Huyen',
                'age': 20,
                'gender': 'female',
                'work' : 'Student'
                }
    }
    if username in users:
        return render_template('users.html', data = users[username])
    else:
        return 'User not found'

if __name__ == '__main__':
  app.run(host='127.0.0.1', port = 80, debug=True)