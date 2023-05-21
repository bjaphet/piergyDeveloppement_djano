from django import forms

class LoginForm(forms.Form):
    username =forms.CharField(label='',max_length=15, required=True, widget = forms.TextInput (
        attrs={
            'placeholder':"Nom d'utilisateur",
            "class":'form-control'
            }
        )
        )
    pwd = forms.CharField(label='',required=True ,widget=forms.PasswordInput  (
        attrs={
            'placeholder':"Mot de passe",
            "class":'form-control'
            }
        )
        )
    # max_length=15, required=False 
