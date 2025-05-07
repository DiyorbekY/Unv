from django.db.models import TextField
from django.utils import timezone
from django.db import models
from django.utils.text import slugify


class Univer(models.Model):
    unver_id=models.AutoField(primary_key=True)
    nomi=models.CharField(max_length=50,blank=True,null=True)
    content=models.TextField(null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nomi

    def save(self,*args,**kwargs):
        if not self.slug and self.nomi:
            self.slug=slugify(self.nomi)
        super(Univer,self).save(*args,**kwargs)

class Fakultet(models.Model):
    fakultet_id=models.AutoField(primary_key=True)
    fakultet_nomi=models.CharField(max_length=250,blank=True,null=True)
    unver_id=models.ForeignKey(Univer,null=True,on_delete=models.CASCADE,related_name='fakultetlar')
    def __str__(self):
        return self.fakultet_nomi

class Yonalish(models.Model):
    yonalish_id=models.AutoField(primary_key=True)
    yonalish_nomi=models.CharField(max_length=250,blank=True,null=True)
    fakultet_id=models.ForeignKey(Fakultet,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.yonalish_nomi


class Guruh(models.Model):
    guruh_id=models.AutoField(primary_key=True)
    guruh_nomi=models.CharField(max_length=50,blank=True,null=True)
    yonalish_id = models.ForeignKey(Yonalish,null=True,on_delete=models.CASCADE)
    def __str__(self):
        return self.guruh_nomi


class Talaba(models.Model):
    talaba_id = models.AutoField(primary_key=True)
    ismi=models.CharField(max_length=50,blank=True,null=True)
    yoshi=models.SmallIntegerField()
    kursi=models.SmallIntegerField()
    guruh_id = models.ForeignKey(Guruh, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.ismi


class Fanlar(models.Model):
    fan_id=models.AutoField(primary_key=True)
    fan_nomi=models.CharField(max_length=50,blank=True,null=True)
    def __str__(self):
        return self.fan_nomi


class TalabaFan(models.Model):
    talaba_id= models.ForeignKey(Talaba, null=True, on_delete=models.CASCADE)
    fan_id= models.ForeignKey(Fanlar, null=True, on_delete=models.CASCADE)
    baho=models.SmallIntegerField()



class Domla(models.Model):
    domla_id=models.AutoField(primary_key=True)
    ismi = models.CharField(max_length=50, blank=True, null=True)
    yoshi = models.SmallIntegerField()
    ish_staji=models.SmallIntegerField()
    lavozimi=models.CharField(max_length=20,blank=True,null=True)
    def __str__(self):
        return self.ismi


class DomlaFan(models.Model):
    domla_id = models.ForeignKey(Domla, null=True, on_delete=models.CASCADE)
    fan_id = models.ForeignKey(Fanlar, null=True, on_delete=models.CASCADE)






