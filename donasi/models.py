from django.db import models

class Donate(models.Model):
    email = models.CharField(max_length=255)
    name = models.TextField()
    amount = models.TextField()
    note = models.TextField()
    donateKey = models.TextField()
    
    # magic method
    def __str__(self):
        return "{}".format(self.donateKey)
