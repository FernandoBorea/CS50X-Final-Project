from flask import Blueprint, render_template
from flask import current_app as app

# Set up blueprint
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@index_bp.route("/")
def index():
    return render_template('index.html')