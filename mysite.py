from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request


import sqlite3 as sql

app = Flask(__name__)


@app.route("/welcome/")
def welcome():
    return render_template('welcome.html')

@app.route("/greetings/<greet>")
def greeting_message(greet):
    if greet == 'christmas':
        return "Merry Christmas"
    elif greet == 'newyear':
        return "Happy New Year"
    elif greet == 'thanksgiving':
        return "Happy Thanksgiving"
    else:
        return "{0}".format(greet)

# def create_database():
#     conn = sql.connect("users.db")
#     conn.execute("CREATE TABLE user_list (fname TEXT, lname TEXT, username TEXT, password TEXT)")
#     conn.close()

# create_database()

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/myform/')
def register():
	return render_template('register.html')

@app.route('/submit',methods = ['POST'] )
def submit():
    if request.method == 'POST':
        _fname = request.form["fname"]
        _lname = request.form["lname"]
        _uname = request.form["username"]
        _pass = request.form["password"]

        with sql.connect("users.db") as con:
            cur = con.cursor()
            cur.execute("INSERT INTO user_list (fname, lname, username, password) VALUES (?, ?, ?, ?)", [_fname, _lname, _uname, _pass])
        con.commit()
        return 'successfully added'

@app.route('/entries')
def entries():
    con = sql.connect("users.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM user_list")

    _rows = cur.fetchall()
    return render_template("mydblist.html", rows = _rows)


   

if __name__ =="__main__":
	app.run(debug=True)

