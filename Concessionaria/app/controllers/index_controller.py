from flask import render_template, request

def home():
    return render_template('index.html', username=request.cookies.get('login'))