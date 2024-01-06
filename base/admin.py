from django.contrib import admin
from .models import Advocate, Company, Profile
# Register your models here.

admin.site.register(Advocate)
admin.site.register(Company)
admin.site.register(Profile)