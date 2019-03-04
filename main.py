# The main.py is the server that routes the user to the homepage and to the result page.
# The weather.py file creates a function with API that retrieves the weather data based on the city selected.
# The function populates the resulting page.

from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api

app = Flask(__name__)

@app.route('/')
def index():
    data = [{'name':'Singapore'}]
    return render_template('weather.html', data=data)

@app.route("/result", methods = ['GET','POST'])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
        data.append(resp)
    if len(data) != 2:
        error = 'Bad response weather app'
    return render_template('result.html',data=data,error=error)

if __name__ == '__main__':
    app.run(debug=True)