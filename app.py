from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Required for Vercel
def handler(environ, start_response):
    return app(environ, start_response)
