from django.db import models

# Create your models here.
class Tblcommonmasters(models.Model):
    autoid = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    isactive = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    userid = models.IntegerField(blank=True, null=True)
    createdon = models.DateTimeField(blank=True, null=True)
    otherfield = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.title
    def time_pretty(self):
        return self.time.strftime('%d %e , %Y')


class Tbloptions(models.Model):
    optionid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=550, blank=True, null=True)


    email = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    alternet_number = models.CharField(max_length=16)
    facebook_link = models.CharField(max_length=300)
    twitter_link = models.CharField(max_length=300)
    youtube_link = models.CharField(max_length=300)
    instagram_link = models.CharField(max_length=300)
    linkedin_link = models.CharField(max_length=300)
    github_link = models.CharField(max_length=300,null=True)

    google_ver_id = models.CharField(max_length=50, blank=True, null=True)
    googleana_script = models.TextField(blank=True, null=True)
    facebook_script = models.TextField(blank=True, null=True)
    logo = models.CharField(max_length=150, blank=True, null=True)
    favicon = models.CharField(max_length=150, blank=True, null=True)
    address = models.CharField(max_length=150, blank=True, null=True)
    meta_title = models.CharField(max_length=150, blank=True, null=True)
    meta_keywords = models.CharField(max_length=150, blank=True, null=True)
    meta_description = models.CharField(max_length=150, blank=True, null=True)
    created_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
       return self.title