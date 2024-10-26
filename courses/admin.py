from django.contrib import admin
from .models import Course,Category


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug")
    list_display_links = ("title","slug")
    readonly_fields = ("slug",) #readonly alanlar
    list_filter = ("title","isActive")
    list_editable = ("isActive",) #editable alanlar
    search_fields = ("title","description") #search alanları
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

# Register your models here.
# admin.site.register(Course,CourseAdmin) #Course modelini admin paneline ekledik.
# admin.site.register(Category) #Category modelini admin paneline ekledik.


