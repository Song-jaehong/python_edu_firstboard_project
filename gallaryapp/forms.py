from django.forms import ModelForm, fields
from gallaryapp.models import Gallary


class GallaryCreationForm(ModelForm):
    class Meta:
        model = Gallary
        fields = ["title", "content"]
