from flask import Flask
from flask.globals import request
app = Flask(__name__)

@app.route("/")
def hello():
    return "Minseok!"

@app.route("/para", methods=['POST'])
def para():
    # a = request.args.get('a', '하하하')
    a = request.form['a']
    return "hello!"+a


@app.route("/dan")
def dan():
    a = request.args.get('dan','2')
    code = ""
    for i in range(1,10):
        code += "{} * {} = {}\n".format(a, i, int(a)*i)
    return code

if __name__ == "__main__":
    app.run(debug=True)