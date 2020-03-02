from django.contrib import admin
from trading .models import User_Signup, Verification,transictions
# Register your models here.
admin.site.register(User_Signup)
admin.site.register(Verification)
admin.site.register(transictions)



