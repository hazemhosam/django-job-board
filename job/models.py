from django.db import models

# Create your models here.


'''
-html widgit 
-validation 
-db size 

'''
JOP_TYPE = (
    ('Full-time','Full-time'),
    ('Part-time','Part-time'),
)
class Job(models.Model): # table 
    title = models.CharField(max_length=10) #column 
    #location [use external lib]
    jop_type = models.CharField(max_length=15,choices=JOP_TYPE)
    description = models.TextField(max_length=1000) 
    puplished_at = models.DateTimeField(auto_now=True)
    vanancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    experance = models.IntegerField(default=1) 

    def __str__(self): # to show the title of the job out 
        return self.title 
    
class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name 