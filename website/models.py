from django.db import models
import random
import datetime

class StatusPage(models.Model):
    domain = models.CharField( max_length=100)
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.domain
        
class Service(models.Model):
    page = models.ForeignKey(StatusPage)
    name = models.CharField(max_length=100)
    UP,DOWN,WARNING = range(3)
    STATUS = ((UP, 'UP'),(DOWN, 'DOWN'),(WARNING, 'WARNING'))
    status = models.SmallIntegerField(choices=STATUS)
    url = models.URLField()

    def __str__(self):
        return self.name

class Metric(models.Model):
    service = models.ForeignKey(Service)
    interval = models.PositiveIntegerField(Service) #in seconds
    last_checked = models.DateTimeField(auto_now=True)
    RT,LT,UP = range(3)
    METRICS = ((RT,"Response Time"),(LT,"Load Time"),(UP,"Uptime"))
    metric = models.SmallIntegerField(choices=METRICS)

    def check(self):
        now = datetime.datetime.now()
        if (now - self.last_checked).seconds < self.interval:
            return None
        self.last_checked = now
        self.save()
        m = 0
        if self.metric == self.RT: m = ResponseTime.measure(self)
        if self.metric == self.LT: m = LoadTime.measure(self)
        if self.metric == self.UP: m = Uptime.measure(self)
        return Measure(self.service,m).save()

    def __str__(self):
        return str(self.service) + " - " + str(self.metric)

class ResponseTime:
    def measure(self):
        m = random/random()*20+90
        print "Response time:",m
        return m
        
class LoadTime:
    def measure(self):
        m = random/random()*200+1000
        print "Load time:",m
        return m

class Uptime:
    def measure(self):
        m = 1 if random.random()*0.3+0.6 else 0
        print "Uptime:",m*100,"%"
        return m

class Measure(models.Model):
    metric = models.ForeignKey(Metric)
    time = models.DateTimeField(auto_now=True)
    measure = models.FloatField()

    def __str__(self):
        return str(self.metri) + ":" + str(self.measure) + " at " + str(self.time)

#Events,downntime,status,..
