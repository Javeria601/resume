from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

@app.route('/')
def resume():
    with open('resume.json') as f:
        data = json.load(f)
    return render_template('resume.html', data=data)

@app.route('/api/resume')
def resume_api():
    with open('resume.json') as f:
        data = json.load(f)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
