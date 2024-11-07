from django.urls import path
from . import views
# http://127.0.0.1:8000/   => anasayfa
# http://127.0.0.1:8000/home   => anasayfa
# http://127.0.0.1:8000/kurslar   => kurs listesi

urlpatterns = [
    path('',views.index,name="index"),
    path('search',views.search,name="search"),
    path('create-course',views.create_course,name="create_course"),
    path('<slug:slug>',views.details,name="course_details"),
    path('kategori/<slug:slug>',views.getCoursesByCategory,name='courses_by_category'),
]
