from django.contrib import admin
from .models import Team, Activity, Project, UserImage
# Register your models here.

admin.site.register(Team)
admin.site.register(Activity)
admin.site.register(Project)
admin.site.register(UserImage)
