from flask import Blueprint, render_template, url_for, redirect
from .quote_forms import ContactForm, LabTestQuote, ServicesQuote, TransformerQuote, SpecialTransformerQuote


# Set up blueprint
index_bp = Blueprint(
    'index_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@index_bp.route( '/')
def index():
    contact_form = ContactForm()
    trafo_convencional = TransformerQuote()
    trafo_padmounted = SpecialTransformerQuote()
    trafo_seco = SpecialTransformerQuote()
    prueba_lab = LabTestQuote()
    services = ServicesQuote()

    return render_template('index.html',
    contact_form=contact_form,
    convencional_form=trafo_convencional,
    padmounted_form=trafo_padmounted,
    seco_form=trafo_seco,
    lab_form=prueba_lab,
    service_form=services
    )


@index_bp.route('/contact', methods=['POST'])
def contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        print('Formulario recibido')
    
    return redirect(url_for('.index'))


@index_bp.route('/standard_trans_quote', methods=['POST'])
def standard_trans_quote():
    form = TransformerQuote()

    if form.validate_on_submit():
        print('Cotización transformador convencional recibida')
    
    return redirect(url_for('.index'))


@index_bp.route('/padmounted_trans_quote', methods=['POST'])
def padmounted_trans_quote():
    form = SpecialTransformerQuote()

    if form.validate_on_submit():
        print('Cotización transformador padmounted recibida')
    
    return redirect(url_for('.index'))


@index_bp.route('/dry_trans_quote', methods=['POST'])
def dry_trans_quote():
    form = SpecialTransformerQuote()

    if form.validate_on_submit():
        print('Cotización transformador seco recibida')
    
    return redirect(url_for('.index'))


@index_bp.route('/lab_test_quote')
def lab_test_quote():
    form = LabTestQuote()

    if form.validate_on_submit():
        print('Cotización prueba de laboratorio recibida')

    return redirect(url_for('.index'))