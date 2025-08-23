from django import forms


class UserForm(forms.Form):
    name = forms.CharField(label="Имя введите:",widget=forms.Textarea,initial="Undefind",min_length=2,max_length=20)
    age = forms.IntegerField(label="возраст",help_text="Введи возраст:",required=False,min_value=1,max_value=100)
    password = forms.CharField(label="пароль  введите:",widget=forms.Textarea,min_length=8,)

    required_css_class = 'field'
    error_css_class = 'error'
    email = forms.EmailField(label="почта",required=False)
    # date = forms.DateField(label="дата")
    # file = forms.FileField(label="файл", widget=forms.FileInput())