from flask import Flask, render_template

app = Flask(__name__)

@app.route("/bmi/<int:w>/<int:h>")
def bmi(w, h):
    bmi = w / ((h / 100) ** 2)
    result = ""
    if bmi < 16:
        result = "Severely underweight"
    elif bmi < 18.5:
        result = "Underweight"
    elif bmi < 25:
        result = "Normal"
    elif bmi < 30:
        result = "Overweight"
    else:
        result = "Obese"
    return render_template('bmi.html', bmi = BMI, result = conclusion)

if __name__ == '__main__':
  app.run(debug=True)
