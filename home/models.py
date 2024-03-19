# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Custom-1(models.Model):

    #__Custom-1_FIELDS__
    firstname = models.CharField(max_length=255, null=True, blank=True)
    lastname = models.CharField(max_length=255, null=True, blank=True)
    dob = models.CharField(max_length=255, null=True, blank=True)
    primaryphone = models.CharField(max_length=255, null=True, blank=True)
    secondaryphone = models.CharField(max_length=255, null=True, blank=True)
    primaryemail = models.CharField(max_length=255, null=True, blank=True)
    secondaryemail = models.CharField(max_length=255, null=True, blank=True)
    residencestr = models.CharField(max_length=255, null=True, blank=True)
    residencestr2 = models.CharField(max_length=255, null=True, blank=True)
    residencecity = models.CharField(max_length=255, null=True, blank=True)
    residencezip = models.CharField(max_length=255, null=True, blank=True)
    residencestate = models.CharField(max_length=255, null=True, blank=True)

    #__Custom-1_FIELDS__END

    class Meta:
        verbose_name        = _("Custom-1")
        verbose_name_plural = _("Custom-1")



#__MODELS__END
