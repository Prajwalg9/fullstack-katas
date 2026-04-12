from django.contrib import admin
from .models import ChaiVaraity, Reviews,Stores,Certificate

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model=Reviews
    extra=2

class chaiVaraityAdmin(admin.ModelAdmin):
    list_display=['name','type','date_added',]
    inlines=[ChaiReviewInline,]
    
class StoreAdmin(admin.ModelAdmin):
    list_display=['name','location',]
    filter_horizontal=('chai_varaity',)
    
class CertificateAdmin(admin.ModelAdmin):
    list_display=['chai','certificate_number',]
    
admin.site.register(ChaiVaraity,chaiVaraityAdmin)
admin.site.register(Stores,StoreAdmin)
admin.site.register(Certificate,CertificateAdmin)