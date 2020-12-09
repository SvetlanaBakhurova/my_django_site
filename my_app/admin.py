from django.contrib import admin
from .models import Client
from .models import Service
from .models import Contract

# Register your models here.
admin.site.register(Client)
admin.site.register(Service)
admin.site.register(Contract)