from django.contrib import admin
from .models import Client
from .models import Fund
from .models import Contract

admin.site.register(Client)
admin.site.register(Fund)
admin.site.register(Contract)
