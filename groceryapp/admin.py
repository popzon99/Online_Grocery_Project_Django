from django.contrib import admin
from .models import Booking,Category,Product,UserProfile,Cart,Feedback

# Register your models here.


admin.site.register(Category)


admin.site.register(Product)

admin.site.register(UserProfile)


admin.site.register(Cart)


admin.site.register(Booking)

admin.site.register(Feedback)