from django import forms
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

from .models import PasswordReset


User = get_user_model()



class AuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input-lg','placeholder': 'Usuário'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-lg','placeholder':'Senha'}))

class PasswordResetForm(forms.Form):

    email = forms.EmailField(label='Email')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            return email
        raise forms.ValidationError('Email não cadastrado.')

    def save(self):
        user = User.objects.get(email=self.cleaned_data['email'])
        key = generate_hash_key(user.username)
        reset = PasswordReset(key=key, user=user)
        reset.save()
        template_name = 'accounts/password_reset_mail.html'
        subject = 'Criar nova senha no Simple MOOC'
        context = {
            'reset': reset
        }
        send_mail_template(subject, template_name, context, [user.email])


class RegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={
        'placeholder':'Senha',
        'class':'form-control input-lg',
        'required':'required',}))
    password2 = forms.CharField(
        label='Confirmação de senha',
        widget=forms.PasswordInput(attrs={
        'placeholder':'Confirmação Senha',
        'class':'form-control input-lg',
        'required':'required',}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Confirmação de senha incorreta.')
        return password2

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'placeholder':'Usuário',
                'class':'form-control input-lg',
                'required':'required',
                
            }),
            'email': forms.TextInput(attrs={
                'placeholder':'E-mail',
                'class':'form-control input-lg',
                'required':'required',
                
            }),
        }


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'name']
