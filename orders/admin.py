from django.contrib import admin

from .models import Pizza, Pasta, Sub, SubExtras, Salads, DinnerPlatters, Catagories, Orders

admin.site.register(Pizza)
admin.site.register(Pasta)
admin.site.register(Sub)
admin.site.register(SubExtras)
admin.site.register(Salads)
admin.site.register(DinnerPlatters)
admin.site.register(Catagories)
admin.site.register(Orders)

