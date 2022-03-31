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

import os
from flask import Flask, redirect, request, url_for, render_template

# Flask does not know where the root folder for the project is
# so this must be used to see html templates
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'C:\\Users\\lunke\\OneDrive\\Documents\\Github\\WebBrowser\\testing')
app = Flask(__name__, template_folder=template_path)

@app.route("/")
def home():
    return render_template("index.html")


# @app.route("/login", methods=["POST", "GET"])
# def login():
#     if request.method == "POST":
#         user = request.form["nm"]
#         return redirect(url_for("user", usr=user))
#     else:
#         return render_template("login.html")

# @app.route("/<usr>")
# def user(usr):
#     return f"<h1>{usr}</h1>"


if __name__ == "__main__":
    app.run()

