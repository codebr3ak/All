from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Corey James'
        'title': 'Blog post 1'
        'content': 'First post content'
        'date': 'April 20, 2020'
    }
    {
        'author': 'Ralp Bunche'
        'title': 'Blog post 2'
        'content': 'Second post content'
        'date': 'September 21, 2021'
    }
]

@app.route('/')
@app.route('/home')
def home():     
    return render_template('home.html' posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug = True)