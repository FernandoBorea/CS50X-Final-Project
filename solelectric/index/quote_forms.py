from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, Email


class ContactForm(FlaskForm):
    name = StringField(
        'Nombre',
        [DataRequired()]
    )
    
    email = StringField(
        'Correo electrónico',
        [
            Email(message=('Correo inválido.')),
            DataRequired()
        ]
    )

    body = TextAreaField(
        'Mensaje',
        [
            DataRequired(),
            Length(min=10,
            message=('El mensaje es demasiado corto.'))
        ]
    )

    # recaptcha = RecaptchaField() Will set later, need API keys
    submit = SubmitField('Enviar')


class TransformerQuote(ContactForm):
    primary = SelectField(
        'Primario',
        [DataRequired()],
        choices=['Opción 1', 'Opción 2', 'Opción 3']
    )

    secondary = SelectField(
        'Secundario',
        [DataRequired()],
        choices=['Opción 1', 'Opción 2', 'Opción 3']
    )

    special_requirements = TextAreaField(
        'Requisitos especiales',
        [
            Length(min=10,
            message=('EL mensaje es demasiado corto.'))
        ]
    )


class SpecialTransformerQuote(TransformerQuote):
    core_layout = SelectField(
        'Diseño del núcleo',
        [DataRequired()],
        choices=['Opción 1', 'Opción 2', 'Opción 3']
    )


class LabTestQuote(ContactForm):
    test = SelectField(
        'Prueba de laboratorio',
        [DataRequired()],
        choices=['Opción 1', 'Opción 2', 'Opción 3']
    )


class ServicesQuote(ContactForm):
    service = SelectField(
        'Servicio',
        [DataRequired()],
        choices=['Opción 1', 'Opción 2', 'Opción 3']
    )