from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Registers)
admin.site.register(ApplicationForm)
admin.site.register(CardType)
admin.site.register(LostOrStolen)
admin.site.register(PaymentStatus)
admin.site.register(AdmPanel)