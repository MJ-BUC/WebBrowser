import os
from flask import Flask, request, render_template
from googleapiclient.discovery import build
import pprint

# Flask does not know where the root folder for the project is
# so this must be used to see html templates
project_root = os.path.dirname(__file__)
template_path = os.path.join(project_root, 'C:\\Users\\lunke\\OneDrive\\Documents\\Github\\WebBrowser\\templates')
app = Flask(__name__, template_folder=template_path)

titleList = []
displayLinkList = []
snippetList = []
linkList = []

### Google custom search using google api ###
my_api_key = ""
my_cse_id = ""

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
### Google custom search using google api ###


@app.route('/')
def webbrowser():
    return render_template('index.html')

@app.route('/result', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /result is accessed directly. Try going to '/index' to submit form"
    if request.method == 'POST':
        form_data = request.form["search"] # uses the name attribute of the html input as the key because form data is saved as dict
        print(form_data)

        results = google_search(form_data, my_api_key, my_cse_id, num=10)
        for result in results:
            # pprint.pprint(result)
            titleList.append(result['title'])
            displayLinkList.append(result['displayLink'])
            snippetList.append(result['snippet'])
            linkList.append(result['link'])
            print('\n\n')
            pprint.pprint(result['title'])
            pprint.pprint(result['displayLink'])
            pprint.pprint(result['snippet'])
            pprint.pprint(result['link'])

            tListLen = 0

        for i in range(len(titleList)):
            tListLen = i
            

        return render_template('result.html', titleListNum=tListLen, formData=form_data, tList=titleList, dList=displayLinkList, sList=snippetList, lList=linkList)

if __name__ == "__main__":
    app.run(debug=True)