from django.db import models

# Create your models here.


class Free(models.Model):
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=False)
    create_at = models.DateField(auto_now_add=True)
