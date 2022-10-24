from flask import Blueprint, render_template, request
from functions import *

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')

@main_blueprint.route('/')
def index_page():
    return render_template('index.html')

@main_blueprint.route('/search')
def search_page():
    substr = request.args.get('s')
    posts = search_post(substr)
    return render_template('post_list.html', posts=posts, substr = substr)

