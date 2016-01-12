from flask import Flask, render_template, jsonify, request
import json, os

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/coords", methods=['GET','POST'])
def helloname():

    x = json.loads(request.values.get("xarr", ""))
    y = json.loads(request.values.get("yarr", ""))
    # color = json.loads(request.values.get("colorarr", ""))
    # size = json.loads(request.values.get("sizearr", ""))

    currJsonText = open('data.json', 'r').read()
    currJsonData = json.loads(currJsonText)
    currJsonData['x'].extend(x)
    currJsonData['y'].extend(y)
    # currJsonData['color'].extend(color)
    # currJsonData['size'].extend(size)
    
    open('data.json', 'w').write(json.dumps(currJsonData))

    return jsonify(result=open('data.json', 'r').read())

@app.route("/clear", methods=['GET','POST'])
def clear():

    currJsonText = open('data.json', 'r').read()
    toSend = currJsonText
    currJsonData = json.loads(currJsonText)
    currJsonData['x'] = []
    currJsonData['y'] = []
    currJsonData['size'] = []
    currJsonData['color'] = []
    open('data.json', 'w').write(json.dumps(currJsonData))

    return jsonify(result=currJsonText)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 33507))
    app.run(host='0.0.0.0', port=port, debug=True)