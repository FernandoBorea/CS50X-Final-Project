from flask import Blueprint, render_template, url_for, redirect
from .quote_forms import ContactForm, LabTestQuote, ServicesQuote, TransformerQuote, SpecialTransformerQuote
from flask_mail import Message
from solelectric import mail
from os import environ


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
        msg = Message('Forma de contacto recibida', recipients=[environ.get('TARGET_MAIL')])
        msg.body = (f'Se ha recibido una solicitud de contacto de {form.name.data}\n\n'
                    f'Responder en la dirección de correo: {form.email.data}\n\n'
                    f'Mensaje:\n{form.body.data}')
        mail.send(msg)

    
    return redirect(url_for('.index'))


@index_bp.route('/standard_trans_quote', methods=['POST'])
def standard_trans_quote():
    form = TransformerQuote()

    if form.validate_on_submit():
        msg = Message('Solicitud de cotización: Transformador convencional', recipients=[environ.get('TARGET_MAIL')])
        msg.body = (f'Se ha recibido una solicitud de contacto de {form.name.data}\n\n'
                    f'Responder en la dirección de correo: {form.email.data}\n\n'
                    f'Primario: {form.primary.data}\n'
                    f'Secundario: {form.secondary.data}\n'
                    f'Requisitos especiales: {form.special_requirements.data}\n\n'
                    f'Mensaje:\n{form.body.data}')
        mail.send(msg)
    
    return redirect(url_for('.index'))


@index_bp.route('/padmounted_trans_quote', methods=['POST'])
def padmounted_trans_quote():
    form = SpecialTransformerQuote()

    if form.validate_on_submit():
        msg = Message('Solicitud de cotización: Transformador padmounted', recipients=[environ.get('TARGET_MAIL')])
        msg.body = (f'Se ha recibido una solicitud de contacto de {form.name.data}\n\n'
                    f'Responder en la dirección de correo: {form.email.data}\n\n'
                    f'Primario: {form.primary.data}\n'
                    f'Secundario: {form.secondary.data}\n'
                    f'Diseño del núcleo: {form.core_layout.data}\n'
                    f'Requisitos especiales: {form.special_requirements.data}\n\n'
                    f'Mensaje:\n{form.body.data}')
        mail.send(msg)
    
    return redirect(url_for('.index'))


@index_bp.route('/dry_trans_quote', methods=['POST'])
def dry_trans_quote():
    form = SpecialTransformerQuote()

    if form.validate_on_submit():
        msg = Message('Solicitud de cotización: Transformador seco', recipients=[environ.get('TARGET_MAIL')])
        msg.body = (f'Se ha recibido una solicitud de contacto de {form.name.data}\n\n'
                    f'Responder en la dirección de correo: {form.email.data}\n\n'
                    f'Primario: {form.primary.data}\n'
                    f'Secundario: {form.secondary.data}\n'
                    f'Diseño del núcleo: {form.core_layout.data}\n'
                    f'Requisitos especiales: {form.special_requirements.data}\n\n'
                    f'Mensaje:\n{form.body.data}')
        mail.send(msg)
    
    return redirect(url_for('.index'))


@index_bp.route('/lab_test_quote', methods=['POST'])
def lab_test_quote():
    form = LabTestQuote()

    if form.validate_on_submit():
        msg = Message('Solicitud de cotización: Prueba de laboratorio', recipients=[environ.get('TARGET_MAIL')])
        msg.body = (f'Se ha recibido una solicitud de contacto de {form.name.data}\n\n'
                    f'Responder en la dirección de correo: {form.email.data}\n\n'
                    f'Prueba de laboratorio solicitada: {form.test.data}\n\n'
                    f'Mensaje:\n{form.body.data}')
        mail.send(msg)

    return redirect(url_for('.index'))

@index_bp.route('/services_quote', methods=['POST'])
def services_quote():
    form = ServicesQuote()

    if form.validate_on_submit():
        msg = Message('Solicitud de cotización: Servicio', recipients=[environ.get('TARGET_MAIL')])
        msg.body = (f'Se ha recibido una solicitud de contacto de {form.name.data}\n\n'
                    f'Responder en la dirección de correo: {form.email.data}\n\n'
                    f'Servicio solicitado: {form.service.data}\n\n'
                    f'Mensaje:\n{form.body.data}')
        mail.send(msg)

    return redirect(url_for('.index'))