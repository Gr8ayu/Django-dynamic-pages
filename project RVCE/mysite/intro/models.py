from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
#
#
YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year + 1)):
    YEAR_CHOICES.append((r, r))


#
class branch(models.Model):
    branch_name = models.CharField(max_length=100);
    branch_code = models.CharField(max_length=5);
    launch_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year);
    approved_intake = models.IntegerField();
    branch_detail = models.TextField(blank=True);

    class Meta:
        ordering = ['branch_name']

    def __str__(self):
        return self.branch_code



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=6, choices=[('male', 'Male'), ('female', 'Female'), ('other', "Other"), ],
                             null=True)
    birth_date = models.DateField(null=True, blank=True)
    reg_no = models.CharField(max_length=15, null=True);
    branch = models.ForeignKey(branch, on_delete=models.SET_NULL, null=True)
    semester = models.IntegerField(('semester'),
                                   choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)], default=1)
    admission_year = models.IntegerField(('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    bio = models.TextField(max_length=500, blank=True, null=True)
    location = models.CharField(max_length=30, blank=True)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
