from django.contrib import admin
from .models import Tour

# Register your models here.
@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ('origin_country', 'destination_country', 'number_of_nights', 'price')
    search_fields = ('origin_country', 'destination_country')
    list_filter = ('price', 'number_of_nights') 