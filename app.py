from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/shortenurl')
def shortenurl():
    return render_template('shortenurl.html')

