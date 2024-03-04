from django.contrib import admin
from .models import Comida, Bebida, Snack

# Register your models here.
admin.site.register(Comida)
admin.site.register(Bebida)
admin.site.register(Snack)