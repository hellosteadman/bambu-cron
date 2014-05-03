from django.db import models

class Job(models.Model):
    """Defines a scheduled task"""
    
    next_run = models.DateTimeField()
    """The date the job should next run"""
    
    name = models.CharField(max_length = 255, unique = True)
    """The fully-qualified name of the job to run"""
    
    running = models.BooleanField(default = False)
    """A flag denoting whether the job is running or not"""
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        db_table = 'cron_job'
