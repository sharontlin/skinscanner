from flask import Flask, render_template, url_for, jsonify, request
import detector

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route("/")
def hello():
    return render_template("index.html")

@app.route('/diagnose', methods=['POST'])
def diagnose_image():
    data = request.get_json()
    if data["type"] == "webcam":
        response = detector.transform_webcam(data)
    elif data["type"] == "url":
        response = detector.transform_url(data)
    return jsonify(response)