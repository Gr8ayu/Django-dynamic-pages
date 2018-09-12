from django.db import models
from intro.models import Profile
import datetime
from django.urls import reverse, reverse_lazy, resolve


# Create your models here.



class Posts(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True )
    creationDate = models.DateField(("Date"), default=datetime.date.today)
    publish = models.BooleanField(default=True)
    type = models.CharField(max_length=10 , choices=[('Notice', 'Notice'), ('Announcement', 'Announcement'), ('other', "Other"), ], blank=True );
    title = models.CharField(max_length=50, blank=True)
    content = models.TextField(blank=True);

    class Meta:
        ordering = ['creationDate']

    def get_absolute_url(self):
        return reverse('blogs:BlogDetail',kwargs={'pk':self.pk} )

    def __str__(self):
        return self.title