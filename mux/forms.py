from django import forms

from mux.models import Mix


class CreateSetForm(forms.ModelForm):
    class Meta:
        model = Mix
        fields = ("title", "recorded_at", "description")
