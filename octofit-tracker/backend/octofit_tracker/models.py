from djongo import models

class User(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    is_superhero = models.BooleanField(default=False)

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=50, unique=True)
    members = models.JSONField(default=list)

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24)
    name = models.CharField(max_length=100)
    description = models.TextField()
    suggested_for = models.CharField(max_length=50)
