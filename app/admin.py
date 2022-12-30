from django.contrib import admin

from app.models import *
class three(admin.TabularInline):
    model=threeimag1
class additionals(admin.TabularInline):
    model=additional1
class product_Admin(admin.ModelAdmin):
    inlines=(three,additionals)
admin.site.register(slider)
admin.site.register(banner)
admin.site.register(products,product_Admin)
admin.site.register(section)
admin.site.register(banner1)
admin.site.register(selling)
admin.site.register(feature)
admin.site.register(feature1)
admin.site.register(moving)
admin.site.register(banner3)
admin.site.register(banner4)
admin.site.register(banner5)
admin.site.register(banner6)
admin.site.register(recommended1)
admin.site.register(brand)
admin.site.register(main)
admin.site.register(sub_main)
admin.site.register(sub_sub)
admin.site.register(threeimag1)
admin.site.register(additional1)




