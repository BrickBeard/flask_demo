from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return """
            <br>
            <h1>Hello OKC Python!</h1>
            <br>
            <p>Thank you for joining us today to talk about <strong>Flask</strong>!</p>
            <br>    
           """

if __name__ == "__main__":
    app.run()