from django.contrib import admin
from .models import person, address, educational_background, interpersonal_relationship

admin.site.register(person)
admin.site.register(address)
admin.site.register(educational_background)
admin.site.register(interpersonal_relationship)