from flask import render_template, session, redirect, url_for
from . import main
# from .. import db
# from ..models import [Model]

@main.route('/', methods=['GET', 'POST'])
def index():
    return "<h1>Docker Flask app successfully set up</h1>"


@main.route('/template', methods=['GET', 'POST'])
def template_test():
    return render_template('main/index.html')