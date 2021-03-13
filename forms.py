from django import forms
class unrform(forms.Form):
	emails =forms.EmailField(required=True,widget=forms.TextInput(attrs={"placeholder":"enter your mail"}))
	password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={"placeholder":"enter your password"}))