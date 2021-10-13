from django.contrib import admin
from remainderone.models import appuser,Room,imageproblem,Follower,message

admin.site.register(appuser)
admin.site.register(Room)
admin.site.register(message)
admin.site.register(imageproblem)
admin.site.register(Follower)
# Register your models here.
