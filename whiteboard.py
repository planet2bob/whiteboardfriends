from flask import Flask, render_template, jsonify, request
import json

app = Flask(__name__)

def readJson(filename):
    jsonText = open(filename, 'r').read()
    return json.loads(jsonText)

def updateCoords(x, y):
    currDat = readJson('data.json')
    currDat.append((x,y))
    newJson = json.dumps(currDat)
    open('data.json', 'w').write(newJson)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/update", methods=['GET','POST'])
def updateData():
    x = request.values.get("x", "")
    y = request.values.get("y", "")
    updateCoords(x,y)
    return jsonify(result=readJson('data.json'))

@app.route("/get", methods=['GET','POST'])
def getData():
    return jsonify(result=readJson('data.json'))

if __name__ == "__main__":
    app.run(debug=True)