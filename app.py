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

title = ""
dispLink = ""
snippet = ""
link = ""

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
            
        title = titleList[0]
        dispLink = displayLinkList[0]
        snippet = snippetList[0]
        link = linkList[0]

        title = str(title)
        dispLink = str(dispLink)
        snippet = str(snippet)
        link = str(link)


        title2 = titleList[1]
        dispLink2 = displayLinkList[1]
        snippet2 = snippetList[1]
        link2 = linkList[1]

        title2 = str(title2)
        dispLink2 = str(dispLink2)
        snippet2 = str(snippet2)
        link2 = str(link2)


        title3 = titleList[2]
        dispLink3 = displayLinkList[2]
        snippet3 = snippetList[2]
        link3 = linkList[2]

        title3 = str(title3)
        dispLink3 = str(dispLink3)
        snippet3 = str(snippet3)
        link3 = str(link3)


        title4 = titleList[3]
        dispLink4 = displayLinkList[3]
        snippet4 = snippetList[3]
        link4 = linkList[3]

        title4 = str(title4)
        dispLink4 = str(dispLink4)
        snippet4 = str(snippet4)
        link4 = str(link4)


        title5 = titleList[4]
        dispLink5 = displayLinkList[4]
        snippet5 = snippetList[4]
        link5 = linkList[4]

        title5 = str(title5)
        dispLink5 = str(dispLink5)
        snippet5 = str(snippet5)
        link5 = str(link5)


        title6 = titleList[5]
        dispLink6 = displayLinkList[5]
        snippet6 = snippetList[5]
        link6 = linkList[5]

        title6 = str(title6)
        dispLink6 = str(dispLink6)
        snippet6 = str(snippet6)
        link6 = str(link6)


        title7 = titleList[6]
        dispLink7 = displayLinkList[6]
        snippet7 = snippetList[6]
        link7 = linkList[6]

        title7 = str(title7)
        dispLink7 = str(dispLink7)
        snippet7 = str(snippet7)
        link7 = str(link7)


        title8 = titleList[7]
        dispLink8 = displayLinkList[7]
        snippet8 = snippetList[7]
        link8 = linkList[7]

        title8 = str(title8)
        dispLink8 = str(dispLink8)
        snippet8 = str(snippet8)
        link8 = str(link8)


        title9 = titleList[8]
        dispLink9 = displayLinkList[8]
        snippet9 = snippetList[8]
        link9 = linkList[8]

        title9 = str(title9)
        dispLink9 = str(dispLink9)
        snippet9 = str(snippet9)
        link9 = str(link9)


        title10 = titleList[9]
        dispLink10 = displayLinkList[9]
        snippet10 = snippetList[9]
        link10 = linkList[9]

        title10 = str(title10)
        dispLink10 = str(dispLink10)
        snippet10 = str(snippet10)
        link10 = str(link10)

        # print("\n\n\n\n"+snippet)  debugging purposes

        # titleListNum=tListLen, 
        return render_template('result.html', formData=form_data, title1=title,dispLink1=dispLink,snippet1=snippet, link1=link, 
        title2=title2, dispLink2=dispLink2, snippet2=snippet2, link2=link2, 
        title3=title3, dispLink3=dispLink3, snippet3=snippet3, link3=link3, 
        title4=title4, dispLink4=dispLink4, snippet4=snippet4, link4=link4, 
        title5=title5, dispLink5=dispLink5, snippet5=snippet5, link5=link5, 
        title6=title6, dispLink6=dispLink6, snippet6=snippet6, link6=link6, 
        title7=title7, dispLink7=dispLink7, snippet7=snippet7, link7=link7, 
        title8=title8, dispLink8=dispLink8, snippet8=snippet8, link8=link8, 
        title9=title9, dispLink9=dispLink9, snippet9=snippet9, link9=link9, 
        title10=title10, dispLink10=dispLink10, snippet10=snippet10, link10=link10, )

if __name__ == "__main__":
    app.run(debug=True)