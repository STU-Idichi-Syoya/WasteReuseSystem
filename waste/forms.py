from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from waste.model import User

class RegisterForm(FlaskForm):
  def validate_username(self, username_to_check):
    user = User.query.filter_by(username=username_to_check.data).first()
    if user:
      raise ValidationError('他の名前を試してください')

  def validate_email_address(self, email_address_to_check):
    email_address = User.query.filter_by(email_address=email_address_to_check.data).first()
    if email_address:
      raise ValidationError('他のメールを試してください')

  user_name = StringField(label='名前:', validators=[Length(min=2, max=30), DataRequired()])
  birthday = StringField(label='生年月日:', validators=[Length(max=8), DataRequired()])
  univercity_name = StringField(label='大学名:', validators=[Length(min=2, max=30), DataRequired()])
  email_address = StringField(label="メールアドレス:", validators=[Email(), DataRequired()])
  password1 = PasswordField(label="パスワード:", validators=[Length(min=6), DataRequired()])
  password2 = PasswordField(label="パスワード確認用:", validators=[EqualTo('password1'), DataRequired()])
  submit = SubmitField(label="アカウント作成")

class LoginForm(FlaskForm):
  user_name = StringField(label="名前:", validators=[DataRequired()])
  password = StringField(label="パスワード:", validators=[DataRequired()])
  submit = SubmitField(label="サインイン")

