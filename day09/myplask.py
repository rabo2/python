from flask import Flask
from flask.templating import render_template
from day09.dao_emp import DaoEmp
from flask.globals import request
from flask.json import jsonify


app = Flask(__name__,static_url_path='',static_folder='static')

de = DaoEmp()

@app.route("/")
def hello():
    return "Minseok!"

@app.route("/emp")
def emp():
    emps = de.select()
    return render_template("emp.html", emps=emps)


@app.route("/insert", methods=['POST'])
def add():
    data = request.get_json()
    cnt = de.insert(data['e_id'], data['name'], data['tel'])
    result = "ng"
    if cnt == 1 : 
        result = "ok"
    return jsonify(result=result)


@app.route("/update", methods=['POST'])
def update():
    data = request.get_json()
    cnt = de.update(data['e_id'], data['name'], data['tel'])
    result = "ng"
    if cnt == 1 : 
        result = "ok"
    return jsonify(result=result)
    

@app.route("/delete", methods=['POST'])
def delete():
    data = request.get_json()
    cnt = de.delete(data['e_id'])
    result = "ng"
    if cnt == 1 : 
        result = "ok"
    return jsonify(result=result)
    
    
    
if __name__ == "__main__":
    app.run(debug=True)
