from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Income_add_model)
# admin.site.register(Daily_add_model)

@admin.register(Daily_add_model)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Daily_add_model._meta.get_fields()]

@admin.register(Income_add_model)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Income_add_model._meta.get_fields()]
  
@admin.register(Expanse_add_model)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Expanse_add_model._meta.get_fields()]
  
@admin.register(Transfer_amount_model)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Transfer_amount_model._meta.get_fields()]
  
@admin.register(Goal_create_model)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Goal_create_model._meta.get_fields()]
  
@admin.register(Budget_create_model)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = [field.name for field in
Budget_create_model._meta.get_fields()]
  
