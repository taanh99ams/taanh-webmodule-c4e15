from flask import Flask

app = Flask(__name__)

@app.route("/bmi2/<int:w>/<int:h>")
def bmi(w, h):
    bmi = w / ((h / 100) ** 2)
    if bmi < 16:
        return "Severely underweight"
    elif bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

if __name__ == '__main__':
  app.run(debug=True)
