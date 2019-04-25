from flask import Flask, render_template, request
app = Flask(__name__)

users = [
        {
            'username': 'Huybui0795@gmail.com',
            'password' : 'Huybui0795'
        },
        {
            'username': 'Tientran4404@gmail.com',
            'password' : 'Tientran4404'
        },
        {
            'username': 'Huyenle1612@gmail.com',
            'password' : 'Huyenle1612'
        }
]

@app.route('/',methods = ["POST"])
def get_login():

    login = {
        'username': request.form.get('User_name'), 
        'password': request.form.get('Pass_word')
    }

    if login in users:
        return 'Login Sussesful'
    else:
        return 'Login Failed!'

@app.route('/')
def get_user():  
    return render_template('login.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port = 80, debug=True)