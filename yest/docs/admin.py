from django.contrib import admin
from .models import CustomerModel, CorpModel, StaffModel,PropertyModel, ContModel

# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(PropertyModel)
admin.site.register(CorpModel)
admin.site.register(StaffModel)
admin.site.register(ContModel)
