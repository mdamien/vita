from django.db import models
from django.contrib.sites.models import Site
import random

class StatusPage(Site):
    slug = models.SlugField()
    
class Service(models.Model):
    page = models.ForeignKey(StatusPage)
    name = models.CharField(max_length=100)
    UP,DOWN,WARNING = range(3)
    STATUS = ((UP, 'UP'),(DOWN, 'DOWN'),(WARNING, 'WARNING'))
    status = models.SmallIntegerField(choices=STATUS)

class Check(models.Model):
    service = models.ForeignKey(Service)
    def check(self):
        return Measure(self.service,self.measure())
    class Meta:
        abstract = True

class CheckResponseTime(Check):
    def measure(self):
        return random/random()*20+90
        
class CheckLoadTime(Check):
    def measure(self):
        return random/random()*200+1000

class CheckUptime(Check):
    def measure(self):
        return 1 if random.random() > 0.1 else 0
        
class Measure(models.Model):
    check = models.ForeignKey(Check)
    time = models.TimeField(auto_now=True)
    measure = models.FloatField()

#Events,downntime,status,..
