from django import forms
from .models import PersonInLine


class PersonInLineForm(forms.ModelForm):
    """
    form for create PersonInLine
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['wish_year'].widget.attrs.update({'class': 'form-control'})
        self.fields['privilege'].widget.attrs.update({'class': 'form-control'})
        self.fields['group_age'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = PersonInLine
        exclude = ('is_approve', )
