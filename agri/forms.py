from django import forms
from .models import Contact, Comment, RentalRegistraion
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Button, Fieldset

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your E-mail'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'message']


class RentalRegistraionForm(forms.ModelForm):
    CHOICES = ((0, 'Personal'), (1, 'Organisation'))
    class Meta:
        model = RentalRegistraion
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        my_field_text = [
            ('name', 'Full Name', ''),
            ('rental_type', 'Type', 'Who is renting?'),
            ('region', 'Region', ''),
            ('zone', 'Zone', ''),
            ('district', 'District', ''),
            ('kebele', 'Kebele', ''),
            ('phone_no_1', 'Phone number (1)', ''),
            ('phone_no_2', '(2)', 'Optional phone number'),
            ('email', 'Email', ''),
            ('floor', 'Floor', 'In which floor are you going to rent?'),
            ('business_type', 'What business are you planning to start?', '')
            ]


        for x in my_field_text:
            self.fields[x[0]].label=x[1]
            self.fields[x[0]].help_text=x[2]

        self.helper = FormHelper()
        self.helper.layout = Layout(
            Div(
                Div('name', css_class="col-sm-8"),
                Div('rental_type', css_class="col-sm-4"),
                css_class = 'row'
            ),

            Div(
                Div('region', css_class="col-sm-4"),
                Div('zone', css_class="col-sm-4"),
                Div('district', css_class="col-sm-4"),
                css_class = 'row'
            ),
            Div(
                Div('kebele', css_class='col-sm-6'),
                Div('email', css_class='col-sm-6'),
                css_class ='row'
            ),
            Div(
                Div('phone_no_1', 'mobile_number', css_class="col-sm-6"),
                Div('phone_no_2', 'mobile_number', css_class="col-sm-6"),
                css_class = 'row'
            ),

            Div('floor'),
            Div('business_type'),

        )





























