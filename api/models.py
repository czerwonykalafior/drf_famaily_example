from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=50)


class Papa(models.Model):
    name = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='papa')


class Mama(models.Model):
    name = models.CharField(max_length=100)
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='mama')


class Kid(models.Model):
    name = models.CharField(max_length=100)
    papa = models.ForeignKey(Papa, on_delete=models.CASCADE, related_name='kid')
    mama = models.ForeignKey(Mama, on_delete=models.CASCADE, related_name='kid')
    family = models.ForeignKey(Family, on_delete=models.CASCADE, related_name='kid')


class Toy(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)


class ToyOwner(models.Model):
    toy = models.ForeignKey(Toy, on_delete=models.CASCADE)
    owner = models.ForeignKey(Kid, on_delete=models.CASCADE)
