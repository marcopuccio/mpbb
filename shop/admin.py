from django.contrib import admin

from shop.models import (
    Order, UserProfile, Laptop, Camara, Minicomponente
)


admin.site.register(Order)
admin.site.register(UserProfile)
admin.site.register(Laptop)
admin.site.register(Camara)
admin.site.register(Minicomponente)