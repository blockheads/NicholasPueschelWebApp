from flask import *
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('home.html')

@app.route('/resume') #the url you'll send the user to when he wants the pdf
def pdfviewer():
    return redirect("/resume.pdf") #the pdf itself

# https://stackoverflow.com/questions/21714653/flask-css-not-updating
# for browser caching
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

