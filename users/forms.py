from django.contrib.auth.models import User
from django import forms

class UserProfileForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=30,help_text=False)
    class Meta:
        model = User
        fields = ('first_name','last_name','username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_confirm_password(self):
        print "here"
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('confirm_password')

        if not cpassword:
            raise forms.ValidationError("You must confirm your password")
        if password != cpassword:
            raise forms.ValidationError("Your passwords do not match")
        return cpassword


