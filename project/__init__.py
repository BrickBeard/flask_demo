from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users')
def users():
    return render_template('index.html')

@app.route('/api')
def contact():
    return render_template('index.html')