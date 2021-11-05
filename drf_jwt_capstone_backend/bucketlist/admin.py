from django.contrib import admin
from .models import Bucketlist, Community, Reviews

# Register your models here.
admin.site.register(Bucketlist)
admin.site.register(Reviews)
admin.site.register(Community)