from django import forms
from .models import Opcao

class VotoForm(forms.Form):
    def __init__(self, *args, **kwargs):
        enquete_id = kwargs.pop('enquete_id', None)
        super().__init__(*args, **kwargs)
        self.fields['opcao'] = forms.ChoiceField(
            choices=[(opcao.id, opcao.texto) for opcao in Opcao.objects.filter(enquete_id=enquete_id)],
            widget=forms.RadioSelect
        )