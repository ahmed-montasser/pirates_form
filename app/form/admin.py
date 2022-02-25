from django.contrib import admin
from form.models import University, FormApplierModel, Faculty

# Register your models here.

admin.site.register(FormApplierModel)
admin.site.register(University)
admin.site.register(Faculty)
# admin.site.register(TimeSlot)
