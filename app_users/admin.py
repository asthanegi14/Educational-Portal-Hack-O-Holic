from django.contrib import admin
from app_users.models import UserProfileInfo
from app_users.models import Contact

admin.site.register(UserProfileInfo)

admin.site.register(Contact)
