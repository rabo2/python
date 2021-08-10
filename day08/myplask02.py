from flask import Flask
from flask.templating import render_template
from flask.globals import request

app = Flask(__name__)

@app.route("/dan")
def dan():
    a = request.args.get('dan','4')
    b = ["홍길동","전우치","강감찬"]
    return render_template("dan.html", a=a, b=b, int=int, enumerate=enumerate)



if __name__ == "__main__":
    app.run(debug=True)