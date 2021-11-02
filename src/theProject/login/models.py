from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Userz(models.Model):

    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name=models.CharField(max_length=200, null=True)
    profile_pic=models.ImageField(default='',blank=True, null=True, upload_to=f'profile_pics/{user.name}')

    def __str__(self):
        return self.user

class ApplicationID(models.Model):
    ID_Number=models.IntegerField(blank=False, null=False)
    BC=models.ImageField(null=False)
    parent_ID= models.ImageField(null=False, blank=False)
    payslip=models.ImageField(null=False, blank=False)
    
    def __str__(self):
        return self.ID_Number

class ApplicationPassport(models.Model):
    PASSPORT_Number=models.IntegerField(blank=False, null=False)
    BC=models.ImageField(null=False)
    parent_ID= models.ImageField(null=False, blank=False)
    payslip=models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.PASSPORT_Number


class ADMIN_PANEL(models.Model):
    user=models.ForeignKey(Userz, null=True, on_delete=models.CASCADE)
    id_number =models.ForeignKey(ApplicationID, null=True, on_delete=models.CASCADE)
    passport_number=models.ForeignKey(ApplicationPassport, null=True, on_delete=models.CASCADE)


