from django.contrib import admin
from .models import Users, Room, Message, Users_Rooms

# Register your models here.
admin.site.register(Users)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Users_Rooms)
