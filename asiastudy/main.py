# -*- coding: utf-8 -*-
"""
    Main file for Kanjies analyzer application
"""

import os
from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from kanji_main import KanjiesText

# create our little application
app = Flask(__name__)

analyzed_text = 'Please enter your text and then press key.'
list_of_percents = []
list_of_find_kanjies = []

# pages routing

# home page
@app.route('/')
def home_view():
    return render_template('home.html')

#JLPT pages
@app.route('/jlpt')
def jlpt_view():
    return render_template('jlpt.html')


#Application
@app.route('/applications')
def applications_view():
    return render_template('applications.html')

#Application/kanji analyzer
@app.route('/applications/kanji_analyzer')
def show_entries():
    global analyzed_text
    global list_of_percents
    global list_of_find_kanjies
    return render_template('show_entries.html', analyzed_text=analyzed_text, list_of_percents=list_of_percents,
                           list_of_find_kanjies=list_of_find_kanjies)

@app.route('/applications/kanji_analyzer', methods=['POST'])
def add_entry():
    global analyzed_text
    global list_of_percents
    global list_of_find_kanjies

    analyzed_text = request.form['text']

    if len(analyzed_text) == 0:
        analyzed_text = 'Nothing to analyze. Please enter your text and then press key.'
    else:
        a = KanjiesText(analyzed_text)
        a.remove_spaces_from_text()
        list_of_percents = a.take_percent_count()
        list_of_find_kanjies = a.list_find_kanjies()
        for i in range(0,5):
            if len(list_of_find_kanjies[i]) == 0:
                list_of_find_kanjies[i] = ''
    return redirect(url_for('show_entries'))


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/png')


@app.errorhandler(404)
def page_not_found(e):
    render_template('404.html'), 404


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5001))
    app.run(host='0.0.0.0', port=port, debug = True)