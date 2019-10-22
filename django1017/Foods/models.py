from django.db import models

class Foods_type(models.Model):
    label = models.CharField(max_length=32)
    description = models.TextField()
class Foods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    picture = models.ImageField(upload_to='img')
    description = models.TextField()
    type_id = models.ForeignKey(to=Foods_type,on_delete=models.CASCADE)
    def __str__(self):
        return (self.name,self.id,self.type_id_id)
class Shop(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="img")
    foods_id = models.ManyToManyField(to = Foods)
    open_time = models.CharField(max_length=32)
    stop_car = models.CharField(max_length=32)
    address = models.TextField()
    label = models.TextField()
    def __str__(self):
        return self.name,self.picture
class Company(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="img")
    phone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    post_code = models.CharField(max_length=32)
    address = models.TextField()

class News(models.Model):
    class Meta:
        verbose_name = "news新闻"
        verbose_name_plural= "开口了"
    title = models.CharField(max_length=32)
    time = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to="img/upload")
    content = models.TextField()
    type = models.CharField(max_length = 32)

class User(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
# Create your models here.
