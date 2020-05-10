from flask import Blueprint #clases
from flask import render_template #funciones

page = Blueprint('page', __name__)

@page.app_errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404

@page.route('/')
def index():
    return render_template('index.html', title='Nuevo titulo')