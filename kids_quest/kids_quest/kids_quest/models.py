from django.db import models
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=6,decimal_places=2)
    def __str__(self):
        return self.title
class Team(models.Model):
    name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=6,max_length=2)
    cab = models.CharField(max_length=100)
    discription = models.TextField()
    additional_field = models.CharField(max_length=50)
    # ЭТО Я ДЕЛАЛ ДЗ
class Team1(models.Model):
    name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=6, max_length=2)
    cab = models.CharField(max_length=100)
    discription = models.TextField()
    additional_field = models.CharField(max_length=50)

class Team2(models.Model):
    name = models.CharField(max_length=100)
    money = models.DecimalField(max_digits=6, max_length=2)
    cab = models.CharField(max_length=100)
    discription = models.TextField()
    additional_field = models.CharField(max_length=50)



    def __str__(self):
        return self.name



class Employee(models.Model):
    name = models.CharField(max_length=100)
    birth_year = models.IntegerField()
    position = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Team1, on_delete=models.CASCADE)
    team2 = models.ForeignKey(Team2, on_delete=models.CASCADE)

    # ЭТО Я ДЕЛАЛ ДЗ

    def __str__(self):
        return self.name







