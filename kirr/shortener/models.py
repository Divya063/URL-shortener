from django.conf import settings
from django.db import models
from .utils import code_generator, create_shortcode
SHORTCODE_MAX=getattr(settings,"SHORTCODE_MAX", 15)
# Create your models here.
class KirrUrlManager(models.Manager):
    def all(self, *args, **kwargs):
        qs=super(KirrUrlManager, self).all(*args, **kwargs)
        qs=qs.filter(active=True)
        return qs
    def refresh_shortcodes(self,items=100):
        print(items)
        qs=KirrURL.objects.filter(id__gte=1)
        newcodes=0
        for q in qs:

            q.shortcode=create_shortcode(q)
            print(q.shortcode)
            q.save()
            newcodes+=1
        return "new codes made: {i}".format(i=newcodes)



class KirrURL(models.Model):
    url=models.CharField(max_length=220,)
    shortcode=models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)#this will allow in the admin page to live it in blank
    updated=models.DateTimeField(auto_now=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    objects=KirrUrlManager()

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode=="" : #this will create new shortcode every time it is blank
            self.shortcode=create_shortcode(self)
        super(KirrURL, self).save(*args, **kwargs)
    def __str__(self):
        return str(self.url)
    def __unicode__(self):
        return str(self.url)
