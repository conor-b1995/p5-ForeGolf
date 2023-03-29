from django.db import models


class Contact(models.Model):

    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=155)
    subject = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return f'{self.name}'

    class Meta:
        """ Set verbose name """
        verbose_name = 'Contact Form'
