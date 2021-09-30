from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>This is the Home</h1>'

@app.route('/')
def about():
    return '<h1>This is About page</h1>'


if __name__ == '__main__':
    app.run(debug = True)