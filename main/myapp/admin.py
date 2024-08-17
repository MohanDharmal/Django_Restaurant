from django.contrib import admin
from .models import Contact,Profile,Dish,Category,Team,Order,Booking,Reviews

# Register your models here.
admin.site.site_header = "FoodZone | Admin"
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject','added_on','is_approved']
admin.site.register(Contact,ContactAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']
admin.site.register(Category,CategoryAdmin)


class DishAdmin(admin.ModelAdmin):
    list_display = ['id','name','price','added_on','updated_on']
admin.site.register(Dish,DishAdmin)


class TeamAdmin(admin.ModelAdmin):
    list_display = ['id','name','added_on','updated_on']
admin.site.register(Team,TeamAdmin)


admin.site.register(Profile)
admin.site.register(Order)
admin.site.register(Booking)
admin.site.register(Reviews)