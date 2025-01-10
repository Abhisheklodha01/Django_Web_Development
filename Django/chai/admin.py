from django.contrib import admin
from .models import ChaiVariety, ChaiCertificate, ChaiReviews, ChaiStore

# Register your models here.
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReviews
    extra = 2

class ChaiVerietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'types', 'added_date',)
    inlines = [ChaiReviewInline]

class ChaiStoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)      

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certficate_number', 'issue_date',)    

admin.site.register(ChaiVariety, ChaiVerietyAdmin)
admin.site.register(ChaiStore, ChaiStoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)

