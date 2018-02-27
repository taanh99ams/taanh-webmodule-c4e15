from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
# @app.route("/hello")
# def hello():
#     return "hello c4e15"
#
# @app.route("/sayhi/<name>")
# def sayhi(name):
#     return "hi" + name

# @app.route("/sum/<num1>/<num2>")
# def sum(num1, num2):
#     result = str(int(num1) + int(num2))
#     return "The result is " + result

#Better way:
@app.route("/sum/<int:a>/<int:b>")
def sum(a, b):
    return "The result is " + str(a + b)

@app.route("/html")
def heading():
    return "<h1> I love Vietnam </h1>"

@app.route("/blog")
def blog():
    article_name = "Hit rewind"
    # post_1 = "Đã lỡ yêu em nhiều"
    # post_2 = "Mặt trời của em"
    # posts = [
    #     "We are young",
    #     "Girl on fire",
    #     "Made in the USA",
    #     "Burn"
    # ]
    posts = [
            {"content": "We are young",
            "author" : "Fun"
            },
            {"content": "Girl on fire",
            "author": "Alicia Keys"
            },
            {"content": "Made in the USA",
            "author": "Miley"
            }
            ]

    return render_template("blog.html", article_title=article_name,
                                        posts=posts,
                                        )

@app.route("/user/<username>")
def user(username):
    article_name = "User information"
    # if username == "trang":
    users = ["trang", "anh"]
    user_info = [
    {"name": "Trang",
    "age": "18",
    "sex": "female",
    "interest": "swimming"},
    {"name": "Ta Anh",
    "age": "19",
    "sex": "male",
    "interest": "music"}
    ]
# {username: "taanh", {"name": "Ta Anh",
# "age": "19",
# "sex": "male",
# "interest": "music"}},
    if username == "trang":
        return render_template("user.html", article_name=article_name,
                            user_info=user_info)
    elif username == "anh":
        return render_template("user.html", article_name=article_name,
                            user_info=user_info[1])
    else:
        return("No information")





if __name__ == '__main__':
  app.run(debug=True)
