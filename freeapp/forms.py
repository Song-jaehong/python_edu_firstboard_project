from django.forms import ModelForm, fields
from freeapp.models import Free


class FreeCreationForm(ModelForm):
    class Meta:
        model = Free
        fields = ["title", "content"]
