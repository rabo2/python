from flask import Flask
from flask.templating import render_template
from flask.globals import request

app = Flask(__name__)

@app.route("/home")
def home():
    vos = [
        {"e_id" : 1, "name" : "홍길동", "tel":"01022223333"},
        {"e_id" : 2, "name" : "전우치", "tel":"01033334444"}
        ]
    return render_template("vos.html", vos=vos, enumerate=enumerate)



if __name__ == "__main__":
    app.run(debug=True)