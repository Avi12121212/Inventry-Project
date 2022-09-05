from django.db import models


# Create your models here.

class Phone(models.Model):
    phone = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    price = models.IntegerField()
    model = models.CharField(max_length=200)
    feature = models.CharField(max_length=200)
    camera = models.CharField(max_length=200)

    def getPhone(self):
        return self.phone

    def __str__(self):
        return "Phone={0},Color={1},Price={2},Model={3},Feature={4},camera={5}".format(self.phone, self.color,
                                                                                       self.price, self.model,
                                                                                       self.feature, self.camera)

    class Meta:
        db_table = "phone"


class Myusers(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def getName(self):
        return self.name

    def __str__(self):
        return "Name={0},Username={1},Password={2},Email={3}".format(self.name, self.username, self.password,
                                                                     self.email)

    class Meta:
        db_table = "myusers"


class We(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def getName(self):
        return self.name

    def __str__(self):
        return "Name={0},Username={1},Password={2},Email={3}".format(self.name, self.username, self.password,
                                                                     self.email)

    class Meta:
        db_table = "we"
