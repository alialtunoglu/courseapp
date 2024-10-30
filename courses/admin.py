from django.contrib import admin
from .models import Course,Category


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","slug","category_list",)
    list_display_links = ("title","slug")
    prepopulated_fields = {"slug": ("title",)} #slug alanının title'a göre otomatik olarak oluşturulması
    list_filter = ("title","isActive",)
    list_editable = ("isActive",) #editable alanlar
    search_fields = ("title","description") #search alanları
    def category_list(self,obj):
        html =""
        for category in obj.categories.all():
            html += category.name + " "
        return html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","category_count")
    prepopulated_fields = {"slug": ("name",)} #slug alanının name'a göre otomatik olarak oluşturulması

    def category_count(self,obj):
        
        return obj.course_set.count()  # kursların sayısını veriyoruz.

# Register your models here.
# admin.site.register(Course,CourseAdmin) #Course modelini admin paneline ekledik.
# admin.site.register(Category) #Category modelini admin paneline ekledik.


