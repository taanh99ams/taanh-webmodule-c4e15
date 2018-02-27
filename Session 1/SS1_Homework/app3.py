from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def user(username):
    users = {
            "anh":  {
                    "name": "Ta Anh",
                    "age": 19
                    },
            "trang": {
                        "name": "Ha Trang",
                        "age": 20
                        }
            }
    if username in users:
        return render_template('username.html',
            name = users[username]["name"],
            age = users[username]["age"])
    else:
        return "Not_found"

if __name__ == '__main__':
  app.run(debug=True)
