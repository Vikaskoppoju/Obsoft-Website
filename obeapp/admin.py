from django.contrib import admin
# from dynamic_models.models import ModelSchema, FieldSchema
from .models import CustomUser
# # Register your models here.
# admin.site.register(ModelSchema)
# admin.site.register(FieldSchema)
admin.site.register(CustomUser)