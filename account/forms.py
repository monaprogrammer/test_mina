from django import forms

messages = {
    'required': 'این فیلد اجباری است',
    'invalid':'لطفا یک ایمیل معتبر وارد کنید',
    'max-length':'تعداد کاراکتر ها بیشتر از حد مجاز است'
}



class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Username'}))
    password = forms.CharField(max_length=40, widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'}))

class UserRegistrationForm(forms.Form):
    username = forms.CharField(error_messages=messages,max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(error_messages=messages,max_length=50, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(error_messages=messages, max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
