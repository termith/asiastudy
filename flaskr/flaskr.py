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

@app.route('/')
def show_entries():
    global analyzed_text
    global list_of_percents
    global list_of_find_kanjies
    return render_template('show_entries.html', analyzed_text=analyzed_text, list_of_percents=list_of_percents, list_of_find_kanjies=list_of_find_kanjies)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'favicon.ico', mimetype='image/png')

@app.route('/add', methods=['POST'])
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
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug = True)