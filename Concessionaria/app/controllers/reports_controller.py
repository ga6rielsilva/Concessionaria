from flask import render_template, request

def reports():
    return render_template('reports.html', username=request.cookies.get('username'))