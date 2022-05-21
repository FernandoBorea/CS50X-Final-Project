from flask_wtf import FlaskForm
from wtforms import StringField, TextField, SubmitField
from wtform.validators import DateRequired, Length

class ContactForm(FlaskForm):
    name = StringField(
        'Nombre',
        [DataRequired()]
    )
    
    email = StringField(
        'Correo',
        [
            Email(message=('Correo inválido.')),
            DataRequired()
        ]
    )

    body = TextField(
        'Mensaje',
        {
            DataRequired(),
            Length(min=4,
            message=('El mensaje es demasiado corto.'))
        }
    )

    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')