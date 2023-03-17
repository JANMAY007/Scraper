from django.db import models

class LinkedinScraper(models.Model):
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15, null=True, blank=True)
    object = models.manager

    def __str__(self):
        return self.email + '<->' + self.phone


class LinkedinScraperLoginDetails(models.Model):
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    object = models.manager

    def __str__(self):
        return self.email
