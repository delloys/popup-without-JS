from app import app
from flask import render_template, request, session
import pandas as pd
@app.route('/', methods=['get', 'post'])
def index():
    html=render_template('index.html')
    
    return html
