from django.db import models
#from django.urls import reverse

class UploadedFile(models.Model):
    file = models.FileField(upload_to='uploaded_files/')
    content = models.TextField(blank=True)