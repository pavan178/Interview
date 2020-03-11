from django.db import models

#adding the created models

class Snippet(models.Model):
    name = models.CharField(max_length=20) #saving name
    Phone = models.IntegerField(max_length=10) #saving phone number
    Email = models.EmailField() #saving email address

    def __str__(self):
        return self.name
