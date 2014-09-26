from django.contrib.auth.models import User
from users.models import UserProfile
from django import forms
from localflavor.in_.forms import INPhoneNumberField, INZipCodeField
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit

class UserProfileForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(max_length=30,help_text = False)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        cpassword = self.cleaned_data.get('confirm_password')

        if not cpassword:
            raise forms.ValidationError("You must confirm your password")
        if password != cpassword:
            raise forms.ValidationError("Your passwords do not match")
        return cpassword


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        exclude = ('password','confirm_password')
        labels = {
            'avatar': _('Upload Profile picture'),
            'plot_num': _('Plot Num/House No'),
            'street': _('Street/Apartment')
        }
        widgets = {
            'contact_no': INPhoneNumberField(),
            'zipcode': INZipCodeField()
        }

        def __init__(self):
            self.helper = FormHelper()
            self.helper.layout = Layout(
                Fieldset(
                    'Personal details',
                    'first_name',
                    'last_name',
                    'username',
                    'email'
                ),
                Fieldset(
                    'Address',
                    'plot_no',
                    'street',
                    'city',
                    'state',
                    'zipcode'
                )
                )
            super(EditProfileForm, self).__init__()