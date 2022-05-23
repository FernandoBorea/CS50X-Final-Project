from flask import Blueprint, render_template, url_for, redirect
from .quote_forms import ContactForm


# Set up blueprint
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)

@index_bp.route( '/')
def index():
    contact_form = ContactForm()

    return render_template('index.html',
    contact_form=contact_form)


@index_bp.route('/contact', methods=['POST'])
def contact():
    contact_form = ContactForm()
    
    if contact_form.validate_on_submit():
        print('Formulario recibido')
    
    return redirect(url_for('.index'))