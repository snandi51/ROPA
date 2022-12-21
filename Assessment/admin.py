from django.contrib import admin

# Register your models here.
from Assessment.models import *
admin.site.register(UserDetails)
admin.site.register(RopaType)
admin.site.register(BgMain)
# admin.site.register(auth_users)

