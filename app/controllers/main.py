from flask import Blueprint, render_template, flash, request, redirect, url_for
from subprocess import call

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html', name='Kaku App')


@main.route('/error', methods=['GET'])
def error():
    return render_template('error.html', msg=request.args.get('msg'))


@main.route('/switch', methods=['POST'])
def switch():
    op = request.form.get("operation", "Off")
    options = {
        'On': '/usr/local/bin/lamp_aan',
        'Off': '/usr/local/bin/lamp_uit'
    }
    command = options.get(op, None)
    if command is not None:
        try:
            call([command])
        except OSError as err:
            # Handle error
            return redirect(url_for('.error', msg=err.strerror))

    return redirect(url_for('.index'))
