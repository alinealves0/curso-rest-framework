from django.contrib import admin #type:ignore


from authors.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    ...
