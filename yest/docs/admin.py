from django.contrib import admin
from .models import CustomerModel, CorpModel

# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(CorpModel)