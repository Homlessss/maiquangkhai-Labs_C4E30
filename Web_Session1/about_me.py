from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route('/about-me')
def index():
    return render_template('about-me.html')

@app.route('/school')
def Chuyenhuong():
    return redirect("http://techkids.vn ", code = 302)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port = 5000, debug=True)