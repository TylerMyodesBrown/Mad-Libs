from ast import Num
from random import randint, choice, sample
import re
from flask import Flask, request, render_template
# from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
# app.config['SECRET_KEY'] = 'WhatATime'
# debug = DebugToolbarExtension(app)

from stories import Story

Associat = {'place': 'cedar',
"noun": 'it',
 "verb": 'ran',
 "adjective": 'fuzzy',
 "plural_noun": 'thems'}


story = Story( ['place', 'noun', 'verb,', 'adjective', 'plural_noun'], 
"""Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb}.""")


story2 = Story( ['place', 'noun', 'verb,', 'adjective', 'plural_noun'], 
"""Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb}.""")

story3 = Story( ['place', 'noun', 'verb,', 'adjective', 'plural_noun'], 
"""Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb}.""")

story4 = Story( ['place', 'noun', 'verb,', 'adjective', 'plural_noun'], 
"""Once upon a time in a long-ago {place}, there lived a large {adjective} {noun}. It loved to {verb}.""")


@app.route('/')
def show_start():
    return render_template('form.html')

@app.route('/story')
def show_story():
    place = request.args['place']
    adjective = request.args['adjective']
    noun = request.args['noun']
    verb = request.args['verb']
    fin_arr = {'place':place,'adjective':adjective,'noun':noun,'verb':verb}
    thing = request.args['story-choice']
    if thing == 'story':
        return story.generate(fin_arr)
    elif thing == 'Better_story':
        return  story2.generate(fin_arr)
    elif thing == 'Nice_Story':
        return story3.generate(fin_arr)
    elif thing == 'Great_Story':
        return story4.generate(fin_arr)
    else:
        return f'<h1>Failed to enter 1 of the above options. Please go back and try again!</h1>'
