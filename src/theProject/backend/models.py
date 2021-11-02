from django.db import models



class Registers(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField(max_length=300)
    ID_number = models.IntegerField(max_length=13)
    password = models.CharField(max_length=200)
    cPassword = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}  {self.surname}'



# Create your models here.
class ApplicationForm(models.Model):

  parent_id  = models.ImageField()
  birth_certificate  = models.ImageField()
  lostOrStolen = models.CharField(max_length=200)
  proofOfResidency = models.CharField(max_length=200)
  identityType = models.CharField(max_length=200)



class AdmPanel(models.Model):
    username = models.CharField(max_length=200)
    users = models.CharField(max_length=200)
    application_forms = models.ImageField()
    payments  = models.ImageField()

    def __str__(self):
        return self.username



class CardType(models.Model):
  PaymentOf = models.CharField(max_length=200)

  def __str__(self):
    return self.PaymentOf



class LostOrStolen(models.Model):
  PaymentOf = models.CharField(max_length=200)

  def __str__(self):
    return self.PaymentOf


class PaymentStatus(models.Model):
  payment_Status = models.CharField(max_length=200)

  def __str__(self):
    return self.payment_Status