from django.contrib import admin

from CarAds.models import CarAds


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'location', 'price')

    search_fields = ('title',)


admin.site.register(CarAds, PostAdmin)
