from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    message=models.TextField()
    coursee=models.TextField()

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"