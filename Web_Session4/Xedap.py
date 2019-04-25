from flask import Flask, render_template, request, redirect, url_for
from db1 import get_all, add_xedap
app = Flask(__name__)
app.secret_key = 'homlessss2308'

@app.route('/new',methods = ['POST'])
def post_xedaps():
  Model = request.form.get('model')
  Daily_fee = request.form.get('daily_fee')
  Image_url = request.form.get('image_url')
  Year = request.form.get('year')
  add_xedap(Model, Daily_fee, Image_url, Year)
  print(get_all())
  return render_template('xedap.html')
  
@app.route('/new')
def get_xedaps():
  return render_template('xedap.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=80, debug=True)
 