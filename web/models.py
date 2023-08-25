from django.db import models

# Create your models here.
STATUS_CHOICES = [
    ("","Services"),
    ('finance', 'Finance'),
    ('investment', 'Investment'),
    ('others', 'Others'),
]


class Update(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
    user = models.CharField(max_length=20)
    comment = models.CharField(max_length=10)
    posted = models.CharField(max_length=10)
    image = models.ImageField(upload_to="image")
    summary = models.TextField()

    def __str__(self):
        return str(self.title)



class Contact(models.Model):
    name = models.CharField(max_length=100)
    # last_name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50, choices=STATUS_CHOICES)
    number = models.CharField(max_length=10)
    # website = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.name


class Sector(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    date = models.DateField()
    summary = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="upload")


    def __str__(self):
        return str(self.title)