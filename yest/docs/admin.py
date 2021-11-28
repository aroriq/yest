from django.contrib import admin
from .models import CustomerModel, CorpModel,PropertyModel, KanriModel, TransModel, GuarantModel, ContractModel, InvoiceModel
#, StaffModel
# from .forms import CulcForm

# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(CorpModel)
# admin.site.register(StaffModel)
admin.site.register(PropertyModel)
admin.site.register(KanriModel)
admin.site.register(TransModel)
admin.site.register(GuarantModel)
admin.site.register(ContractModel)
# admin.site.register(CulcForm)
admin.site.register(InvoiceModel)
