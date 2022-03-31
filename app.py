import os
from flask import Flask, request, render_template

# Flask does not know where the root folder for the project is
# so this must be used to see html templates
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'C:\\Users\\lunke\\OneDrive\\Documents\\Github\\WebBrowser\\templates')
app = Flask(__name__, template_folder=template_path)

@app.route('/')
def webbrowser():
    return render_template('index.html')

# @app.route('/', methods=['POST'])
# def my_form_post():
#     text = request.form['text']
#     processed_text = text.upper()
#     return processed_text

@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)

if __name__ == "__main__":
    app.run(debug=True)