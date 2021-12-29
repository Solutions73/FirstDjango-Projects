from django.db import models

# makemigration -> create changes and store in a file
# migrate -> apply the pending changes created by migrations

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=12)
    desc= models.TextField(max_length=600)
    date= models.DateField()

    def __str__(self):
        return self.name
