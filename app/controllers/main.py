from flask import Blueprint, render_template, flash, request, redirect, url_for
from subprocess import call

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', name='Kaku App')


@main.route('/switch', methods=['POST'])
def switch():
    op = request.form.get("switch", "Off")
    options = {
        'On': '/usr/local/bin/lamp_aan',
        'Off': '/usr/local/bin/lamp_uit'
    }
    command = options.get(op, None)
    if command is not None:
        call([command])
    return redirect(url_for('main.index'))
