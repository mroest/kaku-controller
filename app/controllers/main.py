from flask import Blueprint, render_template, request, redirect, url_for

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html', name='Kaku App')


@main.route('/error', methods=['GET'])
def error():
    return render_template('error.html', msg=request.args.get('msg'))


@main.route('/switch', methods=['POST'])
def switch():
    from app.kaku.switch import switch_off, switch_on

    op = request.form.get("operation", "Off")
    options = {
        'On': switch_on,
        'Off': switch_off
    }
    command = options.get(op, None)
    if command is not None:
        command(4, 1, 0)

    return redirect(url_for('.index'))
