from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return self.site_name + "::" +str(self.url)  #사이트 이름 뜨게 하기




