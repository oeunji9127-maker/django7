from django.db import models

class Student(models.Model):
    id= models.IntegerField(default=1,primary_key=True),
    name= models.CharField(max_length=100)
    age= models.IntegerField(default=0)
    birth= models.DateField()
    rank= models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.id}.{self.name}/{self.rank}"
        