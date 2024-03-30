from django.db import models

class Talaba(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.IntegerField()
    kurs = models.IntegerField()
    talaba_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.ism

class Loyiha(models.Model):
    sarlavha = models.CharField(max_length=100)
    sana = models.DateField()
    tafsilotlar = models.TextField()
    tugallangan = models.BooleanField(default=False)
    talaba = models.ForeignKey(Talaba, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
