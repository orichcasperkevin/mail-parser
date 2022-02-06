from django.contrib import admin

# Register your models here.
from mails.models import Mail,Settings

admin.site.register(Mail)
admin.site.register(Settings)
