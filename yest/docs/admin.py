from django.contrib import admin
from .models import CustomerModel, CorpModel, StaffModel,PropertyModel, KanriModel, TransModel, GuarantModel, ContractModel

# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(CorpModel)
admin.site.register(StaffModel)
admin.site.register(PropertyModel)
admin.site.register(KanriModel)
admin.site.register(TransModel)
admin.site.register(GuarantModel)
admin.site.register(ContractModel)