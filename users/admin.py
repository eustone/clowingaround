from django.contrib import admin
from .models import User,Troupe, TroupeLeader, Clown, Client

# Register your models here.
admin.site.register(User)
admin.site.register(Troupe)
admin.site.register(TroupeLeader)
admin.site.register(Clown)
admin.site.register(Client)