from django.contrib import admin


from .models import Customer, City, State

admin.site.site_header = 'Hobby Lobby'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_joined')
admin.site.register(Customer, CustomerAdmin)


admin.site.register(City)
admin.site.register(State)


