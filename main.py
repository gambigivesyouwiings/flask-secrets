from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap4
from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, InputRequired


class MyForm(FlaskForm):
    #name = StringField(label='name', validators=[DataRequired(), InputRequired(), Length(min=8)])
    email = EmailField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label='Submit')


app = Flask(__name__)
app.secret_key = "secret"
bootstrap = Bootstrap4(app)


@app.route("/")
def home():
    return render_template('index.html', bootstrap=bootstrap)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        print(form.email.data)
        if form.email.data == "admin@email.com" and form.password.data == "12345678":
            return render_template('success.html')
        else:
            return render_template('denied.html')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
