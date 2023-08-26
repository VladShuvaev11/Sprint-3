from django.contrib import admin

from .models import User, Level, Coordinates, Mountain,PerevalImages

admin.site.register(User)
admin.site.register(Level)
admin.site.register(Coordinates)
admin.site.register(Mountain)
admin.site.register(PerevalImages)
