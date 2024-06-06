from django.contrib import admin
from .models import CustomUser
from .forms import CustomUserChangeForm,CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    form=CustomUserChangeForm
    add_form=CustomUserCreationForm
    model=CustomUser
    list_display=['username','email','first_name','last_name','age','is_staff',]
    fieldsets =UserAdmin.fieldsets+ (
        (None, {
            "fields": (
                'age',
            ),
        }),
    )
    
    add_fieldsets=UserAdmin.add_fieldsets+(
        (None, {
            "fields": (
                'age',
            ),
        }),
    )
    
    
    
admin.site.register(CustomUser,CustomUserAdmin)
        
