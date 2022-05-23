from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
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
        {
            DataRequired(),
            Length(min=10,
            message=('El mensaje es demasiado corto.'))
        }
    )

    # recaptcha = RecaptchaField() Will set later, need API keys
    submit = SubmitField('Enviar')