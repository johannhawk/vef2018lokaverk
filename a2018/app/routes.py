from app import app
from flask import Flask
from flask import render_template



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/tonlist')
def tonlist():
    return render_template('tonlist.html')

@app.route('/gallery1')
def gallery1():
    return render_template('gallery1.html')

@app.route('/gallery2')
def gallery2():
    return render_template('gallery2.html')

@app.route('/bloghub')
def bloghub():
    return render_template('bloghub.html')

@app.route('/post/<variable>')
def post(variable):
    return render_template("/post/"+variable+".html")