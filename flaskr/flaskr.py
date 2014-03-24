# -*- coding: utf-8 -*-
"""
    Main file for Kanjies analyzer application
"""

import os
from flask import Flask, request, redirect, url_for, render_template
from kanji_main import KanjiesText

# create our little application
app = Flask(__name__)

analyzed_text = 'Please enter your text and then press key.'
list_of_percents = []

@app.route('/')
def show_entries():
    global analyzed_text
    global list_of_percents
    return render_template('show_entries.html', analyzed_text=analyzed_text, list_of_percents=list_of_percents)


@app.route('/add', methods=['POST'])
def add_entry():
    global analyzed_text
    global list_of_percents
    analyzed_text = request.form['text']
    a = KanjiesText(analyzed_text)
    a.remove_spaces_from_text()
    a.remove_kana_symbols()
    list_of_percents = a.take_percent_count()
    print(list_of_percents)
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)