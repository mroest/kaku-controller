from flask import Blueprint, render_template, flash, request, redirect, url_for


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html', name='Kaku App')
