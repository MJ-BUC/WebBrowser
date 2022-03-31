# from flask import Flask,render_template,request
 
# app = Flask(__name__)
 
# @app.route('/form')
# def form():
#     return render_template('form.html')
 
# @app.route('/data/', methods = ['POST', 'GET'])
# def data():
#     if request.method == 'GET':
#         return f"The URL /data is accessed directly. Try going to '/form' to submit form"
#     if request.method == 'POST':
#         form_data = request.form
#         return render_template('data.html',form_data = form_data)
 
 
# app.run(host='localhost', port=5000)

from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def form():
    return render_template("form.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run(debug=True)

