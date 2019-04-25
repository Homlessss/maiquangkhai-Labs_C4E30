from flask import Flask, render_template
app = Flask(__name__)

#C1:
@app.route('/bmi/<weight>/<height>')
def BMI(weight,height):
    Data_Body = {
        'weight': float(weight),
        'height': float(height),
        'BMI': float(weight)/((float(height)/100)**2)
    }
    return render_template('BMI.html', data = Data_Body)

#C2
# @app.route('/bmi/<weight>/<height>')
# def BMI(weight,height):
#     BMI = float(weight)/((float(height)/100)**2)
#     if BMI < 16:
#         return 'Severely underweight'
#     elif BMI < 18.5:
#         return 'Underweight'
#     elif BMI < 25:
#         return 'Normal'
#     elif BMI < 30:
#         return 'Overweight'
#     else:
#         return 'Obese'

    
if __name__ == '__main__':
  app.run(host='127.0.0.1', port = 80, debug=True)
    