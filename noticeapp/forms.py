from django.forms import ModelForm, fields
from noticeapp.models import Notice


class NoticeCreationForm(ModelForm):
    class Meta:
        model = Notice
        fields = ["title", "content"]
