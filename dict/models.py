from django.db import models
from django.conf import settings


# Create your models here.
#email signup: date
class Contact(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True) #if registered user detected
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    # subject = models.CharField(max_length=120)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated  = models.DateTimeField(auto_now_add=False, auto_now=True)


    #unicode in py3
    def __str__(self):
        #return self.name or self.email
        return "Нам хтось написа(в)ла!"
