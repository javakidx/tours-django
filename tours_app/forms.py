from django import forms
from django.core import validators
from tours_app.models import User


def check_for_z(value):
    if not value or value[0].lower() != 'z':
        pass
        # raise forms.ValidationError("Name must start with 'z'")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter your email again")
    text = forms.CharField(widget=forms.Textarea)

    # bot_catcher = forms.CharField(required=False, widget=forms.HiddenInput,
    #                               validators=[validators.MaxLengthValidator(0)])

    # def clean_bot_catcher(self):  # with convention prefix clean_
    #     bot_catcher = self.cleaned_data['bot_catcher']
    #     if len(bot_catcher) > 0:
    #         raise forms.ValidationError("Gotcha BOT!")

    #     return bot_catcher

    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_email = all_clean_data['verify_email']

        if email != verify_email:
            raise forms.ValidationError("Email not matched")


class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
